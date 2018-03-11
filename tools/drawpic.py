import cv2
import numpy

im = cv2.imread("test1.jpg")
landmarks = numpy.loadtxt('landmark1.txt', delimiter=',', usecols=range(136))

for idx in range(0, len(landmarks)/2):
    cv2.circle(im, (int(landmarks[idx * 2]), int(landmarks[idx * 2 + 1])), 1, (0, 0, 255), -1)
    cv2.imshow("image", im)
    cv2.waitKey(0)


