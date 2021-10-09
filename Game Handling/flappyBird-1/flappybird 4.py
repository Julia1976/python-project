import pygame
import random
import sys

pygame.init()
screen = pygame.display.set_mode([288,512])
background = pygame.image.load("assets/background.png")
pygame.display.set_caption("Flappy Bird")


bgm = pygame.mixer.Sound('sound/bgm.wav')
channel_1 = pygame.mixer.Channel(1)
channel_1.play(bgm)

keep_going = True
clock = pygame.time.Clock()

score = 0
class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.birdSprite = [pygame.image.load("assets/0.png"),pygame.image.load("assets/1.png"),pygame.image.load("assets/2.png")]
        self.a = 0   
        self.birdX = 50
        self.birdY = 100
        self.JumpSpeed = 7
        self.gravity = 0.1
        
        self.rect = self.birdSprite[self.a].get_rect()
        self.rect.center = (self.birdX,self.birdY)
        
    def birdUpdate(self):
        self.JumpSpeed -=self.gravity
        self.birdY -=self.JumpSpeed
        
        self.rect.center = (self.birdX,self.birdY)
        
        if self.JumpSpeed > 0:
            self.a =1
        if self.JumpSpeed < 0:
            self.a =2
        
        global score    
        if self.rect.left == newWall.wallUpRect.right:
            score += 1 
        
        
    def birdCrush(self):
        global keep_going
        resultU = self.rect.colliderect(newWall.wallUpRect)
        resultD = self.rect.colliderect(newWall.wallDownRect)
        
        if resultU or resultD or newBird.rect.top>512:
            hit = pygame.mixer.Sound('sound/hit.wav')
            channel_3 = pygame.mixer.Channel(3)
            channel_3.play(hit)
            keep_going=False
            
class Wall():
    def __init__(self):
        self.wallUp = pygame.image.load("assets/bottom.png") 
        self.wallDown = pygame.image.load("assets/top.png")
        self.wallUpRect = self.wallUp.get_rect()
        self.wallDownRect = self.wallDown.get_rect()
        
        self.gap = 50
        self.wallx = 288
        self.offset = random.randint(-50,50)
        
        self.wallUpY=360 + self.gap - self.offset
        self.wallDownY = 0- self.gap - self.offset
        self.wallUpRect.center = (self.wallx,self.wallUpY)
        self.wallDownRect.center = (self.wallx,self.wallDownY)
        
    def wallUpdate(self):
        self.wallx -= 3
        self.wallUpRect.center = (self.wallx,self.wallUpY)
        self.wallDownRect.center = (self.wallx,self.wallDownY)
        if self.wallx < -80:
            self.wallx = 288
            self.offset = random.randint(-50,50)
            self.wallUpY=360 + self.gap - self.offset
            self.wallDownY = 0- self.gap - self.offset
class Text():
    """docstring for showText"""
    
    def __init__(self,content):
        red = (100,50,50)
        self.color = red
        self.font = pygame.font.SysFont(None,52)
        #SysFont(字体名，大小) -> frozenset
        contentStr = str(content)
        self.Image = self.font.render(contentStr,True,self.color)
        #pygame.font.render(你想要渲染的文字内容，渲染出来的文字是否更平滑呢，文字的颜色)
    def updateText(self,content):
        contentStr = str(content)
        self.Image = self.font.render(contentStr,True,self.color)
newBird = Bird() 
newWall = Wall()
coolText = Text(score)
while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
        if (event.type == pygame.MOUSEBUTTONDOWN):
            newBird.JumpSpeed = 7
            
            channel_2=pygame.mixer.Channel(2)
            fly = pygame.mixer.Sound('sound/fly.WAV')
            channel_2.play(fly)
            
    screen.blit(background,(0,0))
    screen.blit(newBird.birdSprite[newBird.a],newBird.rect)
    screen.blit(newWall.wallUp,newWall.wallUpRect)
    screen.blit(newWall.wallDown,newWall.wallDownRect)
    screen.blit(coolText.Image,(10,10))
    newWall.wallUpdate()
    newBird.birdUpdate()
    coolText.updateText(score)
    newBird.birdCrush()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
