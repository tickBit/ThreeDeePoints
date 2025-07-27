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
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# red point's x, y, z
redPoint = Point3D.Point3D(0, 0, 0)

# red point's bouncing values
bounching_value = 0
bouncinng_angle = 0

# Create a list of 3D points forming a ball
points = []

# form a box with 6 faces
for x in np.linspace(-1.0, 1.0, 10):
    for y in np.linspace(-1.0, 1.0, 10):
        
        z = -1.0
        points.append(Point3D.Point3D(x, y, z))
        
        z = 1.0
        points.append(Point3D.Point3D(x, y, z))
        
for z in np.linspace(-1.0, 1.0, 10):
    for x in np.linspace(-1.0, 1.0, 10):
        
        y = -1.0
        points.append(Point3D.Point3D(x, y, z))

        y = 1.0
        points.append(Point3D.Point3D(x, y, z))
        
for z in np.linspace(-1.0, 1.0, 10):
    for y in np.linspace(-1.0, 1.0, 10):
        
        x = -1.0
        points.append(Point3D.Point3D(x, y, z))

        x = 1.0
        points.append(Point3D.Point3D(x, y, z))

angle = 0
# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Fill the screen with black
    screen.fill(BLACK)

    # sort points by z value to improve rendering order
    points.sort(key=lambda point: point.getZ(), reverse=True)
    
    # Project and draw the points
    for point in points:
        
        pz = point.getZ()
        
        # Now, the box won't shrink, because the original coordinates are not changed in the rotation;
        # only current coordinates are calculated based on the angle
        
        # Rotate the point around the y-axis
        zn = point.z * np.cos(angle) - point.x * np.sin(angle)
        xn = point.x * np.cos(angle) + point.z * np.sin(angle)
        
        # color is is gray shaded based on z value, white, when z is closest to camera
        color_value = int(255 * (1 - (pz + 2) / 4))
        if color_value < 80:
            color_value = 80
        elif color_value > 255:
            color_value = 255
            
        color = (color_value, color_value, color_value)
        
        if redPoint.getZ() < pz:
            # draw the red point first
            rx_proj, ry_proj = redPoint.project()
            ry_proj += bounching_value
            pygame.draw.circle(screen, RED, (rx_proj, ry_proj), 6)
            
            x_proj, y_proj = point.project_with_xn_yn_zn(xn, point.getY(), zn)
            pygame.draw.circle(screen, color, (x_proj, y_proj), 3)
            
        else:
            x_proj, y_proj = point.project_with_xn_yn_zn(xn, point.getY(), zn)
            pygame.draw.circle(screen, color, (x_proj, y_proj), 3)
        
            rx_proj, ry_proj = redPoint.project()
            ry_proj += bounching_value
            pygame.draw.circle(screen, RED, (rx_proj, ry_proj), 6)
        
    
    angle += np.pi/180.0
                       
    bouncinng_angle += 0.05
    if bouncinng_angle > 2 * np.pi:
        bouncinng_angle = 0
    bounching_value = int(50 * np.sin(bouncinng_angle))
            
    # Update the display
    pygame.display.flip()
    # Control the frame rate
    clock.tick(60)