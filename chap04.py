import numpy as np
import cv2 as cv

img = np.full((400, 400, 3), 255, np.uint8)

cv.line(img, (50, 50), (200, 50), (0, 0, 255))
cv.line(img, (50, 100), (200, 100), (255, 0, 255), 3)
cv.line(img, (50, 150), (200, 150), (255, 0, 0), 10)

cv.line(img, (250, 50), (350, 100), (0, 0, 255), 1, cv.LINE_4)
cv.line(img, (250, 70), (350, 120), (255, 0, 255), 1, cv.LINE_8)
cv.line(img, (250, 90), (350, 140), (255, 0, 0), 1, cv.LINE_AA)

cv.imshow("img", img)
cv.waitKey()
cv.destroyAllWindows()