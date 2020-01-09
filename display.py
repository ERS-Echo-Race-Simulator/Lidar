from rplidar import RPLidar
import pygame
import math
import time

def run():
    
    lidar = RPLidar('/dev/ttyUSB0')
    pygame.init()
    surface = pygame.display.set_mode((1000, 1000))
    surface.fill((0, 0, 0))
    
    try:
        print('Initializing')
        time.sleep(5)
        print('Recording data')
        for new, quality, theta, r in lidar.iter_measurments(max_buf_meas = 800):
            x = math.cos(theta) * r
            y = math.sin(theta) * r
            surface.set_at((int(x + 500), int(y + 500)), (255, 255, 255))
            if theta > 350 or theta < 15:
                pass
                surface.fill((0, 0, 0))
            pygame.display.update()
    except KeyboardInterrupt:
        print('Stopping')

    lidar.stop()
    lidar.stop_motor()
    lidar.disconnect()

if __name__ == "__main__":
    run()