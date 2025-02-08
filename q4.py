import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('image.jpg', cv.IMREAD_COLOR_RGB)
pixel = img[100, 100]
print("number of pixels: ", pixel)

dimensions = img.shape 
height = img.shape[0]  
width = img.shape[1]  
channels = img.shape[2]  
size1 = img.size  

# dimensions of the image == img.shape 
print('Image Dimension    : ',dimensions)  
print('Image Height       : ',height)  
print('Image Width        : ',width)  
print('Number of Channels : ',channels)  
print('Image Size  :', size1)  

## Splitting the image into its three channels (slow method)
# b,g,r = cv.split(img)  
# img = cv.merge((b,g,r))  

## Splitting the image into its three channels (fast method using numpy indexing)
b = img[:,:,0]  

BLUE = [255,0,0]  
replicate = cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_REPLICATE)  
reflect = cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_REFLECT)  
reflect101 = cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_REFLECT_101)  
wrap = cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_WRAP)  
constant= cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_CONSTANT,value=BLUE)  
plt.subplot(231),plt.imshow(img,'gray'),plt.title('ORIGINAL')  
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')  
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')  
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')  
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')  
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')  
plt.show()   

## BGR to Gray scale conversion
image = cv.cvtColor(img, cv.COLOR_BGR2GRAY )      
cv.imshow('Image', image)  
cv.waitKey(0)
cv.destroyAllWindows()  

## Image resizing
scale = 60  
width = int(img.shape[1] * scale / 100)  
height = int(img.shape[0] * scale / 100)  
dim = (width, height)  

resized = cv.resize(img, dim, interpolation=cv.INTER_AREA)  
print('Resized Dimensions : ', resized.shape)  
  
cv.imshow("Resized image", resized)  
cv.waitKey(0)  
cv.destroyAllWindows()  

# Downscale with resize()
print('Original Dimensions : ', img.shape)  

scale = 60  # percent of original size  
width = int(img.shape[1] * scale / 100)  
height = int(img.shape[0] * scale / 100)  
dim = (width, height)  

resized = cv.resize(img, dim, interpolation=cv.INTER_AREA)  
  
print('Resized Dimensions : ', resized.shape)  
  
cv.imshow("Resized image", resized)  
cv.waitKey(0)  
cv.destroyAllWindows()  

# Upscale with resize()
print('Original Dimensions : ', img.shape)  
  
scale = 150  # percent of original size  
width = int(img.shape[1] * scale / 100)  
height = int(img.shape[0] * scale / 100)  
dim = (width, height)  
# resize image  
resized = cv.resize(img, dim, interpolation=cv.INTER_AREA)  
  
print('Resized Dimensions : ', resized.shape)  
  
cv.imshow("Resized image", resized)  
cv.waitKey(0)  
cv.destroyAllWindows()  