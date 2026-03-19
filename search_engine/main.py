from storage import load_documents, save_index, load_index
from indexer import build_index
from search import search, ORsearch, search_relevance

def main():
    documents = load_documents()
    if documents == None:
        print("Currently document store is empty to search")
        return
    index = load_index()
    if index is None:
        print("Building index...")
        index = build_index(documents)
        save_index(index)
    else:
        print("Loaded cached index")
    # print(index)

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

        for doc_id, score in results[:3]:
            print(f"{score:.4f} → {documents[doc_id]}")


if __name__ == "__main__":
    main()
