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


def search_relevance(doc_id, query_tokens, index):
    # query_tokens:searched query
    # index:  holds the requency of each document apperance like:  {'machine': {0: 1, 1: 1}, 'learning': {0: 1, 1: 1, 3: 1}, 'is': {0: 1, 1: 1, 2: 1, 3: 2}, 'powerful': {0: 1}, 'python': {1: 1, 3: 2}, 'great': {1: 1}, 'for': {1: 1}, 'ai': {2: 1}, 'the': {2: 1}, 'future': {2: 1}, 'fun.': {3: 1}, 'popular': {3: 1}, 'too.': {3: 1}}
    if "OR" in query_tokens:
        query_tokens = query_tokens.replace("OR", " ")
    tokens = tokenize(query_tokens)

    print("query_tokens:",query_tokens)
    print("index:", index)

    relevance_score = {}

    print("new tokensss: ")
    for token in tokens:
        for key, value in index[token].items():
            try:
                relevance_score[key] += value
            except KeyError:
                relevance_score[key] = value
    
    documents = {}
    for i in doc_id:
        documents[i] = relevance_score[i]
    relevance_score = dict(sorted(documents.items(), key=lambda item: item[1], reverse=True))
    return relevance_score
