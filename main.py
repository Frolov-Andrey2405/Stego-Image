import os
from stegano import lsb, exifHeader

class ImageSteganography:
    def __init__(self, img_dir='img/'):
        self.img_dir = img_dir

    def hide_msg_png(self, img, msg, secret_img=None):
        if secret_img is None:
            secret_img = f'{os.path.splitext(img)[0]}_secret.png'
        secret_img_path = os.path.join(self.img_dir, secret_img)
        img_path = os.path.join(self.img_dir, img)

        secret_img = lsb.hide(img_path, msg)
        secret_img.save(secret_img_path)

    def reveal_msg_png(self, secret_img):
        secret_img_path = os.path.join(self.img_dir, secret_img)
        return lsb.reveal(secret_img_path)

    def hide_msg_jpg(self, img, msg, secret_img=None):
        if secret_img is None:
            secret_img = f'{os.path.splitext(img)[0]}_secret.jpg'
        secret_img_path = os.path.join(self.img_dir, secret_img)
        img_path = os.path.join(self.img_dir, img)

        exifHeader.hide(img_path, secret_img_path, msg)

    def reveal_msg_jpg(self, secret_img):
        secret_img_path = os.path.join(self.img_dir, secret_img)
        return exifHeader.reveal(secret_img_path).decode()

if __name__ == '__main__':
    try:
        steg = ImageSteganography()
        PNG_IMG = '1.png'
        JPG_IMG = '2.jpg'
        SECRET_MSG_PNG = 'Png image format'
        SECRET_MSG_JPG = 'Jpg image format'

        steg.hide_msg_png(PNG_IMG, SECRET_MSG_PNG)
        print(steg.reveal_msg_png(f'{PNG_IMG.split(".")[0]}_secret.png'))

        steg.hide_msg_jpg(JPG_IMG, SECRET_MSG_JPG)
        print(steg.reveal_msg_jpg(f'{JPG_IMG.split(".")[0]}_secret.jpg'))
    except Exception as e:
        print(f'An error occurred: {e}')
