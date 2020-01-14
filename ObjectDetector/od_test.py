from ObjectDetector import ObjectDetector
from rplidar import RPLidar
import time

obd = ObjectDetector(ObjectDetector.gen_segments(
    right = ObjectDetector.segment_range(30, 90),
    front = ObjectDetector.segment_range(-30, 30),
    left =  ObjectDetector.segment_range(-90, -30)
))

try:
    lidar = RPLidar('/dev/ttyUSB0')

    print('Initializing')
    time.sleep(5)
    print('Collecting data')
    
    for data in lidar.iter_measurments(max_buf_meas=800):
        if obd.update(data):
            print(obd.detect())
    
except KeyboardInterrupt:
    pass
    
lidar.stop()
lidar.stop_motor()
lidar.disconnect()