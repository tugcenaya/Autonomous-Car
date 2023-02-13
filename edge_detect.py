import cv2
import numpy as np
from imutils.video import VideoStream
import math
import time

import motors as mot

vs = VideoStream(usePiCamera=1 > 0).start()
time.sleep(2.0)

def lane_detect(image):
    
    threshold1 = 90
    threshold2 = 90
    theta=0
    
    minLineLength = 15
    maxLineGap = 5
    
    k_width = 3
    k_height = 3
    max_slider = 10
    # Convert the image to gray-scale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (k_width, k_height), 0)
    # Find the edges in the image using canny detector
    edged = cv2.Canny(blurred, threshold1, threshold2)
    # Detect points that form a line
    lines = cv2.HoughLinesP(edged,1,np.pi/180,max_slider,minLineLength,maxLineGap)
    #if lines in not None:
        #print(lines[0])
    for x in range(0, len(lines)):
        for x1,y1,x2,y2 in lines[x]:
            cv2.line(image,(x1,y1),(x2,y2),(255,0,0),3)
            theta=theta+math.atan2((y2-y1),(x2-x1))
            #print(theta)
    cv2.imshow("Line Detection",image)
    #cv2.imshow("Gray Image",gray)
    #cv2.imshow("blurred",blurred)
    #cv2.imshow("Edged",edged)
    return theta

if __name__=="__main__":
       
    try:
        while True:
            r_width = 500
            r_height = 300
            frame = vs.read()
            frame = cv2.resize(frame,(r_width,r_height))
            try:
                theta = lane_detect(frame)
            except:
                continue
            speed = 70
            threshold = 10
            
            if(theta>threshold):
                mot.stop()
                mot.fleft(100, 0.2)
                mot.forward()
                mot.go(50, 0.3)
                print("Go left", theta)
                mot.stop()
            if(theta<-threshold):
                mot.stop()
                mot.fright(100, 0.2)
                mot.forward()
                mot.go(50, 0.3)
                print("Go right", theta)
                mot.stop()
            if(abs(theta)<threshold):
                mot.forward()
                mot.go(70, 0.3)
                print("Go straight", theta)
            
            key = cv2.waitKey(1) & 0xFF
            # if the `q` key was pressed, break from the loop
            if key == ord("q"):
                break
    finally:
        #vs.stream.stream.release()
        mot.stop()
        cv2.destroyAllWindows()
