import numpy as np
import cv2

img=cv2.imread("images/circles_target.jpg")
cv2.namedWindow("Lab5")

img = cv2.medianBlur(img,5)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,20,
                            param1=150,param2=58,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(img,(i[0],i[1]),3,(0,0,255),3)


cv2.imshow("Lab5",img)
cv2.waitKey(0)
