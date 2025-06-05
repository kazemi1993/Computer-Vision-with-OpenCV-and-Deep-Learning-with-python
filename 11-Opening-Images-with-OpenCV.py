import cv2

img = cv2.imread('C:/Users/kazem/Desktop/code/DATA/ai.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('window_name',img)
cv2.waitKey()