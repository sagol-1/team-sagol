import random
import hashlib

class DHKE:
    def __init__(self, G, P):
        self.G_param = G
        self.P_param = P

    def generate_privatekey(self):
        self.pk = random.randrange(start=1, stop=10, step=1)  # Private key

    def generate_publickey(self):
        self.pub_key = pow(self.G_param, self.pk, self.P_param)  # Public key

    def exchange_key(self, other_public):
        self.share_key = pow(other_public, self.pk, self.P_param)  # Shared key

    def keyForAes(self):
        # Hash the shared key to derive a 128-bit AES key
        sharedSecretBytes = str(self.share_key).encode()
        hashObj = hashlib.sha256(sharedSecretBytes)  # Secure hash
        aesKey = hashObj.digest()[:16]  # 16 bytes = 128 bits
        return aesKey  # Return raw bytes for AES

# Function to simulate key exchange and generate AES key
def firstCommunicationToMakeKey():
    # Common generator (G) and prime (P)
    G = 2
    P = 326667157375743383456244446378089901791

    # Create encryptor 1
    encryptor1 = DHKE(G, P)
    encryptor1.generate_privatekey()
    encryptor1.generate_publickey()

    # Create encryptor 2
    encryptor2 = DHKE(G, P)
    encryptor2.generate_privatekey()
    encryptor2.generate_publickey()

    # Exchange keys
    encryptor1.exchange_key(encryptor2.pub_key)
    encryptor2.exchange_key(encryptor1.pub_key)

    # Verify shared keys match
    assert encryptor1.keyForAes() == encryptor2.keyForAes(), "Key exchange failed!"

    # Return the shared AES key (128 bits)
    return encryptor1.keyForAes()
