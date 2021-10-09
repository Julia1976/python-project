import sys
import pygame
import random


pygame.init()
pygame.display.set_caption("who is the caption")
window = pygame.display.set_mode((500,500))
font = pygame.font.Font("思源黑体.otf",35)

wheel_pics = []
for i in range(25):
    filename = './pics/' + str(i) + '.png'
    pic = pygame.image.load(filename)
    wheel_pics.append(pic)
start_pic = pygame.image.load('start.png')
window.fill((255,255,255))
window.blit(start_pic,(0,0))
pygame.display.flip()

with open('names.txt',encoding = 'utf8') as f:
    name_list = []
    for i in range(6):
        name_list.append(f.readline().strip())

choice = random.choice(name_list)

print(choice)

rolling = False
pic_index = 0
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                rolling = True
    if rolling:
        window.fill((255,255,255))
        window.blit(wheel_pics[pic_index % 25],(0,0))
        pic_index += 1
        if pic_index >= 25:
            rolling = False
            pic_index = 0
            choice = random.choice(name_list)
            text = font.render(choice, True, (255,255,255))
            window.blit(text,(215,220))
    
    pygame.display.flip()
    clock.tick(30)