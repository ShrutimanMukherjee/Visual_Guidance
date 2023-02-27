import numpy as np
import cv2
# import database api such as psycopgl
# import Rpi0 odules for picam

##### pins n globals ######
#set pin mode to gpio
#Rpi0 GPIO pins for camera
#image_queue

##### Functions ###########
def rpi_pinsetup():
    pass

def cam_capture():
    pass
    #return image (numpy matrix)

def img2blob(img)
    pass
    #return blob_string

def blob2img(blob)
    pass
    #return blob_string

def db_setup():
    pass
    #return relevant database/connection object

def db_update(person_type , name, img_blob):
    pass
    '''
    if person_type == known:
        append img_blob to persons img_list {maybe space separated string}
    elif person_type == unknown:
        create new entry for the person with the singleton list of the blob
    else:
        Incorrect type
    '''

def person_met():
    pass
    '''
    global image_queue
    
    use face detection [not recognition] library
    decide if a person has been met based on queue of images
    return True/False
    '''

def recognize(img):
    pass
    '''
    ```recognition algo -- improvise on library```
    
    return name if recognized else 'Cannot Find'    
    '''

if __name__ == 'main':
    pass
    '''
    image = np.zeros(5,5)
    while True:
        image = cam_capture()
        append image to image_queue
        
        if person_met():
            break
    
    person_name = recognize(image)
    if person=='Cannot Find':
        person_status = {known / new} input() {speech to text input}
        person_name = input() {speech to text input}
        db_update(person_type , person_name, img2blob(image))
    else:
        speech('Hello'+person_name)
    '''
