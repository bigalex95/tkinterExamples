from PIL import Image, ImageDraw, ImageFont
# get an image
base = Image.open("test2.jpeg").convert("RGBA")

# make a blank image for the text, initialized to transparent text color
txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

# get a drawing context
draw = ImageDraw.Draw(txt)
x, y, w, h = 10, 10, 100, 100  # Rectangle parameters
draw.line([(x, y), (x+w, y+h)], fill=(0, 0, 255, 100), width=20)
draw.line([(x+w, y), (x, y+h)], fill=(255, 255, 255, 100), width=20)
del draw
out = Image.alpha_composite(base, txt)

out.show()
