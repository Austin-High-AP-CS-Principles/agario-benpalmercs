import pygame
import sys
import random

class Food(pygame.sprite.Sprite):
    # Constructor
    def __init__(self, color):
        super(Food,self).__init__() #calling on the contructor for the Sprite class
        self.radius = 10
        self.image = pygame.Surface((self.radius*2,self.radius*2), pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        pygame.draw.circle(self.image, color, (self.radius, self.radius), self.radius,)
        self.rect = self.image.get_rect(center = (random.randint(10,790),random.randint(10,590)))
    





# Initialize Pygame and give access to all the methods in the package
pygame.init()

# Set up the screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Tutorial")

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0,0,0)
# Create clock to later control frame rate
clock = pygame.time.Clock()

meals = pygame.sprite.Group() # Group is a high powered list
for num in range(20):
    meals.add(Food("blue"))
# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get(): # pygame.event.get()
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (e.g., white)
    screen.fill(BLACK)

    # Paste all of the Food objects ont he screen.
    meals.draw(screen)
    # Update the display
    pygame.display.flip()

    # Set a frame rate to 60 frames per second
    clock.tick(60)

# Quit Pygame properly
pygame.quit()
sys.exit()
