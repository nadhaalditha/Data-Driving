import os.path
import io as io

from flask import Flask, request, Response
import json

def check_os_platform(timeout, press):
    import platform
    return platform.system()
    face_cascade = cv2.CascadeClassifier(folder_path + 'face_detect_cascade.xml')

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for(x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0))
    
    new_image = 'static/%s.jpg' %uuid.uuid4().hex
    cv2.imwrite((folder_path + new_image), img)
    
    return json.dumps(new_image)

control_flow[x] = check_os_platform(0,0)
