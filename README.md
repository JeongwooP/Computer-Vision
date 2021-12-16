# Computer_Vision
Computer Vision Assignments

## assignment01_01
lenna.bmp 파일을 회색조(grayscale)로 열어서 전체 이미지 중 [200:400, 200:400] 부분만 20 만큼 밝게 처리하여 lenna_20.bmp로 저장했습니다.

![20211215_213539_1](https://user-images.githubusercontent.com/20348923/146374035-233d5387-5e15-45ec-a2c1-12df757a3005.png)

## assignment01_02
lenna.bmp 파일을 회색조(grayscale)로 열어서 전체 이미지 중 [200:400, 200:400] 부분만 50 만큼 밝게 처리하여 lenna_50.bmp로 저장했습니다. (단, 밝기가 255를 넘어가는 부분은 255가 되도록 처리함)

![20211215_213539_2](https://user-images.githubusercontent.com/20348923/146374041-10341c32-94f2-4573-ae67-2aa6c704b1cf.png)

## assignment01_03
stopwatch.avi 파일에서 동영상 시작 10초 후부터 마지막까지 화면의 우하단 1/4 부분을 색상 반전하여 stopwatch_inv.avi로 저장하게 했습니다.

* 출력은 원본 길이인 12초를 유지하되 마지막 2초만 색상 반전

![20211215_213539_3](https://user-images.githubusercontent.com/20348923/146374044-41dce692-789d-420c-b28f-73c173ea22f7.png)


![20211215_213539_4](https://user-images.githubusercontent.com/20348923/146374047-3304c0bb-7f72-47a0-bcdc-f6f3eddbf0a2.png)

## assignment02

### 스캐너 앱

사진을 입력으로 좌측상단부터 시계방향으로 문자인식을 할 영역의 네 모서리를 지정하여 찍습니다.

![20211216_222216_1](https://user-images.githubusercontent.com/20348923/146379685-a936cbc0-fb20-48fe-bd13-f52e430bae5d.png)

1. 장방형으로 화면에 출력

![20211216_222216_2](https://user-images.githubusercontent.com/20348923/146379695-592becbc-5718-465e-939c-679fff7e10df.png)

2. 글자 인식을 위한 이미지 전처리
* 영상의 이진화 -> 영상에서의 noise 제거 -> 모폴로지(erosion) 연산 수행

![20211216_222216_3](https://user-images.githubusercontent.com/20348923/146379697-b4c8ff62-84e5-4e1e-bf32-ba4a5dff0708.png)

3. 전처리를 수행한 이미지에 대하여 Tesseract OCR 엔진을 활용해 이미지 내의 글자를 인식 한 후 일반 텍스트로 콘솔에 출력

![20211216_222216_4](https://user-images.githubusercontent.com/20348923/146379700-79a178b6-b3ed-48bf-9f79-f1d5be8c39c8.png)