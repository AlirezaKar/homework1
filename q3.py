import cv2 as cv

path = 'image.jpg'

image = cv.imread(path, cv.IMREAD_COLOR)
window_name = 'Image with text'
font = cv.FONT_HERSHEY_SIMPLEX
org = (48, 120)
fontScale = 1
color = (0, 0, 255)
thickness = 2
image = cv.putText(image, 'OpenCV', org, font, fontScale, color, thickness, cv.LINE_AA)
cv.imshow(window_name, image) 
cv.waitKey(0)