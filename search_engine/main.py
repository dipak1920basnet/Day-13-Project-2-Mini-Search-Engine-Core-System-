from storage import load_documents
from indexer import build_index
from search import search, ORsearch, search_relevance


def main():
    documents = load_documents()

    index = build_index(documents)
    print(index)

    while True:
        query = input("Search: ")

        if query == "exit":
            break
        if "OR" in query:
            query = query.replace("OR", "")
            results = ORsearch(query, index)
        else:
            results = search(query, index, documents)

        # ranked_results = search_relevance(results, query, index)
        # for doc_id, score in ranked_results.items():
        #     print(documents[doc_id])

        for doc_id, score in results:
            print(f"{score:.4f} → {documents[doc_id]}")


if __name__ == "__main__":
    main()
