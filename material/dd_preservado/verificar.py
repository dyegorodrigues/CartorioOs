"""Output-integrity checks; these do not certify pedagogical or doctrinal completeness."""
import json,re,hashlib,fitz
from pathlib import Path
from html.parser import HTMLParser
H=Path(__file__).resolve().parent;O=H.parents[2]/'output/pdf'
load=lambda n:json.loads((H/n).read_text())
m=load('apresentacao.json');qa=load('recuperacao.json');bank=load('banco_questoes.json')['questions'];spans=load('fonte_segmentos_v3.json')['segments'];old=load('fonte.json')['blocks'];dec=load('decisoes_v3.json')
class Parse(HTMLParser):
 def __init__(self):super().__init__();self.skip=0;self.text=[];self.ids=[];self.links=[];self.collapsed=[]
 def handle_starttag(self,t,attrs):
  a=dict(attrs)
  if t=='br':self.text.append(' ')
  if t in ['script','style']:self.skip+=1
  if 'id' in a:self.ids.append(a['id'])
  if t=='a' and a.get('href','').startswith('#'):self.links.append(a['href'][1:])
  if t=='details' and 'open' not in a:self.collapsed.append(a.get('id'))
 def handle_endtag(self,t):
  if t in ['script','style']:self.skip-=1
  if t in ['p','li','th','td','h1','h3','h4','summary','cite']:self.text.append(' ')
 def handle_data(self,t):
  if not self.skip:self.text.append(t)
def plain(t):return t.replace('**','').replace('!!','').replace('==','')
def norm(t):return re.sub(r'\s*/\s*', '/', re.sub(r'\s+',' ',plain(t))).strip()
h=Parse();html=(O/'Penal_DD_conteudo_preservado.html').read_text();h.feed(html);ht=norm(''.join(h.text));d=fitz.open(O/'Penal_DD_conteudo_preservado.pdf');pt=norm(' '.join(re.sub(r'DIREITO PENAL \| Noções iniciais\n\d+\n','',p.get_text()) for p in d))
assert len(h.ids)==len(set(h.ids)), 'duplicate IDs'
assert set(h.links)<=set(h.ids),set(h.links)-set(h.ids)
assert set(q['target'] for q in qa)<=set(h.ids)
assert 'aprofundamento' in h.collapsed
assert not re.search(r'\d{3}\.\d{3}\.\d{3}-\d{2}|retome:|\*\*|!!|==',ht,re.I)
assert 'definições formais que destacam seu foco na lei e na sanção' in ht
assert [s['id'] for s in m['sections'][:6]]==['conceito','caracteristicas','bens','evolucao','funcoes','classificacoes']
assert not m['approved']
mapping={};passages=[]
for s in m['sections']:
 assert [u['number'] for u in s['units']]==[s['number']+'.'+str(i+1) for i in range(len(s['units']))]
 for u in s['units']:
  for n in u['nodes']:
   for sid in n.get('source_ids',[]):mapping.setdefault(sid,[]).append({'unit':u['id'],'number':u['number'],'node':n['id']})
   if n.get('text'):passages.append((n['id'],n['text']))
   for r in n.get('rows',[]):passages.extend((n['id'],t) for t in r['cells'])
   for item in n.get('items',[]):passages.append((n['id'],item['text']))
for q in qa:
 passages.append((q['id'],q['question']));passages.extend((q['id'],t) for t in q['answer'])
for k,t in passages:
 assert norm(t) in ht,('HTML passage missing',k,t[:60])
 assert norm(t) in pt,('PDF passage missing',k,t[:60])
for a,b in zip(spans,spans[1:]):assert a['end']==b['start']
assert spans[-1]['end']==len(re.sub(r'\s+',' ',load('fonte_capitulo_1.json')['chapter_text']).strip())
labels=set(dec['source_only_labels'])
assert {x['id'] for x in spans}<=set(mapping)|labels
assert {x['id'] for x in old}<=set(mapping)|{'dd-23'}
assert {q['number']:q['answer'] for q in bank}=={52:'E',53:'C',54:'E'}
for page in d:
 for block in page.get_text('blocks'):
  assert block[0]>=39 and block[2]<=page.rect.width-38,(page.number,'horizontal overflow')
  assert block[1]>=30 and block[3]<=page.rect.height-13,(page.number,'vertical overflow')
 assert '<br' not in page.get_text()
audit={'edition':m['edition'],'source_to_destination':mapping,'title_destinations':{'dd-23':'3. OBJETO DE PROTEÇÃO: BENS JURÍDICOS','evo-transicao':'4.4 Escolas penais','func-outras':'5.4 a 5.6','class-titulo':'6. CLASSIFICAÇÕES'},'documented_changes':dec['changes'],'meaning':'Mapping of source passages and editorial dispositions; not an independent semantic certification.'}
(H/'destinos_editoriais_v3.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
r={'edition':m['edition'],'approval_scope':'GitHub operation only; material remains unapproved','chapter_source_pages':[5,13],'supplement_source_pages':[26,29],'legacy_source_blocks_accounted_for':len(old),'new_contiguous_source_spans':len(spans),'declared_model_passages_present_in_both_outputs':len(passages),'dd04_explanatory_link_restored':True,'semantic_completeness_independently_certified':False,'sections':len(m['sections']),'units':sum(len(s['units']) for s in m['sections']),'grouped_review_questions':len(qa),'full_official_items':len(bank),'additional_official_reference':'PC/CE 2025 Q22, alternative E, official booklet/key matched; only source excerpt reproduced','pdf_pages':len(d),'pdf_bookmarks':len(d.get_toc()),'html_ids_unique':True,'internal_links_valid':True,'browser_visual_validation':False,'pdf_visual_review':'all pages inspected as contact sheets; representative full-size pages also inspected','full_booklet_review_complete':False,'exam_corpus_sufficiency_established':False,'notion_content_imported':False,'held_out_opened':False,'pending':dec['pending'],'pdf_sha256':hashlib.sha256((O/'Penal_DD_conteudo_preservado.pdf').read_bytes()).hexdigest()}
(H/'verificacao.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');print(json.dumps(r,ensure_ascii=False))
