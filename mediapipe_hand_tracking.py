import mediapipe as mp 
import cv2
import numpy as np 

cap=cv2.VideoCapture(0)

black_background=np.zeros((512,512,3),np.uint8)

ha=mp.solutions.hands
hands=ha.Hands()

hd=mp.solutions.drawing_utils


while True:
    _,frame=cap.read()
    frame=cv2.flip(frame, 1)
    frame_c=frame.copy()
    ret,t=cv2.threshold(frame_c, 50, 200, cv2.THRESH_BINARY_INV)
    rgb=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    r=hands.process(rgb)
    #print(r.multi_hand_landmarks)

    if r.multi_hand_landmarks:
        for hl in r.multi_hand_landmarks:
            #hd.draw_landmarks(frame, hl,ha.HAND_CONNECTIONS)
            hd.draw_landmarks(black_background, hl,ha.HAND_CONNECTIONS)



    #cv2.imshow('hands',frame)
    #cv2.imshow('hands',t)
    cv2.imshow('Hand Tracking',black_background)
    black_background=np.zeros((512,512,3),np.uint8)

    if cv2.waitKey(1) & 0xFF==27:
        break

cap.release()
cv2.destroyAllWindows()