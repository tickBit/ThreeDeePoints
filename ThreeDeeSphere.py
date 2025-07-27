import pygame
import numpy as np
import Point3D

# Initialize Pygame
pygame.init()
# Set up the display
screen = pygame.display.set_mode((800, 600))
# Set the title of the window
pygame.display.set_caption("3D Point Ball Simulation")
# Set the clock for controlling the frame rate
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

points = []
# Create a list of 3D points forming a ball
# The idea is: points form the surface of a sphere
theta = np.linspace(0, 2 * np.pi, 50)
for p in range(50):
    for t in theta:
        y = 2 * np.cos(t)
        x = 2 * np.sin(t) * np.cos(p * 0.1)
        z = 2 * np.sin(t) * np.sin(p * 0.1)
        
        # Create a Point3D object and add it to the list
        points.append(Point3D.Point3D(x, y, z))

angle = 0
# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Fill the screen with black
    screen.fill(BLACK)

    # Project and draw the points
    for point in points:
        pz = point.getZ()
        
        # update points around the y-axis
        # Now, the box won't shrink, because the original coordinates are not changed in the rotation;
        # only current coordinates are calculated based on the angle
        
        # Rotate the point around the y-axis
        zn = point.z * np.cos(angle) - point.x * np.sin(angle)
        xn = point.x * np.cos(angle) + point.z * np.sin(angle)
        
        # color is gray shaded based on z value, white when z is closest to camera
        color_value = int(255 * (1 - (pz + 2) / 4))
        color = (color_value, color_value, color_value)
        
        x_proj, y_proj = point.project_with_xn_yn_zn(xn, point.getY(), zn)
        pygame.draw.circle(screen, color, (x_proj, y_proj), 2)
    
    angle += 0.0025
    
    # Update the display
    pygame.display.flip()
    # Control the frame rate
    clock.tick(60)