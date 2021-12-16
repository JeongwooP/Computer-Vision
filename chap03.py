import cv2 as cv
import numpy

#과제

def func3():
    img1 = cv.imread('penguin.jpg')

    img2 = img1[100:250, 50:300]
    img1[100:250, 50:300] = 255 - img1[100:250, 50:300]
    img3 = img1[100:250, 50:300].copy()

    img2 = 255 - img2

    cv.imshow('img1', img1)
    cv.imshow('img2', img2)
    cv.imshow('img3', img3)

    cv.waitKey()
    cv.destroyAllWindows()

func3()
