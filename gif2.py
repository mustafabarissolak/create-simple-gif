from PIL import Image, ImageDraw
# pip install pillow

width, height = 300, 300
background_color = (255, 255, 255)  # Beyaz
frames = []

for i in range(10):
    image = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(image)
    shape_box = (i * 10, i * 10, width - i * 10, height - i * 10)
    draw.rectangle(shape_box, outline=(0, 0, 0))
    frames.append(image)

frames[0].save("simple_shape.gif", save_all=True, append_images=frames[1:], duration=100, loop=0)
