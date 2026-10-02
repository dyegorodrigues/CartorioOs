"""Explicit human-reviewed extension. No keyword match promotes an exam to audited.

Rows paraphrase selected assertions; the official PDFs remain the originals.
Historical key, current-law verification and editorial judgment are separate.
"""
from pathlib import Path
import csv, json, hashlib, collections

ROOT=Path(__file__).parent
BASE=ROOT.parent/'work_2026-10-01'
questions=[]; assertions=[]
REVIEW_DATE='2026-10-02'

def read_csv(path):
    with path.open(newline='') as f:return list(csv.DictReader(f))

def write_csv(name, rows):
    if not rows:return
    fields=list(dict.fromkeys(k for row in rows for k in row))
    with (ROOT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)

def question(qid, exam, career, bank, date, number, source, key_source, answer,
             atoms, relevance, note, phase='objetiva', defect='NO_DEFECT_ESTABLISHED',
             status='DEFINITIVE', difficulty='EDITORIAL_NOT_CALIBRATED', pages='',
             eligibility='LEGAL_REVIEW_PENDING'):
    q=dict(question_id=qid,exam_id=exam,career=career,bank=bank,application_date=date,
      phase=phase,form='tipo1/padrao' if phase=='objetiva' else 'Penal',question_number=number,
      source_id=source,key_source_id=key_source,official_answer=answer,key_status=status,
      knowledge_atoms=atoms,relevance=relevance,evidence_type='REAL_ITEM',
      source_confidence='OFFICIAL_DOCUMENT',legal_state_at_exam=date,reviewed_as_of=REVIEW_DATE,
      expert_disagreement='NOT_SEARCHED_SYSTEMATICALLY',
      legal_verification='BANK_POSITION_ONLY_UNLESS_ASSERTION_SPECIFIES_SOURCE',
      defect_status=defect,note=note,review_status='NEW_SELECTED_DECOMPOSITION',
      estimated_difficulty=difficulty,source_pages=pages,training_eligibility=eligibility,
      empirical_difficulty='UNKNOWN',global_incidence='UNKNOWN_DENOMINATOR_NOT_CLOSED')
    questions.append(q);return q

def assertion(q, label, claim, position, atoms, mechanism='', authority='', verification='',
              implication='', weight='', defect='', aliases='', author=''):
    assertions.append(dict(assertion_id=q['question_id']+'::'+label,question_id=q['question_id'],
      option_or_assertion=label,paraphrased_claim=claim,bank_position=position,knowledge_atoms=atoms,
      aliases=aliases,author_doctrine=author,statute_precedent=authority,distractor_mechanism=mechanism,
      official_answer=q['official_answer'],expert_disagreement=q['expert_disagreement'],
      source_confidence='OFFICIAL_DOCUMENT',source_id=q['source_id'],key_source_id=q['key_source_id'],
      legal_state_date=q['application_date'],legal_verification=verification or q['legal_verification'],
      defect_status=defect or q['defect_status'],editorial_implication=implication or q['note'],
      rubric_weight=weight,canonical_atom_ids=atoms))

def options(q, rows):
    for label,claim,atoms,mechanism,*rest in rows:
        pos='NO_VALIDATED_OPTION_ANNULLED' if q['official_answer']=='X' else ('ACCEPTED_BY_KEY' if label==q['official_answer'] else 'REJECTED_BY_KEY')
        assertion(q,label,claim,pos,atoms,mechanism,*(rest or []))

# Recent applied evidence first. Rubric acceptance is not general legal truth.
q=question('FGV_OAB45_2026_Q2','OAB45_PENAL_2FASE','OAB','FGV','2026-02-22','2',
 'OAB45_2026_PENAL_PROVA','OAB45_2026_PENAL_KEY','RUBRIC_A_0.65_B_0.60',
 'legality.strict;legality.analogy;typicity.typification_financing;procedure.adversarial_response',
 'CORE_WITH_PROCESSUAL_BRIDGE','Distinguir atipicidade em relação ao art.19 de ausência de qualquer infração. A banca admite desclassificação; só o item B integra diretamente o núcleo de analogia.',
 phase='discursiva',difficulty='MEDIUM_INTEGRATION_ESTIMATE',pages='prova PDF10; padrão PDF5')
assertion(q,'A','A ausência de intimação do denunciado para contrarrazões à rejeição da denúncia não é suprida apenas por defensor dativo.','ACCEPTED_BY_RUBRIC','procedure.adversarial_response',authority='Súmula STF707; CPP263; CF5LV — referências do espelho',weight='0.65')
assertion(q,'B1','O empréstimo pessoal fraudulento não deve ser assimilado ao financiamento do art.19; o espelho aceita atipicidade relativa ao enquadramento ou desclassificação para estelionato.','ACCEPTED_BY_RUBRIC','typicity.typification_financing;legality.strict',mechanism='TYPE_SCOPE_AND_RELATIVE_ATYPICALITY',authority='Lei7.492/1986 art.19; CP171 — cotejo jurisprudencial específico pendente',weight='0.35')
assertion(q,'B2','É vedada analogia prejudicial ao acusado para fundamentar aquele enquadramento.','ACCEPTED_BY_RUBRIC','legality.analogy;legality.strict',mechanism='ANALOGY_IN_MALAM_PARTEM',authority='CP1; CF5XXXIX',verification='PRIMARY_CP1_SUPPORTS_LEGALITY; exact financing precedent pending',weight='0.25',aliases='analogia in malam partem')

