from AES import AES, Key
from CHECKSUM import Checksum

key = Key.firstCommunicationToMakeKey()
aes = AES.AES(key)

def encode(data):
    encrypted, iv = aes.encrypt(data)
    new_data = Checksum.createChecksum(encrypted)
    
    return new_data, iv

def decode(new_data, iv):
    result, data = Checksum.checkChecksumValidation(new_data)
    
    if(result):
        decrypted = aes.decrypt(data, iv)

        return decrypted

if __name__ == "__main__":
    original_data = "Hello, Team Sagol!"
    print(f"Original Data: {original_data}")
    encoded_data, iv = encode(original_data)
    decoded_data = decode(encoded_data, iv)
    print(f"New Data: {decoded_data}")
    