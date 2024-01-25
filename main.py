

import pygame
import sys
import random
import math



class Food(pygame.sprite.Sprite):
    # Constructor
    def __init__(self, color):
        super(Food,self).__init__() #calling on the contructor for the Sprite class
        self.radius = 5
        self.image = pygame.Surface((self.radius*2,self.radius*2), pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        pygame.draw.circle(self.image, color, (self.radius, self.radius), self.radius,)
        self.rect = self.image.get_rect(center = (random.randint(10,790),random.randint(10,590)))
    def relocate(self):
        self.rect = (random.randint(10,790),random.randint(10,790))
        
    

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy,self).__init__()
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.radius = random.randint(15,50)
        self.image = pygame.Surface((self.radius*2,self.radius*2), pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius,)
        self.rect = self.image.get_rect(center = (random.randint(10,790),random.randint(10,590)))
        self.speed = 80
        self.deltax = random.choice([-1,1])
        self.deltay = random.choice([-1,1])
        

    def move(self):
        if self.rect.left <= 0 or self.rect.right >= 800:
            self.deltax *= -1
        if self.rect.top <= 0 or self.rect.bottom >= 600:
            self.deltay *= -1
                    
        if self.radius<150:
            self.rect.centerx += self.deltax * self.speed * (1/self.radius)
            self.rect.centery += self.deltay * self.speed * (1/self.radius)
        if self.radius>=150:
            self.rect.centerx += self.deltax * self.speed * (1/150)
            self.rect.centery += self.deltay * self.speed * (1/150)

 

    def collisionDetector(self,other):
        if (math.dist(self.rect.center,other.rect.center) <= self.radius):
            return True
        else:
            return False
        

    def grow(self, growth):
        self.rect.inflate((growth/2),(growth/2))
        pos = self.rect.center
        self.radius += growth/2
        self.image = pygame.Surface((self.radius*2,self.radius*2), pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)
        self.rect.center = pos
        print(self.radius)
      


class Player(Enemy):
    def __init__(self):
        super().__init__()
        self.color=(255,255,255,255)
        self.radius = 25
        self.image = pygame.Surface((self.radius*2,self.radius*2), pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius,)
        self.rect = self.image.get_rect(center = (100,100))
        self.speed = 80


    def move(self):
        mx,my = pygame.mouse.get_pos()
        self.distx = (self.rect.centerx - mx)*-1
        self.disty = (self.rect.centery - my)*-1
        hyp = math.dist(self.rect.center,(mx,my))
        if hyp==0:
            hyp=0.0001
        self.deltax = self.distx/hyp
        self.deltay = self.disty/hyp
        if self.radius<150:
            self.rect.centerx += self.deltax * self.speed * (1/self.radius)
            self.rect.centery += self.deltay * self.speed * (1/self.radius)
        if self.radius>=150:
            self.rect.centerx += self.deltax * self.speed * (1/150)
            self.rect.centery += self.deltay * self.speed * (1/150)
        




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
    enemies.add(Enemy())

players = pygame.sprite.Group()
player = Player()
players.add(player)

objects = pygame.sprite.Group()
objects.add(enemies)
objects.add(meals)
objects.add(players)
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
                    if type(obj) == Enemy:
                        print("collision")
                        enemy.grow(obj.radius)
                        obj.kill()

    for player in players:
        player.move()
        for obj in objects:
            if player != obj:
                if player.collisionDetector(obj):
                    player.grow(obj.radius)
                    obj.kill()
    players.draw(screen)
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























