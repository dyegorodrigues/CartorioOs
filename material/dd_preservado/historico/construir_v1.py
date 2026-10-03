"""One content model, faithful source blocks, interactive HTML and print PDF."""
import json,re,html,hashlib
from pathlib import Path
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Table,TableStyle,KeepTogether,PageBreak
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_LEFT
HERE=Path(__file__).resolve().parent
OUT=HERE.parents[2]/'output/pdf'
OUT.mkdir(parents=True,exist_ok=True)
data=json.loads((HERE/'fonte.json').read_text()); blocks={b['id']:b for b in data['blocks']}
qa=json.loads((HERE/'recuperacao.json').read_text())
CP='https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848compilado.htm'
CF='https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm'
ROX='https://revistas.mjusticia.gob.es/index.php/ADPCP/article/download/404/404/400'
PROVA='https://cdn.cebraspe.org.br/concursos/PF_25/arquivos/106_PF_001_01.pdf'
GAB='https://cdn.cebraspe.org.br/concursos/PF_25/arquivos/D202E48A0B1EBF5039E398F0B49D0186DD625DFF53498E36EE4D88DE4501E3A8.pdf'
PUC='https://periodicos.pucminas.br/delictae/article/download/36614/24124'
notes={
'nota-vias':('Precisão: três vias não são três espécies de pena','A terceira via é uma proposta doutrinária de reparação e reconciliação, tratada por Roxin ao lado da pena e das medidas de segurança. Não é uma terceira espécie de pena no rol do art. 32 do CP.','Roxin, Pena y reparación, seção IV.1; CP, art. 32.',ROX),
'nota-sancao':('Precisão: sanção penal não se limita à prisão','A menção à pena privativa de liberdade no enfoque sociológico exemplifica a resposta penal mais severa. O art. 32 do CP também prevê penas restritivas de direitos e multa.','Código Penal, art. 32.',CP),
'nota-finalista':('Precisão de nomenclatura','Neste quadro de características, “finalista” indica a finalidade de proteger bens jurídicos. A referência não está classificando o Direito Penal segundo a teoria finalista da ação de Welzel.','Distinção entre as características e a definição atribuída a Welzel no próprio DD.',None),
'nota-corrente':('Atribuição doutrinária','A formulação sobre bens coletivos aparentes acima é apresentada pelo DD com atribuição a Martinelli e Schmitt de Bem. No item 53 da PF 2025, a própria banca delimita a afirmação com “Segundo doutrinadores em direito penal”. Mantenha essa atribuição ao explicar a posição.','PF 2025, item 53; DD, pp. 28-29.',PROVA)
}
laws={
'lei-32':('CP, art. 32 - espécies de pena','Art. 32 - As penas são:\nI - privativas de liberdade;\nII - restritivas de direitos;\nIII - de multa.',CP),
'lei-96':('CP, art. 96 - medidas de segurança','Art. 96. As medidas de segurança são:\nI - Internação em hospital de custódia e tratamento psiquiátrico ou, à falta, em outro estabelecimento adequado;\nII - sujeição a tratamento ambulatorial.\nParágrafo único - Extinta a punibilidade, não se impõe medida de segurança nem subsiste a que tenha sido imposta.',CP),
'lei-22':('CF, art. 22, I - nomenclatura e competência','Art. 22. Compete privativamente à União legislar sobre:\nI - direito civil, comercial, penal, processual, eleitoral, agrário, marítimo, aeronáutico, espacial e do trabalho;',CF)
}
# The original DD questions/comments are moved intact into an exercise view.
questions=[
{'number':52,'block':'dd-56','comment':'dd-57','key':'Errado','return':'dd-31','extra':'O gabarito oficial é errado. O comentário do DD simplifica uma discussão histórica: Paiva distingue a ideia de bem em Birnbaum da expressão bem jurídico em Binding e registra interpretações divergentes sobre a função limitadora da primeira. Evite transformar essa síntese em consenso sobre toda a evolução da teoria.','extra_source':PUC},
{'number':53,'block':'dd-58','comment':None,'key':'Certo','return':'dd-52','extra':'Observe a delimitação “Segundo doutrinadores em direito penal”. O item cobra a posição sobre bens coletivos aparentes apresentada acima, e foi considerado certo no gabarito definitivo.','extra_source':PROVA},
{'number':54,'block':'dd-54','comment':'dd-55','key':'Errado','return':'dd-26','extra':None,'extra_source':None}
]
# Mixed reading: concept -> characteristics -> unified legal-interest section.
sections=[('conceito','1. Conceito de Direito Penal','DD, pp. 5-6',list(blocks)[:14]),('caracteristicas','2. Características','DD, pp. 6-7',list(blocks)[14:22]),('bens','3. Bens jurídicos e sua proteção','DD, p. 7 + pp. 26-29',list(blocks)[22:])]
question_ids={'dd-54','dd-55','dd-56','dd-57','dd-58','dd-59'}
# Emphasis adds no words and replaces no legal terminology.
terms=['sanção penal','penas e as medidas de segurança','Direito Público','sujeito passivo','Franz von Liszt','Edmund Mezger','Hans Welzel','Juarez Cirino dos Santos','ASPECTO FORMAL','ASPECTO MATERIAL','ASPECTO SOCIOLÓGICO','dever ser','predominantemente sancionador','constitutivo','fragmentário','fragmentária','bens jurídicos','objeto jurídico','objeto material','Resultado Jurídico','Ofensividade','Bens Jurídicos Individuais','Bens Jurídicos Coletivos','Espiritualização','Liquefação','ratio legis','ultima ratio','NÃO','João Paulo Martinelli','Leonardo Schmitt de Bem']
pattern=re.compile('|'.join(re.escape(t) for t in sorted(terms,key=len,reverse=True)))
def rich(t):
    out=[];start=0
    for m in pattern.finditer(t):
        out.append(html.escape(t[start:m.start()]));out.append('<b>'+html.escape(m.group())+'</b>');start=m.end()
    out.append(html.escape(t[start:]));return ''.join(out)
