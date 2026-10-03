from pathlib import Path
from html import escape
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle

OUT=Path('/workspace/scratch/498175f9d04d/output/pdf/Proposta_material_integrado_DD_Gran.pdf')
OUT.parent.mkdir(parents=True,exist_ok=True)
for name,file in [('Sans','DejaVuSans.ttf'),('SansB','DejaVuSans-Bold.ttf'),('Serif','DejaVuSerif.ttf')]:
 pdfmetrics.registerFont(TTFont(name,'/usr/share/fonts/truetype/dejavu/'+file))
pdfmetrics.registerFontFamily('Sans',normal='Sans',bold='SansB',italic='Sans',boldItalic='SansB')
W,H=A4; M=46; CW=W-2*M
NAVY=colors.HexColor('#163950'); BLUE=colors.HexColor('#245E90'); INK=colors.HexColor('#263642'); MUTED=colors.HexColor('#667785'); RED=colors.HexColor('#993F54'); GREEN=colors.HexColor('#2E7164'); AMBER=colors.HexColor('#FFF2BD'); PALE=colors.HexColor('#EEF4F8'); LINE=colors.HexColor('#D8E1E7')
c=canvas.Canvas(str(OUT),pagesize=A4);c.setTitle('Material integrado - diagnóstico DD e Gran');c.setAuthor('Legal Tutor OS')
styles={
 'body':ParagraphStyle('body',fontName='Sans',fontSize=10.3,leading=15,textColor=INK,spaceAfter=0),
 'small':ParagraphStyle('small',fontName='Sans',fontSize=8.4,leading=12,textColor=MUTED),
 'h2':ParagraphStyle('h2',fontName='SansB',fontSize=13.2,leading=18,textColor=NAVY),
 'cell':ParagraphStyle('cell',fontName='Sans',fontSize=9.1,leading=13,textColor=INK),
 'th':ParagraphStyle('th',fontName='SansB',fontSize=9.1,leading=13,textColor=colors.white),
}
y=0; page=0
def para(txt,style='body',x=M,width=CW,gap=10):
 global y
 p=Paragraph(txt,styles[style]);_,h=p.wrap(width,800);p.drawOn(c,x,y-h);y-=h+gap
def heading(txt):
 global y
 y-=5;para(txt,'h2',gap=9)
def box(label,txt,color=BLUE,bg=PALE):
 global y
 p=Paragraph(txt,styles['body']);_,h=p.wrap(CW-28,800);total=h+45
 c.setFillColor(bg);c.roundRect(M,y-total,CW,total,5,fill=1,stroke=0)
 c.setFillColor(color);c.rect(M,y-total,3,total,fill=1,stroke=0)
 c.setFont('SansB',9);c.drawString(M+14,y-18,label.upper())
 p.drawOn(c,M+14,y-total+12);y-=total+13
def table(headers,rows,widths):
 global y
 data=[[Paragraph(escape(v),styles['th']) for v in headers]]+[[Paragraph(v,styles['cell']) for v in row] for row in rows]
 t=Table(data,colWidths=widths,hAlign='LEFT');t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),NAVY),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),9),('RIGHTPADDING',(0,0),(-1,-1),9),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#F3F6F8')]),('LINEBELOW',(0,0),(-1,-1),0.4,LINE)]));_,h=t.wrap(CW,1000);t.drawOn(c,M,y-h);y-=h+13
def start(kicker,title,sub):
 global page,y
 if page:
  assert y>=53,(page,y)
  c.showPage()
 page+=1;c.setFillColor(BLUE);c.rect(0,H-7,W,7,fill=1,stroke=0)
 c.setFont('SansB',9);c.drawString(M,H-42,kicker.upper());c.setFont('Sans',8);c.setFillColor(MUTED);c.drawRightString(W-M,H-42,'LEGAL TUTOR OS  /  02 OUT 2026')
 c.setFillColor(NAVY);c.setFont('SansB',25);c.drawString(M,H-80,title)
 y=H-100;para(sub,'small',gap=17)
 c.setStrokeColor(LINE);c.line(M,40,W-M,40);c.setFont('Sans',8);c.setFillColor(MUTED);c.drawString(M,26,'Análise editorial e proposta de trabalho  |  Uso pessoal');c.drawRightString(W-M,26,f'{page:02d} / 07')

