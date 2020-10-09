import numpy as np
import cv2
from sklearn.cluster import KMeans
from collections import Counter

n_clusters = 3 # pick the 3 most common colors

cap = cv2.VideoCapture(0)
width  = int(cap.get(3))
height = int(cap.get(4))

while(1):

	_, frame = cap.read()

	# draw rectangle and get image inside
	x1 = width // 4
	y1 = height // 4
	x2 = width * 3 // 4
	y2 = height * 3 // 4

	frame = cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0),1)
	image = frame[y1:y2, x1:x2].copy()

	# reshape image to be a list of pixels
	image = image.reshape((image.shape[0] * image.shape[1],3))
	# apply K-Means
	clt = KMeans(n_clusters = n_clusters)
	# assign labels to pixels
	labels = clt.fit_predict(image)
	# count labels to find most popular
	label_counts = Counter(labels)
	# get most popular centroid
	dom_color = clt.cluster_centers_[label_counts.most_common(1)[0][0]]

	dom_img = np.zeros((height,width,3), np.uint8)
	dom_img = cv2.rectangle(dom_img, (0,0), (width,height), dom_color, -1)

	cv2.imshow('frame',frame)
	cv2.imshow('dominant color', dom_img)
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
cv2.destroyAllWindows()