from search import search

class SearchEngine:

    def __init__(self, documents, index):
        self.documents = documents
        self.index = index

    def query(self, text):
        return search(text, self.index, self.documents)
    