def bhtml(b):
    if b.get('kind')=='table':
        return '<div class="table-wrap"><table id="'+b['id']+'"><thead><tr>'+''.join('<th>'+html.escape(c)+'</th>' for c in b['headers'])+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+rich(c)+'</td>' for c in row)+'</tr>' for row in b['rows'])+'</tbody></table></div>'
    cls='source'
    if b['id'] in ['dd-02','dd-09','dd-51']:cls+=' dica'
    if b['id'] in ['dd-05','dd-06','dd-07','dd-08','dd-24','dd-52','dd-53']:cls+=' quote'
    if b['id'] in ['dd-11','dd-12','dd-13']:cls+=' aspect'
    if b['id'] in ['dd-16','dd-17','dd-18','dd-19','dd-20','dd-21','dd-22']:cls+=' characteristic'
    return f'<p id="{b["id"]}" class="{cls}">{rich(b["text"])}</p>'
def nhtml(key):
    title,text,source,url=notes[key]
    cite='<a href="'+url+'">'+html.escape(source)+'</a>' if url else html.escape(source)
    return f'<aside id="{key}" class="note"><b>{html.escape(title)}</b><p>{rich(text)}</p><small>Acréscimo editorial. {cite}</small></aside>'
def lhtml(key):
    title,text,url=laws[key]
    return f'<aside id="{key}" class="law"><b>{html.escape(title)}</b><p>{html.escape(text).replace(chr(10),"<br>")}</p><small>Texto legal conferido em 03/10/2026. <a href="{url}">Fonte oficial</a>.</small></aside>'
