"""Render a single, numbered editorial model into HTML and printable PDF."""
import json,re,html
from pathlib import Path
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Table,TableStyle,KeepTogether,PageBreak
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
HERE=Path(__file__).resolve().parent;OUT=HERE.parents[2]/'output/pdf';OUT.mkdir(parents=True,exist_ok=True)
model=json.loads((HERE/'apresentacao.json').read_text());qa=json.loads((HERE/'recuperacao.json').read_text());bank=json.loads((HERE/'banco_questoes.json').read_text())['questions']
terms=['sanção penal','penas e as medidas de segurança','Direito Público','sujeito passivo','Franz von Liszt','Edmund Mezger','Hans Welzel','Juarez Cirino dos Santos','dever ser','predominantemente sancionador','constitutivo','fragmentário','fragmentária','objeto jurídico','objeto material','resultado jurídico','bens jurídicos indispensáveis','bens jurídicos relevantes','titulares determináveis','titulares indetermináveis','interesses metaindividuais','antecipação da tutela penal','Espiritualização','Liquefação','ratio legis','ultima ratio','NÃO','João Paulo Martinelli','Leonardo Schmitt de Bem']
rx=re.compile('|'.join(re.escape(t) for t in sorted(terms,key=len,reverse=True)),re.I)
def rich(t,pdf=False):
 parts=[];pos=0
 for m in rx.finditer(t):
  parts.append(html.escape(t[pos:m.start()]));txt=html.escape(m.group());parts.append(('<b><font color="#1264a3">'+txt+'</font></b>') if pdf else '<strong class="key">'+txt+'</strong>');pos=m.end()
 parts.append(html.escape(t[pos:]));return ''.join(parts).replace('\n','<br/>')
def node_html(n):
 kind=n['kind'];key=n['id']
 if kind=='table':
  head='<thead><tr>'+''.join('<th scope="col">'+html.escape(x)+'</th>' for x in n['headers'])+'</tr></thead>'
  rows=[]
  for row in n['rows']:
   rid=' id="'+row['id']+'"' if row.get('id') else ''
   rows.append('<tr'+rid+'>'+''.join(('<th scope="row">' if i==0 else '<td>')+rich(c)+('</th>' if i==0 else '</td>') for i,c in enumerate(row['cells']))+'</tr>')
  return f'<div class="table-wrap"><table id="{key}">{head}<tbody>'+''.join(rows)+'</tbody></table></div>'
 if kind=='list':return f'<ul id="{key}" class="content-list">'+''.join(f'<li id="{x["id"]}">{rich(x["text"])}</li>' for x in n['items'])+'</ul>'
 if kind=='law':return f'<details class="law" id="{key}" open><summary>LEI SECA · {html.escape(n["title"])}</summary><div><p>{rich(n["text"])}</p><small><a href="{n["url"]}">Texto oficial</a></small></div></details>'
 if kind=='callout':return f'<aside class="attention" id="{key}"><h4>{html.escape(n["title"])}</h4><p>{rich(n["text"])}</p></aside>'
 if kind=='quote':return f'<blockquote id="{key}"><p>{rich(n["text"])}</p>'+(f'<cite>{html.escape(n["citation"])}</cite>' if n.get('citation') else '')+'</blockquote>'
 if kind=='tip':return f'<aside class="tip" id="{key}"><span class="tag">ATENÇÃO</span><p>{rich(n["text"])}</p></aside>'
 if kind=='partial_exam':
  text=n['text'];prefix=''
  return f'<aside class="tip" id="{key}"><span class="tag">REFERÊNCIA DE PROVA · AM/2022</span><p>{rich(text[len(prefix):])}</p><small>Referência abreviada; caderno completo ainda a conferir.</small></aside>'
 if kind=='question_bank':
  pieces=[]
  for q in bank:
   key=q['id'];g='Certo' if q['answer']=='C' else 'Errado'
   answer='<p class="verdict"><b>Gabarito: '+g+'.</b></p>'
   if q['comment']:answer+='<p>'+rich(q['comment'])+'</p>'
   if q['precision']:answer+='<aside class="precision"><b>Cuidado na leitura</b><p>'+rich(q['precision'])+'</p></aside>'
   answer+=f'<a class="return" href="#{q["subtopic"]}">Rever a explicação</a>'
   choices=f'<fieldset><legend>Julgue o item</legend><label><input type="radio" name="{key}" value="C"> Certo</label><label><input type="radio" name="{key}" value="E"> Errado</label><button type="button" class="check" data-question="{key}">Conferir</button><span class="result" role="status" aria-live="polite"></span></fieldset>'
   pieces.append(f'<article id="{key}" class="exam" data-key="{q["answer"]}"><h4>Cebraspe · PF 2025 · Delegado · item {q["number"]}</h4><p class="difficulty">{q["difficulty"]} · dificuldade estimada</p><p class="stem">{rich(q["stem"])}</p>'+choices+f'<details class="answer"><summary>Ver gabarito e comentário</summary><div class="answer-body">{answer}</div></details></article>')
  return f'<div id="{n["id"]}">'+''.join(pieces)+'</div>'
 return f'<p id="{key}" class="body-text">{rich(n["text"])}</p>'
