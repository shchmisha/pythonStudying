import json
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.utils import (
    encode_dss_signature, decode_dss_signature
)
import rsa


class Wallet():
    def __init__(self):
        self.eccPrivateKey = ec.generate_private_key(
            ec.SECP256K1(),
            default_backend()
        )
        self.eccPublicKey = self.eccPrivateKey.public_key()
        self.serializeKeys()
        rsa_public_key, rsa_private_key = rsa.newkeys(512)
        self.rsaPrivateKey = rsa_private_key
        self.rsaPublicKey = rsa_public_key



    def serializeKeys(self):
        self.eccPublicKey = self.eccPublicKey.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).decode('utf-8')
        self.eccPrivateKey = self.eccPrivateKey.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        ).decode('utf-8')

    @staticmethod
    def getPublicKey(serPrivateKey):
        privateKey = serialization.load_pem_private_key(serPrivateKey.encode("utf-8"), None, default_backend())
        publicKey = privateKey.public_key()
        return publicKey.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).decode('utf-8')

    @staticmethod
    def sign(serPrivateKey, data):
        privateKey = serialization.load_pem_private_key(serPrivateKey.encode("utf-8"), None, default_backend())
        return decode_dss_signature(privateKey.sign(
            json.dumps(data).encode('utf-8'),
            ec.ECDSA(hashes.SHA256())
        ))


    @staticmethod
    def verify(public_key, data, signature):

        deserialized_public_key = serialization.load_pem_public_key(
            public_key.encode('utf-8'),
            default_backend()
        )

        (r, s) = signature

        try:
            deserialized_public_key.verify(
                encode_dss_signature(r, s),
                json.dumps(data).encode('utf-8'),
                ec.ECDSA(hashes.SHA256())
            )
            return True
        except InvalidSignature:
            return False

    @staticmethod
    def encode(rsaPublicKey, data):
        encData = rsa.encrypt(data.encode('utf-8'),rsaPublicKey)
        return encData

    @staticmethod
    def decode(rsaPrivateKey, encData):
        data = rsa.decrypt(encData, rsaPrivateKey)
        return data

    # encMessage = rsa.encrypt(message.encode(),
    #                          publicKey)
    #
    # print("original string: ", message)
    # print("encrypted string: ", encMessage)
    #
    # # the encrypted message can be decrypted
    # # with ras.decrypt method and private key
    # # decrypt method returns encoded byte string,
    # # use decode method to convert it to string
    # # public key cannot be used for decryption
    # decMessage = rsa.decrypt(encMessage, privateKey).decode()

    # def serializePublicKey(self):
    #     self.publicKey = self.publicKey.public_bytes(
    #         encoding=serialization.Encoding.PEM,
    #         format=serialization.PublicFormat.SubjectPublicKeyInfo
    #     ).decode('utf-8')
    #
    # def serializePrivateKey(self):
    #     serPrivateKey = self.privateKey.private_bytes(
    #         encoding=serialization.Encoding.PEM,
    #         format=serialization.PrivateFormat.TraditionalOpenSSL,
    #         encryption_algorithm=serialization.NoEncryption()
    #     ).decode('utf-8')
    #     return serPrivateKey

# wallet = Wallet()
# # print(wallet.privateKey)
# # print(wallet.publicKey)
# # wallet.serializeKeys()
# # print(wallet.privateKey)
# # print(wallet.publicKey)
# #
# serPrK = wallet.serializePrivateKey()
# print(serPrK)
#

# rsa_public_key, rsa_private_key = rsa.newkeys(512)
# print(rsa_public_key)
# print(Wallet.verify(wallet.publicKey, 'hello', Wallet.sign(serPrK, 'hello')))