from PIL import Image
# i = 1
for i in range(1,61):
    img = Image.open(f'img-{i}.png')
    box = (150, 170, 1300, 1000)
    img2 = img.crop(box)
    img2.save(f'QueNo-{i}.png')
    # img2.show()