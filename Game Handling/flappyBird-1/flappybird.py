import pygame
import random

pygame.init()
screen = pygame.display.set_mode([288,512])

background = pygame.image.load("assets/background.png")
pygame.display.set_caption("Flappy Bird")

keep_going = True
clock = pygame.time.Clock()

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.birdSprite = pygame.image.load("assets/0.png")
        self.birdX = 50
        self.birdY = 100
        self.JumpSpeed = 7
        self.gravity = 0.4
    def birdUpdate(self):
        self.JumpSpeed -=self.gravity
        self.birdY -=self.JumpSpeed
        
newBird = Bird()    

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
        if (event.type == pygame.MOUSEBUTTONDOWN):
            newBird.JumpSpeed = 7
            
    screen.blit(background,(0,0))
    screen.blit(newBird.birdSprite,(newBird.birdX,newBird.birdY))
    
    newBird.birdUpdate()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
