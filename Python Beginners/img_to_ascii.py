from PIL import Image

# ASCII characters that will be used to create the output
ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100):
    """Resize the image while maintaining the aspect ratio."""
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)  # The 0.55 accounts for character height scaling
    return image.resize((new_width, new_height))

def grayify(image):
    """Convert the image to grayscale."""
    return image.convert("L")

def pixels_to_ascii(image):
    """Convert the image to ASCII characters."""
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel // 32]  # Map pixel value to ASCII character
    return ascii_str

def image_to_ascii(image_path, new_width=100):
    """Main function to convert an image to ASCII art."""
    # Open the image
    image = Image.open(image_path)
    
    # Resize the image
    image = resize_image(image, new_width)
    
    # Convert the image to grayscale
    image = grayify(image)
    
    # Convert pixels to ASCII
    ascii_str = pixels_to_ascii(image)
    
    # Format the ASCII string into proper width lines
    img_width = image.width
    ascii_str_len = len(ascii_str)
    ascii_img = "\n".join([ascii_str[i:(i + img_width)] for i in range(0, ascii_str_len, img_width)])
    
    return ascii_img

def save_ascii_image(ascii_img, output_path="ascii_image.txt"):
    """Save the ASCII art to a text file."""
    with open(output_path, "w") as f:
        f.write(ascii_img)

# Path to the image
image_path = "/"

# Convert image to ASCII
ascii_art = image_to_ascii(image_path)

# Save the ASCII art to a file
save_ascii_image(ascii_art)

# Optionally, print the ASCII art
print(ascii_art)
