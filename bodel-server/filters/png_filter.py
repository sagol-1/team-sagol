def png_validation(png_img):
    try:
        cursor_0 = 0
        chunksList = []
    
        with open(png_img, 'r+b') as image:
            hexData = image.read().hex()
    
            # check signature / magic bytes
            start = 0
            stop = cursor_0+(8*2)
            cursor_0 = stop 

            if hexData[start:stop] != "89504e470d0a1a0a":
                #print("signature fail")
                return False
            #else:
                #print("signature succeeded")
            
            read = True

            while read:
                # new chunk reading
                # read length of the chunk (4 bytes)
                start = cursor_0
                stop = cursor_0+(4*2)
                cursor_0 = stop
                chunkDataLength = int(hexData[start:stop],16)
                #print("chunk data length")
                #print(chunkDataLength)

                # read type of the chunk (4 bytes)
                start = cursor_0
                stop = cursor_0+(4*2)
                cursor_0 = stop
                chunkTypeHex = hexData[start:stop]
                chunkType = bytes.fromhex(hexData[start:stop]).decode()
                #print("chunk type: ")
                #print(chunkType)
                chunksList.append(chunkType)

                # read the data of the chunk (variable)
                start = cursor_0
                stop = cursor_0+(chunkDataLength*2)
                cursor_0 = stop
                chunkDataHex = hexData[start:stop]
                # print("chunk data hex: ")
                # print(chunkDataHex)

                # read the CRC of the chunk (4 bytes)
                start = cursor_0
                stop = cursor_0+(4*2)
                cursor_0 = stop
                chunkCrcHex = hexData[start:stop]
                #print("chunk crc hex: ")
                #print(chunkCrcHex)

                if chunkType == "IEND":
                    read = False

        # future: condition that checks for duplicate chunks
        # future: condition that checks crc calculation
        chunksSet = set(chunksList)
        if("IHDR" not in chunksSet or "IDAT" not in chunksSet or "IEND" not in chunksSet):
            return False
        #print(chunksList)
        return True
    except Exception as e:
        print("Exception occured: ")
        print(e)
        return False