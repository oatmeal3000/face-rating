# USAGE
# python facial_landmarks.py --image images/example_01.jpg 

# import the necessary packages
from imutils import face_utils
import numpy as np
import argparse
import imutils
import dlib
import cv2
import os
import time

def find_facial_landmark(file_name):
	detector = dlib.get_frontal_face_detector()
	image = cv2.imread(file_name)
	#image = imutils.resize(image, width=256)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	rects = detector(gray, 1)
        	
        predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
	landmark_file = open(file_name + '.mark.txt','w')
	for (i, rect) in enumerate(rects):
		shape = predictor(gray, rect)
         	shape = face_utils.shape_to_np(shape)
		for (x, y) in shape:
	        	cv2.circle(image, (x, y), 1, (0, 0, 255), -1)
	        	landmark_file.write(str(x) + ', ' + str(y) + ', ')
	       	landmark_file.write("\n")
        landmark_file.close()
        cv2.imshow("image", image)
        cv2.waitKey(3000)
        return shape


def find_facial_landmarks(file_name):
	# initialize dlib's face detector (HOG-based) and then create
	# the facial landmark predictor
	detector = dlib.get_frontal_face_detector()
	predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

	# load the input image, resize it, and convert it to grayscale
	image = cv2.imread(file_name)
	#image = imutils.resize(image, width=256)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# detect faces in the grayscale image
	rects = detector(gray, 1)

	landmark_file = open('../data/landmark.txt','a')
	# loop over the face detections
	for (i, rect) in enumerate(rects):
	# determine the facial landmarks for the face region, then
	# convert the facial landmark (x, y)-coordinates to a NumPy
	# array
		shape = predictor(gray, rect)
         	shape = face_utils.shape_to_np(shape)

	# convert dlib's rectangle to a OpenCV-style bounding box
	# [i.e., (x, y, w, h)], then draw the face bounding box
	#	(x, y, w, h) = face_utils.rect_to_bb(rect)
	#cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

	# show the face number
	#cv2.putText(image, "Face #{}".format(i + 1), (x - 10, y - 10),
	#cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

	# loop over the (x, y)-coordinates for the facial landmarks
	# and draw them on the image
		for (x, y) in shape:
	#	cv2.circle(image, (x, y), 1, (0, 0, 255), -1)
	        	landmark_file.write(str(x) + ', ' + str(y) + ', ')
	       	landmark_file.write("\n")
        landmark_file.close()


if __name__=="__main__":
# construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True,
	help="path to input image")
    args = vars(ap.parse_args())

    if os.path.isdir(args["image"]):
        list_im = os.listdir(args["image"])
        list_im.sort(reverse = True, key=lambda x:int(x[8:-4]))
        for im_file in list_im:
            find_facial_landmarks(args["image"] + "/" + im_file)
    else:
        find_facial_landmark(args["image"])


