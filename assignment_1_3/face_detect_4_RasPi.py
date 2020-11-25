#created using a mix of tutorials from www.pyimagesearch.com

from imutils import face_utils
import dlib # dlib library
import cv2 #openCV library
from imutils.video import VideoStream
import imutils # basic image procesing library
import time


detector = dlib.get_frontal_face_detector() #frontal face detecrtor 

print("->Starting Face Detection")
c = VideoStream(usePiCamera=True).start() #video feed

#camera warm up
time.sleep(0.5)

while True:

    frame = c.read()
    #frame size
    frame = imutils.resize(frame, width=720)
    #mirror frame 
    frame = cv2.flip(frame, 1)
    #convert to greyscale for detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    rects = detector(gray, 0)

#create rectangle
    for rect in rects:
        x1 = rect.left()
        y1 = rect.top()
        x2 = rect.right()
        y2 = rect.bottom()
        frame = cv2.rectangle(frame, (x1,y1), (x2,y2), (0, 255, 0), 2)
# show the frame
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    
# quit when pressing q
    if key == ord("q"):
        break

cv2.destroyAllWindows()
c.stop()
