import pygame
import random

background = "D:\\python\\pygame游戏制作\\游戏制作2\\image\\background.png"
duan_left = "D:\\python\\pygame游戏制作\\游戏制作2\\image\\duan_left.png"
duan_right = "D:\\python\\pygame游戏制作\\游戏制作2\\image\\duan_right.png"
bing = "D:\\python\\pygame游戏制作\\游戏制作2\\image\\bing.png"

pygame.init()
screen = pygame.display.set_mode((410,595))

background_image = pygame.image.load(background)
duan_image = pygame.image.load(duan_left)
bing_image = pygame.image.load(bing)

bing_x = 0
bing_y = -50
duan_x=200
duan_y=500
duan_move_x = 0

keep_going = True
while keep_going:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			keep_going = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				duan_image = pygame.image.load(duan_left)
				duan_move_x = -2
			if event.key == pygame.K_RIGHT:
				duan_image = pygame.image.load(duan_right)
				duan_move_x = +2
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				duan_image = pygame.image.load(duan_left)
				duan_move_x = 0
			if event.key == pygame.K_RIGHT:
				duan_image = pygame.image.load(duan_right)
				duan_move_x = 0

	bing_y += 3
	duan_x += duan_move_x

	if duan_x<0:
		duan_x = 0
	elif duan_x > 350:
		duan_x = 350

	if bing_y > 600:
		bing_x = random.randint(10,350)
		bing_y = -50

	screen.blit(background_image,(0,0))
	screen.blit(duan_image,(duan_x,duan_y))
	screen.blit(bing_image,(bing_x,bing_y))
	pygame.display.update()

pygame.quit()
