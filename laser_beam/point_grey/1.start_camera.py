from pyspin import PySpin
import cv2
def acquire_and_display_images(cam):
        cam.PixelFormat.SetValue(PySpin.PixelFormat_RGB8)# for color    
        cam.BeginAcquisition()        
        while(True):
         image_result = cam.GetNextImage(1000)              
         image_data = image_result.GetNDArray()#
         resize=50                    
         x = int(image_data.shape[1]*resize/100)
         y = int(image_data.shape[0]*resize/100) 
         image_data=img=cv2.resize(image_data,(x,y))
         cv2.imwrite('C:/Users/Desktop/camera/Aperture/image2.jpg',image_data)
         break
         #image_data = cv2.cvtColor(image_data, cv2.COLOR_BGR2HSV)
         cv2.imshow("img",image_data)
         cv2.waitKey(1)                    
        cam.EndAcquisition()
def run_single_camera(cam):
        result = True
        cam.Init()                                                           # Initialize camera
        nodemap = cam.GetNodeMap()                                           # Retrieve GenICam nodemap
        result &= acquire_and_display_images(cam) # Acquire images       
def main():
    result =   True
    system =   PySpin.System.GetInstance()     # Retrieve singleton reference to system object
    cam_list = system.GetCameras()
    num_cameras = cam_list.GetSize()
    for i, cam in enumerate(cam_list):       # Run example on each camera
        result &= run_single_camera(cam)
    return result
main()
