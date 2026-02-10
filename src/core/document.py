class Document:
    def __init__(self, name):
        self.name = name
        self.content = ""

    def open(self):
        print("Document opened")

    def save(self):
        print("Document saved")

    def format(self):
        print("Formatting document")
