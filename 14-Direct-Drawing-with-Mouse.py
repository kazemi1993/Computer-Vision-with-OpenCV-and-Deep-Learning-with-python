import cv2
import numpy as np

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),100,(255,0,0),9)

img = cv2.imread("C:/Users/kazem/Desktop/code/DATA/ai.jpg")
cv2.namedWindow(winname='ai')
cv2.setMouseCallback('ai',draw_circle)

while True:
    cv2.imshow('ai',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
