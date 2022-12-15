from PIL import Image


def is_image_contains_box(image):
    width, height = image.size
    # if (image.getpixel((1, 1)) != (248, 241, 231)):
    #     return False
    count_in_box = 0
    count_out_box = 0
    for y in range(height):
        color = image.getpixel((1, y))
        print(color, y)
        # if all colors are between 60 and 65
        if all(50 <= c <= 70 for c in color):
            count_in_box += 1
        # if color are similar to (248, 241, 231)
        if all(220 <= c <= 250 for c in color):
            count_out_box += 1

    if count_in_box > 100 and count_out_box > 1000:
        return True
    return False


image = Image.open("./images/1602581918905733120_1.jpg")
print(is_image_contains_box(image))
