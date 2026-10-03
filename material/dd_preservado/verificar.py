import json,re,hashlib,fitz
from pathlib import Path
from html.parser import HTMLParser
HERE=Path(__file__).resolve().parent;OUT=HERE.parents[2]/'output/pdf'
source=json.loads((HERE/'fonte.json').read_text());model=json.loads((HERE/'apresentacao.json').read_text());audit=json.loads((HERE/'destinos_editoriais.json').read_text())['entries'];qa=json.loads((HERE/'recuperacao.json').read_text());qs=json.loads((HERE/'banco_questoes.json').read_text())['questions']
class Parse(HTMLParser):
 def __init__(self):super().__init__();self.skip=0;self.text=[];self.ids=[];self.links=[];self.heading_tags=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag in ['script','style']:self.skip+=1
  if 'id' in a:self.ids.append(a['id'])
  if tag=='a' and a.get('href','').startswith('#'):self.links.append(a['href'][1:])
  if tag in ['h1','h3','h4']:self.heading_tags.append(tag)
 def handle_endtag(self,tag):
  if tag in ['script','style']:self.skip-=1
  if tag in ['p','li','th','td','h1','h3','h4','summary','cite']:self.text.append(' ')
 def handle_data(self,s):
  if not self.skip:self.text.append(s)
def norm(t):return re.sub(r'\s+',' ',t).strip()
h=Parse();htmltext=(OUT/'Penal_DD_conteudo_preservado.html').read_text();h.feed(htmltext);visible=norm(''.join(h.text))
assert len(h.ids)==len(set(h.ids)),'duplicate IDs'
assert set(h.links)<=set(h.ids),'broken internal links'
assert set(q['target'] for q in qa)<=set(h.ids),'unlinked recovery cards'
assert len(audit)==len(source['blocks'])==60
assert {e['source_id'] for e in audit}=={b['id'] for b in source['blocks']}
for e in audit:
 assert e['original']==next(b['text'] for b in source['blocks'] if b['id']==e['source_id'])
 for text in e['display_passages']:assert norm(text) in visible,(e['source_id'],text[:100])
# Main reading contains one hierarchy, and no recurrent references to the course provider.
main=htmltext.split('<main>')[1].split('<details class="references">')[0]
assert not re.search(r'7\.1\.1|a\) CONCEITO|b\) CARACTERÍSTICAS|c\) OBJETO|DICA DD|no DD|pelo DD|na apostila|comentário do DD',main,re.I)
assert not re.search(r'\d{3}\.\d{3}\.\d{3}-\d{2}|retome:',visible,re.I)
assert [s['number'] for s in model['sections']]==['1','2','3']
for s in model['sections']:
 assert [u['number'] for u in s['units']]==[s['number']+'.'+str(i+1) for i in range(len(s['units']))]
 assert s['reference'].startswith('DD, ')
for q in qs:
 assert q['kind']=='real' and q['source_state']=='OFFICIAL_STATEMENT_AND_FINAL_KEY_CHECKED'
assert {q['number']:q['answer'] for q in qs}=={52:'E',53:'C',54:'E'}
assert all(q['kind']=='authored_retrieval' and q['essential_elements'] for q in qa)
# PDF content check, removing only the repeated page footer and page number.
doc=fitz.open(OUT/'Penal_DD_conteudo_preservado.pdf')
pdftext=norm(' '.join(re.sub(r'DIREITO PENAL \| Noções iniciais\n\d+\n','',p.get_text()) for p in doc))
for e in audit:
 for text in e['display_passages']:assert norm(text) in pdftext,('PDF',e['source_id'],text[:100])
for page in doc:
 for b in page.get_text('blocks'):
  assert b[0]>=39 and b[2]<=page.rect.width-38,(page.number,b[:4])
 assert '<br' not in page.get_text()
assert len(doc.get_toc())>=sum(len(s['units']) for s in model['sections'])+3
# No nearly-empty page caused by forced breaks; the final references page may be shorter.
for i,p in enumerate(doc):
 if i<len(doc)-1:assert len(p.get_text().split())>=170,('sparse page',i+1)
result={'edition':'v2','source_blocks_mapped':60,'declared_display_passages_present_html_and_pdf':True,'semantic_completeness_established':False,'known_semantic_omission':'dd-04: formal definitions focus on law and sanction removed as editorial preface','pedagogical_review':'USER_FOUND_V2_CONFUSING_AND_INCOMPLETE' ,'editorial_numbering_and_metadata_changes_traced':True,'sections':3,'numbered_units':18,'comparison_tables':sum(n['kind']=='table' for s in model['sections'] for u in s['units'] for n in u['nodes']),'authored_retrieval_questions':len(qa),'real_exam_questions':len(qs),'internal_links':len(h.links),'pdf_pages':len(doc),'pdf_bookmarks':len(doc.get_toc()),'browser_visual_validation':False,'held_out_opened':False,'full_booklet_review_complete':False,'all_questions_sufficiency_established':False,'pdf_sha256':hashlib.sha256((OUT/'Penal_DD_conteudo_preservado.pdf').read_bytes()).hexdigest()}
(HERE/'verificacao.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));print(json.dumps(result,ensure_ascii=False))
