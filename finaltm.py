import cv2 
import numpy as np 
  
x=0
cap = cv2.VideoCapture(0)
while(1):
 ret,frame = cap.read()

 img_rgb = cv2.imread('stop.jpg') 
 temp2 = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2HSV)
 temp = cv2.GaussianBlur(temp2,(5,5),0)
 hsv2 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  
 hsv = cv2.GaussianBlur(hsv2,(5,5),0)
 

 lower_red= np.array([0,133,180])             
 upper_red= np.array([7,179,255])
 
 mask = cv2.inRange(hsv, lower_red, upper_red)  
 ret,bin = cv2.threshold(mask,127,255,cv2.THRESH_BINARY)
 
 mask1 = cv2.inRange(temp, lower_red, upper_red)
 ret1,bin1 = cv2.threshold(mask1,127,255,cv2.THRESH_BINARY)
 
 w,h = bin1.shape[::-1]
 res = cv2.matchTemplate(bin,bin1,cv2.TM_CCOEFF_NORMED)
 threshold = 0.09
 loc = np.where(res>=threshold)
 for pt in zip(*loc[::-1]): 
    cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2) 
    x=1
 print(x)
 cv2.imshow('original',frame)
 cv2.imshow('template',img_rgb)
 cv2.imshow('res',res)
 cv2.imshow('hsv1',hsv)
 cv2.imshow('bin',bin)
 k= cv2.waitKey(5) & 0xFF
 if k==27:
  break

cap.release()
cv2.destroyAllWindows()
