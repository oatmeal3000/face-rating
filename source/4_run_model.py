from sklearn.externals import joblib
import numpy as np
from sklearn import decomposition
from 1_facial_landmarks import find_facial_landmark
from 2_create_feature import generateALLFeatures

p = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())

landmarks = find_facial_landmark(args["image"])
my_features = generateAllFeatures(landmarks) 
#use your own path
clf = joblib.load('../model/face_model.pkl')
predictions = clf.predict(my_features)
print predictions
