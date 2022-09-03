from BlockChainNetwork.BlockChainNode.documents.document import Document

class DocumentPool:
    def __init__(self):
        # self.documentMap = {}
        self.documentMap = []

    def clear(self):
        self.documentMap = []

    def setDocument(self, document):
        if Document.verifyDocument(document):
            self.documentMap.append(document)
            return True
        else:
            return False

    def setMap(self, documentMap):
        self.documentMap = documentMap

    # def existingDocument(self, address):
    #     for document in self.documentMap.values():
    #         if document.address == address:
    #             return document

    def documentData(self):
        return list(map(lambda doc: doc.data, self.documentMap))

    @staticmethod
    def validDocuments(documentMap):
        return [doc.to_json() for doc in documentMap if Document.verifyDocument(doc)]

    def clearBlockchainDocuments(self, chain):
        for block in chain:
            for document in block.data:
                self.documentMap.remove(document)
                # del self.documentMap[address]
        # self.documentMap = {}

    def to_json(self):
        return [document.to_json() for document in self.documentMap]

    @staticmethod
    def from_json(documentMapJson):
        # map = {}
        # for documentJson in documentMapJson:
        #     document = Document.from_json(documentJson)
        #     map[document.address] = document
        return [Document.from_json(docJson) for docJson in documentMapJson]

