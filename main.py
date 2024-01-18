

import pygame
import sys
import random
import math

class Food(pygame.sprite.Sprite):
    # Constructor
    def __init__(self, color):
        super(Food,self).__init__() #calling on the contructor for the Sprite class
        self.radius = 10
        self.image = pygame.Surface((self.radius*2,self.radius*2), pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        pygame.draw.circle(self.image, color, (self.radius, self.radius), self.radius,)
        self.rect = self.image.get_rect(center = (random.randint(10,790),random.randint(10,590)))
    

class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(Enemy,self).__init__()
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.radius = random.randint(30,120)
  
        self.image = pygame.Surface((self.radius*2,self.radius*2), pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius,)
        self.rect = self.image.get_rect(center = (random.randint(10,790),random.randint(10,590)))
        self.rect = self.image.get_rect(center = (x,y))
        self.deltax = random.choice([-2,-1,1,2])
        self.deltay = random.choice([-2,-1,1,2])

    def move(self):
        if self.rect.left <= 0 or self.rect.right >= 800:
            self.deltax *= -1
        if self.rect.top <= 0 or self.rect.bottom >= 600:
            self.deltay *= -1
                    

        self.rect.centerx += self.deltax
        self.rect.centery += self.deltay

 

    def collisionDetector(self,other):
        if (math.dist(self.rect.center,other.rect.center) <= self.radius):
            return True
        else:
            return False
        

    def grow(self, growth):
        self.radius += growth/2
        self.image = pygame.Surface((self.radius*2,self.radius*2), pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)







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
BLACK = (0, 0, 0)
# Create clock to later control frame rate
clock = pygame.time.Clock()

meals = pygame.sprite.Group() # Group is a high powered list
for num in range(20):
    meals.add(Food("blue"))


enemies = pygame.sprite.Group()
for num in range(5):
    enemies.add(Enemy(random.randint(0,800),random.randint(0,600)))


objects = pygame.sprite.Group()
objects.add(enemies)
objects.add(meals)

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get(): # pygame.event.get()
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (e.g., white)
    screen.fill(BLACK)

    for enemy in enemies:
        enemy.move()
        for obj in objects:
            if enemy != obj:
              if enemy.collisionDetector(obj):
                print("collision")
                enemy.grow(obj.radius)
                obj.kill()


  
    enemies.draw(screen)
    # Paste all of the Food objects ont he screen.
    meals.draw(screen)
    # Update the display
    pygame.display.flip()

    # Set a frame rate to 60 frames per second
    clock.tick(60)

# Quit Pygame properly
pygame.quit()
sys.exit()
