q=question('FGV_OAB45_2026_Q3','OAB45_PENAL_2FASE','OAB','FGV','2026-02-22','3',
 'OAB45_2026_PENAL_PROVA','OAB45_2026_PENAL_KEY','RUBRIC_A_0.65_B_0.60',
 'law.harsher_nonretroactivity;procedure.reformatio_in_pejus','CORE_WITH_PROCESSUAL_BRIDGE',
 'Separar lei penal no tempo de limite processual à nova condenação. A data do novo júri não substitui a data do fato.',phase='discursiva',difficulty='MEDIUM_INTEGRATION_ESTIMATE',pages='padrão PDF6')
assertion(q,'A','A lei posterior mais gravosa não pode elevar a pena mínima aplicável ao fato anterior.','ACCEPTED_BY_RUBRIC','law.harsher_nonretroactivity',mechanism='JUDGMENT_DATE_FOR_OFFENSE_DATE',authority='CP2; CF5XL; Lei14.994/2024',verification='PRIMARY_CP2_SUPPORTS_TEMPORAL_RULE; exam-specific chronology from official rubric',weight='0.65')
assertion(q,'B','Após anulação provocada apenas pela defesa, o espelho exige a vedação à reformatio in pejus indireta.','ACCEPTED_BY_RUBRIC','procedure.reformatio_in_pejus',authority='CPP617 — referência do espelho; limites e exceções exigem auditoria própria',weight='0.60')

q=question('FGV_OAB46_2026_PECA','OAB46_PENAL_2FASE','OAB','FGV','2026-06-21','PECA',
 'OAB46_2026_PENAL_PROVA','OAB46_2026_PENAL_KEY','RESPOSTA_A_ACUSACAO_RUBRIC_5.00',
 'legality.strict;classification.crime_contravention;typicity.formal;procedure.response_accusation',
 'CORE_EMBEDDED_IN_PRACTICAL','A peça inteira vale5.00, mas o item6 de atipicidade/limite do tipo vale0.80. Não atribuir toda a pontuação ao núcleo de Introdução. Atipicidade é do art.288-A no caso; não descriminaliza jogos de azar.',
 phase='pratica',difficulty='HIGH_INTEGRATION_ESTIMATE',pages='padrão PDF1-3',defect='RUBRIC_SCOPE_CAUTION_TELEMATIC_GENERALIZATION')
rubric=[
 ('1','Endereçar ao juízo criminal da comarca indicada.','procedure.response_accusation','CPP — espelho','0.10'),
 ('2','Identificar resposta à acusação e seu fundamento.','procedure.response_accusation','CPP396/396-A','0.10'),
 ('3','Indicar prazo de dez dias.','procedure.response_accusation','CPP396','0.10'),
 ('4','Alegar inépcia pela falta de descrição da conduta típica atribuível ao acusado.','procedure.accusation_individualization','CPP41','0.80'),
 ('5','O espelho considera ilícito o acesso aos dados do telefone sem autorização no caso apresentado.','procedure.digital_evidence','CF5XII — fundamento do espelho; extensão e exceções pendentes','0.80'),
 ('6','Reconhecer atipicidade do art.288-A: a finalidade descrita envolve contravenção em lei especial, fora dos crimes previstos no CP exigidos pelo tipo.','legality.strict;classification.crime_contravention;typicity.formal','CP288-A','0.80'),
 ('7','Pedir desentranhamento da prova ilícita.','procedure.digital_evidence','CPP157; CF5LVI','0.45'),
 ('8','Pedir rejeição por inépcia.','procedure.accusation_individualization','CPP395I','0.30'),
 ('9','Pedir rejeição por ausência de justa causa diante da falta de prova lícita indicada.','procedure.just_cause','CPP395III','0.30'),
 ('10','Pedir absolvição sumária por atipicidade.','typicity.formal;procedure.summary_acquittal','CPP397III','0.60'),
 ('11','Apresentar rol respeitando o máximo de oito testemunhas.','procedure.witness_list','CPP401','0.45'),
 ('12','Datar em18/06/2026, último dia segundo o espelho.','procedure.deadline','Cronologia do enunciado e padrão','0.10'),
 ('13','Fechar com local, data e identificação profissional.','procedure.response_accusation','Espelho oficial','0.10')]
for label,claim,atoms,law,w in rubric:
    ver='PRIMARY_CP288A_TEXT_CHECKED; application according to official rubric' if label=='6' else ''
    assertion(q,label,claim,'ACCEPTED_BY_RUBRIC',atoms,authority=law,verification=ver,weight=w,
     implication='Transformar identificação do limite do tipo em fundamento e pedido; a decomposição da rubrica não autoriza renderizar a peça antes de auditar os pré-requisitos processuais.')

