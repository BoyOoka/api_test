import tesserocr
from PIL import Image
import pytesseract

if __name__ == '__main__':
    image = Image.open('C:/Users/lijiafei/Desktop/verifycode/verfycode.jpg')
    # print(tesserocr.image_to_text(image))  # print ocr text from image
    # or
    print(tesserocr.file_to_text('C:/Users/lijiafei/Desktop/verifycode/verfycode.jpg'))
    print(pytesseract.image_to_string(image), 1)
