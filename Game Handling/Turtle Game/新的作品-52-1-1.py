import pygame
from pygame.locals import*
import random
pygame.init()
sc_size = 300
sc = pygame.display.set_mode((sc_size,sc_size))
class Ball():
    def __init__(self,surface,color,size):
        self.surface = surface
        self.size = size
        self.color = color
    def create_ball(self,pos):
        pygame.draw.circle(self.surface,self.color,pos,self.size)
    
    def run(self,pos,sc_size,speed_x,speed_y,score):
        if pos[0] < self.size or pos[0] > sc_size-self.size:
            speed_x = -speed_x
        if pos[1] < self.size:
            speed_y = -speed_y
        if pos[1] > sc_size-self.size-5:
            if  rect_x < pos[0] <rect_x + 80:
                score += 1
                speed_y = -speed_y
        if pos[1] > sc_size - self.size:
            exit()

                
        pos[0] += speed_x
        pos[1] += speed_y
        return speed_x,speed_y,pos[0],pos[1],score

pos_x =  150
pos_y = 280

speed_x = random.randint(-5,5)
list_speed_y = [-5,-4,3,-2,-1]
speed_y = random.choice(list_speed_y)

#方块参数
rect_x = 150 -40
rect_y = 300 - 5
hight = 5
width = 80

ball = Ball(sc,(255,0,0),20)

ziti = pygame.font.SysFont('Arial',24)

score = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.display.quit()
            exit()
        elif event.type == MOUSEMOTION:
            rect_x, _ = pygame.mouse.get_pos()
    sc.fill((255,255,255))
    ball.create_ball([pos_x,pos_y])
    pygame.draw.rect(sc,(0,0,255),[rect_x,rect_y,width,hight])
    text = ziti.render(str(score),True,(255,0,0))
    sc.blit(text,(10,10))
    pygame.display.update()
    pygame.time.delay(50)
    speed_x, speed_y,pos_x,pos_y,score = ball.run([pos_x,pos_y],sc_size,speed_x,speed_y,score)
