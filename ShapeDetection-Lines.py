import cv2
import numpy as np

img = cv2.imread('images/lines_target.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(gray,21)
edges = cv2.Canny(blur,200,400)
    
lines = cv2.HoughLines(edges,1,np.pi/180,63)
for x in range(0, len(lines)):
    for rho,theta in lines[x]:
       
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))

        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)


cv2.imshow('lab5-b',img)
cv2.waitKey(0)
