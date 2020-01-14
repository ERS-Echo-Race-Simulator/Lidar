from rplidar import RPLidar
from sys import argv

lidar = RPLidar(argv[1])
lidar.stop()
lidar.stop_motor()
lidar.disconnect()