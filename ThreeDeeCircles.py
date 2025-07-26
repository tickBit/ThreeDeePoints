import pygame
import numpy as np
import Point3D

# Initialize Pygame
pygame.init()
# Set up the display
screen = pygame.display.set_mode((800, 600))
# Set the title of the window
pygame.display.set_caption("Strange 3D point effect")
# Set the clock for controlling the frame rate
clock = pygame.time.Clock()
# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create a list of 3D points forming a ball
points = []

# z around y-axis
theta = np.linspace(0, 2 * np.pi, 100)
for y in np.linspace(-2, 2, 10):
    for t in theta:
        x = 2 * np.cos(t)
        z = 2 * np.sin(t)
    
                    
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

        # update points, so that the go around the y-axis
        point.x = point.x * np.cos(0.0025) - point.z * np.sin(0.0025)
        point.z = point.x * np.sin(0.0025) + point.z * np.cos(0.0025)
        
    # Update the display
    pygame.display.flip()
    # Control the frame rate
    clock.tick(60)