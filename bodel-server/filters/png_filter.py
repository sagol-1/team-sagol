from PIL import Image, PngImagePlugin

def validate_png(image_path):
    try:
        with open(image_path, 'r+b') as image:
            if(not image.read().hex().startswith("89504e470d0a1a0a")):
                print("signature invalid")
                return False
            
        im = Image.open(image_path)
        rawChunkList = PngImagePlugin.getchunks(im)
        chunkList = list(map(lambda element: element[0].decode(), rawChunkList))

        if(chunkList[0] != "IHDR" or chunkList[len(chunkList) - 1] != "IEND"):
            return False
        
        if("PLTE" in chunkList):
            if(chunkList.index("PLTE") > chunkList.index("IDAT") or chunkList.count("PLTE") > 1):
                return False
        
        validChunkHeaders = {"IHDR", "PLTE", "IDAT", "IEND", "bKGD", "cHRM", "cICP", "dSIG", "eXIf", "gAMA", "hIST", "iCCP", "iTXt", "pHYs", "sBIT", "sPLT", "sRGB", "sTER", "tEXt", "tIME", "tRNS", "zTXt"}
        
        chunksSet = set(chunkList)

        for chunkHeader in chunksSet:
            if(chunkHeader not in validChunkHeaders):
                return False

        if("IHDR" not in chunksSet or "IDAT" not in chunksSet or "IEND" not in chunksSet):
            return False

        return True
    except Exception as e:
        print("Exception occured: ")
        print(e)
        return False

# usage example
print(validate_png(r"C:\\Users\DanielPorath\Documents\TEAM-SAGOL\images\bird.png"))
