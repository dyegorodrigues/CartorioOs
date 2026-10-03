"""Editorial hierarchy; source wording is immutable in fonte.json."""
import json,re
from pathlib import Path
HERE=Path(__file__).resolve().parent
raw=json.loads((HERE/'fonte.json').read_text());src={b['id']:b for b in raw['blocks']}
audit=[]
def take(key,prefix=None,why=None):
 t=src[key]['text'];removed=''
 if prefix:
  assert t.startswith(prefix),(key,prefix,t[:100]);removed=prefix;t=t[len(prefix):].lstrip()
 audit.append({'source_id':key,'original':src[key]['text'],'display_passages':[t],'removed_editorial_prefix':removed,'reason':why or ('Numeração/título original substituído pela hierarquia única; corpo preservado.' if removed else 'Corpo preservado literalmente.')})
 return t
def track(key,passages,removed,reason):audit.append({'source_id':key,'original':src[key]['text'],'display_passages':passages,'removed_editorial_prefix':removed,'reason':reason})
def p(key,prefix=None,kind='paragraph'):
 return {'kind':kind,'id':key,'text':take(key,prefix),'source_ids':[key]}
def note(key,title,text):return {'kind':'callout','id':key,'title':title,'text':text,'source_ids':[]}
def law(key,title,text,url):return {'kind':'law','id':key,'title':title,'text':text,'url':url,'source_ids':[]}
def table(key,headers,rows,source_ids):return {'kind':'table','id':key,'headers':headers,'rows':rows,'source_ids':source_ids}
def split_row(key,pattern):
 t=src[key]['text'];m=re.match(pattern,t);assert m,(key,t[:100]);label=m.group(1);body=t[m.end():]
 track(key,[body],t[:m.end()],'Título/identificador transferido à primeira coluna; explicação preservada.')
 return {'id':key,'cells':[label,body]}
