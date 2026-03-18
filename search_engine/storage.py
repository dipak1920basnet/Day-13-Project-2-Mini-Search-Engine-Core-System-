def load_documents():

    with open("data/documents.txt","r") as file:
        return file.readlines()