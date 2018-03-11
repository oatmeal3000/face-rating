import math
import numpy
import itertools

def facialRatio(points):
	x1 = points[0];
	y1 = points[1];
	x2 = points[2];
	y2 = points[3];
	x3 = points[4];
	y3 = points[5];
	x4 = points[6];
	y4 = points[7];

	dist1 = math.sqrt((x1-x2)**2 + (y1-y2)**2)
	dist2 = math.sqrt((x3-x4)**2 + (y3-y4)**2)

	ratio = dist1/dist2

	return ratio


def generateFeatures(pointIndices1, pointIndices2, pointIndices3, pointIndices4, allLandmarkCoordinates):
	size = allLandmarkCoordinates.shape
        if allLandmarkCoordinates.ndim == 1:
            line_index = 1 
	    allFeatures = numpy.zeros((1, len(pointIndices1)))
        else:
	    allFeatures = numpy.zeros((size[0], len(pointIndices1)))
            line_index = size[0]
            
	for x in range(0, line_index):
                if line_index == 1:
                    landmarkCoordinates = allLandmarkCoordinates
                else:
                    landmarkCoordinates = allLandmarkCoordinates[x, :]
		ratios = [];
		for i in range(0, len(pointIndices1)):
			x1 = landmarkCoordinates[2*(pointIndices1[i]-1)]
			y1 = landmarkCoordinates[2*pointIndices1[i] - 1]
			x2 = landmarkCoordinates[2*(pointIndices2[i]-1)]
			y2 = landmarkCoordinates[2*pointIndices2[i] - 1]

			x3 = landmarkCoordinates[2*(pointIndices3[i]-1)]
			y3 = landmarkCoordinates[2*pointIndices3[i] - 1]
			x4 = landmarkCoordinates[2*(pointIndices4[i]-1)]
			y4 = landmarkCoordinates[2*pointIndices4[i] - 1]

			points = [x1, y1, x2, y2, x3, y3, x4, y4]
			ratios.append(facialRatio(points))
		allFeatures[x, :] = numpy.asarray(ratios)
	return allFeatures


def generateAllFeatures(allLandmarkCoordinates):
        combinations = [[28, 34, 34, 9], [40, 43, 32, 36], [40, 43, 37, 40], [40, 43, 43, 46], [37, 40, 43, 46], [49, 55, 32, 36], [3, 15, 32, 36], [41, 47, 40, 43], [41, 47, 32, 36], [49, 55, 40, 43], [52, 9, 40, 43], [52, 9, 32, 36],[40, 43, 52, 58], [32, 36, 52, 63], [40, 43, 34, 63], [52, 58, 34, 63], [34, 9, 63, 9], [32, 36, 34, 63], [20, 28,25, 28], [40, 28, 43, 28], [42, 28, 47, 28], [32, 34, 36, 34], [51, 34, 53, 52], [49, 63, 49, 55], [1, 28, 17, 28], [38, 44, 28, 63], [38, 44, 3, 15], [39, 63, 44, 63], [28, 30, 30, 9]] 

	pointIndices1 = [];
	pointIndices2 = [];
	pointIndices3 = [];
	pointIndices4 = [];

	for combination in combinations:
		pointIndices1.append(combination[0])
		pointIndices2.append(combination[1])
		pointIndices3.append(combination[2])
		pointIndices4.append(combination[3])

        return generateFeatures(pointIndices1, pointIndices2, pointIndices3, pointIndices4, allLandmarkCoordinates)




if __name__=="__main__":
    landmarks = numpy.loadtxt('../data/landmark.txt', delimiter=',', usecols=range(136))
    featuresALL = generateAllFeatures(landmarks)
    numpy.savetxt('../data/features_ALL.txt', featuresALL, delimiter=',', fmt = '%.04f')

