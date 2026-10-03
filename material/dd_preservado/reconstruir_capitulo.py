"""v3: source-led chapter reconstruction; explicit spans and editorial decisions."""
import json,re,copy,hashlib
from pathlib import Path
H=Path(__file__).resolve().parent
load=lambda p:json.loads((H/p).read_text())
def save(p,x):(H/p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
m=load('historico/v2/apresentacao.json');old={b['id']:b for b in load('fonte.json')['blocks']}
raw=load('fonte_capitulo_1.json');raw['chapter_text']=raw['chapter_text'][raw['chapter_text'].index('1. CONCEITO,'):];save('fonte_capitulo_1.json',raw)
flat=re.sub(r'\s+',' ',raw['chapter_text']).strip()
allnodes={n['id']:n for s in m['sections'] for u in s['units'] for n in u['nodes']}
def n(id):return copy.deepcopy(allnodes[id])
def p(id,text,kind='paragraph',**kw):return {'id':id,'kind':kind,'text':text,'source_ids':[],**kw}
def unit(id,title,nodes):return {'id':id,'number':'','title':title,'nodes':nodes}
def sec(id,title,ref,units):return {'id':id,'number':'','title':title,'reference':ref,'units':units}
def table(id,headers,rows,source_ids=[]):return {'id':id,'kind':'table','headers':headers,'rows':[{'cells':r} for r in rows],'source_ids':source_ids}
changes=[]
def change(id,reason):changes.append({'id':id,'reason':reason})
# First three topics: full base text, repaired conceptual bridge, modest reordering.
concept=m['sections'][0]
a=n('dd-01');sentences=re.split(r'(?<=\.) ',a['text']);a['text']='\n\n'.join([' '.join(sentences[:-1]),sentences[-1]])
concept['units']=[unit('conceito-definicao','Conceito, sanção penal e natureza pública',[a,n('dd-03'),n('dd-09')]),unit('conceito-sancoes','Penas, medidas de segurança e reparação',[n('dd-02'),n('nota-vias'),n('lei-32'),n('lei-96')]),unit('conceito-aspectos','Aspectos formal, material e sociológico',[p('dd-10','O Direito Penal pode ser compreendido sob os aspectos formal, material e sociológico.',source_ids=['dd-10']),n('tabela-aspectos')]),unit('conceito-autores','Definições dos autores: o enfoque formal',[p('dd-04','Autores renomados forneceram definições formais que destacam seu foco na lei e na sanção.',source_ids=['dd-04']),n('tabela-autores')]),unit('conceito-controle','Controle social e intensidade da resposta penal',[n('dd-14'),n('nota-sancao')])]
concept['units'][-1]['nodes'][0]['text']=n('dd-14')['text'].replace('O que diferencia a norma penal das demais é a espécie de consequência jurídica (pena privativa de liberdade).','O que diferencia a norma penal das demais é a espécie de consequência jurídica: a sanção penal, que pode envolver pena privativa de liberdade, mas não se reduz a ela.')
change('dd-14','Corrigida a restrição da consequência penal à prisão: CP, arts. 32 e 96. Mantida a explicação de controle social.')
change('dd-04','Restaurada a ligação entre os autores e o enfoque formal (lei e sanção); referência de Batista permanece no rodapé bibliográfico.')
chars=m['sections'][1];chars['units'][0]['nodes']+=chars['units'][1]['nodes'];chars['units']=chars['units'][:1]
bens=sec('bens','OBJETO DE PROTEÇÃO: BENS JURÍDICOS','DD, p. 7',[unit('bens-introducao','O que o Direito Penal protege',[n('dd-24')]),unit('bens-constituicao','Constituição: orientação e limites',[n('dd-25'),n('dd-26'),n('limites-constitucionais')])])
# Contiguous, exhaustive segmentation of the newly restored portion, including headings.
anchors=[('evo-abertura','d) EVOLUÇÃO DO DIREITO PENAL:'),('evo-privada','O primeiro período diz respeito'),('evo-divina','O segundo período refere-se'),('evo-publica','O terceiro e último período'),('evo-humanitario','Como resposta direta à barbárie'),('evo-cientifico','Depois, surge o Período Científico'),('evo-transicao','Aprofundando...'),('escola-classica','A Escola Clássica,'),('escola-positiva','A Escola Positivista'),('escola-ecletica','Já as Escolas Ecléticas'),('evo-contemporaneo','Período Contemporâneo:'),('evo-brasil','No que concerne à evolução'),('prova-ce','Caiu em prova Delegado PC/CE 2025!'),('func-intro','e) FUNÇÕES DO DIREITO PENAL:'),('func-mediata','a) Missão mediata:'),('func-imediata','b) Missão imediata:'),('func-roxin','Funcionalismo teleológico (moderado)'),('prova-sp','Caiu em prova Delegado SP/2023!'),('func-jakobs','Funcionalismo sistêmico (radical)'),('func-tabela','APROFUNDANDO: vamos a uma tabelinha'),('func-outras','Outras funções do Direito Penal (Masson):'),('func-costumes','Função criadora ou modificadora de costumes.'),('func-simbolica','Simbólica –'),('prova-ro','CAIU na prova de Delegado de Polícia PCRO/2022'),('func-motivadora','Motivadora de comportamento'),('func-reducao','Redução da violência estatal'),('func-promocional','Promocional de transformação social'),('class-titulo','B) CLASSIFICAÇÕES DO DIREITO PENAL'),('class-1','1. Direito Penal Fundamental'),('class-2','2. Direito Penal Complementar'),('class-3','3. Direito Penal Comum'),('class-4','4. Direito Penal Especial'),('class-5','5. Direito Penal Geral'),('class-6','6. Direito Penal Local'),('class-7','7. Direito Penal Objetivo'),('class-8','8. Direito Penal Subjetivo'),('class-9','9. Direito Penal Substantivo'),('class-10','10. Direito Penal Adjetivo'),('intervencao','#DICA DD: O Direito Penal de Intervenção'),('intervencao-sintese','Em suma, o objetivo é transferir')]
spans=[];cursor=0
for id,anchor in anchors:
 start=flat.index(anchor,cursor);spans.append({'id':id,'start':start,'anchor':anchor});cursor=start+len(anchor)
for i,b in enumerate(spans):
 b['end']=spans[i+1]['start'] if i+1<len(spans) else len(flat);b['text']=flat[b['start']:b['end']].strip();b['sha256']=hashlib.sha256(b['text'].encode()).hexdigest()
source={b['id']:b for b in spans}
def src(id,kind='paragraph',text=None,**kw):return p(id,source[id]['text'] if text is None else text,kind,source_ids=[id],**kw)
def clean(id,prefix):return source[id]['text'].removeprefix(prefix).strip()
evo=sec('evolucao','EVOLUÇÃO DO DIREITO PENAL','DD, pp. 7–9',[
 unit('evolucao-origem','Origem das regras de convivência',[src('evo-abertura',text=clean('evo-abertura','d) EVOLUÇÃO DO DIREITO PENAL:'))]),
 unit('evolucao-vingancas','Vinganças privada, divina e pública',[table('quadro-vingancas',['Período','Explicação'],[[label,source[id]['text']] for id,label in [('evo-privada','Vingança privada'),('evo-divina','Vingança divina'),('evo-publica','Vingança pública')]],['evo-privada','evo-divina','evo-publica'])]),
 unit('evolucao-humanitario','Períodos humanitário e científico',[src('evo-humanitario'),src('evo-cientifico')]),
 unit('evolucao-escolas','Escolas penais: fundamentos e consequências',[src('escola-classica',text=source['escola-classica']['text'].replace(', como aponta seu documento,', '')),src('escola-positiva'),src('escola-ecletica',text='As escolas ecléticas buscam conciliar aspectos das escolas Clássica e Positiva. A Terza Scuola italiana é uma dessas tendências. Em vez de equipará-la à defesa clássica do livre-arbítrio, destaque seu modelo dualista: penas ligadas à responsabilidade e medidas de segurança ligadas à periculosidade. Seus expoentes incluem Alimena, Carnevale e Impallomeni. A conciliação permite tratar a resposta ao delito para além de uma finalidade exclusivamente retributiva.'),src('prova-ce',kind='exam_reference',title='Cebraspe · PC/CE 2025 · questão 22',text='A terceira escola, também chamada de escola eclética, buscou superar o antagonismo entre as escolas clássica e positiva, mantendo a estrutura dogmática da imputabilidade e introduzindo as medidas de segurança para os inimputáveis.',answer='Alternativa E — gabarito definitivo do caderno 084_PC_CE_001_01.',comment='O ponto cobrado é a conciliação entre imputabilidade e medidas de segurança. Compare esse modelo com o livre-arbítrio da Escola Clássica e com o determinismo da Escola Positiva.',url='https://cdn.cebraspe.org.br/concursos/PC_CE_25_DELEGADO/arquivos/084_PC_CE_001_01.pdf#page=4',key_url='https://cdn.cebraspe.org.br/concursos/PC_CE_25_DELEGADO/arquivos/Gab_Definitivo_084_PC_CE_001_01.pdf')]),
 unit('evolucao-contemporanea','Período contemporâneo e percurso brasileiro',[src('evo-contemporaneo'),src('evo-brasil'),p('nota-historia','As fases acima são uma periodização didática. A referência genérica à vingança privada no Brasil anterior à colonização não deve ser lida como descrição uniforme de todos os povos indígenas. O percurso brasileiro apresentado aqui é o recorte colonial do texto-base.','callout',title='Alcance do quadro histórico')])])
change('escola-classica','Removida apenas a expressão metatextual “como aponta seu documento”.')
change('escola-ecletica','Corrigida a equivalência indiscriminada escolas ecléticas = Terza Scuola e o vínculo simplista ao livre-arbítrio. Horta e Romero, TRF1 2024, p. 91.')
change('evo-transicao','Chamamento promocional substituído pelo subtítulo Escolas penais; sem conteúdo doutrinário suprimido.')
# Functionalism: explanatory paragraphs remain, comparison explicitly separated by criterion.
mediata=clean('func-mediata','a) Missão mediata:')
mediata=mediata.replace('Instrumento de Controle Social','**Instrumento de Controle Social**').replace('Limitação ao poder de punir estatal ou Função de Garantia','**Limitação ao poder de punir estatal ou Função de Garantia**')
mediata=mediata.replace('Limitação ao poder','\n\nLimitação ao poder').replace('**Limitação','\n\n**Limitação').replace('Para Franz','\n\nPara Franz').replace('Se, de um lado','\n\nSe, de um lado')
roxin=clean('func-roxin','Funcionalismo teleológico (moderado) – Claus Roxin (Predomina)')
jakobs=clean('func-jakobs','Funcionalismo sistêmico (radical) – Günter Jakobs')
# Split thesis of norm confirmation from enemy theory, preserving words and marking attribution.
split=jakobs.index('E, ainda, entende ele')
j1=jakobs[:split].strip();j2=jakobs[split:].strip()
attrs=[['Finalidade','Proteção de bens jurídicos indispensáveis; não visa impor valores éticos ou morais.','Confirmação da vigência da norma penal e das expectativas normativas.'],['Limites e relação com o sistema','Moderado: limites impostos pelo próprio Direito Penal e pelos demais ramos. Dualista: convive com os demais ramos e reconhece o sistema jurídico em geral.','Radical e monista: apresentado como um sistema próprio de regras e valores, centrado na manutenção do sistema normativo. Esses rótulos doutrinários não dispensam os limites constitucionais brasileiros.'],['Política criminal e sociedade','De política criminal: aplica a lei considerando os anseios sociais e se adapta à sociedade em que se insere. Racional teleológico: orientado pela razão e pela finalidade.','Sistêmico: autônomo, autorreferente (busca referências e conceitos no próprio sistema) e autorreprodutivo. A fórmula didática é a adaptação social às expectativas normativas.']]
functions=sec('funcoes','FUNÇÕES DO DIREITO PENAL','DD, pp. 9–12',[
 unit('funcoes-mediatas','Missão mediata: controle social e garantia',[src('func-intro',text=clean('func-intro','e) FUNÇÕES DO DIREITO PENAL:')),src('func-mediata',text=mediata),p('lei-1','Art. 1º - Não há crime sem lei anterior que o defina. Não há pena sem prévia cominação legal.','law',title='CP, art. 1º — legalidade',url='https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848compilado.htm')]),
 unit('funcoes-imediatas','Missão imediata: Roxin e Jakobs',[src('func-imediata',text='A missão imediata é explicada pelas duas correntes de funcionalismo penal a seguir.'),p('roxin-label','**Funcionalismo teleológico (moderado) — Claus Roxin.**'),src('func-roxin',text=roxin),src('prova-sp',kind='source_exam',title='PC/SP 2023 · referência presente no texto-base',text=source['prova-sp']['text'].replace('Caiu em prova Delegado SP/2023! ','')),p('jakobs-label','**Funcionalismo sistêmico (radical) — Günther Jakobs.**'),src('func-jakobs',text=j1),table('func-tabela',['Critério','Roxin','Jakobs'],attrs,['func-tabela'])]),
 unit('funcoes-inimigo','Direito Penal do Inimigo: descrição da tese',[p('inimigo-intro','Na formulação do **Direito Penal do Inimigo**, atribuída a Jakobs, a distinção entre cidadão e inimigo conduz à antecipação da intervenção e à redução de garantias. Os parágrafos seguintes descrevem essa tese.'),p('func-jakobs-inimigo',j2,source_ids=['func-jakobs']),p('inimigo-limite','!!A descrição da tese não autoriza retirar direitos fundamentais de alguém no Brasil.!! A Constituição assegura garantias como a vedação da tortura e o devido processo legal. Não se deve converter a fórmula “não-cidadão = não tem direitos” em regra jurídica vigente.','callout',title='Tese doutrinária e direito brasileiro'),p('lei-5','Art. 5º, III - ninguém será submetido a tortura nem a tratamento desumano ou degradante;\nLIV - ninguém será privado da liberdade ou de seus bens sem o devido processo legal;','law',title='CF, art. 5º, III e LIV — limites constitucionais',url='https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm')]),
 unit('funcoes-costumes','Função criadora ou modificadora de costumes',[src('func-costumes')]),
 unit('funcoes-simbolica','Função simbólica, inflação legislativa e hipertrofia',[src('func-simbolica'),src('prova-ro',kind='source_exam',title='PC/RO 2022 · referência presente no texto-base')]),
 unit('funcoes-outras','Motivação, redução da violência e transformação social',[table('outras-funcoes',['Função','Explicação'],[[name,source[id]['text']] for id,name in [('func-motivadora','Motivadora'),('func-reducao','Redução da violência estatal'),('func-promocional','Promocional')]],['func-motivadora','func-reducao','func-promocional'])])])
change('func-tabela','Reorganização por critério, com as características de ambas as correntes. A fórmula “não tem direitos” recebe qualificação constitucional em 5.3, e não é reproduzida como regra brasileira. Rótulos radical/monista não significam poder penal brasileiro ilimitado.')
change('func-imediata','Removido o chamamento “anote esses nomes na testa”; função de ponte mantida.')
change('func-outras','Rótulo convertido nos subtítulos 5.4–5.6; autoria Masson mantida na referência de origem.')
# Classifications grouped by the question each distinction answers; no condensed definitions.
class_units=[]
for a,b,id,title,labels in [(1,2,'class-sistema','Normas fundamentais e complementares',['Fundamental (primário)','Complementar (secundário)']),(3,4,'class-destinatarios','Destinatários: comum e especial',['Comum','Especial']),(5,6,'class-territorio','Âmbito territorial: geral e local',['Geral','Local']),(7,8,'class-objetivo','Normas e poder de punir: objetivo e subjetivo',['Objetivo','Subjetivo']),(9,10,'class-substantivo','Conteúdo e processo: substantivo e adjetivo',['Substantivo (material)','Adjetivo (formal)'])]:
 rows=[]
 for num,label in zip([a,b],labels):
  text=source[f'class-{num}']['text'].split(':',1)[1].strip().rstrip(';').rstrip('.')+'.'
  if num==8:text='é o direito de punir (ius puniendi), pertencente ao Estado. A violação da lei penal faz surgir a pretensão punitiva relativa ao fato concreto; o poder estatal de estabelecer normas e sanções existe em abstrato antes dessa violação.'
  if num==9:text='é o Direito Penal material, propriamente dito, presente no Código Penal e também na legislação penal especial.'
  rows.append([label,text])
 class_units.append(unit(id,title,[table('quadro-'+id,['Classificação','Significado e exemplos'],rows,[f'class-{a}',f'class-{b}'])]))
class_units[2]['nodes'].append(n('lei-22'))
class_units[2]['nodes'][-1]['title']='CF, art. 22, I e parágrafo único — competência'
class_units[2]['nodes'][-1]['text']+='\nParágrafo único. Lei complementar poderá autorizar os Estados a legislar sobre questões específicas das matérias relacionadas neste artigo.'
class_units[4]['nodes'].append(p('formal-distincao','O adjetivo **formal** tem usos diferentes: no conceito formal de Direito Penal, olha-se para normas e sanções; na oposição substantivo/adjetivo, “formal” designa o Direito Processual Penal. O contexto determina o sentido.','callout',title='A mesma palavra, dois contextos'))
class_units.append(unit('class-intervencao','Direito de Intervenção: a proposta de Hassemer',[src('intervencao',text=clean('intervencao','#DICA DD:')),src('intervencao-sintese'),p('nota-intervencao','Trata-se de uma **proposta de política criminal**, não de uma descrição automática da legislação brasileira. A Lei de Improbidade é mencionada como aproximação didática a um regime sancionador sem prisão; isso não extingue crimes ambientais ou econômicos nem transforma toda sanção administrativa em sanção penal.','callout',title='Proposta doutrinária e exemplo brasileiro')]))
classif=sec('classificacoes','CLASSIFICAÇÕES DO DIREITO PENAL','DD, pp. 12–13',class_units)
change('class-8','Explicitada a diferença entre poder punitivo em abstrato e pretensão relativa ao caso; evitar impressão de inexistência do poder legislativo penal antes do crime.')
change('class-9','Corrigida leitura que restringia o Direito Penal material ao Código; inclui legislação especial.')
change('intervencao','Texto-base mantido com ressalva de que se trata de proposta. Formulação “sob autoridade judicial” permanece como apresentação didática da fonte, com revisão doutrinária aprofundada pendente.')
# Existing deeper treatment retained after the complete introductory chapter.
supp=copy.deepcopy(m['sections'][2]);supp['id']='aprofundamento';supp['title']='APROFUNDAMENTO: BEM JURÍDICO E LIMITES DA TUTELA';supp['reference']='DD, pp. 26–29';supp['collapsed']=True
supp['units']=[u for u in supp['units'] if u['id']!='bens-constituicao']
supp['units'][0]['nodes']=[x for x in supp['units'][0]['nodes'] if x['id']!='dd-24']
sections=[concept,chars,bens,evo,functions,classif,supp]
for i,s in enumerate(sections,1):
 s['number']=str(i)
 for j,u in enumerate(s['units'],1):u['number']=f'{i}.{j}'
m.update(edition='v3-em-revisao',title='Direito Penal — Noções iniciais',sections=sections,scope='Capítulo inicial: conceito, características, objeto, evolução, funções e classificações (DD, pp. 5–13). Aprofundamento complementar sobre bens jurídicos (pp. 26–29). Versão em revisão.',approved=False)
m['references'][0]['label']='Texto-base pessoal: DD — Noções iniciais e princípios, capítulo inicial, pp. 5–13; aprofundamento, pp. 26–29.'
m['references'] += [{'label':'PC/CE 2025, questão 22, caderno 084_PC_CE_001_01, p. 4. Referência conferida em 03/10/2026.','url':'https://cdn.cebraspe.org.br/concursos/PC_CE_25_DELEGADO/arquivos/084_PC_CE_001_01.pdf#page=4'},{'label':'PC/CE 2025, gabarito definitivo: questão 22, alternativa E.','url':'https://cdn.cebraspe.org.br/concursos/PC_CE_25_DELEGADO/arquivos/Gab_Definitivo_084_PC_CE_001_01.pdf'},{'label':'Horta e Romero, Revista do TRF1, ano 36, n. 2, 2024, p. 91: escolas penais e Terza Scuola.','url':'https://revista.trf1.jus.br/trf1/article/download/556/419/2617'},{'label':'Funções adicionais: classificação de Cleber Masson apresentada no texto-base, pp. 11–12. Referências PC/SP 2023 e PC/RO 2022 ainda sem cotejo integral do caderno.','url':None}]
# Semantic emphasis is explicitly selected per passage, never a global word regex.
emphasis={
'dd-01':['conjunto de princípios e regras','crime e a contravenção penal','“sanção penal” é gênero','as penas e as medidas de segurança'],
'dd-03':['ramo do Direito Público','Estado é o titular do direito de punir','sujeito passivo','de forma mediata'],
'dd-02':['pena é a 1ª via','medida de segurança é a 2ª','reparação do dano é a 3ª'],
'dd-04':['definições formais','lei e na sanção'],
'dd-09':['expressão Direito Penal','art. 22, I'],
'dd-14':['controle social','soldado de reserva','sanção penal'],
'dd-15':['ciência cultural, normativa, valorativa, finalista','predominantemente sancionatória','fragmentária'],
'dd-24':['desenvolvimento pessoal de seu titular','todo o corpo social'],
'dd-25':['valores garantidos na Lei Fundamental','limites da atividade punitiva'],
'dd-26':['NÃO se pode falar em discricionariedade ampla e irrestrita'],
'evo-abertura':['regras de conduta','evolui conjuntamente'],
'evo-humanitario':['Período Humanitário','século XVIII','Cesare Beccaria','humanização das penas','proporcionalidade, a legalidade, a publicidade e a moderação','finalidade preventiva'],
'evo-cientifico':['Período Científico','século XIX','Escola Clássica e a Positivista'],
'escola-classica':['livre-arbítrio','"ente jurídico"','essencialmente retributivo','Francesco Carrara','legalidade','culpabilidade e a responsabilidade moral'],
'escola-positiva':['Nega o livre-arbítrio','fatores biológicos, psicológicos e sociais','do crime para o criminoso','defesa social','Cesare Lombroso, Enrico Ferri, Raffaele Garofalo'],
'escola-ecletica':['Terza Scuola italiana','modelo dualista','penas ligadas à responsabilidade','medidas de segurança ligadas à periculosidade'],
'evo-contemporaneo':['constitucionalização do Direito Penal','direitos fundamentais','ressocialização'],
'evo-brasil':['Ordenações Afonsinas','Ordenações Manuelinas','Ordenações Filipinas'],
'func-roxin':['proteção dos bens jurídicos mais relevantes','não deve incidir o direito penal','valores éticos, morais','função exclusiva'],
'func-jakobs':['vigência do sistema','norma continua vigorando e deve ser obedecida','expectativa garantida'],
'func-jakobs-inimigo':['deliberada e reiteradamente','grave e duradoura','não-cidadão','Direito Penal do Inimigo','eliminar o risco','antes mesmo'],
'func-costumes':['Disseminação ético-social de valores','função educativa','doutrina divergir','interação social e não por coação'],
'func-simbolica':['somente na mente dos cidadãos e governantes','credibilidade do direito penal','Inflação legislativa','direito penal de emergência','Hipertrofia do Direito Penal','desproporcional e injustificadamente'],
'intervencao':['Hassemer','bens jurídicos individuais','perigo concreto','sistema intermediário','sem privação de liberdade','Lei de Improbidade Administrativa'],
'intervencao-sintese':['regime mais flexível e célere','garantias individuais'],
'dd-31':['fundamento e o limite do poder punitivo estatal'],
'dd-32':['valor ou interesse','imprescindível','juízo de valor positivo'],
'dd-37':['bens jurídicos indispensáveis'],
'dd-50':['Espiritualização','Liquefação','antecipação da tutela penal']}
row_emphasis={
'dd-11':['normas','infrações penais','sanções'], 'dd-12':['altamente reprováveis ou danosos','bens jurídicos indispensáveis'],'dd-13':['controle social','disciplina social'],
'dd-16':['normas e princípios','dogmática jurídico-penal'],'dd-17':['“dever ser”','“ser”'],'dd-18':['lei penal','Direito positivo'],'dd-19':['escala de valores','critérios e princípios'],'dd-20':['proteção de bens jurídicos fundamentais'],'dd-21':['predominantemente sancionador','constitutivo'],'dd-22':['não tutela todos os valores ou interesses','mais importantes'],
'dd-27':['Orienta o legislador','mandados de criminalização','obrigatoriedade'],'dd-28':['Impede','direitos fundamentais']}
def mark(text,phrases):
 for phrase in sorted(phrases,key=len,reverse=True):
  if phrase in text:text=text.replace(phrase,'**'+phrase+'**',1)
 return text
for s in sections:
 for u in s['units']:
  for node in u['nodes']:
   if 'text' in node:node['text']=mark(node['text'],emphasis.get(node['id'],[]))
   for row in node.get('rows',[]):
    row['cells']=[mark(c,row_emphasis.get(row.get('id'),[])) for c in row['cells']]
   for item in node.get('items',[]):item['text']=mark(item['text'],row_emphasis.get(item['id'],[]))
# Mark key relations in whole-table rows whose original text has no standalone node id.
for s in sections:
 for u in s['units']:
  for node in u['nodes']:
   if node['id']=='quadro-vingancas':
    for row,phrases in zip(node['rows'],[['resposta da vítima','reação desproporcional'],['sacerdotes','purificação da alma'],['monarca','segurança do soberano']]):row['cells'][1]=mark(row['cells'][1],phrases)
   if node['id'].startswith('quadro-class-'):
    for row in node['rows']:row['cells'][1]=mark(row['cells'][1],['genericamente','legislação penal extravagante','indistintamente a todas as pessoas','pessoas determinadas','todo o território nacional','lei complementar','questões específicas','leis penais em vigor','direito de punir','Direito Penal material','direito processual penal'])
# Dates / visual highlights used sparingly, on propositions rather than keyword dumping.
for s in sections:
 for u in s['units']:
  for node in u['nodes']:
   if node['id']=='nota-vias':node['text']=node['text'].replace('Não é uma terceira espécie de pena no rol do art. 32 do CP.','!!Não é uma terceira espécie de pena no rol do art. 32 do CP.!!')
   if node['id']=='dd-02':node['text']='=='+node['text'].replace('**','')+'=='
# Readability corrections and explicitly traceable repairs in the retained supplement.
more_marks={
'dd-29':['apenas e tão somente','lesão ou o perigo de lesão'], 'dd-30':['não pode incriminar pensamentos ou intenções','valores constitucionais','direito fundamental à vida'],
'dd-36':['vida segura e livre','direitos humanos e fundamentais'], 'dd-37':['missão precípua','proteção de bens jurídicos fundamentais'],
'dd-38':['fragmentário','lesões de maior gravidade'], 'dd-39':['limitação do poder punitivo'], 'dd-40':['critério material ou substancial','lesa ou expõe a perigo'],
'dd-41':['relevância jurídico-penal','dano ou ao menos exposição à situação de perigo'], 'dd-46':['valor abstrato'], 'dd-52':['bem jurídico aparente','ausência de um efetivo bem jurídico'],
'dd-53-c':['impossível','soma de vários bens jurídicos individuais'], 'dd-60':['orienta o legislador','protege o cidadão','ofensa concreta ou potencial']}
for section in sections:
 for u in section['units']:
  for node in u['nodes']:
   if node['id']=='dd-41':node['text']=node['text'].replace('Para que uma conduta seja considerada penalmente ilícita e legítima em um Estado Democrático de Direito','Para que a criminalização de uma conduta seja legítima em um Estado Democrático de Direito')
   if node['id']=='dd-51':node['text']='**Aplicação em provas:** os itens da PF 2025 abaixo exploram diferentes aspectos do bem jurídico. Eles permitem estudar a forma de cobrança, mas esse conjunto reduzido não demonstra, sozinho, uma tendência estatística das bancas.'
   if 'text' in node:
    node['text']=mark(node['text'],more_marks.get(node['id'],[]))
    for prefix in {'evo-abertura':['Para entender','Nesse contexto'], 'func-costumes':['É uma função','Esta função'], 'func-simbolica':['Enquanto os governados','Geralmente é manifestada','**Inflação legislativa**','**Hipertrofia do Direito Penal**'], 'func-jakobs-inimigo':['Ao delinquente-cidadão','Essa vertente'], 'intervencao':['Esse sistema','A proposta enfrenta']}.get(node['id'],[]):
     node['text']=node['text'].replace(prefix,'\n\n'+prefix)
   for row in node.get('rows',[]):
    if row.get('id')=='dd-48':row['cells'][1]=row['cells'][1].replace(' (a pessoa que pode dispor dele)','')+' A titularidade individual não significa disponibilidade irrestrita do bem.'
    if row.get('id')=='dd-53-b':row['cells'][1]=row['cells'][1].replace('a autenticidades das moedas','a autenticidade das moedas')
    if node['id']=='tabela-especies':row['cells'][0]=row['cells'][0].replace('Supraindividuais/Transindividuais','Supraindividuais / Transindividuais');row['cells'][1]=mark(row['cells'][1],['titulares determináveis','titulares indetermináveis','não significa disponibilidade irrestrita'])
    if node['id']=='tabela-ofensa':row['cells'][1]=mark(row['cells'][1],['lesão ou exposição a perigo de lesão','Não há crime sem resultado jurídico','ofensa a bem jurídico-penal'])
    if node['id']=='tabela-reais-aparentes':row['cells'][1]=mark(row['cells'][1],['somatório de integridades físicas individuais','não podem ser fracionados em bens individuais somados'])
change('dd-41','Corrigida impropriedade textual: quem deve ser legítima é a criminalização, não a conduta ilícita.')
change('dd-48','Retirada equivalência entre titular determinável e disponibilidade; a vida exemplifica a necessidade da ressalva.')
change('dd-51','Substituída afirmação genérica de modinha por descrição do pequeno conjunto efetivamente examinado, sem inferir frequência estatística.')
change('dd-53-b','Correção de concordância: autenticidade das moedas.')
save('apresentacao.json',m)
save('fonte_segmentos_v3.json',{'scope':'Porção d) evolução até o fim do capítulo, pp. 7–13','segments':spans})
save('decisoes_v3.json',{'approval_scope':'Autorização de operação no GitHub; conteúdo e formato NÃO aprovados.','changes':changes,'source_only_labels':['evo-transicao','func-outras','class-titulo'],'pending':['Revisão doutrinária aprofundada do modelo de Hassemer, em especial autoridade judicial.','Cotejo oficial dos excertos SP/2023, RO/2022 e AM/2022.','Restante da amostra de 58 páginas e comparação integral com apostilas antigas.','Ampliação do banco por banca/ano: ainda não realizada nesta edição.']})
print('v3 model',len(sections),'sections',sum(len(s['units']) for s in sections),'units',len(spans),'source spans')
