from PIL import Image, PngImagePlugin

def png_validation(image_path):
    try:
        if(not image_path.read().hex().startswith("89504e470d0a1a0a")):
            print("error")
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
            
        for chunkHeaderIndex, chunkHeader in enumerate(chunkList):
            if chunkHeader in {"sPLT", "iTXt", "tEXt", "zTXt"}:
                if chunkHeader == "sPLT" and chunkHeaderIndex < chunkList.index("IDAT"):
                    return False
            else:
                if chunkHeader != "IDAT" and chunkList.count(chunkHeader) > 1:
                    return False
                if chunkHeader == "pHYs" and chunkHeaderIndex < chunkList.index("IDAT"):
                    return False
                if chunkHeader in {"bKGD", "hIST", "tRNS"} and chunkHeaderIndex < len(chunkList) - 1 - chunkList[::-1].index("IDAT") and chunkHeaderIndex > chunkList.index("PLTE"):
                    return False
                elif chunkHeader in {"cHRM", "gAMA", "iCCP", "sBIT", "sRGB"} and chunkHeaderIndex > len(chunkList) - 1 - chunkList[::-1].index("IDAT"):
                    return False

            
        if("IHDR" not in chunksSet or "IDAT" not in chunksSet or "IEND" not in chunksSet):
            return False

        return True
    except Exception as e:
        print("Exception occured: ")
        print(e)
        return False

# usage example
#print(png_validation(r"C:\\Users\DanielPorath\Documents\TEAM-SAGOL\images\beach.jpg"))
#print(png_validation(r"C:\\Users\DanielPorath\Documents\TEAM-SAGOL\images\bird.png"))
#print(png_validation(r"C:\\Users\DanielPorath\Documents\TEAM-SAGOL\images\butterfly.png"))
#print(png_validation(r"C:\\Users\DanielPorath\Documents\TEAM-SAGOL\images\cat.jpg"))
#print(png_validation(r"C:\\Users\DanielPorath\Documents\TEAM-SAGOL\images\mario.png"))
#print(png_validation(r"C:\\Users\DanielPorath\Documents\TEAM-SAGOL\images\sunflower.jpg"))
