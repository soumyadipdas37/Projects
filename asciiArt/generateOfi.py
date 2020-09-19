import PIL.Image
ASCII_CHARS=["@","#","S","%","?","*","+",";",":",",","."]
new_width=40
def resize(image,new_width=80):
    width,height,=image.size
    ratio=height/width
    new_height=int(new_width*ratio)
    resizedImage=image.resize((new_width,new_height))
    return(resizedImage)

def grayify(image):
    grayscaleImage=image.convert("L")
    return(grayscaleImage)

def pixelsToAscii(image):
    pixels=image.getdata()
    characters="".join([ASCII_CHARS[pixel//25]for pixel in pixels])
    return characters

def main(new_width=80):
    path=input("Direccion de la imagen:\n")
    try:
        image=PIL.Image.open(path)
    except:
        print(path,"no es valido")
    newImageData=pixelsToAscii(grayify(resize(image)))
    pixelCount=len(newImageData)
    asciiImage="\n".join(newImageData[i:(i+new_width)]for i in range(0,pixelCount,new_width))
    print(asciiImage)
    with open("pruebas.txt","w" )as f:
        f.write(asciiImage)
    

main()