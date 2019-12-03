from PIL import Image
import glob
import os


def center_image(image, size):
    # Creates a new image with the given size and transparent background
    centered = Image.new('RGBA', size, color=(0, 0, 0, 0))
    # Finds the offset needed to center the given image to the new one
    center = (int((size[0] - image.size[0]) / 2),
              int((size[1] - image.size[1]) / 2))
    # Pastes the given image into the new one using the offset
    centered.paste(image, center)
    return centered


def resize(image, size):
    ''' Checks if the image needs rezising,
    if so resize the image maintaining the proportions'''
    if image.size != size:
        image.thumbnail((size[0], size[1]), Image.ANTIALIAS)

        ''' Checks if the doesn't complies to the given size,
        adding transparent borders if needed'''
        if image.size != size:
            image = center_image(image, size)

    return image


def resize_all(extensions, size, path=os.getcwd() + '/'):
    # Searches the given folder for all files with the given extensions
    imgNames = []
    for ext in extensions:
        imgNames.extend(glob.glob(path + '*.' + ext))

    # Checks if the subfolder 'RESIZED' doens't exists before creating
    if(not os.path.isdir(path + 'RESIZED')):
        os.mkdir(path + 'RESIZED')

    # Resizes all the images found and saves at the 'RESIZED' subfolder
    for img in imgNames:
        imgName = os.path.basename(img)
        resize(Image.open(img), size).save(path + 'RESIZED/' + imgName)


def resize_one(name, size, path=os.getcwd() + '/'):
    # Checks if the subfolder 'RESIZED' doens't exists before creating
    if(not os.path.isdir(path + 'RESIZED')):
        os.mkdir(path + 'RESIZED')

    # Resizes the image and saves at the 'RESIZED' subfolder
    img = Image.open(path + name)
    resize(img, size).save(path + 'RESIZED/' + name)