start('01  /  acesso e leitura','O material que vamos construir','Um caderno para aprender, revisar e treinar, tomando o DD como referência principal e o Gran como referência visual complementar.')
box('Direção proposta','<b>Teoria + lei + jurisprudência + exercícios no mesmo percurso.</b> O PDF será a principal superfície de estudo. A organização digital dará suporte à atualização, às revisões e à ampliação para outras carreiras.')
heading('O acesso funcionou')
para('Encontrei a pasta <b>Dedicação Delta 2026 G</b> na conta Fentanes e abri, pela Russgod, o <b>Extensivo 2025</b> e o <b>Mapa da Lei Seca</b> compartilhados. A pasta nova tem <b>39 PDFs</b>, distribuídos entre seis subpastas e a raiz.')
table(['Fonte','Escopo da análise'],[
 ('DD teoria de Penal','58 páginas: leitura editorial integral.'),
 ('Gran: duas amostras','11 + 23 páginas: leitura integral e revisão visual selecionada.'),
 ('DD Juris / Súmulas de Penal','15 + 13 páginas: conteúdo percorrido; fontes jurídicas verificadas apenas em pontos específicos.'),
 ('DD Legis: CP novo','282 páginas: extraídas; páginas 1-8 lidas, incluindo todo o bloco inicial do art. 1º.'),
 ('Orientações e metas','6 + 2 páginas: leitura da proposta de uso do curso.'),
 ('Acervo antigo','Comparação amostral da teoria, CP e Mapa. O curso inteiro não foi lido.'),
],[145,CW-145])
para('<b>Limite claro:</b> inventariar 39 PDFs não equivale a analisar 39 apostilas. A leitura editorial também não certifica a correção e a atualização de cada afirmação. As páginas citadas neste documento são as do PDF.','small')

start('02  /  diagnóstico editorial','O que manter e o que melhorar','A comparação usa assuntos coincidentes: ciências penais, legalidade e insignificância.')
table(['Referência','O que funciona','Como aprimorar'],[
 ('DD teoria','Explicação desenvolvida, distinções, quadros e provas intercaladas.','Reunir repetições; separar tentativa e resposta; comentar alternativas e limites da tese.'),
 ('DD Legis','Lei acompanhada de doutrina e perguntas. Art. 1º: p. 3-4.','Integrar ao ponto de aprendizagem; conservar um índice por artigo para revisar a lei.'),
 ('DD Juris','Regras, ressalvas e divergências. Insignificância: p. 4-15.','Ligar cada decisão ao fato, à data e ao órgão julgador; conferir a referência original.'),
 ('Gran sintético','Cores com função, quadros curtos e retomadas. Princípios p. 6-10; Ciências p. 7 e 12.','Aplicar essa clareza visual à explicação completa; usar tabelas quando a comparação ajudar.'),
],[82,202,CW-284])
heading('A lacuna não é simplesmente “ter poucas questões”')
para('A teoria DD contém questões completas, como nas p. <b>35, 50 e 56</b>, e uma discursiva com padrão de resposta nas p. <b>33-34</b>. Entretanto, muitos apontamentos já entregam a solução. Isso ajuda a explicar a matéria, mas oferece menos oportunidade de tentar resolver sozinho.')
para('As orientações DD encaminham a prática diária para o banco externo. As duas amostras do Gran também terminam remetendo à plataforma de questões. Para o seu objetivo, o caderno precisa incorporar uma seleção real, progressiva e comentada, sem depender desse acesso.')
box('Decisão editorial','Preservar a profundidade do DD e adotar uma hierarquia visual mais confortável. O resultado pretendido é um material de aprendizagem desenvolvido, acompanhado de formas curtas de revisão.',GREEN,colors.HexColor('#EAF5F0'))

