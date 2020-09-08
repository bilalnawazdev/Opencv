import cv2

image=cv2.imread(r'C:\Users\bilal\Pictures\Downloaded Wallpapers\lastofus_1.jpg')

gray_scale=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imshow('Gray scale Image',gray_scale)

cv2.waitKey()

cv2.destroyAllWindows()