CP='https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848compilado.htm';CF='https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm'
sections=[]
concept=[]
concept.append({'id':'conceito-definicao','number':'1.1','title':'Definição e natureza jurídica','nodes':[p('dd-01','a) CONCEITO: '),p('dd-03')]})
concept.append({'id':'conceito-sancoes','number':'1.2','title':'Sanções penais e as três vias','nodes':[
 p('dd-02','#DICA DD: ',kind='tip'),
 note('nota-vias','Distinga as classificações','A terceira via é uma proposta doutrinária de reparação e reconciliação, tratada por Roxin ao lado da pena e das medidas de segurança. Não é uma terceira espécie de pena no rol do art. 32 do CP.'),
 law('lei-32','CP, art. 32 - espécies de pena','Art. 32 - As penas são:\nI - privativas de liberdade;\nII - restritivas de direitos;\nIII - de multa.',CP),
 law('lei-96','CP, art. 96 - medidas de segurança','Art. 96. As medidas de segurança são:\nI - Internação em hospital de custódia e tratamento psiquiátrico ou, à falta, em outro estabelecimento adequado;\nII - sujeição a tratamento ambulatorial.\nParágrafo único - Extinta a punibilidade, não se impõe medida de segurança nem subsiste a que tenha sido imposta.',CP)
]})
# The citation intro is held in discreet references; it is not repeated in the teaching prose.
track('dd-04',[],src['dd-04']['text'],'Introdução editorial e indicação bibliográfica transferidas para referências; a tabela conserva todas as definições.')
rows=[split_row(key,r'(.+?): ') for key in ['dd-05','dd-06','dd-07','dd-08']]
concept.append({'id':'conceito-autores','number':'1.3','title':'Definições doutrinárias','nodes':[table('tabela-autores',['Autor e corrente','Definição'],rows,[r['id'] for r in rows])]})
track('dd-10',[],src['dd-10']['text'],'Frase de ligação substituída pelo título do bloco de aspectos.')
rows=[split_row(key,r'(ASPECTO [A-ZÓ]+): ') for key in ['dd-11','dd-12','dd-13']]
concept.append({'id':'conceito-aspectos','number':'1.4','title':'Aspectos formal, material e sociológico','nodes':[table('tabela-aspectos',['Aspecto','Conteúdo'],rows,[r['id'] for r in rows])]})
concept.append({'id':'conceito-controle','number':'1.5','title':'Direito Penal como controle social','nodes':[p('dd-14','Aprofundando o enfoque sociológico '),note('nota-sancao','A sanção penal não se limita à prisão','A pena privativa de liberdade exemplifica a resposta penal mais severa. O art. 32 do CP também prevê penas restritivas de direitos e multa.')]})
concept.append({'id':'conceito-nomenclatura','number':'1.6','title':'Direito Penal e Direito Criminal','nodes':[p('dd-09','#DICA DD: ',kind='tip'),law('lei-22','CF, art. 22, I - nomenclatura e competência','Art. 22. Compete privativamente à União legislar sobre:\nI - direito civil, comercial, penal, processual, eleitoral, agrário, marítimo, aeronáutico, espacial e do trabalho;',CF)]})
sections.append({'id':'conceito','number':'1','title':'CONCEITO DE DIREITO PENAL','reference':'DD, pp. 5-6','units':concept})
rows=[split_row(key,r'[IVX]+ - (.+?): ') for key in ['dd-16','dd-17','dd-18','dd-19','dd-20','dd-21','dd-22']]
sections.append({'id':'caracteristicas','number':'2','title':'CARACTERÍSTICAS DO DIREITO PENAL','reference':'DD, pp. 6-7','units':[
 {'id':'caracteristicas-quadro','number':'2.1','title':'Características e seus significados','nodes':[p('dd-15','b) CARACTERÍSTICAS: '),table('tabela-caracteristicas',['Característica','Significado'],rows,[r['id'] for r in rows])]},
 {'id':'caracteristicas-finalista','number':'2.2','title':'Cuidado com a palavra “finalista”','nodes':[note('nota-finalista','Finalidade de proteção ≠ teoria da ação','Neste quadro de características, “finalista” indica a finalidade de proteger bens jurídicos. Isso não se confunde com a teoria finalista da ação de Welzel.')]}
]})
track('dd-23',[],src['dd-23']['text'],'Título de origem absorvido pela entrada única Bens jurídicos; não se exibe c) junto de 3.')
bens=[]
bens.append({'id':'bens-definicao','number':'3.1','title':'Conceito e natureza do bem jurídico','nodes':[
 p('dd-31',kind='paragraph'),
 p('dd-32','1.Definição e Natureza: '),
 p('dd-24',kind='quote'),
 {'kind':'list','id':'perspectivas-bem','items':[{'id':k,'text':take(k)} for k in ['dd-33','dd-34','dd-35']],'source_ids':['dd-33','dd-34','dd-35']},
 p('dd-36',kind='quote')
]})
bens.append({'id':'bens-constituicao','number':'3.2','title':'Constituição: orientação e limites','nodes':[p('dd-25',kind='quote'),p('dd-26'),{'kind':'list','id':'limites-constitucionais','items':[{'id':k,'text':take(k)} for k in ['dd-27','dd-28']],'source_ids':['dd-27','dd-28']}]})
bens.append({'id':'bens-protecao','number':'3.3','title':'Princípio da exclusiva proteção de bens jurídicos','nodes':[
 p('dd-29','7.1.1 Princípio da Exclusiva Proteção de Bens Jurídicos '),p('dd-30'),p('dd-37','2. Função Primordial do Direito Penal: '),p('dd-38'),p('dd-39')
]})
rows=[]
for k,label in [('dd-42','Resultado jurídico'),('dd-43','Ofensividade')]:
 text=take(k,src[k]['text'].split(': ')[0]+': ');rows.append({'id':k,'cells':[label,text]})
