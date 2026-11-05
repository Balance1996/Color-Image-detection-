from PIL import Image

# Open the AVIF image you saved
img = Image.open("colorwonder.avif")

# Convert and save it as a perfect PNG file
img.save("Ready_for_wonder"
         ".png", "PNG") #The save() function takes the raw pixels and repackages them
#    into a brand-new compressed file format container.
print("Conversion complete! Check your project sidebar for g")
