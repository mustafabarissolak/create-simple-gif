# pip install pillow

from PIL import Image, ImageDraw

width, height = 300, 300
background_color = (255, 255, 255) 
frames = []
num_frames = 30

for i in range(num_frames):
    image = Image.new("RGB", (width, height), background_color)
    gradient_color = (i * 10, 0, 255 - i * 10)
    
    draw = ImageDraw.Draw(image)
    draw.rectangle([0, 0, width, height], fill=background_color)
    
    radius = 20
    x_pos = (width - 2 * radius) * i / (num_frames - 1)
    y_pos = height / 2
    circle_box = [x_pos, y_pos - radius, x_pos + 2 * radius, y_pos + radius]
    
    draw.ellipse(circle_box, fill=gradient_color, outline=(0, 0, 0))
    frames.append(image)


frames[0].save("colorful_circle.gif", save_all=True, append_images=frames[1:], duration=100, loop=0)
