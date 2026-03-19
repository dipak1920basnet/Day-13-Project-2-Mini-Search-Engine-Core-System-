from tokenizer import tokenize


def build_index(documents):

    index = {}

    for doc_id, text in enumerate(documents):
        tokens = tokenize(text.lower())

        for token in tokens:

            if token not in index:
                index[token] = {}

            if doc_id not in index[token]:
                index[token][doc_id] =0
            
            index[token][doc_id] += 1

    return index