bens.append({'id':'bens-crime','number':'3.4','title':'Bem jurídico, crime e ofensividade','nodes':[p('dd-40','3. Bem Jurídico e Conceito de Crime (Critério Material): '),p('dd-41'),table('tabela-ofensa',['Conceito','Significado'],rows,['dd-42','dd-43'])]})
b=src['dd-45'];track('dd-45',sum(b['rows'],[]),'CONCEITO DESCRIÇÃO EXEMPLO (HOMICÍDIO)','Tabela original preservada; apenas os cabeçalhos recebem capitalização consistente.')
bens.append({'id':'bens-objetos','number':'3.5','title':'Objeto jurídico × objeto material','nodes':[p('dd-44','4. Distinção Crucial: Objeto Jurídico vs. Objeto Material: '),table('dd-45',['Conceito','Descrição','Exemplo: homicídio'],[{'id':None,'cells':r} for r in b['rows']],['dd-45']),p('dd-46')]})
rows=[split_row(k,r'(.+?): ') for k in ['dd-48','dd-49']]
bens.append({'id':'bens-classificacao','number':'3.6','title':'Bens individuais e coletivos','nodes':[p('dd-47','5. Classificação e Tendências: '),table('tabela-especies',['Categoria','Titularidade e exemplos'],rows,['dd-48','dd-49'])]})
bens.append({'id':'bens-espiritualizacao','number':'3.7','title':'Espiritualização ou liquefação','nodes':[p('dd-50')]})
text=src['dd-52']['text'];q=text.index('“A noção de');definition=text[q:];track('dd-52',[definition],text[:q],'Definição mantida; autores, obra, editora e página em citação discreta no mesmo bloco.')
text=src['dd-53']['text'];prefix='Explicam ainda os autores: "';assert text.startswith(prefix);body=text[len(prefix):].removesuffix('"');first,second=body.split('Por outro lado, ',1);second,last=second.split('Em síntese, ',1)
passages=[first.strip(),'Por outro lado, '+second.strip(),'Em síntese, '+last.strip()];track('dd-53',passages,prefix,'Passagem repartida em comparação aparente/real e exemplo, mantendo a redação substantiva e atribuição.')
bens.append({'id':'bens-aparentes','number':'3.8','title':'Bens coletivos reais e aparentes','nodes':[
 {'kind':'quote','id':'dd-52','text':definition,'citation':'Martinelli e Schmitt de Bem, Direito Penal - Lições Fundamentais, D’Plácido, p. 171.','source_ids':['dd-52']},
 table('tabela-reais-aparentes',['Categoria','Explicação e exemplos'],[{'id':'dd-53-a','cells':['Coletivo aparente',passages[0]]},{'id':'dd-53-b','cells':['Coletivo real',passages[1]]}],['dd-53']),
 {'kind':'paragraph','id':'dd-53-c','text':passages[2],'source_ids':['dd-53']},
 note('nota-corrente','Delimitação da posição doutrinária','No item 53 da PF 2025, a banca empregou “Segundo doutrinadores em direito penal”. A distinção acima deve ser apresentada com a atribuição doutrinária correspondente, sem convertê-la em definição universal.'),
 p('dd-51',kind='tip')
]})
bens.append({'id':'bens-questoes','number':'3.9','title':'Questões de concurso','nodes':[{'kind':'question_bank','id':'questoes','source_ids':['dd-54','dd-55','dd-56','dd-57','dd-58']},p('dd-59','Caiu em prova Delegado AM/2022! ',kind='partial_exam')]})
bens.append({'id':'bens-sintese','number':'3.10','title':'Síntese do assunto','nodes':[p('dd-60','Em síntese: ',kind='tip')]})
sections.append({'id':'bens','number':'3','title':'BENS JURÍDICOS E SUA PROTEÇÃO','reference':'DD, p. 7 e pp. 26-29','units':bens})
# Real exam data lives outside the presentation. Retrieval practice is a separate authored file.
PROVA='https://cdn.cebraspe.org.br/concursos/PF_25/arquivos/106_PF_001_01.pdf';GAB='https://cdn.cebraspe.org.br/concursos/PF_25/arquivos/D202E48A0B1EBF5039E398F0B49D0186DD625DFF53498E36EE4D88DE4501E3A8.pdf'
qs=[]
for number,key,comment,answer,return_id in [(52,'dd-56','dd-57','E','bens-definicao'),(53,'dd-58',None,'C','bens-aparentes'),(54,'dd-54','dd-55','E','bens-constituicao')]:
 text=src[key]['text'];prefix,stem=text.split('emanações. ',1);stem=re.sub(r'\s*\(item (?:errado|correto)\)\.?$','',stem)
 track(key,[stem],prefix+'emanações. ','Identidade da prova e comando separados em metadados; enunciado substantivo e gabarito preservados.')
 c=take(comment) if comment else None
 if number==52:extra='A discussão histórica exige cuidado: Paiva distingue a ideia de bem em Birnbaum da expressão bem jurídico em Binding e registra interpretações divergentes sobre a função limitadora da primeira. A síntese acima não resolve toda a evolução da teoria.'
 elif number==53:extra='O enunciado delimita a posição com “Segundo doutrinadores em direito penal”. A banca considerou correta essa formulação no gabarito definitivo.'
 else:extra=None
 qs.append({'id':f'PF-2025-DELEGADO-{number}','kind':'real','exam':'Polícia Federal','role':'Delegado','year':2025,'date':'2025-07-27','bank':'Cebraspe','booklet':'106_PF_001_01','number':number,'stem':stem,'answer':answer,'comment':c,'precision':extra,'topic':'bens','subtopic':return_id,'source_block_ids':[key]+([comment] if comment else []),'exam_url':PROVA,'key_url':GAB,'source_state':'OFFICIAL_STATEMENT_AND_FINAL_KEY_CHECKED','difficulty':'Difícil' if number in [52,53] else 'Médio','difficulty_basis':'Estimativa pedagógica; não calibrada por desempenho','requirements':{52:['origem da noção de bem jurídico','bem jurídico e ratio legis','função crítica e interpretativa'],53:['coletivo real/aparente','soma de interesses individuais','indeterminação e função crítica','atribuição doutrinária'],54:['valores constitucionais','seleção penal','ultima ratio','paternalismo']}[number]})
