import pygame
import random

pygame.init()
screen = pygame.display.set_mode([288,512])

background = pygame.image.load("assets/background.png")
pygame.display.set_caption("Flappy Bird")

bgm = pygame.mixer.Sound('sound/bgm.wav')
channel_1 = pygame.mixer.Channel(1)
channel_1.play(bgm)

keep_going = True
clock = pygame.time.Clock()

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.birdSprite = [pygame.image.load("assets/0.png"),pygame.image.load("assets/1.png"),pygame.image.load("assets/2.png")]
        self.a = 0   
        self.birdX = 50
        self.birdY = 100
        self.JumpSpeed = 7
        self.gravity = 0.4
    def birdUpdate(self):
        self.JumpSpeed -=self.gravity
        self.birdY -=self.JumpSpeed
        if self.JumpSpeed > 0:
            self.a =1
        if self.JumpSpeed < 0:
            self.a =2
class Wall():
    def __init__(self):
        self.wallUp = pygame.image.load("assets/top.png") 
        self.wallDown = pygame.image.load("assets/bottom.png")
        self.gap = 50
        self.wallx = 288
        self.offset = random.randint(-50,50)
    def wallUpdate(self):
        self.wallx -= 3
        if self.wallx < -80:
            self.wallx = 288
            self.offset = random.randint(-50,50)
    
newBird = Bird() 
newWall = Wall()

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
        if (event.type == pygame.MOUSEBUTTONDOWN):
            newBird.JumpSpeed = 7
            
            channel_2=pygame.Channel(2)
            fly = pygame.mixer.Sound('sound/fly.WAV')
            channel_2.play(fly)
            
    screen.blit(background,(0,0))
    screen.blit(newBird.birdSprite[newBird.a],(newBird.birdX,newBird.birdY))
    screen.blit(newWall.wallUp,(newWall.wallx, 360 + newWall.gap - newWall.offset))
    screen.blit(newWall.wallDown,(newWall.wallx, 0 + newWall.gap - newWall.offset))
    newWall.wallUpdate()
    newBird.birdUpdate()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
