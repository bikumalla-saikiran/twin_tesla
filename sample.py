# OpenCV program to perform Edge detection in real time 
# import libraries of python OpenCV 
# where its functionality resides 
import cv2 

# np is an alias pointing to numpy library 
import numpy as np 
x=1
y=1

# capture frames from a camera 
cap = cv2.VideoCapture(0) 


while(1): 

	# reads frames from a camera 
	ret, frame = cap.read() 

	# converting BGR to HSV 
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
	 
	lower_green = np.array([70,100,100]) 
	upper_green = np.array([90,255,255])
        lower_red= np.array([0,133,180])             
        upper_red= np.array([77,179,255])
 
	mask = cv2.inRange(hsv, lower_red, upper_red)
        _,bin = cv2.threshold(mask,120,255,1)
        
        mask1 = cv2.inRange(hsv,lower_green,upper_green)
        ret,bin1 = cv2.threshold(mask1,120,255,1)

	# Bitwise-AND mask and original image 

	# Display an original image 
 
        im1,contours,heirarchy = cv2.findContours(bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        rc = cv2.minAreaRect(contours[0])
        box = cv2.boxPoints(rc)
        print("red")
        for p in box:
          pt = (p[0],p[1])
          print(pt)
          cv2.circle(mask,pt,5,(200,0,0),2)
        if(pt==(639.0, 0.0)):
           x=0
        else:
           x=1
        print(x)
        
        im2,contours1,heirarchy1 = cv2.findContours(bin1, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        rc1 = cv2.minAreaRect(contours1[0])
        box1 = cv2.boxPoints(rc1)
        print("green")
        for q in box1:
          pt1 = (q[0],q[1])
          print(pt1)
          cv2.circle(mask1,pt1,5,(200,0,0),2)
        if(pt1==(639.0, 0.0)):
           y=0
        else:
           y=1
        print(y)  
        
        cv2.imshow('Original',frame) 
        cv2.imshow('final',mask)
	# Wait for Esc key to stop 
	k = cv2.waitKey(5) & 0xFF
	if k == 27: 
		break


# Close the window 
cap.release() 

# De-allocate any associated memory usage 
cv2.destroyAllWindows() 
