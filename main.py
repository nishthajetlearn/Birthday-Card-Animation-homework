import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 600
HEIGHT = 600

# Set up display surface
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bulb Simulator")

# Load the images for the bulb (off and on states)
bulb_off = pygame.image.load("bulb_off.jpg")  # Replace with your own image file
bulb_on = pygame.image.load("bulb_on.jpg")    # Replace with your own image file

# Scale images to fit the screen (optional)
bulb_off = pygame.transform.scale(bulb_off, (WIDTH, HEIGHT))
bulb_on = pygame.transform.scale(bulb_on, (WIDTH, HEIGHT))

# Initially, the bulb is off
bulb_state = False

# Main loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for mouse click to toggle the bulb's state
        if event.type == pygame.MOUSEBUTTONDOWN:
            bulb_state = not bulb_state  # Toggle between on and off

    # Fill the display surface with a background color (optional)
    display_surface.fill((255, 255, 255))

    # Display the appropriate bulb image based on the current state
    if bulb_state:
        display_surface.blit(bulb_on, (0, 0))  # Show the bulb 'on'
    else:
        display_surface.blit(bulb_off, (0, 0))  # Show the bulb 'off'

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