def review_html(section):
 cards=[]
 for q in [x for x in qa if x['section']==section]:
  checks=' · '.join(html.escape(x) for x in q['essential_elements'])
  cards.append(f'<article class="review-card" id="{q["id"]}"><span class="difficulty">{q["id"]} · {q["level"]}</span><h4>{html.escape(q["question"])}</h4><details class="answer"><summary>Ver resposta esperada</summary><div class="answer-body"><p>{rich(q["answer"])}</p><p class="essentials"><b>Elementos essenciais:</b> {checks}.</p><a class="return" href="#{q["target"]}">Rever este ponto</a></div></details></article>')
 return '<details class="retrieval"><summary>Perguntas de recuperação</summary><div class="retrieval-body"><p class="small">Perguntas autorais. Responda em voz alta antes de abrir a resposta; confira se cobriu os elementos essenciais.</p>'+''.join(cards)+'</div></details>'
chapters=[];toc=[]
for s in model['sections']:
 toc.append(f'<details open><summary><a href="#{s["id"]}">{s["number"]}. {s["title"]}</a></summary><ol>'+''.join(f'<li><a href="#{u["id"]}">{u["number"]} {html.escape(u["title"])}</a></li>' for u in s['units'])+'</ol></details>')
 units=''.join(f'<section id="{u["id"]}" class="unit"><h3><span>{u["number"]}</span> {html.escape(u["title"])}</h3>'+''.join(node_html(n) for n in u['nodes'])+'</section>' for u in s['units'])
 chapters.append(f'<details class="chapter" id="{s["id"]}" open><summary><span>{s["number"]}. {s["title"]}</span><small>{s["reference"]}</small></summary><div class="chapter-body">{units}{review_html(s["id"])}</div></details>')
refs=[]
for r in model['references']:
 text=html.escape(r['label']);refs.append('<li>'+('<a href="'+r['url']+'">'+text+'</a>' if r['url'] else text)+'</li>')
