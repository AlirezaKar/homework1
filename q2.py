import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt       

### Black bar on a cat picture
image = cv.imread("image.jpg", cv.IMREAD_COLOR_BGR) 
start_point = (0, 50)
end_point = (50, 0)
color = (0, 0, 0)
thickness = 7

img = cv.line(image, start_point, end_point, color, thickness)
cv.imshow("Image with a line", img)
cv.waitKey(0)

### White bar on a black screen (using numpy)

# (512, 512) == (x, y) of the screen
Img = np.zeros((512, 512, 3), dtype='uint8')
start_point = (100, 100)
end_point = (450, 450)
color = (255, 250, 255)
image = cv.line(Img, start_point, end_point, color, thickness)
cv.imshow('Drawing_Line', image)
cv.waitKey(0)

### A rectangle on a cat picture
image = cv.imread("image.jpg", cv.IMREAD_COLOR_BGR)
start_point = (10, 10)
end_point = (50, 50)
color = (255, 0, 0)
thickness = 6

# FIXME: how are both rectangles shown when I only have given one of them in "imshow" ?
img_with_rectangle = cv.rectangle(image, start_point, end_point, color, thickness)
img_with_rectangle = cv.rectangle(image, (10, 60),(50, 150) , (0, 255, 0), -1)  # -1 to fill in the rectangle
cv.imshow("Image with a rectangle", img_with_rectangle)
cv.waitKey(0)


### A circle on a cat picture
image = cv.imread("image.jpg", cv.IMREAD_COLOR_BGR)
center_coordinates = (35, 50)
radius = 20
color = (128,0,128)
thickness = 5

img_with_circle = cv.circle(image, center_coordinates, radius, color, thickness)
img_with_circle2 = cv.circle(image, (60, 180), 20,(0, 255, 0), -1)
cv.imshow("Image with a Circle", img_with_circle)
cv.waitKey(0)


### All together 

img = cv.imread("image.jpg", cv.IMREAD_COLOR_BGR)
rectangle = cv.rectangle(img, (10, 40), (50, 70), (0, 255, 0), 6)
circle = cv.circle(img, (100, 80), 30, (255, 0, 0), -1)
line = cv.line(img, (30, 90), (10, 100), (0, 0, 255), 5)
cv.imshow("All", rectangle)
cv.waitKey(0)