q=question('FGV_OAB46_2026_Q1','OAB46_PENAL_2FASE','OAB','FGV','2026-06-21','1',
 'OAB46_2026_PENAL_PROVA','OAB46_2026_PENAL_KEY','A_ALTERNATIVE_ROUTES_0.65_B_0.60',
 'legality.competence;iter_criminis.preparatory;iter_criminis.voluntary_desistance','CORE_WITH_THEORY_CRIME_BRIDGE',
 'Não fundir desistência voluntária e atos preparatórios. São vias alternativas aceitas pela banca, com pressupostos distintos. ItemB permite trabalhar fonte/competência em aplicação.',
 phase='discursiva',difficulty='MEDIUM_WITH_AMBIGUITY_ESTIMATE',pages='padrão PDF4',defect='ALTERNATIVE_DOGMATIC_ROUTES_IN_RUBRIC')
assertion(q,'A_route1','O espelho aceita desistência voluntária, com referência ao art.15.','ACCEPTED_ALTERNATIVE_NOT_CUMULATIVE','iter_criminis.voluntary_desistance',authority='CP15',weight='0.65_CAP_SHARED_WITH_A_route2',defect='EXECUTION_START_NOT_RESOLVED')
assertion(q,'A_route2','O espelho também aceita atipicidade por atos meramente preparatórios.','ACCEPTED_ALTERNATIVE_NOT_CUMULATIVE','iter_criminis.preparatory',weight='0.65_CAP_SHARED_WITH_A_route1',defect='EXECUTION_START_NOT_RESOLVED')
assertion(q,'B','O espelho aceita inconstitucionalidade da lei municipal por competência da União sobre processo penal ou por garantias constitucionais indicadas.','ACCEPTED_ALTERNATIVE_GROUNDS','legality.competence',authority='CF22I; CF5LIV/LV/LVII',verification='PRIMARY_CF22I_CHECKED_FOR_COMPETENCE_ROUTE; no blanket claim of exclusivity ignoring sole paragraph',weight='0.60')

q=question('FGV_ENAC2026_1_Q98','ENAC2026_1','Cartorios_ENAC','FGV','2026-06-14','98',
 'ENAC2026_PROVA','ENAC2026_KEY','A','penalty.multiple_majorants;legality.strict',
 'BRIDGE_ADVANCED','O item já pertence ao ENAC300 pass1. Esta é decomposição complementar, não nova descoberta de prova. Cobrança central de dosimetria; conexão com limites legais não transforma o item inteiro em Introdução.',
 difficulty='MEDIUM_APPLICATION_ESTIMATE',pages='prova PDF31')
options(q,[
 ('A','Se o juiz limita a incidência a uma majorante concorrente da parte especial, aplica a que mais aumenta a pena.','penalty.multiple_majorants;legality.strict','RULE_APPLICATION','CP68parágrafoúnico','PRIMARY_CP68_TEXT_CHECKED'),
 ('B','O juiz teria liberdade para escolher a majorante mais benéfica.','penalty.multiple_majorants','DISCRETION_WITHOUT_STATUTORY_LIMIT'),
 ('C','Seria obrigatória a cumulação de todas as majorantes.','penalty.multiple_majorants','PERMISSION_TURNED_INTO_OBLIGATION'),
 ('D','Individualização e favor rei autorizariam selecionar a menor majorante contra a regra legal.','legality.strict;penalty.multiple_majorants','PRINCIPLE_OVERRIDES_EXPRESS_RULE'),
 ('E','Somente a extorsão exigiria cumulação, permitindo no roubo escolher a mais favorável.','penalty.multiple_majorants','UNSUPPORTED_CRIME_DISTINCTION')])

# Historical selected examples, with application dates from the definitive keys.
q=question('CEBRASPE_PCGO2017_Q16','PCGO_EDITAL2016_APLIC2017','Delegado','CEBRASPE','2017-02-05','16',
 'PCGO2017_PROVA','PCGO2017_KEY','X','criminology.vs_dogmatics;criminology.objects',
 'CORE','Anulada. A justificativa oficial cita depende na opção apontada como gabarito, mas a tabela registra B e o termo aparece em C no caderno. Preservar essa divergência documental. Concurso encerrado em2018 com resultado tornado sem efeito.',
 defect='OFFICIAL_ANNULMENT_AND_REASON_OPTION_MISMATCH',status='ANNULLED',pages='prova PDF1',eligibility='HISTORICAL_QA_ONLY')
options(q,[
 ('A','Criminologia seria normativa e unidisciplinar.','criminology.vs_dogmatics','SCIENCE_METHOD_SWAP'),
 ('B','Direito Penal define condutas e penas; Criminologia observa infrações como fenômeno humano e biopsicossocial.','criminology.vs_dogmatics','CONCEPTUAL_CONTRAST'),
 ('C','Criminologia alimentaria o Direito Penal sem dele depender.','criminology.vs_dogmatics','ABSOLUTE_INDEPENDENCE'),
 ('D','Vítima só seria objeto criminológico se não tivesse responsabilidade no crime.','criminology.objects','VICTIM_RESTRICTION'),
 ('E','Objetos seriam delinquente, vítima, Judiciário e controle social.','criminology.objects','OBJECT_SUBSTITUTION')])

