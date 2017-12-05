import cv2

img=cv2.imread("./sample-images/galaxy.jpg",0)

print(type(img))
print(img)
# print number of pixels in array
print(img.shape)
# print number of dimensions
print(img.ndim)

cv2.imshow("Galaxy", img) #show image
cv2.waitKey(5000) # how long to show in milliseconds
cv2.destroyAllWindows()#close all windows
