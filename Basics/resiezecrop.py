#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 16:54:19 2020

@author: shyam
"""

import cv2

path="obama.jpg"
img=cv2.imread(path)
print(img.shape)

width, height=1000,1000
imgresize=cv2.resize(img,(width,height))
print(imgresize)

imgcropped=img[80:250,150:250]

cv2.imshow("obama",img)
#cv2.imshow("obama resize",imgresize)
cv2.imshow("obamacropped",imgcropped)

cv2.waitKey(10000)

cv2.destroyAllWindows()