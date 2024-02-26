# Import Pillow’s Image class:
from PIL import Image
for i in range(1,34):
    img = Image.open(f'img-{i}.png')
    box = (150, 170, 1300, 1000)
    img2 = img.crop(box)
    img2.save(f'crop-{i}.png')
    # img2.show()