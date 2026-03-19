from search import search
from validator import validate_query

class SearchEngine:

    def __init__(self, documents, index):
        self.documents = documents
        self.index = index

    def query(self, text):
        validate_query(text)
        return search(text, self.index, self.documents)
    
