from PIL import Image

ASCII_CHARS = ["@", "#", "&", ")", "*", "&", "^", "+", ";", "-"]

def resize_img(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_img = image.resize((new_width, new_height))
    return resized_img

def gray(image):
    grayscale_image = image.convert("L")
    return grayscale_image

def toascii(image):
    pixels = image.getdata()
    chars = "".join([ASCII_CHARS[min(pixel // 25, len(ASCII_CHARS) - 1)] for pixel in pixels])
    return chars

def main(new_width=100):
    path = input("Enter path: ").strip()
    try:
        image = Image.open(path)
    except Exception as e:
        print(f"{path} is an invalid path. Error: {e}")
        return

    newimage_data = toascii(gray(resize_img(image, new_width)))   

    pixel_count = len(newimage_data)
    ascii_image = "\n".join(newimage_data[i:(i + new_width)] for i in range(0, pixel_count, new_width))
    print(ascii_image)

    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)

if __name__ == "__main__":
    main()
