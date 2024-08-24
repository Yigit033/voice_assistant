# import spacy


# nlp = spacy.cli.download("en_core_web_sm")

# def process_text(text):
#     doc = nlp(text)
#     for token in doc:
#         print(token.text, token.lemma_, token.pos_, token.dep_)
#     return doc

import spacy

try:
    # Load the spaCy model
    nlp = spacy.load("en_core_web_sm")
except Exception as e:
    print(f"Error loading spaCy model: {e}")
    nlp = None

def process_text(text):
    if nlp is None:
        raise ValueError("spaCy model is not loaded")
    return nlp(text)
