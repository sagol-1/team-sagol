from AES import AES, Key
from CHECKSUM import Checksum

key = Key.firstCommunicationToMakeKey()
aes = AES.AES(key)

# Function to integrate AES and checksum from sender side
def encryptor(data):
    encrypted, iv = aes.encrypt(data)
    new_data = Checksum.createChecksum(encrypted)
    
    return new_data, iv

# Function to integrate AES and checksum fom reciever side
def decryptor(new_data, iv):
    result, data = Checksum.checkChecksumValidation(new_data)
    
    if(result):
        decrypted = aes.decrypt(data, iv)

        return decrypted
