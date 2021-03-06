import spacy as _s
from collections import Counter as _c
from operator import itemgetter as _ig


_nlp = _s.load('en')

text_1 = "Can You Give Me A List Of Artists On C. Framis Museum"
text_2 = "Can you give me a list of the epochs on MACBA"
text_3 = "Tell me information about epochs"

def _split_text(text):
    doc = _nlp(text)
    return dict(
        doc = doc,
        nc = list(doc.noun_chunks),
        pos = map(lambda x: (x, x.pos_), doc),
        tag = map(lambda x: (x, x.tag_), doc))
            
def get_knowledge_tokens(text):
    components = _split_text(text)
    doc, nc, pos, tag = _ig("doc", "nc", "pos", "tag")(components)
    try:
        terms = pos[[i[0] for i in enumerate(tag) if i[1][1] == "VBZ"][0] + 1:]
    except:
        return " ".join(map(lambda x: x.text, nc[1:] if len(nc) > 1 else doc[2:] if len(doc) > 2 else doc))
    return " ".join([term[0].text for term in terms if "ADP" not in term[1]])
    
result = get_knowledge_tokens(text_1)

test1=result.split()[-2].capitalize()
test2=result.split()[-1].strip().capitalize()