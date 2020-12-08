#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 17:16:22 2020

@author: shyam
"""

import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)
print(img)

#img[:]=0,0,255
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),2)
cv2.rectangle(img,(350,100),(450,200),(0,0,255),cv2.FILLED)
cv2.circle(img,(150,400),50,(255,0,0),2)
cv2.putText(img,"Shapes",(75,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),3)

cv2.imshow("Image",img)


cv2.waitKey(10000)
cv2.destroyAllWindows()


