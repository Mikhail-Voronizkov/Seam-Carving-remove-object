# Write Python code here 
# import the necessary packages 
import cv2 
import argparse 
  
# now let's initialize the list of reference point 
ref_point = [] 
  
def shape_selection(event, x, y, flags, param): 
    # grab references to the global variables 
    global ref_point
  
    # if the left mouse button was clicked, record the starting 
    # (x, y) coordinates and indicate that cropping is being performed 
    if event == cv2.EVENT_LBUTTONDOWN: 
        #ref_point = [(x, y)]
        ref_point.append((x, y)) 
        print('Point = ',ref_point)

  
    # check to see if the left mouse button was released 
    elif event == cv2.EVENT_LBUTTONUP: 
        # record the ending (x, y) coordinates and indicate that 
        # the cropping operation is finished 
        ref_point.append((x, y)) 
  
        # draw a rectangle around the region of interest 
        cv2.rectangle(param[0], ref_point[0], ref_point[1], (0, 255, 0), 2) 
        cv2.imshow("Draw zone to remove", param[0]) 

  

def user_select_object(Img):
    clone = Img.copy() 
    cv2.imshow('Draw zone to remove',clone)
    #cv2.namedWindow("Draw zone to remove") 
    param = [clone]
    cv2.setMouseCallback("Draw zone to remove", shape_selection,param) 
  
  
    # keep looping until the 'q' key is pressed 
    while True: 
        # display the Img and wait for a keypress 
        cv2.imshow("Draw zone to remove", clone) 
        key = cv2.waitKey(1) & 0xFF
  
        # if the 'c' key is pressed, break from the loop 
        if key == ord("c"): 
            break
  
    # close all open windows 
    cv2.destroyAllWindows()
    return ref_point


def fill_area(edgeImg,top,bottom,left,right):
    row,col = edgeImg.shape
    value = - 255 * 3 * row
    edgeImg[top:bottom, left:right] = value
    return edgeImg


# load the Img, clone it, and setup the mouse callback function 
#Img = cv2.imread('pic3.jpg')
#rec = user_select_object(Img)




