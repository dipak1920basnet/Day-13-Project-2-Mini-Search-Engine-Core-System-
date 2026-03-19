import json

def load_documents():

    with open("data/documents.txt", "r") as file:
        return file.readlines()

def save_index(index):
    with open("data/index.json","w") as file:
        json.dump(index, file)


def load_index():
    try:
        with open("data/index.json","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return None
    
