def validate_png(image_path):
    PNG_MAGIC_NUMBER = "89504e470d0a1a0a"
    PNG_MAGIC_NUMBER_SIZE = len(PNG_MAGIC_NUMBER)
 
    with open(image_path, 'r+b') as image:
        hexData = image.read().hex()
 
         #check signature (8 bytes)
        start = 0
        stop = cursor_0+(8*2)
        cursor_0 = stop
        if hexData[start:stop] != "89504e470d0a1a0a":
            print("signature fail")
        else:
            print("signature succeeded")
 
 
        # check png signature / magic number
        if(image.read(PNG_MAGIC_NUMBER_SIZE) != PNG_MAGIC_NUMBER):
            return False
        else:
            return True
    return True
 
 
 
# usage examples
#print(validate_png("C:\\Users\miunim132\Downloads\jpgExample.jpg"))
#print(validate_png("C:\\Users\miunim132\Downloads\cubes.png"))