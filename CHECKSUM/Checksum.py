from operator import*

BITS_AMOUNT = 8
BINARY_BASE = 2

# Sum all data parts in binary representation of 8 bits 
def sumDataBlocks(data):
    binaryData = convertToBinary(data)

    # Take the 8 bits from the start of the data and add it to the sum
    while(len(binaryData) > BITS_AMOUNT):
        carry = binaryData[:len(binaryData) - BITS_AMOUNT]
        binaryData = binaryData[len(binaryData) - BITS_AMOUNT:]
        binaryData = bin(add(int(binaryData, BINARY_BASE), int(carry ,BINARY_BASE) ))[2:]

    return binaryData

# Creating checksum of data and adding it to the data in the sender side
def createChecksum(data):
    sum = sumDataBlocks(data)
    checksum = bin(sub(int('11111111', BINARY_BASE), int(sum ,BINARY_BASE)))[2:]

    return data + convertToString(checksum)

# Check the validation of the checksum in the reciever side
def checkChecksumValidation(data):
    sum = sumDataBlocks(data)

    if(sum == '11111111'):
        data = data[:len(data) - 1]
        return True
    
    return False

# Converting string data to binary representation of 8 bits per char
def convertToBinary(messageStr):
    return ''.join(format(ord(messageChar), '08b') for messageChar in messageStr)

# Converting binary representation data of 8 bits to string 
def convertToString(checkSum):
    subBlocks = [checkSum[CSindex:CSindex + BITS_AMOUNT] for CSindex in range(0, len(checkSum), BITS_AMOUNT)]
    return ''.join(chr(int(block, BINARY_BASE)) for block in subBlocks)