refs.append('<li><a href="'+bank[0]['key_url']+'">PF 2025: gabarito definitivo, Cargo 1.</a></li>')
css='''*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:90px}body{margin:0;background:#f3f6fa;color:#253342;font-family:system-ui,-apple-system,Segoe UI,sans-serif;font-size:16px;line-height:1.62}a{color:#155e92;text-underline-offset:3px}.hero{max-width:1200px;padding:30px 22px 18px;margin:auto}.eyebrow{font-size:12px;font-weight:750;letter-spacing:.14em;color:#1468a8}h1{margin:7px 0;font-size:32px;line-height:1.2;color:#183e66}.hero p{margin:8px 0;font-size:14px;color:#5d6e7e}.bar{position:sticky;top:0;z-index:20;background:white;border-bottom:1px solid #d8e2ec}.bar-inner{max-width:1200px;margin:auto;padding:10px 22px;display:flex;gap:12px;align-items:center;flex-wrap:wrap}.bar a{font-size:13px;font-weight:650}.bar button,.check{font:inherit;font-size:13px;border:1px solid #b4cce0;background:#fff;color:#1b4f78;border-radius:5px;padding:6px 11px;cursor:pointer}.layout{max-width:1200px;margin:20px auto 45px;padding:0 22px;display:grid;grid-template-columns:235px minmax(0,1fr);gap:24px}.outline{align-self:start;position:sticky;top:68px;max-height:calc(100vh - 88px);overflow:auto;font-size:12px;padding:4px 0}.outline>strong{display:block;color:#345b7c;margin-bottom:13px;letter-spacing:.05em}.outline details{margin-bottom:15px}.outline summary{font-weight:730;color:#234e73;cursor:pointer;line-height:1.4}.outline summary a{text-decoration:none}.outline ol{list-style:none;padding:0 0 0 10px;margin:10px 0}.outline li{margin:7px 0}.outline li a{text-decoration:none;color:#627489}.outline a:hover{color:#106bbe}.chapter{border:1px solid #ccddeb;border-radius:8px;overflow:clip;background:#fff;margin-bottom:22px}.chapter>summary{cursor:pointer;list-style:none;border-left:5px solid #1976ba;background:#e9f2fa;padding:17px 20px;display:flex;gap:12px;align-items:center;justify-content:space-between;color:#183f6d;font-size:19px;font-weight:780;line-height:1.35}.chapter>summary::after{content:'−';font-size:24px;font-weight:400}.chapter:not([open])>summary::after{content:'+'}.chapter>summary small{font-size:10px;font-weight:450;color:#71859a;white-space:nowrap}.chapter-body{padding:7px 24px 25px}.unit{padding:14px 0 9px;border-bottom:1px solid #e4edf3}.unit:last-of-type{border-bottom:0}h3{margin:4px 0 15px;font-size:18px;line-height:1.4;color:#144d80;font-weight:760;border-bottom:2px solid #c7e0f2;padding-bottom:8px}h3 span{color:#1379b5;margin-right:3px}.unit:target h3{background:#fff4cc}.body-text{margin:12px 0}.key{color:#1264a3;font-weight:750}.tip{margin:15px 0;padding:12px 15px;background:#fff5cc;border-left:4px solid #d1a82b}.tag{font-size:10px;font-weight:800;letter-spacing:.06em;color:#765612}.tip p{margin:7px 0}.tip small{color:#786f5c;font-size:11px}.attention{margin:14px 0;background:#f5f2fa;border:1px solid #e4dcf0;border-left:4px solid #8870b4;padding:12px 15px}.attention h4{margin:0 0 7px;font-size:14px;color:#51417a}.attention p{font-size:14px;margin:0}.law{margin:14px 0;border:1px solid #c5ddd5;background:#f0f8f4;border-radius:4px}.law>summary{padding:10px 13px;font-weight:750;color:#256b55;font-size:13px;cursor:pointer}.law>div{padding:0 15px 12px}.law p{margin:0;font-size:14px}.law small{font-size:10px}.table-wrap{margin:15px 0;overflow:auto}table{border-collapse:collapse;width:100%;font-size:14px;line-height:1.55;table-layout:fixed}thead th{color:#fff;background:#1975b8;font-weight:750;text-align:left}th,td{padding:11px 12px;border:1px solid #d3deeb;vertical-align:top;overflow-wrap:anywhere}thead th:first-child{width:27%}tbody th{font-weight:750;color:#244f78;text-align:left;background:#e8eff8}tbody td{background:#f8fafd}tbody tr:nth-child(even) td{background:#eef3fa}blockquote{margin:16px 0;padding:13px 17px;background:#f7f4fc;border-left:3px solid #9a82bc;font-size:15px}blockquote p{margin:0}cite{display:block;font-style:normal;font-size:10px;color:#746784;margin-top:9px}.content-list{padding-left:21px;margin:13px 0}.content-list li{padding:3px 0}.exam{border:1px solid #cfdfea;border-radius:5px;padding:15px;margin:18px 0}.exam h4{margin:0;color:#225b83;font-size:13px}.difficulty{font-size:10px;letter-spacing:.025em;color:#7e6b97;margin:6px 0}.stem{margin:12px 0}fieldset{border:0;background:#f0f5fa;margin:13px 0;padding:10px 12px;display:flex;gap:14px;align-items:center;flex-wrap:wrap}legend{font-size:11px;color:#5a7287}fieldset label{font-size:14px;cursor:pointer}.result{font-size:12px;font-weight:700;color:#265b56}.answer summary{font-size:13px;font-weight:700;color:#087275;cursor:pointer;margin:10px 0}.answer-body{padding:12px 15px;background:#eef8f5;border-left:3px solid #6db4a3;font-size:14px}.answer-body p{margin:7px 0}.precision{padding:9px 12px;background:#fff7df;font-size:13px;margin:12px 0}.return{display:inline-block;font-size:12px;margin-top:6px}.retrieval{margin:24px 0 0;border-top:2px solid #dcd2ed;padding-top:15px}.retrieval>summary{font-weight:750;font-size:16px;color:#604580;cursor:pointer}.retrieval-body{padding:6px 0}.review-card{padding:15px 0;border-bottom:1px solid #e4eaf0}.review-card h4{margin:5px 0 9px;font-size:15px;font-weight:720;line-height:1.5}.essentials{font-size:11px;color:#66776f}.small{font-size:12px;color:#6e7f8d}.references{background:#fff;border:1px solid #dbe4ec;padding:12px 17px;font-size:11px;color:#637484}.references>summary{cursor:pointer;font-weight:650}.references li{margin:8px 0}.scope{font-size:11px;color:#788894;margin:18px 0}.mobile-toc{display:none}@media(max-width:950px){.layout{grid-template-columns:minmax(0,1fr);max-width:850px}.outline{position:static;max-height:none;font-size:12px;background:#fff;padding:14px;border:1px solid #dbe4ec}.outline>details{display:none}.outline>strong{margin:0}.outline .mobile-toc{display:block;margin-top:9px}.outline .mobile-toc ol{padding-left:15px;list-style:decimal}.outline .mobile-toc li{margin:6px 0}.outline .mobile-toc ol li a{color:#395f7c}}@media(max-width:600px){.hero{padding:22px 15px 12px}h1{font-size:27px}.bar-inner{padding:10px 15px;gap:10px}.layout{padding:0 10px;gap:14px;margin-top:13px}.chapter>summary{font-size:17px;padding:14px;flex-wrap:wrap}.chapter>summary small{white-space:normal;font-size:9px}.chapter-body{padding:5px 15px 20px}h3{font-size:17px}table{font-size:13px}th,td{padding:9px}thead th:first-child{width:30%}blockquote{padding:12px;font-size:14px}}@media print{@page{size:A4;margin:16mm 17mm 18mm}.bar,.outline,fieldset{display:none}.hero{padding:0}.hero h1{font-size:22pt}.hero p{font-size:9pt}body{background:white;font-size:10.4pt;line-height:1.45}.layout{display:block;padding:0;margin:15px 0;max-width:none}.chapter{border:0;overflow:visible;margin-bottom:20px}.chapter>summary{padding:10px;font-size:14pt}.chapter>summary::after{display:none}.chapter>summary small{font-size:8pt}.chapter-body{padding:0}.unit{padding:12px 0}h3{font-size:11.5pt;break-after:avoid}.law,.attention,.tip,.review-card,.exam{break-inside:avoid}.body-text{margin:9px 0}table{font-size:9.2pt}th,td{padding:8px}thead{display:table-header-group}tr{break-inside:avoid}.table-wrap{overflow:visible}.answer-body{font-size:9.5pt}.references{font-size:8pt;border:0}.retrieval{break-before:page}.small,.scope{font-size:8pt}.key{color:#1264a3}*{print-color-adjust:exact;-webkit-print-color-adjust:exact}}'''
script='''const chapters=[...document.querySelectorAll('.chapter')];document.getElementById('open').addEventListener('click',()=>chapters.forEach(x=>x.open=true));document.getElementById('close').addEventListener('click',()=>chapters.forEach(x=>x.open=false));document.querySelectorAll('a[href^="#"]').forEach(a=>a.addEventListener('click',()=>{const t=document.getElementById(a.getAttribute('href').slice(1));if(t){let p=t.parentElement;while(p){if(p.tagName==='DETAILS')p.open=true;p=p.parentElement;}}}));document.querySelectorAll('.check').forEach(b=>b.addEventListener('click',()=>{const card=document.getElementById(b.dataset.question);const choice=card.querySelector('input:checked');const result=card.querySelector('.result');if(!choice){result.textContent='Selecione Certo ou Errado.';return;}result.textContent=choice.value===card.dataset.key?'Resposta correta.':'Resposta incorreta. Reveja a explicação.';card.querySelector('.answer').open=true;}));let printState;function beforePrint(){printState=[...document.querySelectorAll('details')].map(x=>[x,x.open]);printState.forEach(([x])=>x.open=true)}function afterPrint(){if(printState){printState.forEach(([x,s])=>x.open=s);printState=null}}window.addEventListener('beforeprint',beforePrint);window.addEventListener('afterprint',afterPrint);document.getElementById('print').addEventListener('click',()=>window.print());'''
mobile='<details class="mobile-toc"><summary>Ver tópicos e subtópicos</summary><ol>'+''.join(f'<li><a href="#{u["id"]}">{u["number"]} {html.escape(u["title"])}</a></li>' for s in model['sections'] for u in s['units'])+'</ol></details>'
page='<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+model['title']+'</title><style>'+css+'</style></head><body><header class="hero"><div class="eyebrow">DIREITO PENAL · FUNDAMENTOS</div><h1>Noções iniciais</h1><p>Conceito · Características · Bens jurídicos e sua proteção</p></header><nav class="bar" aria-label="Ações e assuntos"><div class="bar-inner"><a href="#conceito">1. Conceito</a><a href="#caracteristicas">2. Características</a><a href="#bens">3. Bens jurídicos</a><button id="open">Abrir assuntos</button><button id="close">Fechar assuntos</button><button id="print">Imprimir</button></div></nav><div class="layout"><aside class="outline"><strong>NESTE RECORTE</strong>'+''.join(toc)+mobile+'</aside><main>'+''.join(chapters)+'<details class="references"><summary>Referências</summary><ul>'+''.join(refs)+'</ul></details><p class="scope">Edição de trabalho · Este recorte cobre os três assuntos acima; a revisão da apostila inteira e a ampliação do banco de questões continuam em andamento.</p></main></div><script>'+script+'</script></body></html>'
(OUT/'Penal_DD_conteudo_preservado.html').write_text(page)
# PDF uses the same nodes and includes PDF outline bookmarks for numbered units.
pdfmetrics.registerFont(TTFont('DD','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'));pdfmetrics.registerFont(TTFont('DDB','/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'));pdfmetrics.registerFontFamily('DD',normal='DD',bold='DDB',italic='DD',boldItalic='DDB')
C=colors.HexColor;W=595.276;H=841.89;M=46;usable=W-2*M
styles={
 'body':ParagraphStyle('body',fontName='DD',fontSize=10.1,leading=14.2,textColor=C('#253342'),spaceAfter=8),
 'small':ParagraphStyle('small',fontName='DD',fontSize=8,leading=11,textColor=C('#6c7f90'),spaceAfter=8),
 'h1':ParagraphStyle('h1',fontName='DDB',fontSize=23,leading=28,textColor=C('#183e66'),spaceAfter=8),
 'h2':ParagraphStyle('h2',fontName='DDB',fontSize=15,leading=19,textColor=C('#183f6d'),spaceBefore=17,spaceAfter=7,keepWithNext=True),
 'h3':ParagraphStyle('h3',fontName='DDB',fontSize=11.5,leading=15.6,textColor=C('#144d80'),spaceBefore=10,spaceAfter=7,keepWithNext=True),
 'cell':ParagraphStyle('cell',fontName='DD',fontSize=9.3,leading=13),
 'rowlabel':ParagraphStyle('rowlabel',fontName='DDB',fontSize=9.3,leading=13,textColor=C('#244f78')),
 'thead':ParagraphStyle('thead',fontName='DDB',fontSize=9.1,leading=12,textColor=colors.white),
 'box':ParagraphStyle('box',fontName='DD',fontSize=9.6,leading=13.5,spaceAfter=5),
 'boxhead':ParagraphStyle('boxhead',fontName='DDB',fontSize=9.5,leading=13,textColor=C('#51417a'),spaceAfter=7),
 'lawhead':ParagraphStyle('lawhead',fontName='DDB',fontSize=9.5,leading=13,textColor=C('#256b55'),spaceAfter=7),
 'question':ParagraphStyle('question',fontName='DDB',fontSize=9.7,leading=13.1,textColor=C('#264d72'),spaceAfter=4),
 'review_answer':ParagraphStyle('review_answer',fontName='DD',fontSize=9.6,leading=13.2,textColor=C('#253342'),spaceAfter=4),
 'review_small':ParagraphStyle('review_small',fontName='DD',fontSize=7.8,leading=10.5,textColor=C('#6c7f90'),spaceAfter=6),
}
def para(t,style='body'):return Paragraph(rich(t,True),styles[style])
story=[]
def heading(text,key,level):
 p=para(text,'h2' if level==0 else 'h3');p.bookmark=(text,key,level);story.append(p)