q=question('CEBRASPE_PCGO2017_Q17','PCGO_EDITAL2016_APLIC2017','Delegado','CEBRASPE','2017-02-05','17',
 'PCGO2017_PROVA','PCGO2017_KEY','D','criminology.empirical;policy_criminal.role','CORE',
 'Gabarito histórico do item não supera o encerramento do concurso. Termos causais/periculosidade exigem delimitação de paradigma; não virar definição exclusiva de toda Criminologia.',
 difficulty='EASY_CONCEPTUAL_ESTIMATE',pages='prova PDF1',eligibility='HISTORICAL_REVIEW_PENDING')
options(q,[
 ('A','Criminologia visaria apenas delinquentes/ressocialização, em contraste com prevenção na Política Criminal.','criminology.empirical;policy_criminal.role','FUNCTION_REDUCTION'),
 ('B','Sua finalidade diante do Direito Penal seria eliminar o crime.','criminology.empirical','ABSOLUTE_OUTCOME'),
 ('C','A determinação da etimologia do crime seria sua finalidade.','criminology.empirical','ETYMOLOGY_FOR_ETIOLOGY'),
 ('D','Entre seus aspectos estariam causas e concausas da criminalidade e periculosidade preparatória.','criminology.empirical','HISTORICAL_ETIOLOGICAL_FORMULATION'),
 ('E','A orientação político-criminal seria de prevenção especial e direta na intervenção descrita.','policy_criminal.role','PREVENTION_AXIS_CONFUSION')])

q=question('CEBRASPE_PCGO2017_Q18','PCGO_EDITAL2016_APLIC2017','Delegado','CEBRASPE','2017-02-05','18',
 'PCGO2017_PROVA','PCGO2017_KEY','E','criminology.prevention_levels','BRIDGE',
 'Distinguir destinatário, momento e mecanismo de prevenção. Histórico de concurso encerrado; não contar como eficácia comprovada de políticas.',difficulty='MEDIUM_DISCRIMINATION_ESTIMATE',pages='prova PDF1',eligibility='HISTORICAL_REVIEW_PENDING')
options(q,[
 ('A','Mudança de gestão escolar para melhorar ensino seria prevenção terciária.','criminology.prevention_levels','PRIMARY_TERTIARY_SWAP'),
 ('B','Trabalho seria prevenção secundária baseada no processo motivacional.','criminology.prevention_levels','PREVENTION_AXIS_CONFUSION'),
 ('C','Prevenção primária seria menos eficaz, individualizada e de curto prazo, dispensando prestações sociais.','criminology.prevention_levels','MULTIPLE_FALSE_RESTRICTIONS'),
 ('D','Apoio investigativo da Força Nacional diante de homicídios seria diretamente prevenção terciária.','criminology.prevention_levels','SECONDARY_TERTIARY_SWAP'),
 ('E','Ações de reabilitação/dissuasão sobre apenado preso para evitar reincidência correspondem à prevenção terciária no item.','criminology.prevention_levels','TARGET_AND_TIMING')])

q=question('CEBRASPE_PCGO2017_Q19','PCGO_EDITAL2016_APLIC2017','Delegado','CEBRASPE','2017-02-05','19',
 'PCGO2017_PROVA','PCGO2017_KEY','C','criminology.restoration;criminology.resocialization;penalty.general_prevention','CORE',
 'Comparar modelos pela finalidade e papel dos envolvidos. Modelo integrador/restaurador é relação terminológica contextual, não sinonímia irrestrita. Histórico de concurso encerrado.',difficulty='MEDIUM_DISCRIMINATION_ESTIMATE',pages='prova PDF1',eligibility='HISTORICAL_REVIEW_PENDING')
options(q,[
 ('A','Modelo clássico atribuiria aos envolvidos a solução consensual com flexibilização das regras estatais.','criminology.restoration','MODEL_SWAP'),
 ('B','Modelo ressocializador evitaria reincidência por cálculo racional entre castigo legal e proveito.','criminology.resocialization;penalty.general_prevention','DISSUASION_RESOCIALIZATION_SWAP'),
 ('C','Medidas despenalizadoras e reparação à vítima com protagonismo dos envolvidos condizem com modelo integrador.','criminology.restoration','MODEL_IDENTIFICATION'),
 ('D','Modelo dissuasório teria por eixo reabilitação e retorno positivo à sociedade.','criminology.resocialization;penalty.general_prevention','RESOCIALIZATION_DISSUASION_SWAP'),
 ('E','Modelo integrador privilegiaria castigo estatal rápido e necessário como intimidação.','criminology.restoration;penalty.general_prevention','RESTORATION_DISSUASION_SWAP')])

q=question('CEBRASPE_DPERN2015_Q85','DPERN2015','Defensoria','CEBRASPE','2015-12-13','85',
 'DPE_RN2015_PROVA_CDN','DPE_RN2015_KEY','C','principle.social_adequacy;principle.insignificance;culpability.prohibition_error;legal_good.copyright',
 'CORE_APPLIED','Questão aplica princípios em tipo da parte especial. Não confundir aceitação social, falta de dano individual provado e erro de proibição inevitável.',difficulty='MEDIUM_DISCRIMINATION_ESTIMATE',pages='prova PDF22')