start('03  /  conferência das fontes','Melhorar também a confiabilidade','Três achados concretos já foram confrontados com fontes oficiais. Eles não equivalem a uma auditoria jurídica completa.')
heading('01. Referência de jurisprudência trocada')
para('<b>DD teoria, p. 36; DD Juris, p. 5.</b> O trecho sobre restituição do bem furtado cita o Tema 1208 e o RMS 68.504/SC. A base oficial vincula a tese ao <b>Tema 1205</b>, REsp 2.062.375/AL e REsp 2.062.095/AL. O RMS citado trata de credenciamento de leiloeiros. [1-2]')
box('Consequência para a organização','A referência errada aparece em dois materiais. A concordância entre eles não é confirmação independente: precisamos rastrear o precedente de origem.',RED,colors.HexColor('#FBEEF1'))
heading('02. Código indicado incorretamente')
para('<b>DD Legis novo e antigo, p. 4; Mapa antigo, p. 9.</b> O exemplo de ato obsceno aponta para o art. 233 do CPP. O dispositivo pertinente é o <b>art. 233 do Código Penal</b>. [3]')
heading('03. Ressalva relevante ausente no resumo')
para('<b>Gran Princípios, p. 10.</b> A lista de não aplicação da insignificância traz contrabando e ressalva medicamentos, mas não inclui a hipótese de cigarros do <b>Tema 1143</b>, julgado em 2023. O complemento precisa trazer seus limites, a reiteração e a modulação, sem transformar o precedente em regra automática. [4]')
heading('Também ficaram registradas pendências editoriais')
para('A teoria DD anuncia dois fundamentos e enumera três (p. 50-51). Nas velocidades do Direito Penal, há uma inconsistência de atribuição entre as p. 20 e 21. O primeiro caso admite correção de contagem; o segundo exige cotejo doutrinário antes da redação.')
para('Fontes [1-4] e links verificáveis estão na página 7. As correções foram registradas na análise; os PDFs originais não foram modificados.','small')

start('04  /  integração por assunto','Uma base, vários usos','O índice por tema orienta a aprendizagem; o índice por artigo permite retomar a lei. Ambos conduzem à mesma explicação.')
table(['Bloco','Passagens já relacionadas','Destino no caderno'],[
 ('Ciências penais','DD p. 13-15; Gran Ciências p. 6-7 e 19-20; Mapa p. 6-7.','Explicação, comparação de objeto/método e um exemplo visto pelas três disciplinas.'),
 ('Legalidade e costumes','DD p. 24-25 e 50-52; DD CP p. 3-4.','Dispositivo oficial + sentido da regra + quatro garantias + aplicações.'),
 ('Insignificância','DD p. 34-48; DD Juris p. 4-15; súmulas pertinentes.','Requisitos, situações, exceções e divergências contextualizadas; treino de casos.'),
 ('Conflito de normas','DD p. 32-34, hoje dentro de subsidiariedade.','Bloco próprio com ponte explicativa: os dois usos da palavra não são idênticos.'),
],[109,198,CW-307])
heading('Como o estudo progride')
para('<b>Compreender:</b> explicação contínua, lei pertinente, exemplo e retomadas breves entre parênteses. A forma da página acompanha o assunto; nem todo trecho precisa virar uma caixa ou uma tabela.')
para('<b>Recuperar e distinguir:</b> perguntas específicas; depois questões que contrapõem conceitos próximos. A resposta aparece após a tentativa. Cartões de revisão derivam das mesmas perguntas.')
para('<b>Aplicar e produzir:</b> casos, questões oficiais, respostas discursivas e falas curtas com critérios de correção. As peças entram quando os pressupostos materiais e processuais estiverem construídos.')
para('<b>Expandir:</b> a base comum recebe complementos para Delegado estadual/PF, MP estadual/federal, cartórios/ENAC e demais carreiras. O recorte do DD não define a sua escolha de carreira.')
para('Questões antigas desde 2010 continuam úteis, preservando o gabarito histórico e identificando alterações. A dificuldade inicialmente estimada será ajustada pelo seu desempenho.','small')

