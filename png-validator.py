def validate_png(image_path):
    PNG_MAGIC_NUMBER = "89504e470d0a1a0a"
    PNG_MAGIC_NUMBER_SIZE = len(PNG_MAGIC_NUMBER)

    cursor_0 = 0
 
    with open(image_path, 'r+b') as image:
        hexData = image.read().hex()
 
        #check signature / magic bytes
        start = 0
        stop = cursor_0+(8*2)
        cursor_0 = stop
        if hexData[start:stop] != "89504e470d0a1a0a":
            print("signature fail")
            return False
        else:
            print("signature succeeded")
            return True
 
    return True
 
 
 
# usage examples
print(validate_png("C:\\Users\DanielPorath\Documents\TEAM-SAGOL\images\\beach.jpg"))
print(validate_png("C:\\Users\DanielPorath\Documents\TEAM-SAGOL\images\\mario.png"))