options(q,[
 ('A','A alegação de desconhecimento da ilicitude isentaria automaticamente Vanessa de culpabilidade.','culpability.prohibition_error','ALLEGATION_AS_PROOF','CP21','PRIMARY_CP21_RULE; inevitability not established by mere allegation'),
 ('B','Seria indispensável prova de prejuízo real aos titulares para configurar o crime.','legal_good.copyright','RESULT_REQUIREMENT_ADDED'),
 ('C','A comercialização descrita viola autoria protegida constitucionalmente e configura violação de direito autoral.','legal_good.copyright','LEGAL_GOOD_IDENTIFICATION','STJ Súmula502; CP184§2','PRIMARY_STJ502_SUPPORTS_TYPICALITY'),
 ('D','A venda/exposição seria atípica por adequação social.','principle.social_adequacy','SOCIAL_TOLERANCE_AS_ATYPICALITY','TJDFT Acórdão1208991; STJ502','PRIMARY_TJDFT_THEMATIC_SOURCE_SUPPORTS_REJECTION'),
 ('E','A venda/exposição seria atípica por insignificância.','principle.insignificance','INSIGNIFICANCE_AUTOMATIC','TJDFT Acórdão1208991','PRIMARY_TJDFT_THEMATIC_SOURCE_SUPPORTS_REJECTION')])

q=question('CESPE_TRF2_2013_Q16','TRF2_EDITAL2012_APLIC2013','Magistratura','CESPE','2013-01-13','16',
 'TRF2_2012_PROVA_CDN','TRF2_2013_KEY','A','legality.analogy;interpretation.methods','CORE',
 'D também admite analogia favorável, gerando possível dupla resposta. Gabarito A preservado; justificativas dos recursos providos não incluem Q16. Não inventar por que D foi rejeitada.',
 defect='EDITORIAL_POSSIBLE_MULTIPLE_ANSWERS_UNRESOLVED',difficulty='DO_NOT_CALIBRATE_WHILE_DISPUTED',pages='prova PDF7',eligibility='QUARANTINE_PENDING_ADVERSARIAL_REVIEW')
options(q,[
 ('A','Interpretação extensiva alcança o sentido real da norma.','interpretation.methods','EXTENSION_DEFINITION'),
 ('B','Interpretação analógica seria sempre inadmissível por prejudicar o réu.','interpretation.methods;legality.analogy','ANALOGY_INTERPRETATION_CONFUSION'),
 ('C','Interpretação teleológica buscaria o sentido pela posição das palavras no texto.','interpretation.methods','TELEOLOGICAL_GRAMMATICAL_SWAP'),
 ('D','Analogia penal poderia suprir lacuna em favor do réu.','legality.analogy','POSSIBLY_CORRECT_DISTRACTOR','STJ AgRgHC629387; cotejo específico pendente','PRIMARY_STJ_EXAMPLE_SUPPORTS_IN_BONAM_PARTEM; historical key conflict remains'),
 ('E','Interpretação judicial se manifestaria em súmulas vinculantes editadas pelos tribunais.','interpretation.methods','COMPETENCE_GENERALIZATION')])

q=question('CESPE_TRF2_2013_Q17','TRF2_EDITAL2012_APLIC2013','Magistratura','CESPE','2013-01-13','17',
 'TRF2_2012_PROVA_CDN','TRF2_2013_KEY','E','principle.insignificance;typicity.typification_administration','BRIDGE',
 'Somente D se liga diretamente ao núcleo de insignificância; demais alternativas exigem tipos e redações próprias. Questão histórica integral não liberada para treino atual.',pages='prova PDF8',eligibility='HISTORICAL_REVIEW_PENDING')
options(q,[
 ('A','Extinção da punibilidade da sonegação previdenciária seria possível pela declaração/confissão após início da ação fiscal e antes da denúncia.','typicity.typification_administration','TEMPORAL_REQUIREMENT_SHIFT'),
 ('B','Retratação da falsa perícia excluiria punibilidade até trânsito em julgado da sentença cível.','typicity.typification_administration','PROCEDURAL_MILESTONE_SHIFT'),
 ('C','Diretor que permite comunicação somente entre presos não praticaria crime, pois só se vedaria comunicação externa.','typicity.typification_administration','TYPE_SCOPE_REDUCTION'),
 ('D','Insignificância seria sempre inaplicável ao descaminho.','principle.insignificance','ABSOLUTE_EXCEPTION_DENIAL'),
 ('E','Imputar contravenção a inocente e provocar investigação pode configurar denunciação caluniosa.','typicity.typification_administration','TYPE_SCOPE_INCLUSION')])