start('05  /  ensaio de diagramação','Restituição e insignificância','Exemplo editorial curto, com redação própria e fonte conferida. Demonstra o formato; não constitui unidade curricular validada.')
box('A ideia central','Devolver imediatamente tudo o que foi subtraído <b>não basta, isoladamente</b>, para reconhecer a insignificância no furto. Essa é a orientação do STJ no Tema 1205. [1, 5]')
heading('Entenda o raciocínio')
para('A devolução é uma circunstância a considerar. Ela não substitui a avaliação da ofensividade, da periculosidade social, da reprovabilidade e da lesão ao bem jurídico <b>(retome: recuperar o objeto e avaliar a gravidade do fato são análises diferentes)</b>. [5]')
box('Atenção à conclusão','A tese afasta a suficiência da devolução por si só. Ela não afirma que toda devolução impede a insignificância.',RED,colors.HexColor('#FBEEF1'))
heading('Tente responder antes de conferir')
para('<b>1. Recuperação direta.</b> A restituição imediata e integral resolve, sozinha, a análise da insignificância?')
para('<b>2. Aplicação.</b> Uma afirmação diz que o objeto recuperado torna o furto automaticamente insignificante. Qual é o salto no raciocínio?')
para('<b>3. Fala curta.</b> Explique em duas frases por que a devolução não encerra a análise. Cite o tribunal e a tese pertinente.')
for i in range(3):
 c.setStrokeColor(LINE);c.line(M,y-5-i*17,W-M,y-5-i*17)
y-=64
box('Confira depois da tentativa','<b>1.</b> Não. <b>2.</b> Transforma uma circunstância em conclusão automática. <b>3.</b> A resposta deve identificar a insuficiência da restituição isolada e a necessidade de examinar o caso, vinculando a orientação ao Tema 1205 do STJ.',GREEN,colors.HexColor('#EAF5F0'))
para('Perguntas autorais para demonstrar o formato; não são questões de concurso. No caderno de treino, comentários extensos podem ficar na página seguinte. Paleta acompanhada de rótulos para funcionar também em impressão cinza.','small')

start('06  /  execução','O que fica em cada lugar','Você estuda o material. A estrutura interna mantém as versões, as fontes e as conexões entre assuntos.')
table(['Ferramenta','Papel proposto'],[
 ('PDF','Caderno principal: leitura, impressão, anotações e uso offline. Data de revisão e versão visíveis.'),
 ('Google Drive','Originais e referências, mantendo as pastas que você organizou; futuras edições para consulta.'),
 ('GitHub','Fonte editável, evidências, relações entre tópicos e histórico de correções. Sem inserir apostilas comerciais no repositório.'),
 ('Notion','Entrada simples: unidade atual, próximas revisões, dúvidas e links para o material.'),
 ('Actions, depois','Verificar referências e gerar arquivos. Automação não certifica validade jurídica.'),
],[100,CW-100])
heading('O que já está concluído nesta rodada')
para('Acesso às duas contas, inventário da pasta nova, leitura editorial principal, comparação amostral com o acervo antigo, achados verificados e mapa inicial de integração. O diagnóstico detalhado registra páginas e limites da análise.')
heading('O que falta antes da primeira unidade liberada')
para('<b>1.</b> Ligar questões e passagens, concluir lacunas de provas recentes e resolver conflitos jurídicos do escopo piloto, seguindo a auditoria já em andamento.<br/><b>2.</b> Cumprir a validação de cobertura, fontes, mapa e questões reservadas prevista no projeto.<br/><b>3.</b> Produzir uma unidade, conferir impressão e recolher sua avaliação de conforto visual.<br/><b>4.</b> Expandir o padrão por unidade e publicar atualizações com o menor retrabalho possível.')
box('Estado honesto','A proposta editorial está pronta para avaliação. A apostila completa e a plataforma não estão prontas. O formato desta amostra não recebeu ainda a sua aprovação de legibilidade.',GREEN,colors.HexColor('#EAF5F0'))

