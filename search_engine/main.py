from storage import load_documents, save_index, load_index
from indexer import build_index
from engine import SearchEngine
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

    engine = SearchEngine(documents,index)
    while True:
        query = input("Search: ")

        if query == "exit":
            break
        
        results = engine.query(query)

        for doc_id, score in results[:3]:
            print(f"{score:.4f} → {documents[doc_id]}")


if __name__ == "__main__":
    main()
