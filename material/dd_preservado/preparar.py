"""Select the supplied DD passages verbatim; normalize whitespace only."""
import json,re,hashlib
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
pages=json.loads((ROOT/'dd_review_2026/dd_penal.json').read_text())
def clean(t):
    t=re.split(r'\n\d{5,}\.\d\d/\d\d/\d{4}',t)[0]
    return '\n'.join(l for l in t.splitlines() if l.strip() and not re.fullmatch(r'\d+',l.strip()) and not re.search(r'dedicacaodelta.com.br|gran.com.br|granconcursosonline.com.br|O conteúdo deste livro eletrônico é licenciado|sendo vedada|uso e reprodução|em qualquer forma ou meio|sob pena de responsabilização',l,re.I))
def norm(t): return re.sub(r'\s+',' ',t).strip().replace('–','-').replace('—','-')
base='\n'.join(clean(pages[i]) for i in range(4,7))
a=base[base.index('a) CONCEITO:'):base.index('b) CARACTERÍSTICAS:')]
b=base[base.index('b) CARACTERÍSTICAS:'):base.index('c) OBJETO DE PROTEÇÃO')]
c=base[base.index('c) OBJETO DE PROTEÇÃO'):base.index('d) EVOLUÇÃO DO DIREITO PENAL:')]
long='\n'.join(clean(pages[i]) for i in range(25,29))
d=long[long.index('7.1.1 Princípio da Exclusiva Proteção'):long.index('7.1.2 Princípio da Intervenção Mínima')]
blocks=[]
def split_passage(text,anchors,pages,target):
    assert text.startswith(anchors[0]),repr(text[:100])
    starts=[text.index(x) for x in anchors]
    assert starts==sorted(starts)
    for i,(start,anchor) in enumerate(zip(starts,anchors)):
        end=starts[i+1] if i+1<len(starts) else len(text)
        chunk=norm(text[start:end])
        blocks.append({'id':f'dd-{len(blocks)+1:02d}','section':target,'source_pages':pages,'text':chunk,'origin':'DD fornecido pelo usuário','anchor':anchor})
    assert norm(' '.join(x['text'] for x in blocks if x['section']==target))==norm(text)
split_passage(a,['a) CONCEITO:','#DICA DD: Diz-se','É um ramo do','Autores renomados','Franz von Liszt','Edmund Mezger','Hans Welzel','Juarez Cirino','#DICA DD: Embora','Ainda sobre o conceito','ASPECTO FORMAL:','ASPECTO MATERIAL:','ASPECTO SOCIOLÓGICO:','Aprofundando o enfoque'],[5,6],'conceito')
split_passage(b,['b) CARACTERÍSTICAS:','I – Ciência:','II – Cultural:','III – Normativa:','IV – Valorativa:','V – Finalista:','VI – Sancionatória:','VII – Fragmentária:'],[6,7],'caracteristicas')
split_passage(c,['c) OBJETO DE PROTEÇÃO','“(...) é a coisa','O legislador seleciona','No entanto, NÃO','Orienta o legislador','Impede que o legislador'],[7],'bens-introducao')
split_passage(d,['7.1.1 Princípio da Exclusiva Proteção','Assim, não pode','Mas o que é bem jurídico?','1.Definição e Natureza:','É o objeto jurídico,','Em \numa \nperspectiva','É a relação reconhecida','Claus Roxin o define','2. Função Primordial','A missão do Direito Penal moderno','O conceito de bem jurídico desempenha','3. Bem Jurídico e Conceito de Crime','Para que uma conduta','Resultado Jurídico:','Ofensividade:','4. Distinção Crucial:','CONCEITO','O bem jurídico não deve','5. Classificação e Tendências:','Bens Jurídicos Individuais:','Bens Jurídicos Coletivos','A Espiritualização','Atenção! Temática','De acordo com os autores','Explicam ainda os autores:','Caiu em prova Delegado de Polícia Federal/2025! Julgue o item a seguir, relativos à\nevolução','A proteção conferida','Caiu em prova Delegado de Polícia Federal/2025! Julgue o item a seguir, relativos à evolução\nda teoria','O item está errado','Caiu em prova Delegado de Polícia Federal/2025! Julgue o item a seguir, relativos à evolução\nda teoria do bem jurídico e suas emanações. Segundo','Caiu em prova Delegado AM/2022!','Em síntese:'],[26,27,28,29],'bens-aprofundamento')
for x in blocks:
    x['sha256_normalized_text']=hashlib.sha256(x['text'].encode()).hexdigest()
# Restore the two-row table, whose PDF extraction is column-sensitive.
table=next(x for x in blocks if x['anchor']=='CONCEITO')
table['kind']='table'
table['headers']=['CONCEITO','DESCRIÇÃO','EXEMPLO (HOMICÍDIO)']
table['rows']=[['Objeto Jurídico (Bem Jurídico)','O interesse ou valor abstrato de ordem social protegido pela norma penal.','A vida humana.'],['Objeto Material','A pessoa ou a coisa que suporta a conduta criminosa (sobre a qual incide a ação ofensiva).','O ser humano que teve sua vida ceifada.']]
assert norm(' '.join(table['headers']+sum(table['rows'],[])))==table['text']
(HERE/'fonte.json').write_text(json.dumps({'title':'Direito Penal - conceito, características e bens jurídicos','status':'EDICAO_DE_TRABALHO','source_drive_id':'1eOcrfOuLyOJYnXTwUaAvyovG7tPZZxhy','source_pdf_sha256':hashlib.sha256((ROOT/'dd_review_2026/dd_penal.pdf').read_bytes()).hexdigest(),'scope':'DD a-c, pp. 5-7; DD 7.1.1, pp. 26-29. As demais seções continuam fora deste recorte.','blocks':blocks},ensure_ascii=False,indent=2))
print(json.dumps({'blocks':len(blocks),'words':sum(len(x['text'].split()) for x in blocks),'verbatim_normalized':True}))
