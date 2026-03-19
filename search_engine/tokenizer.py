from nltk.corpus import stopwords
import string
def tokenize(text):
    text = text.lower()
    # remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    stopword = set(stopwords.words("english"))
    tokens = [w for w in words if w.lower() not in stopword]
    print("new tokens:: ", tokens)
    return tokens

