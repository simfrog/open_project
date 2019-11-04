#gradient(이미지의 변화율)을 이용하여 edge를 찾는 방법

import cv2

src = cv2.imread('edge.png', cv2.IMREAD_COLOR)           #이미지 읽기(cv2.IMREAD_COLOR는 컬러 이미지를 로드한다는 뜻, 이미지 투명성은 무시됨)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)             #이미지의 색상 공간 변경(원본이미지, 색상 변환 코드)

canny = cv2.Canny(src, 100, 255)                         #가장자리 검출 적용(원본 이미지, 임계값1-이하에 포함된 가장자리는 가장자리에서 제외, 임계값2-이상에 포함된 가장자리는 가장자리로 간주, 커널크기-포함안되면 자동할당, L2그라디언트-L1,L2사용 유/무. 사용안하면 자동적 L1)
sobel = cv2.Sobel(gray, cv2.CV_8U, 1, 0, 3)              #가장자리 검출 적용(그레이스케일 이미지, 정밀도, x방향 미분, y방향 미분, 커널-1.3.5.7, 배율, 델타-계산 전 미분 값에 대한 추가값, 픽셀 외삽법-가장자리 처리시, 영역밖의 픽셀은 추정해서 값을 할당)#미분한 결과에 절대값 적용, 값 범위를 8bit unsigned int형으로 바꿈
laplacian = cv2.Laplacian(gray, cv2.CV_8U, ksize=3)      #가장자리 검출 적용(Sobel과 동일)

cv2.imshow("canny", canny)                               #이미지 화면에 표시
cv2.imshow("sobel",sobel)
cv2.imshow("laplacian", laplacian)

cv2.waitKey(0)
cv2.destroyAllWindows()                                 #이미지 윈도우삭제

#3가지 방법을 각각 실행시켜 보았을 때 Sobel은 edge가 잘 추출이 안되었다. Laplacian과 Canny 둘다 edge 추출이 잘 되었지만 Canny가 조금 더 잘 되어서 Canny함수를 이용하기로 결정하였다.
