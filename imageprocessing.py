import numpy as np 
import cv2
import RPi.GPIO as GPIO       

x=1
y=1
z=0

GPIO.setmode(GPIO.BCM)        
GPIO.setwarnings(False)   
GPIO.setup(18,GPIO.OUT)      
cap = cv2.VideoCapture(0) 

while(1): 

	# reads frames from a camera 
	ret, frame = cap.read() 

	# converting BGR to HSV 
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
        img_rgb = cv2.imread('stop.jpg') 
        temp = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2HSV)
	 
	lower_green = np.array([70,100,100]) 
	upper_green = np.array([90,255,255])
        lower_red= np.array([0,133,180])             
        upper_red= np.array([7,179,255])
 
	mask = cv2.inRange(hsv, lower_red, upper_red)
        _,bin = cv2.threshold(mask,120,255,cv2.THRESH_BINARY)
        
        mask1 = cv2.inRange(hsv,lower_green,upper_green)
        ret,bin1 = cv2.threshold(mask1,120,255,cv2.THRESH_BINARY)

        mask2 = cv2.inRange(temp, lower_red, upper_red)
        ret2,bin2 = cv2.threshold(mask2,127,255,cv2.THRESH_BINARY)

        w,h = bin2.shape[::-1]
        res = cv2.matchTemplate(bin,bin2,cv2.TM_CCOEFF_NORMED)
        threshold = 0.09
        loc = np.where(res>=threshold)
        for pt in zip(*loc[::-1]): 
          cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2) 
            z=1 
        print('stop')
        print(z)
 
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
        print('red')
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
        print('green')
        print(y)  
         
        if(x==1 | z==1):
         GPIO.output(18,GPIO.HIGH)             
	else if(x==1 | y==1):
         GPIO.output(18,GPIO.HIGH)
        else if(z==1 | y==1):
         GPIO.output(18,GPIO.HIGH)
        else:
         GPIO.output(18,GPIO.LOW)  
         
	k = cv2.waitKey(5) & 0xFF
	if k == 27: 
		break

cap.release() 
cv2.destroyAllWindows() 
