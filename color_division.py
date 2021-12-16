import cv2

src = cv2.imread('hello.png') # size 축소

src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

lower_red = (150, 50, 50)
upper_red = (180, 255, 255)

dst = cv2.inRange(src_hsv, lower_red, upper_red)
img_result = cv2.bitwise_and(src, src, mask = dst)

no_red = src - img_result
gray = cv2.cvtColor(no_red, cv2.COLOR_BGR2GRAY)

cv2.imshow('src', src)

cv2.imshow('img', gray)

cv2.waitKey()
cv2.destroyAllWindows()
