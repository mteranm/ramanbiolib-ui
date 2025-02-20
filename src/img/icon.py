from PIL import Image

# Open the PNG image
png_image = Image.open("icon.png")

# Convert and save as .ico
png_image.save("icon.ico", format="ICO", sizes=[(32, 32), (64, 64), (128, 128), (256, 256), (512, 512)])
