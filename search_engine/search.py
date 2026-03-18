from tokenizer import tokenize

def search(query, index):
    tokens = tokenize(query)

    results = None

    for token in tokens:
        if token in index:
            docs = set(index[token])

            if results is None:
                results = docs
            
            else:
                results = results.intersection(docs)
        else:
            return []
        
    return list(results) if results else []


def ORsearch(query, index):
    tokens = tokenize(query)

    results = set()

    for token in tokens:
        if token in index:
            docs = set(index[token])

            if results is None:
                results = docs
            
            else:
                results = results.union(docs)
        else:
            continue
        
    return list(results) if results else []
