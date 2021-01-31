from PIL import Image, ImageDraw, ImageFont

text = '4'
color = (255, 0, 0)


def image_add_number(fileName):
    try:
        im = Image.open(fileName)
        x, y = im.size
        print("the size of image:", "x=", x, " ", "y=", y)
        im.show()

        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype('Arial.ttf', 35)
        draw.text((x - 20, 7), text, color, font)
        im.save('number_image.jpeg')
        im.show()
    except:
        print("unable to open image")


if __name__ == '__main__':
    image_add_number("image.jpeg")