def framed(n,bg,line,label=None):
 content=[]
 if label:content.append(para(label,'lawhead' if n['kind']=='law' else 'boxhead'))
 content.append(para(n['text'],'box'))
 if n.get('citation'):content.append(para(n['citation'],'small'))
 table=Table([[content]],colWidths=[usable],hAlign='LEFT')
 table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),C(bg)),('LINEBEFORE',(0,0),(0,-1),2.5,C(line)),('LEFTPADDING',(0,0),(-1,-1),12),('RIGHTPADDING',(0,0),(-1,-1),12),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),3)]));story.extend([table,Spacer(1,10)])
def node_pdf(n):
 kind=n['kind']
 if kind=='table':
  rows=[[para(c,'thead') for c in n['headers']]]+[[para(c,'rowlabel' if i==0 else 'cell') for i,c in enumerate(r['cells'])] for r in n['rows']]
  widths=[usable*.27,usable*.73] if len(n['headers'])==2 else [usable*.24,usable*.49,usable*.27]
  t=Table(rows,colWidths=widths,repeatRows=1,hAlign='LEFT');t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),C('#1975b8')),('BACKGROUND',(0,1),(0,-1),C('#e8eff8')),('ROWBACKGROUNDS',(1,1),(-1,-1),[C('#f8fafd'),C('#eef3fa')]),('GRID',(0,0),(-1,-1),.5,C('#d3deeb')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),10),('RIGHTPADDING',(0,0),(-1,-1),10),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),7)]));story.extend([t,Spacer(1,10)]);return
 if kind=='list':
  for x in n['items']:story.append(Paragraph('• '+rich(x['text'],True),styles['body']))
  return
 if kind=='law':framed(n,'#f0f8f4','#46997b','LEI SECA · '+n['title']);return
 if kind=='callout':framed(n,'#f5f2fa','#8870b4',n['title']);return
 if kind=='quote':framed(n,'#f7f4fc','#9a82bc');return
 if kind=='tip':framed(n,'#fff5cc','#d1a82b','ATENÇÃO');return
 if kind=='partial_exam':
  body=n['text'].removeprefix('Caiu em prova Delegado AM/2022! ')
  framed({'kind':'tip','text':body,'citation':'AM/2022 · referência abreviada; caderno completo a conferir.'},'#fff5cc','#d1a82b','REFERÊNCIA DE PROVA');return
 if kind=='question_bank':
  for q in bank:
   heading(f'Cebraspe · PF 2025 · Delegado · item {q["number"]}',q['id'],2)
   story.extend([para(q['difficulty']+' · dificuldade estimada','small'),para(q['stem']),para('Gabarito: '+('Certo' if q['answer']=='C' else 'Errado')+'.','question')])
   if q['comment']:story.append(para(q['comment']))
   if q['precision']:framed({'kind':'callout','text':q['precision']},'#fff7df','#d1a82b','Cuidado na leitura')
  return
 story.append(para(n['text']))
