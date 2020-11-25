Python_Emilio_2020
I initially wanted to combine blink detection on a Raspberry Pi with an Arduino to control a servo. Unfortunately, I found out this is well beyond my current coding skills, I ended up "just" coding a face tracking program.

The program starts by importing the following libraries:
dlib
opneCV
imutils

followed by turning on the camera 
create a frame
mirror the image 
convert the image to grayscale for open CV
after the face is detected, we create a green rectangle around it.

