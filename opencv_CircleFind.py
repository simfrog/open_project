#houghcircles를 이용하여 원만 추출하기
#edge는 Canny함수를 이용하여 추출

import cv2
import numpy as np

img = cv2.imread('Circles.jpg', 0)
img = cv2.medianBlur(img, 5)
'''관심화소 주변으로 지정한 커널 크기(5x5)내의 픽셀을 크기순으로정렬한 후 중간값을 뽑아서 픽셀값으로 사용
무작위 노이지를 제거하는데 효과적, 하지만 edge가 있는 이미지 경우 결과에서 edge가 사라질 수도 있음.'''

cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 20, param1=5.5, param2=37.5, minRadius=0, maxRadius=0)
'''인자 - 이미지로써 8비트 단일 채널인 Grayscale 이미지, 현재는 cv2.HOUGH_GRADIENT만을 지원, 대부분 1지정
(이 경우 입력 이미지와 동일한 해상도 사용), 검출한 원 중심과의 최소거리값.최소값보다 작으면 원으로 판별안됨,
param1은 Canny Edge에 전달되는 인자값, param2는 검출 결과를 보면서 적당히 조정해야하는 값(작으면 오류 높고,
크면 검출률 낮아짐), minRadius와 masRadius는 각각 원의 최소,최대 반지름(0으로 지정하면 사용안됨)'''

circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
#원 그리기
    
cv2.imshow('img',cimg)

cv2.waitKey(0)
cv2.destroyAllWindows()

'''HoughCircles함수의 인자값 중, param1과 param2를 각각 수정하며 더 정밀하게 원을 추출할수 있도록 하였다.
param2를 먼저조정했을 때 37.5가 가장 원 그림에서 원을 정밀하게 추출하였다. 하지만 색깔이 아주 연한 원은
추출되지 않아 param1을 조정했다. 그결과 param1은 5.5, parma2는 37.5가 원 그림을 가장 정밀하게 추출하였다.'''
