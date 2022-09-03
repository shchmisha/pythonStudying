import time
from uuid import uuid4
from BlockChainNetwork.BlockChainNode.wallet.wallet import Wallet

class Document:
    def __init__(self, publicKey, data, signature, id=None):
        self.id = id or uuid4()
        self.publicKey = publicKey
        self.data = data
        self.signature = signature

    #     documents data should be encrypted useing rsa encryption
    #     the data of a document is decrypted, signed with theec private key of the business and encrypted witht he private key of the business
    #     documents for each business can be told apart by the public key
    #     data of document should be checked for things like: expiration date, type, reference to other docs

    @staticmethod
    def verifyDocument(document):
        valid = Wallet.verify(document.publicKey, document.data, document.signature)
        # make sure the data section is also checked, as it may have a reference to ther documents and the context that this reference holds
        # eg: if reference is present, the older document is invalid:
        #   reference the uuid of the document being overwritten/disregarde
        # if(not(valid)):
        #     return False
        # else:
        #     return True
        # if document.data['expirationDate']:
        #     # do verifications for the expiration date
        #     if document.data['expirationDate'] > time.time():
        #         pass
        #     # check for a reference to another document
        # if document.data['reference']:
        #     pass
        return valid



    def to_json(self):
        return self.__dict__

    @staticmethod
    def from_json(documentJson):
        return Document(**documentJson)

