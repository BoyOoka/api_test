from PIL import Image
import pytesseract


if __name__ == '__main__':
    image = Image.open('word.png')
    result = pytesseract.image_to_string(image, lang='chi_sim')
    print(result)
