import hashlib

SIGNATURE_BYTES_AMOUNT = 64

# Creating checksum of data and adding it to the data in the sender side
def createSignature(data):
    signature = hashlib.sha256(data.encode()).hexdigest()

    return data + signature

# Check the validation of the checksum in the reciever side
def checkSignatureValidation(data):
    actualSignature = hashlib.sha256(data[:len(data) - SIGNATURE_BYTES_AMOUNT].encode()).hexdigest()

    if(data[len(data) - SIGNATURE_BYTES_AMOUNT:] == actualSignature):
        return True, data[:len(data) - SIGNATURE_BYTES_AMOUNT]
    
    return False

