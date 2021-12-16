import numpy as np
import cv2 as cv

def func2():
    img1 = cv.imread('lenna.bmp', cv.IMREAD_GRAYSCALE)

    img1 = img1.astype('int32')
    img1[200:400, 200:400] = np.clip(img1[200:400, 200:400] + 50, 0, 255)
    img1 = img1.astype('uint8')

    cv.imshow('img1', img1)

    cv.imwrite('lenna_50.bmp', img1)

    cv.waitKey()
    cv.destroyAllWindows()

func2()