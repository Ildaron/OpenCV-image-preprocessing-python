import cv2
from pyspin import PySpin
def acquire_and_display_images(cam, nodemap, nodemap_tldevice):
    node_acquisition_mode = PySpin.CEnumerationPtr(nodemap.GetNode('AcquisitionMode'))
    node_acquisition_mode_continuous = node_acquisition_mode.GetEntryByName('Continuous')
    acquisition_mode_continuous = node_acquisition_mode_continuous.GetValue()
    cam.BeginAcquisition()

    while(1):
            image_result = cam.GetNextImage(1000)                
            image_data = image_result.GetNDArray()
            cv2.imshow("img",image_data)
            cv2.waitKey(1)
            image_result.Release()
            break
    cam.EndAcquisition()
    return True     
def run_single_camera(cam):
        result = True
        nodemap_tldevice = cam.GetTLDeviceNodeMap()
        cam.Init()
        nodemap = cam.GetNodeMap()          # Retrieve GenICam nodemap
        result &= acquire_and_display_images(cam, nodemap, nodemap_tldevice) # Acquire images
def main():
    result = True
    system = PySpin.System.GetInstance()
    version = system.GetLibraryVersion()
    cam_list = system.GetCameras()
    num_cameras = cam_list.GetSize()
    for i, cam in enumerate(cam_list):
        result &= run_single_camera(cam)
main()