def qhtml(q):
    b=blocks[q['block']];match=re.search(r'\s*\(item (?:errado|correto)\)\.?$',b['text'])
    assert match,b['text']
    prompt=b['text'][:match.start()]; original=b['text'][match.start():].strip()
    content=f'<p id="{b["id"]}" class="source">{rich(prompt)}</p>'
    content+=f'<details class="answer"><summary>Ver gabarito e comentário</summary><div class="answer-body"><b>{q["key"]}.</b> <span id="{b['id']}-gabarito">{html.escape(original)}</span>'
    if q['comment']:content+=bhtml(blocks[q['comment']])
    if q['extra']:content+=f'<p class="precision">Precisão de leitura: {rich(q["extra"])}</p>'
    content+=f'<a class="back" href="#{q["return"]}">Voltar à explicação correspondente</a></div></details>'
    return f'<article class="exam"><h4>Cebraspe · PF 2025 · Delegado · item {q["number"]}</h4>{content}</article>'
def cardhtml(item):
    links=' · '.join(f'<a href="#{k}">Explicação {i+1}</a>' for i,k in enumerate(item['base']))
    return f'<article class="card"><span class="level">{item["level"]} · pergunta autoral</span><p><b>{html.escape(item["question"])}</b></p><details class="answer"><summary>Ver resposta</summary><div class="answer-body"><p>{rich(item["answer"])}</p><small>{links}</small></div></details></article>'
parts=[]
for sid,title,source,ids in sections:
    content=[]
    for key in ids:
        if key in question_ids:continue
        content.append(bhtml(blocks[key]))
        if key=='dd-02':content+=[nhtml('nota-vias'),lhtml('lei-32'),lhtml('lei-96')]
        if key=='dd-09':content.append(lhtml('lei-22'))
        if key=='dd-14':content.append(nhtml('nota-sancao'))
        if key=='dd-22':content.append(nhtml('nota-finalista'))
        if key=='dd-53':content.append(nhtml('nota-corrente'))
    if sid=='bens':
        # Put original synthesis after the questions as in DD.
        content=[p for p in content if 'id="dd-60"' not in p]
        content.append('<h3 id="questoes">Questões da própria apostila</h3><p class="subtle">PF 2025: enunciados e gabaritos conferidos no caderno 106_PF_001_01 e no gabarito definitivo de Delegado. <a href="'+PROVA+'">Prova oficial</a> · <a href="'+GAB+'">Gabarito oficial</a>.</p>')
        content.extend(qhtml(q) for q in questions)
        content.append('<aside class="note"><b>Referência abreviada no DD</b>'+bhtml(blocks['dd-59'])+'<small>A apostila traz apenas esse fragmento da prova AM/2022. Não foi transformado em questão completa nem contado como item integralmente conferido.</small></aside>')
        content.append(bhtml(blocks['dd-60']))
    content.append('<details class="review"><summary>Perguntas de recuperação deste assunto</summary><p class="subtle">Perguntas autorais. A dificuldade é uma estimativa pedagógica inicial.</p>'+''.join(cardhtml(x) for x in qa if x['section']==sid)+'</details>')
    parts.append(f'<details class="chapter" id="{sid}" open><summary><span>{title}</span><small>{source}</small></summary><div class="chapter-body">'+''.join(content)+'</div></details>')
