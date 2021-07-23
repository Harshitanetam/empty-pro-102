import cv2

def take_snapshot():
    #initailizing cv2
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        #read the frames while the camera is on
        ret,frame = videoCaptureObject.read()
        #cv2.imwrite() method is used to save an image to an
        cv2.imwrite("NewPicture1.jpg",frame)
        result = False

        #releases the camera
        videoCaptureObject.releases()
        #clooses all the window that might be opened while this
        cv2.destroyAllWindows()

        take_snapshot()