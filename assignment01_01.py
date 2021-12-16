import cv2 as cv

def func1():
    img1 = cv.imread('lenna.bmp', cv.IMREAD_GRAYSCALE)

    img1[200:400, 200:400] = img1[200:400, 200:400] + 20

    cv.imshow('img1', img1)

    cv.imwrite('lenna_20.bmp', img1)

    cv.waitKey()
    cv.destroyAllWindows()

func1()