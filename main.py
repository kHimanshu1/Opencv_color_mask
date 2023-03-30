import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def empty(a):
    pass

cv2.namedWindow("HSV")
cv2.resizeWindow("HSV",620,240)
cv2.createTrackbar('Hue_min',"HSV",0,179,empty)
cv2.createTrackbar('Hue_max',"HSV",0,179,empty)
cv2.createTrackbar('Sat_min',"HSV",0,255,empty)
cv2.createTrackbar('Sat_max',"HSV",0,255,empty)
cv2.createTrackbar('Value_min',"HSV",0,255,empty)
cv2.createTrackbar('Value_max',"HSV",0,255,empty)


while True:
    
    h_min = cv2.getTrackbarPos('Hue_min','HSV')
    h_max = cv2.getTrackbarPos('Hue_max','HSV')
    sat_min = cv2.getTrackbarPos('Sat_min','HSV')
    sat_max = cv2.getTrackbarPos('Sat_max','HSV')
    v_min = cv2.getTrackbarPos('Value_min','HSV')
    v_max = cv2.getTrackbarPos('Value_max','HSV')
    
    lower = np.array([h_min,sat_min,v_min])
    upper = np.array([h_max,sat_max,v_max])
    

    _,img=cap.read()
    cv2.imshow('Cam',img)
    hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    #cv2.imshow('HSV_window',hsv_img)
    
    
    mask = cv2.inRange(hsv_img,lower,upper)
    result = cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow('Color_filter',result)
    cv2.imshow('Mask',mask)
    print(mask)
    cv2.waitKey(1)