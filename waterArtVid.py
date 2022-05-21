import cv2
import numpy as np

cap=cv2.VideoCapture(0)
while(cap.isOpened()):
    ret, frame=cap.read()
    org_img=frame
    img=cv2.resize(org_img,None,fx=1,fy=1)

    for i in range(3):
        img=cv2.medianBlur(img,3)

    img=cv2.edgePreservingFilter(img,sigma_s=6)

    img=cv2.bilateralFilter(img,3,10,5)
    for i in range(2):
        img=cv2.bilateralFilter(img,3,20,10)
    for i in range(3):
        img=cv2.bilateralFilter(img,3,30,10)

    img_gaussian=cv2.GaussianBlur(img,(7,7),2)
    img_sharp=cv2.addWeighted(img,1.5,img_gaussian,-0.5,0)
    img_final=cv2.addWeighted(img,1.4,img_gaussian,-0.2,10)

    cv2.imshow('Original Image',org_img)
    cv2.imshow("Final Image",img_final)
    
    if cv2.waitKey(1)  ==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()