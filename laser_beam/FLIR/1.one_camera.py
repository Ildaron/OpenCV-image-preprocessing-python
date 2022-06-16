import cv2
from pyspin import PySpin
def acquire_and_display_images(cam):
    #cam.PixelFormat.SetValue(PySpin.PixelFormat_RGB8)
    cam.BeginAcquisition()
    while(1):
            image_result = cam.GetNextImage(1000)                
            image_data = image_result.GetNDArray()
            resize=25                    
            x = int(image_data.shape[1]*resize/100)
            y = int(image_data.shape[0]*resize/100) 
            image_data=img=cv2.resize(image_data,(x,y))
            #cv2.imwrite('C:/Users/ir2007/Desktop/HW/2.Camera/image3.jpg',image_data)     
            #break
            cv2.imshow("img",image_data)
            cv2.waitKey(1)
            image_result.Release()
    cam.EndAcquisition()
   
def run_single_camera(cam):
        result = True
       
        cam.Init()
        nodemap = cam.GetNodeMap()          # Retrieve GenICam nodemap
        acquire_and_display_images(cam) # Acquire images
def main():
    result = True
    system = PySpin.System.GetInstance()
    version = system.GetLibraryVersion()
    cam_list = system.GetCameras()
    num_cameras = cam_list.GetSize()
    for i, cam in enumerate(cam_list):
        run_single_camera(cam)
main()
