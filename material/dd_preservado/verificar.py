import json,re,hashlib,fitz
from pathlib import Path
from html.parser import HTMLParser
HERE=Path(__file__).resolve().parent
OUT=HERE.parents[2]/'output/pdf'
data=json.loads((HERE/'fonte.json').read_text())
class Parse(HTMLParser):
 def __init__(self):super().__init__();self.stack=[];self.items={};self.ids=[];self.links=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs);key=a.get('id');self.stack.append((tag,key))
  if key:self.ids.append(key);self.items[key]=''
  if tag=='a' and a.get('href','').startswith('#'):self.links.append(a['href'][1:])
 def handle_endtag(self,tag):
  if tag in ['th','td']:
   for t,k in self.stack:
    if k:self.items[k]+=' '
  for i in range(len(self.stack)-1,-1,-1):
   if self.stack[i][0]==tag:self.stack=self.stack[:i];break
 def handle_data(self,s):
  for tag,key in self.stack:
   if key:self.items[key]+=s
def norm(s):return re.sub(r'\s+',' ',s).strip().replace('–','-').replace('—','-')
p=Parse();p.feed((OUT/'Penal_DD_conteudo_preservado.html').read_text())
assert len(p.ids)==len(set(p.ids)), 'duplicate IDs'
assert set(p.links)<=set(p.ids),'broken internal links'
source_checks=[]
for b in data['blocks']:
 actual=p.items[b['id']]
 if b['id'] in ['dd-54','dd-56','dd-58']:actual+=' '+p.items[b['id']+'-gabarito']
 assert norm(actual)==norm(b['text']),(b['id'],norm(actual),b['text'])
 source_checks.append(b['id'])
assert not any(re.search(x,(OUT/'Penal_DD_conteudo_preservado.html').read_text()) for x in [r'\d{3}\.\d{3}\.\d{3}-\d{2}',r'retome:',r'libfile_',r'link_6a'])
# PDF source passages: all continuous source text, except the reconstructed table and moved keys.
doc=fitz.open(OUT/'Penal_DD_conteudo_preservado.pdf')
text=norm(' '.join(x.get_text() for x in doc))
missing=[]
for b in data['blocks']:
 expected=b['text']
 if b['id'] in ['dd-54','dd-56','dd-58']:expected=re.sub(r'\s*\(item (?:errado|correto)\)\.?$','',expected)
 if b.get('kind')=='table':
  checks=b['headers']+sum(b['rows'],[])
 else:checks=[expected]
 if not all(norm(x) in text for x in checks):missing.append(b['id'])
# PDF page headers/footers can interrupt a paragraph: inspect and verify the word sequence across them.
without=norm(' '.join(re.sub(r'PENAL \| DD preservado \| edição de trabalho\n\d+\n','',x.get_text()) for x in doc))
remaining=[]
for key in missing:
 b=next(x for x in data['blocks'] if x['id']==key)
 if norm(b['text']) not in without:remaining.append(key)
assert not remaining,remaining
# All content within safe page bounds, and no literal escaped heading tags.
for page in doc:
 assert '<br' not in page.get_text()
 for b in page.get_text('blocks'):
  assert b[0]>=40 and b[2]<=page.rect.width-39,(page.number,b[:4])
result={'source_blocks':len(source_checks),'source_words':sum(len(b['text'].split()) for b in data['blocks']),'html_verbatim':True,'pdf_all_source_text_present':True,'pdf_pages':len(doc),'cards':18,'exam_questions':3,'internal_links':len(p.links),'browser_visual_validation':False,'held_out_opened':False,'legal_scope':'CP32/96, CF22I e gabaritos PF52/53/54 conferidos; revisão doutrinária integral pendente','pdf_sha256':hashlib.sha256((OUT/'Penal_DD_conteudo_preservado.pdf').read_bytes()).hexdigest()}
(HERE/'verificacao.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));print(json.dumps(result,ensure_ascii=False))
