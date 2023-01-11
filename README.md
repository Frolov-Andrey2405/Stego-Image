# Stego-Image
This code is a Python script that uses the stegano library to perform steganography on image files. Steganography is the process of hiding information within other data, in this case, hiding a text message within an image file.

## Code functionality: 
The script defines a class called `ImageSteganography` which has four methods: `hide_msg_png`, `reveal_msg_png`, `hide_msg_jpg`, and `reveal_msg_jpg`. These methods are used to hide and reveal messages in PNG and JPG image files, respectively.

The `__init__` method of the class takes an optional parameter `img_dir`, which is the directory where the images are stored. If no value is provided, it defaults to `'img/'`. The `img_dir` attribute is then set to the value provided or the default.

The `hide_msg_png` method takes in three parameters: the `img` file name, the `msg` that needs to be hidden, and an optional `secret_img` file name. If the `secret_img` is not provided, it creates a new file name by taking the original file name and appending `'_secret.png'` to it. It then uses the `lsb.hide()` method of the `stegano` library to hide the message within the image, and saves the resulting image with the `secret_img` file name.

The `reveal_msg_png` method takes in one parameter `secret_img` the name of the secret image file. It uses the `lsb.reveal()` method of the `stegano` library to reveal the message hidden within the image.

The hide_msg_jpg and reveal_msg_jpg methods work in a similar way, but they use the exifHeader module of the stegano library to hide and reveal messages in JPG images.

In the `if __name__ == '__main__':` block, the script creates an instance of the `ImageSteganography` class, sets some image and message constants, and then uses the class's methods to hide and reveal messages in PNG and JPG images. The result of each reveal method is printed to the console. If an error occurs during the execution of the script, an error message will be printed.

#### Technologies and Libraries
- **[Python 3.x+](https://www.python.org/)**: the main programming language that was used 
- **[stegano](https://pypi.org/project/stegano/)**: to perform steganography on image files. 