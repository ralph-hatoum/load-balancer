import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SQUARE_SIZE = 200
UPDATE_INTERVAL = 1  # in milliseconds

# Create a screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Data Visualization")

# Function to generate initial values
def generate_initial_values():
    return [[0 for _ in range(SCREEN_HEIGHT // SQUARE_SIZE)] for _ in range(SCREEN_WIDTH // SQUARE_SIZE)]

# Data structure to store current values
current_values = generate_initial_values()

# Main loop
running = True
clock = pygame.time.Clock()

# Function to randomly select and update two squares
def elect_on_2_random(values, workload):
    height, width = len(values), len(values[0])
    x1, y1 = random.randint(0, height-1), random.randint(0, width-1)
    x2, y2 = random.randint(0, height-1), random.randint(0, width-1)
    if values[x1][y1] < values[x2][y2]:
        values[x1][y1] += workload
    else:
        values[x2][y2] += workload

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))
    # print("before :",current_values)
    elect_on_2_random(current_values, 1)
    # print(current_values)
    # Update and draw squares
    for x in range(0, SCREEN_WIDTH, SQUARE_SIZE):
        for y in range(0, SCREEN_HEIGHT, SQUARE_SIZE):
            # Get current value
            value = current_values[x // SQUARE_SIZE][y // SQUARE_SIZE]
            if value!=0:
                # print(value)
                if value <=255:
                    color = (value, 255-value, 0)
                    print(color)
                pygame.draw.rect(screen, color, (x, y, SQUARE_SIZE, SQUARE_SIZE))
            # Calculate color based on value (green to red gradient)
            # color = (0, int(255 * (value / 100)), 0)
            # pygame.draw.rect(screen, color, (x, y, SQUARE_SIZE, SQUARE_SIZE))
            
                # Draw ID label
            font = pygame.font.Font(None, 20)
            text_surface = font.render(str(value), True, (0, 0, 0))
            screen.blit(text_surface, (x + 10, y + 10))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(1000 // UPDATE_INTERVAL)

pygame.quit()

