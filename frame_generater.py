import cv2
import os
import numpy as np

vidcap = cv2.VideoCapture('home/') # give the video directory
try:
    if not os.path.exists('file_name'): # create a file where the images get saved
        os.makedirs('file_name')
except OSError:
    print ('Error: Creating directory of data')

def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite("./file_name/frame"+str(count)+".jpg", image)     # save frame as JPG file
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