css='''*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:95px}body{margin:0;background:#f4f6f8;color:#202d39;font-family:system-ui,-apple-system,Segoe UI,sans-serif;font-size:16px;line-height:1.65}a{color:#135e83;text-underline-offset:3px}b{font-weight:720;color:#162f41}header{max-width:1080px;margin:0 auto;padding:38px 24px 20px}.eyebrow{font-size:12px;font-weight:750;letter-spacing:.13em;color:#007c7a}h1{font-size:34px;line-height:1.18;max-width:760px;margin:10px 0 14px}.intro{max-width:790px;color:#50616e;font-size:15px}.toolbar{position:sticky;top:0;z-index:10;background:#fff;border-bottom:1px solid #dce4e8;padding:12px 24px;display:flex;gap:12px;align-items:center;flex-wrap:wrap}.toolbar-inner{width:1032px;margin:auto;display:flex;align-items:center;gap:12px;flex-wrap:wrap}.toolbar a{font-size:14px;font-weight:650}.toolbar button{font:inherit;font-size:13px;border:1px solid #c4d7df;border-radius:6px;background:#fff;color:#20495c;padding:6px 10px;cursor:pointer}main{max-width:980px;margin:24px auto 60px;padding:0 24px}.chapter{margin:0 0 18px;background:#fff;border:1px solid #d7e2e8;border-radius:10px;overflow:clip}.chapter>summary{cursor:pointer;list-style:none;padding:20px 24px;display:flex;justify-content:space-between;gap:16px;border-left:5px solid #007c7a;background:#eaf4f4;font-size:21px;font-weight:750;line-height:1.3}.chapter>summary::after{content:'−';font-size:25px}.chapter:not([open])>summary::after{content:'+'}.chapter>summary small{color:#58717b;font-size:12px;font-weight:500;align-self:center;white-space:nowrap}.chapter-body{padding:12px 28px 26px;max-width:850px;margin:auto}.source{margin:16px 0}.quote{border-left:3px solid #8c73b3;padding:10px 16px;background:#f7f4fb}.dica{padding:12px 16px;background:#fff5d8;border-left:3px solid #c39727}.aspect{padding:10px 16px;background:#eef5fb;border-left:3px solid #5283ac}.characteristic{padding-bottom:12px;border-bottom:1px solid #e7ecef}.note{margin:16px 0;padding:14px 18px;background:#f8f5eb;border:1px solid #e8ddbd;border-radius:6px;font-size:14px}.note p{margin:9px 0}.note small,.law small{font-size:11.5px;color:#58636b}.law{margin:14px 0;padding:16px 18px;background:#edf7f3;border-left:4px solid #298564;border-radius:4px;font-size:14px}.law p{margin:8px 0}h3{font-size:20px;color:#16586c;margin-top:30px}table{border-collapse:collapse;width:100%;font-size:14px;margin:16px 0}th{background:#215c70;color:white;text-align:left}td,th{padding:12px;border:1px solid #d7e3e8;vertical-align:top}tr:nth-child(even){background:#f2f7f9}.table-wrap{overflow:auto}.exam{border:1px solid #d6e2ea;border-radius:7px;padding:16px 18px;margin:18px 0;background:#fcfdff}.exam h4{font-size:13px;letter-spacing:.02em;color:#3c6380;margin:0}.answer{margin:12px 0}.answer summary{font-size:14px;color:#075e67;cursor:pointer;font-weight:650}.answer-body{padding:12px 16px;border-left:3px solid #70b6b1;background:#eef8f6}.answer-body p{margin:8px 0}.back{font-size:13px;display:inline-block;margin-top:10px}.precision{font-size:14px}.subtle{font-size:13px;color:#5d6e79}.review{margin-top:24px;border-top:1px solid #d9e5e9;padding-top:18px}.review>summary{cursor:pointer;color:#5c467d;font-weight:700}.card{border-bottom:1px solid #e3e9ec;padding:16px 0}.level{font-size:11px;color:#5d5570;font-weight:700}.card>p{margin:5px 0}.card small a{display:inline-block;margin-right:5px}.scope{max-width:980px;margin:0 auto 30px;padding:0 24px;font-size:12px;color:#647581}footer{margin:25px 0;font-size:12px;color:#647581}@media(max-width:700px){header{padding:25px 16px 12px}h1{font-size:28px}main{padding:0 12px;margin-top:15px}.toolbar{padding:10px 16px}.chapter>summary{padding:16px;font-size:18px;flex-wrap:wrap}.chapter>summary small{white-space:normal}.chapter-body{padding:8px 16px 22px}.table-wrap table{min-width:510px}}@media print{@page{size:A4;margin:17mm 17mm 18mm}body{background:white;font-size:10.5pt;line-height:1.45}.toolbar{display:none}header{padding:0}h1{font-size:22pt}.intro{font-size:9pt}main{padding:0;margin:15px 0;max-width:none}.chapter{border:0;margin-bottom:15px;overflow:visible}.chapter>summary{padding:10px 12px;font-size:15pt;background:#edf4f5!important}.chapter>summary::after{display:none}.chapter-body{padding:0;max-width:none}.quote,.aspect,.dica,.law,.note{break-inside:avoid}.source{margin:10px 0}.exam,.card{break-inside:avoid}a{color:inherit}.answer-body{display:block}.answer>summary{font-size:9pt}.table-wrap{overflow:visible}.table-wrap table{min-width:0}th,td{padding:8px}.scope{padding:0;font-size:9pt}.review{break-before:page}.review>summary{font-size:13pt}.subtle{font-size:9pt}*{print-color-adjust:exact;-webkit-print-color-adjust:exact}}'''
script='''const chapters=[...document.querySelectorAll('.chapter')];document.getElementById('open').addEventListener('click',()=>chapters.forEach(x=>x.open=true));document.getElementById('close').addEventListener('click',()=>chapters.forEach(x=>x.open=false));document.querySelectorAll('a[href^="#"]').forEach(a=>a.addEventListener('click',()=>{const t=document.getElementById(a.getAttribute('href').slice(1));if(t){let p=t.parentElement;while(p){if(p.tagName==='DETAILS')p.open=true;p=p.parentElement;}}}));let priorPrint;function beforePrint(){priorPrint=[...document.querySelectorAll('details')].map(x=>[x,x.open]);priorPrint.forEach(([x])=>x.open=true)}function afterPrint(){if(priorPrint){priorPrint.forEach(([x,s])=>x.open=s);priorPrint=null}}window.addEventListener('beforeprint',beforePrint);window.addEventListener('afterprint',afterPrint);document.getElementById('print').addEventListener('click',()=>window.print());'''
page='<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+data['title']+'</title><style>'+css+'</style></head><body><header><div class="eyebrow">DIREITO PENAL · EDIÇÃO DE TRABALHO</div><h1>Conceito, características<br>e bens jurídicos</h1><p class="intro">Conteúdo do DD preservado, com as passagens sobre bens jurídicos reunidas em sequência. Os acréscimos editoriais estão identificados. Questões e perguntas de recuperação permitem abrir a resposta depois de pensar.</p></header><nav class="toolbar" aria-label="Navegação"><div class="toolbar-inner"><a href="#conceito">Conceito</a><a href="#caracteristicas">Características</a><a href="#bens">Bens jurídicos</a><a href="#questoes">Questões</a><button id="open">Abrir assuntos</button><button id="close">Fechar assuntos</button><button id="print">Imprimir</button></div></nav><main>'+''.join(parts)+'</main><div class="scope">Recorte: DD a-c (pp. 5-7) e 7.1.1 (pp. 26-29), da amostra fornecida. As repetições foram conservadas nesta edição para conferir a preservação antes de qualquer redução. A conferência dos três itens da PF não equivale à análise de todo o banco de questões. A revisão doutrinária integral permanece em andamento.</div><script>'+script+'</script></body></html>'
(OUT/'Penal_DD_conteudo_preservado.html').write_text(page)
# PDF: same selected source blocks; recolhible answers become explicit, no hidden content.
pdfmetrics.registerFont(TTFont('DD','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DDB','/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
pdfmetrics.registerFontFamily('DD',normal='DD',bold='DDB',italic='DD',boldItalic='DDB')
C=colors.HexColor
styles={
'body':ParagraphStyle('body',fontName='DD',fontSize=10.1,leading=14.2,textColor=C('#253441'),spaceAfter=9),
'small':ParagraphStyle('small',fontName='DD',fontSize=8.1,leading=11.4,textColor=C('#536672'),spaceAfter=8),
'h1':ParagraphStyle('h1',fontName='DDB',fontSize=23,leading=28,textColor=C('#173d51'),spaceAfter=12),
'h2':ParagraphStyle('h2',fontName='DDB',fontSize=15,leading=20,textColor=C('#086d73'),spaceBefore=18,spaceAfter=11,keepWithNext=True),
'h3':ParagraphStyle('h3',fontName='DDB',fontSize=11.5,leading=16,textColor=C('#265d74'),spaceBefore=11,spaceAfter=7,keepWithNext=True),
'box':ParagraphStyle('box',fontName='DD',fontSize=9.3,leading=13.2,spaceAfter=6),
'cell':ParagraphStyle('cell',fontName='DD',fontSize=9,leading=12.5),
'white':ParagraphStyle('white',fontName='DDB',fontSize=8.5,leading=12,textColor=colors.white),
}
W=210/25.4*72;H=297/25.4*72;M=48;usable=W-2*M
story=[]
def para(t,style='body'):return Paragraph(rich(t).replace('\n','<br/>'),styles[style])
def box(title,text,kind='note',source=None):
    items=[para(title,'h3'),para(text,'box')]
    if source:items.append(para(source,'small'))
    t=Table([[items]],colWidths=[usable],hAlign='LEFT')
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),C('#edf7f3' if kind=='law' else '#f8f5eb')),('BOX',(0,0),(-1,-1),.5,C('#c5ddd3' if kind=='law' else '#e4d9b9')),('LEFTPADDING',(0,0),(-1,-1),12),('RIGHTPADDING',(0,0),(-1,-1),12),('TOPPADDING',(0,0),(-1,-1),2),('BOTTOMPADDING',(0,0),(-1,-1),5)]))
    story.extend([t,Spacer(1,10)])
