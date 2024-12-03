from PIL import Image, ImageEnhance, ImageFilter
import os

path = './images'
pathOut = '/EditedImages'

#access all the imag files and apply the following filter to it.
for filename in os.listdir(path):

    # img variable holds the image object, allowing us to do edits
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN).convert('L')
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    clean_name = os.path.splitext(filename)[0]

    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')


