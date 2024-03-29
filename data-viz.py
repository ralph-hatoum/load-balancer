import pygame
import random
import matplotlib.pyplot as plt
# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SQUARE_SIZE = 200
UPDATE_INTERVAL = 1  # in milliseconds

VIZ = False

# Create a screen
if VIZ:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Data Visualization")

# Function to generate initial values
def generate_initial_values():
    return [[0 for _ in range(SCREEN_HEIGHT // SQUARE_SIZE)] for _ in range(SCREEN_WIDTH // SQUARE_SIZE)]

# Function to randomly select and update two squares
def elect_on_2_random(values, workload):
    height, width = len(values), len(values[0])
    x1, y1 = random.randint(0, height-1), random.randint(0, width-1)
    x2, y2 = random.randint(0, height-1), random.randint(0, width-1)
    if values[x1][y1] < values[x2][y2]:
        values[x1][y1] += workload
    else:
        values[x2][y2] += workload

def elect_random(values, workload):
    height, width = len(values), len(values[0])
    x, y = random.randint(0, height-1), random.randint(0, width-1)
    values[x][y] += workload

def find_min(values):
    values = list(map(min,values))
    return min(values)

def find_max(values):
    values = list(map(max,values))
    return max(values)

def compute_max_diff(values):
    minimum = find_min(values)
    maximum = find_max(values)
    return maximum-minimum

# Data structure to store current values
current_values = generate_initial_values()

# Main loop
if VIZ :
    running = True
    clock = pygame.time.Clock()

iteration = 0
TIME=[]
MAX_DIFF=[]
while iteration<100000:
    if VIZ:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    # Clear the screen
    
        screen.fill((0, 0, 0))
    # print("before :",current_values)
    workload = random.randint(0,24)
    elect_random(current_values, workload)
    # elect_random(current_values, workload)
    # print(current_values)
    # Update and draw squares

    if VIZ:

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
    TIME.append(iteration)
    MAX_DIFF.append(compute_max_diff(current_values))
    current_values = [list(map(lambda x : x-1 if x > 0 else x, sublist)) for sublist in current_values]
    iteration+=1

current_values = generate_initial_values()
iteration = 0
TIME2=[]
MAX_DIFF2=[]
if VIZ:
    clock = pygame.time.Clock()
while iteration<100000:
    if VIZ:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    # Clear the screen
        screen.fill((0, 0, 0))
    # print("before :",current_values)
    workload = random.randint(0,24)
    elect_on_2_random(current_values, workload)
    # elect_random(current_values, workload)
    # print(current_values)
    # Update and draw squares
    if VIZ:
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
    if VIZ:
        clock.tick(1000 // UPDATE_INTERVAL)
    TIME2.append(iteration)
    MAX_DIFF2.append(compute_max_diff(current_values))
    current_values = [list(map(lambda x : x-1 if x > 0 else x, sublist)) for sublist in current_values]
    iteration+=1


pygame.quit()

plt.plot(TIME,MAX_DIFF,"r")
plt.plot(TIME, MAX_DIFF2,color='blue')
plt.xlabel("Number of epochs")
plt.ylabel("Workload difference (arbitrary unit)")
plt.title("Largest workload difference between two machines")
plt.savefig("./graphs/graph.png")
plt.show()