class Book(SimpleDocTemplate):
 def afterFlowable(self,flowable):
  if hasattr(flowable,'bookmark'):
   title,key,level=flowable.bookmark;self.canv.bookmarkPage(key);self.canv.addOutlineEntry(title,key,level=level,closed=(level==0))
 def __init__(self,*args,**kwargs):super().__init__(*args,**kwargs)
story.extend([para('DIREITO PENAL · FUNDAMENTOS','small'),para('Noções iniciais','h1'),para('Conceito · Características · Bens jurídicos e sua proteção','small')])
# A compact clickable overview; no extra cover page.
for s in model['sections']:
 links='<link href="#'+s['id']+'" color="#155e92"><b>'+s['number']+'. '+html.escape(s['title'])+'</b></link>'
 story.append(Paragraph(links,styles['small']))
for s in model['sections']:
 heading(s['number']+'. '+s['title'],s['id'],0);story.append(para(s['reference'],'small'))
 for u in s['units']:
  heading(u['number']+' '+u['title'],u['id'],1)
  for n in u['nodes']:node_pdf(n)
heading('PERGUNTAS DE RECUPERAÇÃO','recuperacao',0);story.append(para('Perguntas autorais · Responda em voz alta e confira os elementos essenciais.','small'))
for s in model['sections']:
 heading(s['number']+'. '+s['title'],'revisao-'+s['id'],1)
 for q in [x for x in qa if x['section']==s['id']]:
  story.append(KeepTogether([para(q['id']+' · '+q['level']+' · '+q['question'],'question'),para(q['answer'],'review_answer'),para('Elementos essenciais: '+' · '.join(q['essential_elements'])+'.','review_small')]))
