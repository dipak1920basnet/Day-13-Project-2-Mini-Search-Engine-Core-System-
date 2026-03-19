from nltk.corpus import stopwords
import string

stopword = set(stopwords.words("english"))
punct_table = str.maketrans("","", string.punctuation)

cache = {}

def tokenize(text):
    if text in cache:
        return cache[text]
    
    # Normalize the text
    text = text.lower().translate(punct_table)
    # remove punctuation
    words = text.split()

    tokens = [w for w in words if w.lower() not in stopword]

    cache[text] = tokens
    
    return tokens