q=question('CESPE_TRF2_2013_Q18','TRF2_EDITAL2012_APLIC2013','Magistratura','CESPE','2013-01-13','18',
 'TRF2_2012_PROVA_CDN','TRF2_2013_KEY','E','principle.insignificance;legal_good.public_faith;law.historical_type_change','BRIDGE',
 'Parte do caderno antecede alterações do art.288 e do tráfico de pessoas. Não trocar nomenclatura quadrilha nem atualizar silenciosamente alternativas. E exemplifica bem jurídico supraindividual.',pages='prova PDF8',defect='HISTORICAL_LEGAL_CHANGE_REVIEW_REQUIRED',eligibility='HISTORICAL_REVIEW_PENDING')
options(q,[
 ('A','Pagamento previdenciário antes do recebimento da denúncia permitiria perdão ou só multa nas condições descritas.','law.historical_type_change','TEMPORAL_REQUIREMENT_SHIFT'),
 ('B','Ampla defesa excluiria falsa identidade usada para escapar de mandado de prisão.','legality.strict','GUARANTEE_AS_UNLIMITED_LICENSE'),
 ('C','A falta de identificação de um dos quatro integrantes impediria condenar os demais por quadrilha.','law.historical_type_change','IDENTIFICATION_FOR_EXISTENCE'),
 ('D','Tráfico internacional para exploração sexual teria redução especial para agente que já foi vítima.','law.historical_type_change','UNSUPPORTED_MITIGATING_RULE'),
 ('E','A fabricação de nota de pequeno valor não autoriza insignificância no caso.','principle.insignificance;legal_good.public_faith','LEGAL_GOOD_BEYOND_AMOUNT','STF notícia institucional localizada; inteiro teor do precedente pendente','PRIMARY_STF_SEARCH_SNIPPET_ONLY; full precedent and present-law sweep pending')])

q=question('CESPE_DPU2010_Q58','DPU2010','Defensoria','CESPE','2010-03-06','58',
 'DPU2010_PROVA_CDN','DPU2010_KEY_CDN','E','iter_criminis.impossible_crime;typicity.material','BRIDGE',
 'Comparação histórica com entendimento posteriormente sumulado. Súmula567 é de2016; não atribuir sua existência à prova de2010.',difficulty='EASY_RECOGNITION_ESTIMATE',pages='prova PDF4')
assertion(q,'ITEM','Sistema eletrônico de vigilância, por si, tornaria impossível o furto por absoluta ineficácia do meio.','REJECTED_BY_KEY','iter_criminis.impossible_crime','RELATIVE_FOR_ABSOLUTE_IMPOSSIBILITY','STJ Súmula567','PRIMARY_STJ567_LATER_CORROBORATION_NOT_2010_SOURCE')

q=question('CESPE_DPU2010_Q59','DPU2010','Defensoria','CESPE','2010-03-06','59',
 'DPU2010_PROVA_CDN','DPU2010_KEY_CDN','C','culpability.theories','BRIDGE',
 'Comparação entre sistemas do delito; não antecipar detalhes antes de explicar os níveis de análise.',difficulty='EASY_WITH_PREREQUISITE_ESTIMATE',pages='prova PDF4')
assertion(q,'ITEM','Na teoria psicológica, dolo e culpa integram a culpabilidade e a imputabilidade é pressuposto.','ACCEPTED_BY_KEY','culpability.theories','DOGMATIC_LOCATION',author='Teoria psicológica; fonte doutrinária específica pendente')

q=question('CESPE_DPU2010_Q60','DPU2010','Defensoria','CESPE','2010-03-06','60',
 'DPU2010_PROVA_CDN','DPU2010_KEY_CDN','X','culpability.theories','QA_ONLY',
 'Justificativa oficial: uso de jurídico em vez de antijurídico prejudicou o julgamento. Preservar original; eventual correção teria outro ID de adaptação.',status='ANNULLED',defect='CONFIRMED_WORD_ERROR_OFFICIAL_REASON',pages='prova PDF4; justificativa PDF1',eligibility='HISTORICAL_QA_ONLY')
assertion(q,'ITEM','Teoria psicológico-normativa inclui censura a fato descrito no original como típico e jurídico.','ANNULLED_NO_TRUTH_LABEL','culpability.theories','WORD_CHANGES_LEGAL_MEANING','DPU2010_RESOURCES_CDN','OFFICIAL_REASON_CONFIRMS_DEFECT')

q=question('CESPE_DPU2010_Q61','DPU2010','Defensoria','CESPE','2010-03-06','61',
 'DPU2010_PROVA_CDN','DPU2010_KEY_CDN','C','culpability.theories;typicity.dolo','BRIDGE',
 'Contrastar com Q59: mudança de localização de dolo/culpa conforme a construção dogmática. Corrente não se confunde com data de vigência de uma lei.',difficulty='MEDIUM_CONTRAST_ESTIMATE',pages='prova PDF4')
assertion(q,'ITEM','Na teoria normativa pura, dolo e culpa são analisados na tipicidade e a culpabilidade expressa reprovação.','ACCEPTED_BY_KEY','culpability.theories;typicity.dolo','DOGMATIC_LOCATION',author='Teoria normativa pura; fonte doutrinária específica pendente')