def npdf(key):
    title,text,source,url=notes[key];box(title,text,source='Acréscimo editorial. '+source)
def lpdf(key):
    title,text,url=laws[key];box(title,text,'law','Texto legal conferido em 03/10/2026. Fonte: Planalto.')
def bpdf(b):
    if b.get('kind')=='table':
        rows=[[Paragraph(html.escape(c),styles['white']) for c in b['headers']]]+[[para(c,'cell') for c in row] for row in b['rows']]
        t=Table(rows,colWidths=[usable*.23,usable*.5,usable*.27],repeatRows=1,hAlign='LEFT')
        t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),C('#215c70')),('ROWBACKGROUNDS',(0,1),(-1,-1),[C('#f1f7f9'),colors.white]),('GRID',(0,0),(-1,-1),.5,C('#cbdde4')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),9),('RIGHTPADDING',(0,0),(-1,-1),9),('TOPPADDING',(0,0),(-1,-1),9),('BOTTOMPADDING',(0,0),(-1,-1),9)]))
        story.extend([t,Spacer(1,10)]);return
    p=para(b['text'])
    if b['id'] in ['dd-02','dd-09','dd-11','dd-12','dd-13','dd-24','dd-51']:
        t=Table([[p]],colWidths=[usable],hAlign='LEFT')
        t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),C('#fff5d8' if b['id'] in ['dd-02','dd-09','dd-51'] else '#eef5fb')),('LEFTPADDING',(0,0),(-1,-1),12),('RIGHTPADDING',(0,0),(-1,-1),12),('TOPPADDING',(0,0),(-1,-1),10),('BOTTOMPADDING',(0,0),(-1,-1),3)]))
        story.extend([t,Spacer(1,10)])
    else:story.append(p)
    # Prevent short author's intro or source headings from orphaning.
    if b['id'] in ['dd-04','dd-10','dd-23','dd-44','dd-47']:p.style=ParagraphStyle('keep-'+b['id'],parent=styles['body'],keepWithNext=True)
