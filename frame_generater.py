import cv2
import os
import numpy as np

vidcap = cv2.VideoCapture('/media/ashish/New Volume3/Technoutsav videos/Unsure/unsure_13.avi')
try:
    if not os.path.exists('Unsure'):
        os.makedirs('Unsure')
except OSError:
    print ('Error: Creating directory of data')

def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite("./Unsure/unsure_13_"+str(count)+".jpg", image)     # save frame as JPG file
    return hasFrames
sec = 0
frameRate = 0.5 #//it will capture image in each 0.5 second
count=1
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)

vidcap.release()
cv2.destroyAllWindows()