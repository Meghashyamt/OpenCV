#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 16:22:47 2020

@author: shyam
"""

import cv2

#img=cv2.imread("obama.jpg")

#cv2.imshow("obama",img)
#cv2.waitKey(1000)

framewidth= 640
frameheight =360

cap=cv2.VideoCapture(0)
cap.set(3,framewidth)
cap.set(4,frameheight)

while True:
    success,img=cap.read()
    cv2.imshow("video",img)
    
    if cv2.waitKey(1000) & 0xFF == ord('q'):
        break