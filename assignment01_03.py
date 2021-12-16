import cv2 as cv

cap = cv.VideoCapture('stopwatch.avi')
frameCount = 0

# 만약 열리지 않으면 아래 내용 출력
if not cap.isOpened():
    print("Failed to load the video")
    exit()

#동영상의 가로길이, 세로길이 받기
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

print('Frame width:', width)
print('Frame height:', height)
print('Frame count:', int(cap.get(cv.CAP_PROP_FRAME_COUNT)))

fps = cap.get(cv.CAP_PROP_FPS)
print('FPS:', fps)
delay = round(1000 / fps)

fourcc = cv.VideoWriter_fourcc(*'DIVX')
outputVid = cv.VideoWriter('stopwatch_inv.avi', fourcc, fps, (width, height))

while True:
    ret, frame = cap.read()

    if not ret:
        break

    if frameCount >= fps * 10:
        frame[height//2:height, width//2:width] = ~frame[height//2:height, width//2:width]
        outputVid.write(frame)

    cv.imshow('inversed', frame)

    if cv.waitKey(delay) == 27:
        break

    frameCount += 1

    outputVid.write(frame)

cv.destroyAllWindows()