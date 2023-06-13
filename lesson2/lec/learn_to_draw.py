from PIL import Image, ImageDraw, ImageFont
canvas = Image.new('RGB', (500, 500), color=(73, 109, 137))
img = ImageDraw.Draw(canvas)

# Draw a rectangle
img.rectangle((100, 100, 400, 400), fill=(255, 255, 255), outline=(0, 0, 0))
img.ellipse((200, 200, 300, 300), fill=(255, 0, 0), outline=(0, 0, 0))

# save the image
canvas.save('rectangle.png')
canvas.show()