story.extend([para('DIREITO PENAL · EDIÇÃO DE TRABALHO','small'),para('Conceito, características\ne bens jurídicos','h1'),para('Conteúdo do DD preservado; passagens reunidas por assunto. As notas editoriais e os textos legais acrescentados estão identificados.','small')])
for sid,title,source,ids in sections:
    story.extend([para(title,'h2'),para(source,'small')])
    for key in ids:
        if key in question_ids or key=='dd-60':continue
        bpdf(blocks[key])
        if key=='dd-02':npdf('nota-vias');lpdf('lei-32');lpdf('lei-96')
        if key=='dd-09':lpdf('lei-22')
        if key=='dd-14':npdf('nota-sancao')
        if key=='dd-22':npdf('nota-finalista')
        if key=='dd-53':npdf('nota-corrente')
    if sid=='bens':
        story.extend([para('Questões da própria apostila','h2'),para('Cebraspe · PF 2025 · Delegado · caderno 106_PF_001_01. Gabarito definitivo conferido.','small')])
        for q in questions:
            b=blocks[q['block']];m=re.search(r'\s*\(item (?:errado|correto)\)\.?$',b['text'])
            # Same words; answer label relocated below the statement.
            story.extend([para(f'Item {q["number"]}','h3'),para(b['text'][:m.start()]),para('Gabarito: '+q['key']+'. '+b['text'][m.start():].strip(),'small')])
            if q['comment']:bpdf(blocks[q['comment']])
            if q['extra']:box('Precisão de leitura',q['extra'],source='Acréscimo editorial. PF 2025; '+('Paiva, Delictae 18, 2025, histórico da teoria do bem jurídico.' if q['number']==52 else 'enunciado e gabarito oficial.'))
        bpdf(blocks['dd-59']);story.append(para('Referência abreviada do DD: o fragmento AM/2022 acima não foi tratado como questão completa conferida.','small'));bpdf(blocks['dd-60'])
