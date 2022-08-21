#!python3
# import the necessary packages
from resources.shape_classifier import Detector
import numpy as np
import imutils
import cv2
import serial



# create shape detector opject 
sd = Detector()
# Starting the webcam
vs = cv2.VideoCapture(0)


#(hMin = 0 , sMin = 0, vMin = 255), (hMax = 179 , sMax = 255, vMax = 255)
#(hMin = 0 , sMin = 0, vMin = 186), (hMax = 179 , sMax = 132, vMax = 255)

while True:
    ret, frame = vs.read()
    # Points counter 
    counter = 0    
    # falg 
    done = False
    # main loop 
    # load the image and resize it to a smaller factor so that
    image = imutils.resize(frame, width=720)
    # resize the images 
    resized = imutils.resize(image, width=480)
    hsv = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)
    # for green color 
    lower = np.array([48 , 79, 0], np.uint8)
    upper = np.array([83 , 255, 255], np.uint8)
    

    mask = cv2.inRange(hsv, lower, upper)
    # reduce the resoluation 
    ratio = image.shape[0] / float(resized.shape[0])
    # convert the resized image to grayscale, blur it slightly,
    #gray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(mask, (5, 5),200)
    # and threshold it
    thresh = cv2.threshold(blurred, 20, 255, cv2.THRESH_BINARY)[1]
    # find contours in the thresholded image and initialize the
    
    
    # shape detector
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    # loop over the contours
    for c in cnts:
        # compute the center of the contour, then detect the name of the
        # shape using only the contour
        try : 
            if cv2.contourArea(c)  < 4000 : continue
            shape = sd.detect(c)
            if shape != "rectangle": continue
            #if shape not in ["square","rectangle"] : continue
            M = cv2.moments(c) 
            cX = int((M["m10"] / M["m00"]) * ratio)
            cY = int((M["m01"] / M["m00"]) * ratio)
            #print(shape,cX,cY)
            # multiply the contour (x, y)-coordinates by the resize ratio,
            # then draw the contours and the name of the shape on the image
            c = c.astype("float")
            c *= ratio
            c = c.astype("int")
            # draw contours around the detected shapes 
            cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
            # draw circle at the center of the shape 
            cv2.circle(image,(cX, cY),1,( 255,0 , 0),10)
            # write the co-ordinates 
            cv2.putText(image, "Detected", (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,0.7, ( 0 , 0 , 255), 2)
            
            # Sending the points to arduino 
            if arduino != None and not  done:
                    # Increase the counter 
                    counter += 1
                    # Sent the points to arduino
                    data = '{},{}'.format(cX,cY)
                    arduino.write(data.encode())
                    # Print 
                    print("Point No. {} sent".format(counter))
        except : pass
    done = True
    # show the output image
    cv2.imshow("MASK", mask)
    cv2.imshow("Image", image)
    cv2.imshow("Thresh", thresh)
    # wait key from keyboard

    cv2.waitKey(1)
    # if the `q` key is pressed, break from the lop
    #if key == ord("q"):
    #	break
    #if video == False: break
    # cleanup the camera and close any open windows
cv2.destroyAllWindows()

'''



while True:
    ret, image = fram_1.read()
    cv2.imshow("F0",image)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    #green color mask = (48 , 79, 0), (83 , 255, 255)
    green_lower = np.array([48 , 79, 0])
    green_upper = np.array([83 , 255, 255])
    #red color mask = (0 ,137,149), (11,255,255)
    red_lower = np.array([0 ,137,149])
    red_upper = np.array([11,255,255])
    
    mask_green = cv2.inRange(hsv,green_lower,green_upper)
    mask_red   = cv2.inRange(hsv,red_lower,red_upper)
    
    green_result = cv2.bitwise_and(image,image, mask= mask_green)
    red_result = cv2.bitwise_and(image,image, mask= mask_red)
    cv2.imshow("green",green_result)
    cv2.imshow("red",red_result)
    if cv2.waitKey(1) == ord('q'):
        break

'''


# Code to send data from python to arduino and recive feedback
'''
# Importing Libraries
import serial
import time
arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)


def write_read(cmd):
    arduino.write(bytes(cmd, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data
while True:
    cmd = input("Enter a command: ") # Taking input from user
    value = write_read(cmd)
    print(value) # printing the value
'''
