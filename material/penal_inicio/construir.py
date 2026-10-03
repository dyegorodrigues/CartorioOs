#!/usr/bin/env python3
"""Gera PDF e leitor HTML a partir do mesmo conteúdo editorial."""
from pathlib import Path
import argparse
import html
import json
import re
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether

HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE / 'conteudo.json').read_text())
NAVY = colors.HexColor('#193653')
TEAL = colors.HexColor('#0E737B')
INK = colors.HexColor('#253547')
MUTED = colors.HexColor('#647384')
BLUE_BG = colors.HexColor('#EFF6FB')


def norm(s):
    return s.replace('–', '-').replace('—', '-').replace('\u2011', '-')


def build_pdf(path):
    for name, file in [('Body','DejaVuSans.ttf'),('BodyBold','DejaVuSans-Bold.ttf')]:
        pdfmetrics.registerFont(TTFont(name, '/usr/share/fonts/truetype/dejavu/' + file))
    pdfmetrics.registerFontFamily('Body', normal='Body', bold='BodyBold', italic='Body', boldItalic='BodyBold')
    styles = {
        'body': ParagraphStyle('body', fontName='Body', fontSize=10.5, leading=15.6, textColor=INK, spaceAfter=9),
        'title': ParagraphStyle('title', fontName='BodyBold', fontSize=23, leading=28, textColor=NAVY, spaceAfter=8),
        'chapter': ParagraphStyle('chapter', fontName='BodyBold', fontSize=19, leading=24, textColor=NAVY, spaceBefore=4, spaceAfter=14, keepWithNext=True),
        'h3': ParagraphStyle('h3', fontName='BodyBold', fontSize=13.3, leading=18, textColor=TEAL, spaceBefore=12, spaceAfter=8, keepWithNext=True),
        'h4': ParagraphStyle('h4', fontName='BodyBold', fontSize=11, leading=16, textColor=NAVY, spaceBefore=9, spaceAfter=6, keepWithNext=True),
        'small': ParagraphStyle('small', fontName='Body', fontSize=8.4, leading=12, textColor=MUTED, spaceAfter=8),
        'cell': ParagraphStyle('cell', fontName='Body', fontSize=8.9, leading=13, textColor=INK),
        'th': ParagraphStyle('th', fontName='BodyBold', fontSize=8.9, leading=13, textColor=colors.white),
        'qmeta': ParagraphStyle('qmeta', fontName='BodyBold', fontSize=8.3, leading=12, textColor=TEAL, spaceBefore=12, spaceAfter=4, keepWithNext=True),
    }
    def p(text, style='body'):
        return Paragraph(norm(text), styles[style])
    story = [p(DATA['edition'],'small'), p(DATA['title'],'title'), p(DATA['subtitle'],'h3'), Spacer(1,6)]
    for i,section in enumerate(DATA['sections']):
        if i:
            story.append(Spacer(1,14))
        story.append(p(section['number']+'  '+section['title'],'chapter'))
        for block in section['blocks']:
            kind=block['type']
            if kind in ['p','h3','h4']:
                story.append(p(block['text'], 'body' if kind=='p' else kind))
            elif kind=='note':
                cell = [p(block['title'],'h4'), p(block['text'])]
                table=Table([[cell]],colWidths=[A4[0]-100])
                table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),BLUE_BG),('BOX',(0,0),(-1,-1),0.4,colors.HexColor('#C4D8E7')),('LEFTPADDING',(0,0),(-1,-1),12),('RIGHTPADDING',(0,0),(-1,-1),12),('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),3)]))
                story.extend([Spacer(1,4),table,Spacer(1,10)])
            elif kind=='table':
                n=len(block['headers']); width=A4[0]-100
                widths=[width/n]*n
                if n==3:widths=[width*.26,width*.36,width*.38]
                rows=[[p(v,'th') for v in block['headers']]]+[[p(v,'cell') for v in row] for row in block['rows']]
                table=Table(rows,colWidths=widths,repeatRows=1,hAlign='LEFT')
                table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),NAVY),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.HexColor('#F1F6F9'),colors.white]),('VALIGN',(0,0),(-1,-1),'TOP'),('LINEBELOW',(0,0),(-1,0),0.6,NAVY),('LINEBELOW',(0,1),(-1,-1),0.4,colors.HexColor('#DDE5EC')),('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8)]))
                story.extend([Spacer(1,6),table,Spacer(1,10)])
    story += [PageBreak(),p('Prática: tente antes de consultar','chapter'),p('As perguntas acompanham a ordem da teoria. As respostas comentadas começam depois do último exercício. As classificações de dificuldade aqui são pedagógicas, sem medida estatística de desempenho.','small')]
    for section in DATA['sections']:
        story.append(p(section['number']+'  '+section['title'],'h3'))
        for q in section['questions']:
            question=[p(q['id']+' · '+q['kind'],'qmeta'),p(q['prompt'])]
            for option in q.get('options',[]):question.append(p(option))
            if 'source_url' in q:
                question.append(p(f'<link href="{q["source_url"]}" color="#0E737B">Prova original</link> · <link href="{q["key_url"]}" color="#0E737B">Gabarito definitivo</link>','small'))
            story.extend([KeepTogether(question),Spacer(1,8)])
    story += [PageBreak(),p('Respostas comentadas','chapter')]
    for section in DATA['sections']:
        story.append(p(section['number']+'  '+section['title'],'h3'))
        for q in section['questions']:
            story.append(p(q['id']+' · '+q['kind'],'qmeta'))
            story.append(p(q['answer']))
    story += [PageBreak(),p('Referências deste trecho','chapter')]
    for source in DATA['sources']:
        story.append(p('['+source['id']+'] '+source['title'],'h4'))
        story.append(p(source['note'],'small'))
        if source.get('url'):story.append(p(f'<link href="{source["url"]}" color="#0E737B">Abrir documento oficial</link>','small'))
    story.append(Spacer(1,12));story.append(p(DATA['scope'],'small'))
    def page(canvas,doc):
        w,h=A4
        canvas.saveState()
        canvas.setStrokeColor(TEAL);canvas.setLineWidth(2);canvas.line(50,h-40,w-50,h-40)
        canvas.setFont('BodyBold',8);canvas.setFillColor(NAVY);canvas.drawString(50,h-31,'DIREITO PENAL  /  FUNDAMENTOS')
        canvas.setFont('Body',8);canvas.setFillColor(MUTED);canvas.drawRightString(w-50,h-31,'Trecho inicial')
        canvas.setStrokeColor(colors.HexColor('#D5DEE6'));canvas.setLineWidth(.5);canvas.line(50,42,w-50,42)
        canvas.setFont('Body',7.7);canvas.drawString(50,28,'Conceito · Características · Bens jurídicos');canvas.drawRightString(w-50,28,str(doc.page))
        canvas.restoreState()
    doc=SimpleDocTemplate(str(path),pagesize=A4,rightMargin=50,leftMargin=50,topMargin=57,bottomMargin=55,title=DATA['title'],author='Material pessoal de estudo',allowSplitting=True)
    doc.build(story,onFirstPage=page,onLaterPages=page)


CSS = '''
:root{--ink:#253547;--navy:#193653;--teal:#0e737b;--muted:#647384;--line:#d7e1e8;--paper:#fff;--bg:#f2f5f7}*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:92px}body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.8 Georgia,"Times New Roman",serif}a{color:var(--teal);text-underline-offset:3px}header{position:sticky;top:0;z-index:3;background:#fff;border-bottom:1px solid var(--line);font-family:system-ui,sans-serif}header .bar{max-width:1120px;margin:auto;display:flex;align-items:center;justify-content:space-between;gap:16px;padding:14px 24px}.brand{font-size:13px;letter-spacing:.08em;color:var(--navy);font-weight:750}.controls{display:flex;gap:8px;flex-wrap:wrap}button{font:600 12px/1.5 system-ui,sans-serif;background:white;border:1px solid #b7cbd6;color:var(--navy);border-radius:6px;padding:8px 12px;cursor:pointer}button:hover{background:#eff6fb}button:focus-visible,a:focus-visible,summary:focus-visible{outline:3px solid #b6790f;outline-offset:4px}.layout{display:grid;grid-template-columns:190px minmax(0,790px);gap:28px;max-width:1090px;margin:30px auto;padding:0 24px}nav{position:sticky;top:98px;align-self:start;font:13px/1.6 system-ui,sans-serif}nav p{color:var(--muted);font-size:11px;letter-spacing:.08em;margin:10px 0}nav a{display:block;padding:10px 4px;text-decoration:none;color:var(--navy);border-bottom:1px solid var(--line)}nav a:hover{color:var(--teal)}main{background:var(--paper);border:1px solid var(--line);padding:38px 48px;box-shadow:0 3px 18px #19365305;min-width:0}.eyebrow{font:12px/1.6 system-ui,sans-serif;color:var(--muted)}h1{font:750 34px/1.18 system-ui,sans-serif;color:var(--navy);margin:16px 0 10px}.subtitle{font:16px/1.5 system-ui,sans-serif;color:var(--teal);margin-bottom:34px}h2{font:750 25px/1.3 system-ui,sans-serif;color:var(--navy);margin:42px 0 22px}h2 .number{font-size:15px;color:var(--teal);margin-right:12px}h3{font:700 19px/1.5 system-ui,sans-serif;color:var(--teal);margin:32px 0 13px}h4{font:700 16px/1.5 system-ui,sans-serif;color:var(--navy);margin:25px 0 10px}p{margin:0 0 17px}b{font-weight:700;color:#183b53}.note{background:#eff6fb;border-left:3px solid #327f9d;padding:17px 20px;margin:23px 0;font-size:16px}.note h4{margin:0 0 9px}.note p:last-child{margin-bottom:0}.table-wrap{overflow:auto;margin:24px 0}table{border-collapse:collapse;width:100%;font:14px/1.55 system-ui,sans-serif}th{text-align:left;background:var(--navy);color:white;padding:12px}td{padding:12px;border-bottom:1px solid var(--line);vertical-align:top}tr:nth-child(even){background:#f1f6f9}.practice{margin:30px 0;border:1px solid #c8d9df;background:#fbfdfd;border-radius:6px;font:15px/1.7 system-ui,sans-serif}.practice>summary{padding:16px 19px;color:var(--teal);font-weight:700;cursor:pointer}.practice-content{padding:0 19px 19px}.question{padding:20px 0;border-top:1px solid var(--line)}.qmeta{font-size:11px;line-height:1.6;color:var(--teal);font-weight:700;margin-bottom:7px}.question p{margin-bottom:10px}.options{list-style:none;padding:0;margin:10px 0}.options li{padding:5px 0}.answer{margin-top:14px}.answer>summary{cursor:pointer;font-weight:650;color:var(--navy);font-size:13px}.answer p{padding-top:12px;color:#34495e;font-size:14px}.source-links{font-size:12px}.references{font:13px/1.65 system-ui,sans-serif;border-top:1px solid var(--line);margin-top:45px}.references h2{font-size:22px}.references li{margin:18px 0}.scope{font:12px/1.7 system-ui,sans-serif;color:var(--muted);border-top:1px solid var(--line);padding-top:19px;margin-top:24px}footer{max-width:1090px;margin:0 auto 32px;padding:0 24px;font:12px system-ui,sans-serif;color:var(--muted)}
@media(max-width:850px){.layout{display:block;max-width:790px;padding:0 16px}nav{position:static;display:flex;gap:6px;flex-wrap:wrap;margin-bottom:18px}nav p{display:none}nav a{padding:8px;font-size:12px;border:1px solid var(--line);border-radius:5px}main{padding:28px 30px}.brand{font-size:11px}header .bar{padding:12px 16px}}@media(max-width:480px){body{font-size:16px}main{padding:23px 21px}h1{font-size:28px}.controls{gap:5px}button{padding:6px 8px;font-size:10px}.layout{padding:0 10px;margin-top:16px}header .bar{align-items:flex-start}.brand{max-width:95px}table{font-size:12px}}
@media print{body{background:white;font-size:11pt}header,nav,footer{display:none}.layout{display:block;margin:0;padding:0;max-width:none}main{border:0;box-shadow:none;padding:0}h1{font-size:24pt}h2{font-size:19pt;break-after:avoid}h3,h4{break-after:avoid}.practice{break-inside:auto;border:0}.practice-content,.answer>*:not(summary){display:block!important}.practice>summary,.answer>summary{list-style:none}.question{break-inside:avoid}.note,table{break-inside:avoid}a{color:inherit} @page{size:A4;margin:18mm}}
'''


def render_block(block):
    kind=block['type']
    if kind in ('p','h3','h4'):return '<'+kind+'>'+block['text']+'</'+kind+'>'
    if kind=='note':return '<aside class="note"><h4>'+block['title']+'</h4><p>'+block['text']+'</p></aside>'
    if kind=='table':
        head=''.join('<th scope="col">'+html.escape(x)+'</th>' for x in block['headers'])
        rows=''.join('<tr>'+''.join('<td>'+html.escape(x)+'</td>' for x in row)+'</tr>' for row in block['rows'])
        return '<div class="table-wrap"><table><thead><tr>'+head+'</tr></thead><tbody>'+rows+'</tbody></table></div>'
    raise ValueError(kind)


def build_html(path):
    nav=''.join(f'<a href="#{s["id"]}">{s["number"]} · {s["title"]}</a>' for s in DATA['sections'])
    chapters=[]
    for section in DATA['sections']:
        questions=[]
        for q in section['questions']:
            opts='<ul class="options">'+''.join('<li>'+html.escape(x)+'</li>' for x in q.get('options',[]))+'</ul>' if q.get('options') else ''
            links=f'<p class="source-links"><a href="{q["source_url"]}" target="_blank" rel="noopener">Prova original</a> · <a href="{q["key_url"]}" target="_blank" rel="noopener">Gabarito definitivo</a></p>' if 'source_url' in q else ''
            questions.append(f'<div class="question" id="questao-{q["id"]}"><p class="qmeta">{q["id"]} · {html.escape(q["kind"])}</p><p>{q["prompt"]}</p>{opts}{links}<details class="answer"><summary>Ver resposta comentada</summary><p>{q["answer"]}</p></details></div>')
        theory='\n'.join(render_block(b) for b in section['blocks'])
        practice=f'<details class="practice"><summary>Perguntas e questões · {len(questions)} exercícios</summary><div class="practice-content">'+''.join(questions)+'</div></details>'
        chapters.append(f'<section id="{section["id"]}"><h2><span class="number">{section["number"]}</span>{section["title"]}</h2>{theory}{practice}</section>')
    refs=[]
    for s in DATA['sources']:
        link=f' <a href="{s["url"]}" target="_blank" rel="noopener">Documento oficial</a>.' if s.get('url') else ''
        refs.append(f'<li><b>[{s["id"]}]</b> {html.escape(s["title"])}{link}<br>{html.escape(s["note"])}</li>')
    script='''document.getElementById('open-questions').addEventListener('click',()=>{document.querySelectorAll('.practice').forEach(e=>e.open=true);document.querySelectorAll('.answer').forEach(e=>e.open=false)});document.getElementById('close-answers').addEventListener('click',()=>document.querySelectorAll('.answer').forEach(e=>e.open=false));document.getElementById('print').addEventListener('click',()=>{const state=[...document.querySelectorAll('details')].map(e=>[e,e.open]);document.querySelectorAll('details').forEach(e=>e.open=true);window.print();state.forEach(([e,open])=>e.open=open)});'''
    page=f'''<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(DATA['title'])}</title><style>{CSS}</style></head><body>
<header><div class="bar"><div class="brand">DIREITO PENAL / FUNDAMENTOS</div><div class="controls"><button id="open-questions" type="button">Abrir perguntas</button><button id="close-answers" type="button">Fechar respostas</button><button id="print" type="button">Imprimir</button></div></div></header>
<div class="layout"><nav aria-label="Assuntos"><p>NESTE TRECHO</p>{nav}<a href="#referencias">Referências</a></nav><main><p class="eyebrow">{html.escape(DATA['edition'])}</p><h1>{html.escape(DATA['title'])}</h1><p class="subtitle">{html.escape(DATA['subtitle'])}</p>{''.join(chapters)}<section class="references" id="referencias"><h2>Referências deste trecho</h2><ul>{''.join(refs)}</ul></section><p class="scope">{html.escape(DATA['scope'])}</p></main></div><footer>Leitura contínua · Respostas abertas depois da tentativa · Funciona offline</footer><script>{script}</script></body></html>
'''
    path.write_text(page,encoding='utf-8')


def main():
    if DATA.get('editorial_status') == 'REJECTED_BY_USER':
        raise SystemExit('Amostra rejeitada: não regenerar como material corrente. Consulte governance/BASE_DD_CONTRACT_2026-10-02.md.')
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True);args=parser.parse_args()
    args.output.mkdir(parents=True,exist_ok=True)
    pdf=args.output/'Penal_primeiros_fundamentos.pdf';web=args.output/'Penal_primeiros_fundamentos.html'
    build_pdf(pdf);build_html(web)
    print(json.dumps({'pdf':str(pdf),'html':str(web),'questions':sum(len(s['questions']) for s in DATA['sections'])},ensure_ascii=False))


if __name__=='__main__':main()