(HERE/'banco_questoes.json').write_text(json.dumps({'status':'INITIAL_TOPIC_BANK_NOT_COMPLETE','questions':qs},ensure_ascii=False,indent=2))
assert len(audit)==60,(len(audit),set(src)-{x['source_id'] for x in audit})
assert len({x['source_id'] for x in audit})==60
(HERE/'apresentacao.json').write_text(json.dumps({'edition':'v2','title':'Direito Penal - Fundamentos','sections':sections,'references':[{'label':'Texto-base: DD - Noções iniciais e princípios, pp. 5-7 e 26-29.','url':None},{'label':'DD Legis CP: arts. 32 e 96, pp. 38 e 81, cotejados com a legislação oficial.','url':CP},{'label':'Nilo Batista, Introdução crítica ao direito penal brasileiro, 2007, pp. 44-49: referência para as definições formais.','url':None},{'label':'CF, art. 22, I.','url':CF},{'label':'Roxin, Pena y reparación, seção IV.1.','url':'https://revistas.mjusticia.gob.es/index.php/ADPCP/article/download/404/404/400'},{'label':'PF 2025, caderno de Delegado e gabarito definitivo.','url':PROVA},{'label':'Paiva, A efetividade da teoria do bem jurídico, Delictae 18/2025.','url':'https://periodicos.pucminas.br/delictae/article/download/36614/24124'}]},ensure_ascii=False,indent=2))
(HERE/'destinos_editoriais.json').write_text(json.dumps({'policy':'Tratamento editorial sujeito a revisão semântica: fonte normalizada conservada em fonte.json, mas presença dos trechos declarados não comprova completude. A revisão posterior detectou perda da ligação explicativa em dd-04; ver DIAGNOSTICO_PEDAGOGICO_2026-10-03.md.','entries':audit},ensure_ascii=False,indent=2))
print(json.dumps({'source_blocks_mapped':len(audit),'sections':len(sections),'units':sum(len(s['units']) for s in sections),'real_questions':len(qs)}))
