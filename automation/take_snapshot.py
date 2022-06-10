import cv2

def take_snapshot():
    #initializing cv2
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        #read the frames while the camera is on
        ret,frame = videoCaptureObject.read()
        #cv2.inwrite() method is used to save an image to any storage device
        cv2.inwrite("NewPicture.jpg",frame)
        result = False

        #releases the camera
        videoCaptureObject.release()
        #closes all the windows that might be opened while this process
        cv2.destroyAllWindows()


        