import cv2
from matplotlib import pyplot as plt


img = cv2.imread("katha.png")
box_img = cv2.boxFilter(img, -1, (5, 5),)
blur = cv2.GaussianBlur(img,(3,3),0)
median = cv2.medianBlur(img,5)#not correct
box_img_d = cv2.boxFilter(img, -1, (9, 9),)
blur_d = cv2.GaussianBlur(img,(5,5),0)
median_d = cv2.medianBlur(img,9)#not correct

f = plt.figure()
f.add_subplot(2,4,1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), cmap=None)
plt.title('Raw image')
f.add_subplot(2,4,2)
plt.imshow(cv2.cvtColor(box_img, cv2.COLOR_BGR2RGB), cmap=None)
plt.title('Box filter implementation (W = 5)')
f.add_subplot(2,4,3)
plt.imshow(cv2.cvtColor(blur, cv2.COLOR_BGR2RGB), cmap=None)
plt.title('Gaussian (\u03C3 = 3)')
f.add_subplot(2,4,4)
plt.imshow(cv2.cvtColor(median, cv2.COLOR_BGR2RGB), cmap=None)
plt.title('Median Filter (W = 5)')
f.add_subplot(2,4,5)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), cmap=None)
plt.title('Raw image')
f.add_subplot(2,4,6)
plt.imshow(cv2.cvtColor(box_img_d, cv2.COLOR_BGR2RGB), cmap=None)
plt.title('Enhanced Box Filter (W = 9)')
f.add_subplot(2,4,7)
plt.imshow(cv2.cvtColor(blur_d, cv2.COLOR_BGR2RGB), cmap=None)
plt.title('Enhanced Gaussian (\u03C3 = 5)')
f.add_subplot(2,4,8)
plt.imshow(cv2.cvtColor(median_d, cv2.COLOR_BGR2RGB), cmap=None)
plt.title('Enhanced Median Filter (W = 9)')
plt.show(block=True)
