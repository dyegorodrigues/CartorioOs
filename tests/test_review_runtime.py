"""Riscos do adaptador: perda de retomada, retry, falso recall e versão de conteúdo."""
from copy import deepcopy
import json
import subprocess
import sys
import unittest

from scripts import review_runtime as rt


class ReviewRuntimeTests(unittest.TestCase):
    def setUp(self):
        fixture = rt.demo()
        self.catalog = fixture["catalog"]
        self.state = rt.unpack(fixture["checkpoint"])
        self.now = "2026-09-10T12:00:00+00:00"

    def event(self, **changes):
        event = {"id": "TEST-ANSWER", "kind": "answer", "item_id": "SYN-1",
                 "at": self.now, "outcome": "correct"}
        event.update(changes)
        return event

    def apply(self, event):
        return rt.apply_event(self.state, event, self.catalog, len(self.state["events"]))

    def test_new_process_resumes_exact_pending_prompt_without_answer(self):
        # Processo sem objeto/variável do processo criador: só envelope persistido.
        code = """
import json,sys
from scripts.review_runtime import unpack,resume
p=json.load(sys.stdin)
print(json.dumps(resume(unpack(p['checkpoint']),p['catalog'],p['now'])))
"""
        payload = {"checkpoint": rt.pack(self.state), "catalog": self.catalog, "now": self.now}
        output = subprocess.check_output([sys.executable, "-B", "-c", code],
                                         input=json.dumps(payload).encode())
        result = json.loads(output)
        self.assertEqual(result["action"], "RESUME")
        self.assertEqual(result["pending"]["prompt"], self.catalog["SYN-1"]["prompt"])
        self.assertNotIn("answer", result["pending"])
        self.assertEqual(len(self.state["events"]), 27)

    def test_retry_all_27_events_is_idempotent(self):
        result = self.state
        for old in self.state["events"]:
            result = rt.apply_event(result, old, self.catalog, expected_revision=0)
        self.assertEqual(result, self.state)

    def test_id_collision_and_stale_revision_rejected(self):
        collision = dict(self.state["events"][0], kind="answer")
        with self.assertRaisesRegex(ValueError, "Colisão"):
            self.apply(collision)
        with self.assertRaisesRegex(ValueError, "Estado antigo"):
            rt.apply_event(self.state, self.event(), self.catalog, 0)

    def test_answer_advances_once_and_does_not_mutate_input(self):
        original = deepcopy(self.state)
        event = self.event()
        after = self.apply(event)
        self.assertIsNone(after["pending"])
        self.assertNotEqual(after["cards"]["SYN-1"]["fsrs"], original["cards"]["SYN-1"]["fsrs"])
        self.assertEqual(self.state, original)
        self.assertEqual(rt.apply_event(after, event, self.catalog, 27), after)

    def test_failed_recall_uses_again_and_no_latency_is_invented(self):
        after = self.apply(self.event(outcome="incorrect"))
        before = rt.Card.from_dict(self.state["cards"]["SYN-1"]["fsrs"])
        expected, log = rt.Scheduler.from_dict(self.state["scheduler"]).review_card(
            before, rt.Rating.Again, review_datetime=rt.utc(self.now))
        self.assertEqual(after["cards"]["SYN-1"]["fsrs"], expected.to_dict())
        self.assertIsNone(log.review_duration)

    def test_assisted_and_material_gap_do_not_train_fsrs(self):
        for outcome in ("assisted", "material_gap"):
            with self.subTest(outcome=outcome):
                after = self.apply(self.event(outcome=outcome))
                self.assertEqual(after["cards"]["SYN-1"]["fsrs"], self.state["cards"]["SYN-1"]["fsrs"])
                self.assertEqual(after["cards"]["SYN-1"]["suspended"], outcome == "material_gap")

    def test_reworded_or_stale_pending_item_requires_revalidation(self):
        for field, value in (("answer", "Nova regra."), ("freshness", "REVALIDATE"),
                             ("release", "BUILD")):
            with self.subTest(field=field):
                catalog = deepcopy(self.catalog)
                catalog["SYN-1"][field] = value
                self.assertEqual(rt.resume(self.state, catalog, self.now)["action"], "REVALIDATE")
                with self.assertRaises(ValueError):
                    rt.apply_event(self.state, self.event(), catalog, 27)

    def test_removed_pending_item_can_be_cancelled_without_scoring(self):
        self.catalog.pop("SYN-1")
        after = self.apply(self.event(kind="cancel", reason="Conteúdo retirado."))
        self.assertIsNone(after["pending"])
        self.assertEqual(after["cards"], self.state["cards"])

    def test_review_budget_and_blocked_content(self):
        after = self.apply(self.event(kind="cancel", reason="Ensaio de fila."))
        query = rt.resume(after, self.catalog, "2027-01-01T12:00:00+00:00", 30)
        self.assertEqual(query["due_count"], 2)
        self.assertEqual(len(query["queue"]), 1)
        self.assertEqual(query["estimated_seconds"], 30)
        self.assertEqual(rt.resume(after, self.catalog, self.now, 0)["queue"], [])
        self.catalog["SYN-1"]["freshness"] = "REVALIDATE"
        query = rt.resume(after, self.catalog, "2027-01-01T12:00:00+00:00", 60)
        self.assertEqual(query["queue"], ["SYN-2"])
        self.assertEqual(query["blocked"], ["SYN-1"])

    def test_no_recall_estimate_or_review_credit_for_unseen_content(self):
        state = rt.new_state()
        with self.assertRaises(ValueError):
            rt.apply_event(state, self.event(), self.catalog, 0)
        state = rt.apply_event(state, self.event(kind="expose"), self.catalog, 0)
        self.assertIsNone(rt.recall_estimate(state, "SYN-1", self.now))
        self.assertEqual(set(state["cards"]), {"SYN-1"})

    def test_clock_and_corrupt_checkpoint_rejected(self):
        for at in ("2026-09-10T12:00:00", "2020-01-01T12:00:00+00:00"):
            with self.subTest(at=at), self.assertRaises(ValueError):
                self.apply(self.event(at=at))
        envelope = rt.pack(self.state)
        envelope["state"]["pending"] = None
        with self.assertRaisesRegex(ValueError, "Checkpoint"):
            rt.unpack(envelope)

    def test_real_learner_mode_is_not_available(self):
        self.state["mode"] = "LIVE"
        with self.assertRaises(ValueError):
            rt.resume(self.state, self.catalog, self.now)


if __name__ == "__main__":
    unittest.main()
