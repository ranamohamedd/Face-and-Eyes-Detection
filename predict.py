import numpy as np
import cv2




face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

def detect_faces_steps (image):
    face_rect= face_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=3)
    for (x,y,w,h) in face_rect:
     cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,255,0),3)
    return image

def detect_faces(image):
    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_detected = detect_faces_steps(gray)
    cv2.imshow("Faces",face_detected)
    
    
    
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')

def detect_eyes_steps (image):
    eye_rect= eye_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=3)
    for (x,y,w,h) in eye_rect:
     cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,255,0),3)
    return image
    
def detect_eyes(image):
    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eyes_detected = detect_eyes_steps(gray)
    cv2.imshow("Eyes",eyes_detected)
    
    

    
