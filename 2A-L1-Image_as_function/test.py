import numpy as np
import cv2
#from matplotlib import *
import matplotlib.pyplot as plt

# Load an color image in grayscale
img = cv2.imread('Fruits.jpg',0);



print img.shape;

print img.dtype;


color = ('b','g','r')
for i,col in enumerate(color):
	histr = cv2.calcHist([img],[i],None,[256],[0,256])
	plt.plot(histr,color = col)
	plt.xlim([0,256])

plt.show()


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
