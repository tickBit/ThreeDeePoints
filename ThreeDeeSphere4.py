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

radius = [] 
# Create a list of 3D points forming a ball
# The idea is: points form the surface of a sphere with constant radius
theta = np.linspace(0, 2 * np.pi, 90)
for p in range(32):
    for t in theta:
        y = 2 * np.cos(t)
        x = 2 * np.sin(t) * np.cos(p * 0.1)
        z = 2 * np.sin(t) * np.sin(p * 0.1)
        
        # Create a Point3D object and add it to the list
        points.append(Point3D.Point3D(x, y, z))

bounching_angle = 0
bounching_angle_y = 0

angle = 0
# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Fill the screen with black
    screen.fill(BLACK)

    # sort points by z value to improve rendering order
    points.sort(key=lambda point: point.getZ(), reverse=True)
    
    bounching_value_x = int(150 * np.cos(bounching_angle))
    bounching_value_y = int(150 * np.sin(bounching_angle_y * 1.34))
    
    # Project and draw the points
    for p, point in enumerate(points):
        pz = point.getZ()
        
        # color is gray shaded based on z value, white when z is closest to camera
        color_value = int(255 * (1 - (pz + 2) / 4))
    
        color = (color_value, color_value, color_value)
    
        # Go around the y-axis
        xn = point.x * np.cos(angle) - point.z * np.sin(angle)
        zn = point.x * np.sin(angle) + point.z * np.cos(angle)
            
        x_proj, y_proj = point.project_with_xn_yn_zn(xn, point.getY(), zn)
        
        x_proj += bounching_value_x
        y_proj += bounching_value_y
        pygame.draw.circle(screen, color, (x_proj, y_proj), 1)

    angle += 0.01
        
    bounching_angle += 0.05
    if bounching_angle > 2 * np.pi:
        bounching_angle = 0
    
    bounching_angle_y += 0.01
    if bounching_angle_y * 1.34 > 2 * np.pi:
        bounching_angle_y = 0
        
    # Update the display
    pygame.display.flip()
    # Control the frame rate
    clock.tick(60)