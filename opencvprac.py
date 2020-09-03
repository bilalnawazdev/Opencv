#import Opencv
import cv2  
  
# import numpy 
import numpy as np  
  
# capture frames from a camera   
cap = cv2.VideoCapture(0)  

while (1):  
  
    # reads frames from a camera   
    Frame = cap.read() 
    
    #Displaying Frame in a window
    cv2.imshow('Original', Frame) 
    
    # Press Esc key to break the while loop
    Break_key = cv2.waitKey(5) & 0xFF  
    if Break_key == 27:  
        break  

#Close the window   
cap.release()  
  
# De-allocate any associated memory usage   
cv2.destroyAllWindows()  
