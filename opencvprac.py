import cv2  
  
# import Numpy by alias name np  
import numpy as np  
  
# capture frames from a camera   
cap = cv2.VideoCapture(0)  

while (1):  
  
    # reads frames from a camera   
    ret, frame = cap.read() 


    #e=cv2.Canny(frame,100,200)

    cv2.imshow('Original', frame) 
    k = cv2.waitKey(5) & 0xFF  
    if k == 27:  
        break  

 #Close the window   
cap.release()  
  
# De-allocate any associated memory usage   
cv2.destroyAllWindows()  