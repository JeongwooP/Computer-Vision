import random
import sys
import csv
import cv2
import numpy as np
import pytesseract
from pytesseract import pytesseract as pt

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

from PIL import Image

def setLabel(img, pts, label): #ch12. 레이블링과 외곽선 검출 ppt
    (x, y, w, h) = cv2.boundingRect(pts)
    pt1 = (x, y)
    pt2 = (x + w, y + h)
    cv2.rectangle(img, pt1, pt2, (0, 0, 255), 1)
    cv2.putText(img, label, pt1, cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255))


#step1 - 투시 변환(ch8)
def on_mouse(event, x, y, flags, param):
    global cnt, src_pts

    if event == cv2.EVENT_LBUTTONDOWN:
        if cnt < 4:
            src_pts[cnt, :] = np.array([x, y]).astype(np.float32)
            cnt += 1

            cv2.circle(src, (x, y), 5, (0, 0, 255), -1)
            cv2.imshow('src', src)

        if cnt == 4:
            w = 700
            h = 550

            dst_pts = np.array([[0, 0],
                                [w - 1, 0],
                                [w - 1, h - 1],
                                [0, h - 1]]).astype(np.float32)

            pers_mat = cv2.getPerspectiveTransform(src_pts, dst_pts)

            dst = cv2.warpPerspective(src, pers_mat, (w, h))

            cv2.imshow('dst', dst)

            # step2 - ch.11 영상의 이진화
            if len(sys.argv) > 1:
                filename = sys.argv[1]

            gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY) #https://marisara.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-openCV-1-%EC%9D%B4%EC%A7%84%ED%99%94binarization-thresholding

            if gray is None:
                print('Image load failed!')
                exit()

            _, dst2 = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)

            # step2 - 영상에서의 noise 제거 ch.7 (양방향 필터)

            dst3 = cv2.bilateralFilter(dst2, -1, 10, 5)

            # step2 - ch.11 모폴로지 연산

            _, src_bin = cv2.threshold(dst3, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

            kernel = np.ones((1, 1), np.uint8) #https://webnautes.tistory.com/1257

            erode = cv2.erode(src_bin, kernel, iterations = 1)

            cv2.imshow('erode', erode)

            # bounding box로 표시하여 저장하기 (미완성) https://stackoverflow.com/questions/47260277/cluster-bounding-boxes-and-draw-line-on-them-opencv-python
            # pt.run_tesseract('receipt.jpg', 'output', lang=None, config="box", extension=None)
            #
            # # To read the coordinates
            # boxes = []
            # with open('output.box', 'rt') as f:
            #     reader = csv.reader(f, delimiter=' ')
            #     for row in reader:
            #         if len(row) == 6:
            #             boxes.append(row)
            #
            # # Draw the bounding box
            # img = cv2.imread('receipt.jpg')
            # h, w, _ = img.shape
            # for b in boxes:
            #     img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

            # bounding box로 표시하여 저장하기 (미완성) --------------------------------------------------------------------
            # cv2.imshow('output', img)
            # original = erode.copy()
            # thresh = cv2.threshold(erode, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
            #
            # ROI_number = 0
            # contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            #
            # contours = contours[0] if len(contours) == 2 else contours[1]
            # for c in contours:
            #     x, y, w, h = cv2.boundingRect(c)
            #     cv2.rectangle(erode, (x - 5, y - 5), (x + w + 5, y + h + 5), (36, 255, 12), 2)
            #     ROI = original[y:y + h, x:x + w]
            #     ROI_number += 1
            #
            # cv2.imshow('dst4', erode)

            #Tesseract 로 OCR 엔진 사용해서 이미지 내 글자를 일반 텍스트로 콘솔에 출력 https://m.blog.naver.com/hn03049/221957851802
            #-l kor+eng --oem 3 --psm 4
            config = ('-l eng --oem 3 --psm 4')
            text = pytesseract.image_to_string(erode, config = config)
            print(text)

cnt = 0
src_pts = np.zeros([4, 2], dtype=np.float32)
src = cv2.imread('Lorem.jpg')
src = cv2.resize(src, (700, 900)) #https://ansan-survivor.tistory.com/951

if src is None:
    print('Image load failed!')
    exit()

cv2.namedWindow('src')
cv2.setMouseCallback('src', on_mouse)

cv2.imshow('src', src)

cv2.waitKey(0)
cv2.destroyAllWindows()