q=question('CESPE_DPU2010_Q70','DPU2010','Defensoria','CESPE','2010-03-06','70',
 'DPU2010_PROVA_CDN','DPU2010_KEY_CDN','E','principle.insignificance;legal_good.public_faith;liability.adolescent','CORE_APPLIED_WITH_BRIDGES',
 'O item é uma conjunção. Seu gabarito E não torna falsas todas as proposições componentes. O adolescente tem17anos; não igualar prisão de adulto e apreensão. Não converter narrativa longa em dificuldade alta automaticamente.',difficulty='MEDIUM_WITH_HIGH_READING_LOAD_ESTIMATE',pages='prova PDF5')
assertion(q,'1','O comando afirma cabimento de prisão em flagrante dos dois agentes, um deles adolescente.','COMPOSITE_FALSE_COMPONENT_NOT_RESOLVED_BY_KEY','liability.adolescent','ADULT_JUVENILE_CATEGORY_MERGE',verification='ECA_SPECIFIC_AUDIT_PENDING')
assertion(q,'2','O comando afirma concurso de pessoas entre os agentes.','COMPOSITE_FALSE_COMPONENT_NOT_RESOLVED_BY_KEY','liability.participation','COMPOSITE_ASSERTION',verification='COMPONENT_LEGAL_AUDIT_PENDING')
assertion(q,'3','Restituição e ausência de prejuízo permitiriam insignificância no caso de moeda falsa.','COMPOSITE_FALSE_COMPONENT_NOT_RESOLVED_BY_KEY','principle.insignificance;legal_good.public_faith','RESTITUTION_AS_AUTOMATIC_ATYPICALITY','STF notícia institucional localizada; inteiro teor do precedente pendente','PRIMARY_STF_SEARCH_SNIPPET_ONLY; component-level verification remains pending, not inferred from whole-item key')

write_csv('QUESTION_EXTENSION_V0_3.csv',questions)
write_csv('ASSERTION_EXTENSION_V0_3.csv',assertions)

# Explicit vocabulary extension; most atoms reuse v0.2 IDs.
old_atoms={r['atom_id'] for r in read_csv(BASE/'KNOWLEDGE_ATOMS_V0_2.csv')}
atom_notes={
 'classification.crime_contravention':'Crime e contravenção não são termos intercambiáveis quando o tipo delimita sua finalidade.',
 'typicity.formal':'Subsunção depende dos elementos do tipo; afastar um tipo não significa licitude global da conduta.',
 'legality.competence':'Competência legislativa precisa acompanhar o ramo e as regras constitucionais de repartição.',
 'interpretation.methods':'Interpretação extensiva, analógica, teleológica e analogia exigem distinção de operações e limites.',
 'law.harsher_nonretroactivity':'Lei penal mais gravosa não se aplica retroativamente ao fato anterior.',
 'culpability.theories':'A localização de dolo e culpa varia conforme a teoria da culpabilidade.',
 'criminology.objects':'Objeto, método e autonomia da Criminologia exigem delimitação histórica e teórica.',
 'criminology.prevention_levels':'Prevenção primária, secundária e terciária têm critérios distintos de destinatário e momento.',
 'legal_good.public_faith':'A tutela da fé pública não se reduz ao prejuízo patrimonial individual.',
 'legal_good.copyright':'Direitos autorais são o bem tutelado na aplicação examinada de comercialização de mídias falsas.',
 'iter_criminis.impossible_crime':'Impossibilidade absoluta não decorre automaticamente de vigilância que dificulta o delito.',
 'iter_criminis.preparatory':'Atos preparatórios e início da execução devem ser diferenciados antes de aplicar desistência.',
 'iter_criminis.voluntary_desistance':'Desistência voluntária tem pressupostos diferentes da não iniciação de atos executórios.',
 'penalty.multiple_majorants':'Faculdade de limitar majorantes não autoriza ignorar o critério legal da mais gravosa.',
}
newids=sorted({a for r in assertions for a in r['canonical_atom_ids'].split(';')}-old_atoms)
atoms=[]
for a in newids:
    ids=sorted({r['question_id'] for r in assertions if a in r['canonical_atom_ids'].split(';')})
    atoms.append(dict(atom_id=a,proposition=atom_notes.get(a,'Átomo de ligação identificado na questão; definição jurídica completa pendente de auditoria própria.'),status='CANDIDATE_NOT_RENDER_READY',core_live='CORE_WITH_DATED_APPLICATION' if a in atom_notes else 'BRIDGE_SCOPE_PENDING',evidence_question_ids=';'.join(ids),global_incidence='UNKNOWN_DENOMINATOR_NOT_CLOSED'))
write_csv('ATOM_EXTENSION_V0_3.csv',atoms)

