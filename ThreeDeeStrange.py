import pygame
import numpy as np
import Point3D

# Initialize Pygame
pygame.init()
# Set up the display
screen = pygame.display.set_mode((800, 600))
# Set the title of the window
pygame.display.set_caption("Strange")
# Set the clock for controlling the frame rate
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

points = []
# Create a list of 3D points forming a ball
# The idea is: points form the surface of a sphere
theta = np.linspace(0, 2 * np.pi, 50)
for p in range(100):
    for t in theta:
        y = 2 * np.cos(t)
        x = 2 * np.sin(t) * np.cos((np.pi/180.0) * p * 0.2)
        z = 2 * np.sin(t) * np.sin((np.pi/180.0) * p * 0.2)
        
        # Create a Point3D object and add it to the list
        points.append(Point3D.Point3D(x, y, z))
        
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
        
        # color is gray shaded based on z value, white when z is closest to camera
        color_value = int(255 * (1 - (pz + 2) / 4))
        color = (color_value, color_value, color_value)
        
        x_proj, y_proj = point.project()
        pygame.draw.circle(screen, color, (x_proj, y_proj), 2)

        # Update points, so that they go around the y-axis
        point.x = point.x * np.cos(0.0125) - point.z * np.sin(0.0125)
        point.z = point.x * np.sin(0.0125) + point.z * np.cos(0.0125)
        
    # Update the display
    pygame.display.flip()
    # Control the frame rate
    clock.tick(60)