heading('REFERÊNCIAS','referencias',0)
reference_lines=[]
for r in model['references']:
 text=html.escape(r['label']);reference_lines.append('<link href="'+r['url']+'" color="#155e92">'+text+'</link>' if r['url'] else text)
reference_lines.append('<link href="'+bank[0]['key_url']+'" color="#155e92">PF 2025: gabarito definitivo, Cargo 1.</link>')
reference_lines.append('Edição de trabalho. Este recorte cobre apenas os assuntos apresentados; a revisão da apostila inteira e a ampliação do banco de questões continuam em andamento.')
refstyle=ParagraphStyle('references',parent=styles['small'],fontSize=7.7,leading=10.3,spaceAfter=4)
story.append(Paragraph('<br/>'.join(reference_lines),refstyle))
def onpage(canvas,doc):
 canvas.saveState();canvas.setStrokeColor(C('#bad1e2'));canvas.line(M,35,W-M,35);canvas.setFont('DD',8);canvas.setFillColor(C('#6c7f90'));canvas.drawString(M,23,'DIREITO PENAL | Noções iniciais');canvas.drawRightString(W-M,23,str(doc.page));canvas.restoreState()
pdf=OUT/'Penal_DD_conteudo_preservado.pdf'
Book(str(pdf),pagesize=(W,H),rightMargin=M,leftMargin=M,topMargin=40,bottomMargin=48,title=model['title'],author='Material pessoal de estudo').build(story,onFirstPage=onpage,onLaterPages=onpage)
print(json.dumps({'html_bytes':len(page.encode()),'pdf_bytes':pdf.stat().st_size,'retrieval_questions':len(qa),'real_questions':len(bank),'numbered_units':sum(len(s['units']) for s in model['sections'])}))
