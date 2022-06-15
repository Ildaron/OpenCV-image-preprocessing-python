import cv2
from pyspin import PySpin
def acquire_and_display_images(cam, number):
    result = True
    nodemap_tldevice = cam.GetTLDeviceNodeMap()
    cam.Init()
    nodemap = cam.GetNodeMap()
    node_acquisition_mode = PySpin.CEnumerationPtr(nodemap.GetNode('AcquisitionMode'))
    node_acquisition_mode_continuous = node_acquisition_mode.GetEntryByName('Continuous')
    acquisition_mode_continuous = node_acquisition_mode_continuous.GetValue()
    node_acquisition_mode.SetIntValue(acquisition_mode_continuous)
    cam.BeginAcquisition()
    node_device_serial_number = PySpin.CStringPtr(nodemap_tldevice.GetNode('DeviceSerialNumber')) 
    image_result = cam.GetNextImage(1000)    
    image_data = image_result.GetNDArray()
    cv2.imshow(str(number),image_data)
    cv2.waitKey(1) 
    image_result.Release()  
    cam.EndAcquisition()
    return True

def main():
    result = True
    system = PySpin.System.GetInstance()
    version = system.GetLibraryVersion()
    cam_list = system.GetCameras()
    num_cameras = cam_list.GetSize() 
    while 1:
        acquire_and_display_images(cam_list[0],1)
        acquire_and_display_images(cam_list[1],2)
main()
