from AES import AES, Key
from CHECKSUM import SHA_256_signature as sha256

key = Key.firstCommunicationToMakeKey()
aes = AES.AES(key)

# Function to integrate AES and checksum from sender side
def encryptor(data):
    encrypted = aes.encrypt(data)

    return sha256.createSignature(encrypted)
    
# Function to integrate AES and checksum fom reciever side
def decryptor(new_data):
    result, data = sha256.checkSignatureValidation(new_data)
    
    if(result):
        return aes.decrypt(data)