story.extend([PageBreak(),para('Perguntas de recuperação','h2'),para('18 perguntas autorais, na sequência dos assuntos. Níveis estimados pela exigência pedagógica; ainda não calibrados pelo desempenho.','small')])
for sid,title,source,ids in sections:
    story.append(para(title,'h3'))
    for i,item in enumerate([x for x in qa if x['section']==sid],1):
        story.append(KeepTogether([para(item['level']+' · '+item['question'],'h3'),para(item['answer'])]))
story.extend([para('Fontes e limites desta edição','h2'),para('Base: amostra DD - Noções iniciais e princípios do Direito Penal, a-c, pp. 5-7, e seção 7.1.1, pp. 26-29. Nenhuma dessas passagens foi suprimida. Repetições foram conservadas para permitir a conferência antes de eventual redução. A revisão doutrinária integral continua em andamento; os três itens da PF não representam um banco completo de questões.','small')])
for label,url in [('CP, arts. 32 e 96',CP),('CF, art. 22, I',CF),('Roxin, Pena y reparación, seção IV.1',ROX),('PF 2025, prova oficial',PROVA),('PF 2025, gabarito definitivo de Delegado',GAB),('Paiva, A efetividade da teoria do bem jurídico, Delictae 18/2025',PUC)]:
    story.append(Paragraph('<link href="'+html.escape(url,quote=True)+'" color="#135e83">'+html.escape(label)+'</link>',styles['small']))
def onpage(canvas,doc):
    canvas.saveState();canvas.setStrokeColor(C('#b9ced8'));canvas.line(M,35,W-M,35);canvas.setFont('DD',8);canvas.setFillColor(C('#59717d'));canvas.drawString(M,23,'PENAL | DD preservado | edição de trabalho');canvas.drawRightString(W-M,23,str(doc.page));canvas.restoreState()
pdf=OUT/'Penal_DD_conteudo_preservado.pdf'
SimpleDocTemplate(str(pdf),pagesize=(W,H),rightMargin=M,leftMargin=M,topMargin=41,bottomMargin=49,title=data['title'],author='Material pessoal de estudo').build(story,onFirstPage=onpage,onLaterPages=onpage)
print(json.dumps({'html_bytes':len(page.encode()),'pdf_bytes':pdf.stat().st_size,'blocks':len(blocks),'cards':len(qa),'question_numbers':[q['number'] for q in questions]}))
