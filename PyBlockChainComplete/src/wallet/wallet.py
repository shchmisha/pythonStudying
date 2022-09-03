import json
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.utils import (
    encode_dss_signature, decode_dss_signature
)

class Wallet():
    def __init__(self, private_key=None, public_key=None):
        self.privateKey = private_key or ec.generate_private_key(ec.SECP256R1(), default_backend())
        self.publicKey = public_key or self.privateKey.public_key()
        

    def serializeKeys(self):
        """
        Reset the public key to it's serialized version
        """
        self.privateKey = self.privateKey.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.BestAvailableEncryption(b'aes-256-cbc')
        ).decode('utf-8')
        self.publicKey = self.publicKey.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).decode('utf-8')

    @staticmethod
    def sign(privateKey, data):
        """
        Generate a signature based on the data using the local private key
        """
        deserialized_private_key = serialization.load_pem_private_key(
            privateKey.encode('utf-8'),
            default_backend()
        )

        return decode_dss_signature(deserialized_private_key.sign(
            json.dumps(data).encode('utf-8'), 
            ec.ECDSA(hashes.SHA256())
        ))

    @staticmethod
    def verify(public_key, data, signature):
        """
        Verify a signature based on the original public key and data
        """

        deserialized_public_key = serialization.load_pem_public_key(
            public_key.encode('utf-8'),
            default_backend()
        )

        # print(signature)
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

wallet = Wallet()
print(wallet.privateKey)
print(wallet.publicKey)
wallet.serializeKeys()
print(wallet.privateKey)
print(wallet.publicKey)

print(Wallet.sign(wallet.privateKey, 'hello'))