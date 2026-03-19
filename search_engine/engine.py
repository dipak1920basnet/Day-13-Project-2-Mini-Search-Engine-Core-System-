from search import search
from validator import validate_query
from logger import log
class SearchEngine:

    def __init__(self, documents, index):
        self.documents = documents
        self.index = index

    def query(self, text):
        log(f"Query received: {text}")
        validate_query(text)
        results = search(text, self.index, self.documents)
        log(f"Results count: {len(results)}")
        return results
    
