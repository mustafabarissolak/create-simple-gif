# teerminale "pip install pillow" yüklüyoruz

# "PIL" kütüphanesinden "Image" ve "ImageDraw" modüllerini içe aktarıyoruz.
from PIL import Image, ImageDraw

# GIF boyutları ve arka plan rengi
width, height = 300, 300
background_color = (255, 255, 255)  # Beyaz

# GIF oluşturmak için bir döngü kullanıyoruz. 
# Bu döngü, her karede bir resim oluşturacak ve ardından bu resmi "frames" adlı bir listeye ekleyecektir. 
# "num_frames" değişkeni toplam kare sayısını belirtir.
frames = []
num_frames = 30

for i in range(num_frames):
    # Yeni bir resim oluştur
    image = Image.new("RGB", (width, height), background_color)

    # Renk geçişi oluşturmak için bir renk oluşturuyoruz. 
    # Bu renk, her karenin arkaplan rengini ve hareket eden dairenin rengini belirlemek için kullanılacaktır
    gradient_color = (i * 10, 0, 255 - i * 10)

    # Resim çizimi için "ImageDraw" nesnesi oluştur
    draw = ImageDraw.Draw(image)

    # Arka planı çizmek için "draw.rectangle" fonksiyonunu kullanıyoruz:
    draw.rectangle([0, 0, width, height], fill=background_color)

    # Hareket eden daireyi çizmek için "draw.ellipse" fonksiyonunu kullanıyoruz. 
    # "x_pos" ve "y_pos" değişkenleri, dairenin her karedeki konumunu belirler:
    radius = 20
    x_pos = (width - 2 * radius) * i / (num_frames - 1)
    y_pos = height / 2
    circle_box = [x_pos, y_pos - radius, x_pos + 2 * radius, y_pos + radius]
    draw.ellipse(circle_box, fill=gradient_color, outline=(0, 0, 0))

    # Oluşturulan resmi "frames" listesine ekliyoruz:
    frames.append(image)

# GIF'i kaydet
frames[0].save("colorful_circle.gif", save_all=True,
               append_images=frames[1:], duration=100, loop=0)
