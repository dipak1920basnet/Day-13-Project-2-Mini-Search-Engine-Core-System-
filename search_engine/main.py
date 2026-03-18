from storage import load_documents
from indexer import build_index
from search import search, ORsearch


def main():
    documents = load_documents()

    index = build_index(documents)
    print(index)

    while True:
        query = input("Search: ")

        if query == "exit":
            break
        if "OR" in query:
            query = query.replace("OR","")
            results = ORsearch(query, index)
        else:
            results = search(query, index)

        print("\nResults: ")
        for r in results:
            print(documents[r])


if __name__ == "__main__":
    main()