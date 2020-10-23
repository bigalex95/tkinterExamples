from PIL import Image, ImageDraw

img = Image.new('RGB', (100, 100))
drw = ImageDraw.Draw(img, 'RGBA')
drw.polygon([(50, 0), (100, 100), (0, 100)], (255, 0, 0, 125))
drw.polygon([(50, 100), (100, 0), (0, 0)], (0, 255, 0, 125))
del drw

img.save('out.png', 'PNG')
