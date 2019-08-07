import cv2 as cv
from PIL import Image
import pytesseract #要配置tesseract-ocr 引擎的


def recognize_text():
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (1, 6))#去除线
    binl = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 1))
    open_out = cv.morphologyEx(binl, cv.MORPH_OPEN, kernel)
    cv.bitwise_not(open_out, open_out)# 黑色背景变为白色背景
    cv.imshow('gray', gray)
    cv.imshow('binary', binary)
    cv.imshow('open_out', open_out)

    textImage = Image.fromarray(open_out)#从np.array 转换成<class 'PIL.Image.Image'>，pytesseract需要接受此类型
    text = pytesseract.image_to_string(textImage)
    print("This OK:%s"%text)


if __name__ == '__main__':
    src = cv.imread("code.png")
    cv.imshow("src", src)
    recognize_text()
    cv.waitKey(0)
    cv.destroyAllWindows()