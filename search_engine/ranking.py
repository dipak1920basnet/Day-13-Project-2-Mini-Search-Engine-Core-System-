import math
from collections import Counter

# Get query weight
def query_weight(query_tokens):
    return Counter(query_tokens)
      

def compute_idf(index, total_docs):
    idf = {}
    for term in index:
        df = len(index[term])

        idf[term] = math.log(total_docs/df)

    return idf


def rank(query_tokens, index, documents):
    scores = {}

    total_docs = len(documents)

    idf = compute_idf(index, total_docs)
    
    query_weights = query_weight(query_tokens)

    for token, q_weight in query_weights.items():

        if token not in index:
            continue

        for doc_id, freq in index[token].items():
            tf = freq / len(documents[doc_id].split())

            score = tf * idf[token] * q_weight

            if doc_id not in scores:
                scores[doc_id] = 0

            scores[doc_id] += score

    return sorted(scores.items(), key=lambda x: x[1], reverse=True)