start('07  /  referências e limites','Como conferir esta análise','O diagnóstico completo e o registro de leitura acompanham o projeto. Nesta página, os principais documentos utilizados.')
def link(label,url):return '<link href="'+escape(url,quote=True)+'" color="#245E90">'+escape(label)+'</link>'
heading('Arquivos de origem no Drive')
refs=[('Pasta Dedicação Delta 2026 G','https://drive.google.com/drive/folders/1JD7EskwZaGvqZqwG0fRq2LT1lFfZEjX_'),('DD teoria - Noções iniciais e princípios','https://drive.google.com/file/d/1eOcrfOuLyOJYnXTwUaAvyovG7tPZZxhy/view'),('DD Legis - Código Penal','https://drive.google.com/file/d/1_1M60DUZlC62tVcDONJ77PXOt6s16bEa/view'),('DD Juris - Insignificância','https://drive.google.com/file/d/1ZIUepJGdKD6ZqJzUzXWyzjlzfjlahh1f/view'),('Gran - Princípios do Direito Penal','https://drive.google.com/file/d/13bgt4B9hD0TWgRk_9aukQMJo3NBrHCUe/view'),('Gran - Ciências penais','https://drive.google.com/file/d/13a1b6h5qZPJHg3oqbX1z0bEavZCv5bvJ/view')]
for label,url in refs:para(link(label,url),'small',gap=5)
heading('Conferência jurídica pontual em fontes oficiais')
web=[('[1] STJ - Tema repetitivo 1205','https://processo.stj.jus.br/repetitivos/temas_repetitivos/pesquisa.jsp?cod_tema_final=1205&cod_tema_inicial=1205&novaConsulta=true&tipo_pesquisa=T'),('[2] STJ - RMS 68.504/SC, inteiro teor','https://www.stj.jus.br/websecstj/cgi/revista/REJ.cgi/ITA?CodOrgaoJgdr=&SeqCgrmaSessao=&dt=20231016&formato=HTML&nreg=202200744520&salvar=false&seq=2365864&tipo=0'),('[3] Presidência da República - Código Penal, art. 233','https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848compilado.htm'),('[4] STJ - Tema repetitivo 1143','https://processo.stj.jus.br/repetitivos/temas_repetitivos/pesquisa.jsp?cod_tema_final=1143&cod_tema_inicial=1143&novaConsulta=true&tipo_pesquisa=T'),('[5] STJ - Restituição e insignificância, 04/12/2023','https://www.stj.jus.br/sites/portalp/Paginas/Comunicacao/Noticias/2023/04122023-Restituicao-imediata-e-integral-do-bem-furtado--por-si-so--nao-justifica-o-principio-da-insignificancia.aspx')]
for label,url in web:para(link(label,url),'small',gap=7)
heading('Escopo que permanece aberto')
para('Os demais 31 PDFs novos ficaram inventariados, sem leitura de conteúdo nesta rodada. O CP novo foi examinado parcialmente. O acervo antigo, Memorex/Iuris, o original do Notion e a versão exata do verticalizado do CÉREBRO do Magistrar não foram auditados integralmente.')
para('O texto de 58 páginas da teoria nova coincide, após normalização de espaços e rodapé, com a amostra que já estava disponível localmente. A novidade desta rodada é a leitura integral e o cotejo com as fontes reunidas agora. A teoria antiga do Extensivo 2025 tem 57 páginas e foi comparada por amostragem.')
para('<b>Diagramação</b> é o nome da organização visual que você descreveu. <b>Gramatura</b> se refere ao papel. Este ensaio usa A4, uma coluna, destaques moderados e texto com tamanho confortável; a sua leitura impressa deve orientar o ajuste final.','small')
assert y>=53,(page,y)
c.save();print(OUT)
