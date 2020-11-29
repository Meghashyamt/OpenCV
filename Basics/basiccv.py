#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 08:07:49 2020

@author: Meghashyam Thiruveedula
"""

import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)
print(kernel)

path ="obama.jpg"
img= cv2.imread(path)
imggrey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgblur=cv2.GaussianBlur(imggrey,(7,7),0)
imgCanny=cv2.Canny(imgblur,100,200)
imgdilation=cv2.dilate(imgCanny,kernel,iterations=1)
imgeroded=cv2.erode(imgdilation,kernel,iterations=1)

cv2.imshow("obama",img)
cv2.imshow("obamagrey",imggrey)
cv2.imshow("blur",imgblur)
cv2.imshow("canny",imgCanny)
cv2.imshow("dilate",imgdilation)
cv2.imshow("erode",imgeroded)

cv2.waitKey(10000)

cv2.destroyAllWindows()