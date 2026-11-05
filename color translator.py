
from  PIL import Image

#Open the PNG
image=Image.open("Ready_for_wonder.png").convert("RGB")



#get width and height
width,height=image.size
#checking for resolutions
print("Width:", width)
print("Height:", height)
print("Resolution:", image.size)
#prep empty list
translate_li=[]
#sampling coordinates
start_x=311
start_y=326
spacing_x=356
spacing_y=356
print("Image dimensions:", image.size)
print("First pixel:", image.getpixel((50, 50)))
for row in range(8):
    for column in range(10):
        x_cor=start_x+column*spacing_x
        y_cor=start_y+row*spacing_y
        color=image.getpixel((x_cor,y_cor))

        
        print(f"Coordinates: ({x_cor}, {y_cor}) | RGB: {color}")
    translate_li.append(color)
print(translate_li)
print("Program finished.")