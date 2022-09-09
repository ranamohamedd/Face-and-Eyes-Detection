import PySimpleGUI as sg
import os
from PIL import Image
import cv2
from predict import detect_eyes, detect_faces


layout = [
    [sg.Text('choose your image'),sg.Input(),sg.FileBrowse(key="-file-")],
     [sg.Button("Detect Faces") , sg.Button("Detect Eyes")],
     [sg.Image(key="-image-")]
 ]

window = sg.Window('Face Detection App',layout)

while True:
    event, values = window.read()
    if event in (None,'Exit'):
        break
        
    
    if event == 'Detect Faces':
        print(values)
        window["-image-"].update(detect_faces(values["-file-"]))
    if event == 'Detect Eyes':
        print(values)
        window["-image-"].update(detect_eyes(values["-file-"]))
    
    
        