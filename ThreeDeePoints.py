import pygame
import numpy as np
import Point3D

# Initialize Pygame
pygame.init()
# Set up the display
screen = pygame.display.set_mode((800, 600))
# Set the title of the window
pygame.display.set_caption("Strange set of 3D points")
# Set the clock for controlling the frame rate
clock = pygame.time.Clock()
# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create a list of 3D points forming a ball
points = []

# form a box with 6 faces
for x in np.linspace(-1.5, 1.5, 10):
    for y in np.linspace(-1.5, 1.5, 10):
        for z in np.linspace(-2, 2, 10):
            # Create a Point3D object and add it to the list
            points.append(Point3D.Point3D(x, y, z))


# Main loop
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
        
        # color is is gray shaded based on z value, white, when z is closest to camera
        color_value = int(255 * (1 - (pz + 2) / 6))
        color = (color_value, color_value, color_value)
        
        x_proj, y_proj = point.project()
        pygame.draw.circle(screen, color, (x_proj, y_proj), 2)

        # update points, so that the go around the z-axis
        point.x = point.x * np.cos(0.0025) - point.y * np.sin(0.0025)
        point.y = point.x * np.sin(0.0025) + point.y * np.cos(0.0025)
        
    # Update the display
    pygame.display.flip()
    # Control the frame rate
    clock.tick(60)