aliases=[
 ('analogia in malam partem;analogia prejudicial','legality.analogy','SCOPED_SYNONYM','FGV_OAB45_2026_Q2','Distinguir de interpretação extensiva e de interpretação analógica.'),
 ('modelo integrador;modelo restaurador','criminology.restoration','CONTEXTUAL_EQUIVALENCE_REQUIRES_DOCTRINE','CEBRASPE_PCGO2017_Q19','Não universalizar sinonímia entre autores.'),
 ('crime;contravenção;infração penal','classification.crime_contravention','GENUS_SPECIES_NOT_SYNONYMS','FGV_OAB46_2026_PECA','Ler a palavra exigida pelo tipo.'),
 ('etimologia;etiologia','criminology.empirical','LEXICAL_CONFUSION_NOT_SYNONYMS','CEBRASPE_PCGO2017_Q17','Origem de palavra versus explicação causal.'),
 ('atos preparatórios;desistência voluntária','iter_criminis.preparatory;iter_criminis.voluntary_desistance','NOT_SYNONYMS_ALTERNATIVE_RUBRIC_ROUTES','FGV_OAB46_2026_Q1','Não somar pontuações alternativas nem fundir pressupostos.'),
 ('atipicidade;desclassificação','typicity.formal;typicity.typification_financing','NOT_SYNONYMS','FGV_OAB45_2026_Q2','Atipicidade relativa ao tipo imputado pode coexistir com outro enquadramento.')]
write_csv('ALIAS_EXTENSION_V0_3.csv',[dict(zip(['terms','atom_ids','relation','evidence_question','editorial_rule'],x)) for x in aliases])

graph={'scope':'selected extension only; not full corpus incidence','question_nodes':[q['question_id'] for q in questions],
 'assertion_nodes':[a['assertion_id'] for a in assertions],
 'edges':[{'from':a['assertion_id'],'to':a['question_id'],'type':'ASSERTION_OF'} for a in assertions]+
 [{'from':a['assertion_id'],'to':atom,'type':'EXAMINES','position':a['bank_position']} for a in assertions for atom in a['canonical_atom_ids'].split(';')]}
(ROOT/'EVIDENCE_EXTENSION_V0_3.json').write_text(json.dumps(graph,ensure_ascii=False,indent=2))

# Restore provenance from local acquisition records; no licensed source text is copied.
used=set()
for q in questions:used.update([q['source_id'],q['key_source_id']])
used.update(['DPU2010_RESOURCES_CDN','PCGO2017_JUSTIFICATIVAS','PCGO2017_ENCERRAMENTO','TRF2_2013_JUSTIFICATIVAS','ENAC2025_1_PROVA','ENAC2025_1_KEY','ENAC2025_2_PROVA','ENAC2025_2_KEY'])
sources=[]
for ident in sorted(used):
    d=json.loads((ROOT/'sources'/(ident+'.json')).read_text())
    path=ROOT/d['path']; assert hashlib.sha256(path.read_bytes()).hexdigest()==d['sha256']
    sources.append(dict(source_id=ident,url=d['url'],retrieved_at=d['retrieved_at'],sha256=d['sha256'],bytes=d['bytes'],http_status=d['status'],local_path=d['path'],role='OFFICIAL_EXAM_KEY_OR_NOTICE',remote_binary_status='NOT_PUBLISHED_IN_THIS_COMMIT'))
write_csv('SOURCE_EXTENSION_V0_3.csv',sources)

oldq=read_csv(BASE/'QUESTION_CORPUS_V0_2.csv'); olda=read_csv(BASE/'ASSERTION_MATRIX_V0_2.csv')
assert len({q['question_id'] for q in questions})==len(questions)
assert not ({q['question_id'] for q in questions}&{q['question_id'] for q in oldq})
assert len({a['assertion_id'] for a in assertions})==len(assertions)
assert all(a['question_id'] in {q['question_id'] for q in questions} for a in assertions)
assert not any('HELDOUT' in s for s in used)
assert abs(sum(float(a['rubric_weight']) for a in assertions if a['question_id']=='FGV_OAB46_2026_PECA')-5.0)<1e-8
assert len([a for a in assertions if a['question_id']=='FGV_OAB46_2026_Q1' and a['option_or_assertion'].startswith('A_')])==2

counts={'extension_questions':len(questions),'extension_assertion_or_rubric_rows':len(assertions),
 'extension_phase_counts':dict(collections.Counter(q['phase'] for q in questions)),
 'extension_family_counts':dict(collections.Counter(q['career'] for q in questions)),
 'official_annulled_items':[q['question_id'] for q in questions if q['key_status']=='ANNULLED'],
 'base_questions':len(oldq),'base_assertions':len(olda),'combined_selected_questions_v02_plus_extension':len(oldq)+len(questions),
 'combined_assertion_or_rubric_rows':len(olda)+len(assertions),'new_to_enac_index':0,
 'all_rows_current_law_verified':False,'universe_enumerated':False,'integrity':'PASS',
 'readiness':'NOT_READY_TO_RENDER','heldout_opened':False,
 'notes':['ENAC2026Q98 already in ENAC300 pass1; extension adds decomposition, not a new discovered exam.',
 'PCGO2017 exam result made ineffective in2018; retain historical key and separate exam-level validity.',
 'Rubric rows do not all equal independent atomic propositions; alternative routes never add points.',
 '35 earlier core reports published; full raw archive remains unsynchronized.']}
(ROOT/'COUNTS_AND_READINESS.json').write_text(json.dumps(counts,ensure_ascii=False,indent=2))
print(json.dumps(counts,ensure_ascii=False,indent=2))
