from tokenizer import tokenize
def build_index(documents):
    
    index = {}
    print("documents: ",documents)

    for doc_id, text in enumerate(documents):
        tokens = tokenize(text.lower())

        for token in tokens:

            if token not in index:
                # index[token] = []
                index[token] = {}

            # if doc_id not in index[token]:
            #     index[token].append(doc_id)

            try:
                index[token][doc_id] += 1
            except KeyError:
                index[token][doc_id] = 1

    return index
    
