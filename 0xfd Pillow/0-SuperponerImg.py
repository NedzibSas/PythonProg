from PIL import Image

blue = Image.open("blue.png")
red = Image.open("red.png")
red.paste(blue, (100,100), blue)
red.save("result.png")
