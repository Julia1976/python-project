import pygame
import random

background = "D:\\python\\pygame游戏制作\\游戏制作2\\image\\background.png"
duan_left = "D:\\python\\pygame游戏制作\\游戏制作2\\image\\duan_left.png"
duan_right = "D:\\python\\pygame游戏制作\\游戏制作2\\image\\duan_right.png"
bing = "D:\\python\\pygame游戏制作\\游戏制作2\\image\\bing.png"

pygame.init()
font = pygame.font.SysFont("SimHei",24)
screen = pygame.display.set_mode((410,595))

background_image = pygame.image.load(background)
duan_image = pygame.image.load(duan_left)
bing_image = pygame.image.load(bing)

bgm = pygame.mixer.Sound("D:\\python\\pygame游戏制作\\游戏制作2\\image\\bgm.wav")
channel_1 = pygame.mixer.Channel(1)
channel_1.play(bgm)

bing_x = 0
bing_y = -50
duan_x=200
duan_y=500
duan_move_x = 0
score = 0

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
		score = score - 10
	elif bing_y > duan_y:
		if(bing_x > duan_x-44)and(bing_x < duan_x+44):
			bing_x = random.randint(10,350)
			bing_y = -50
			score = score + 10
			music = pygame.mixer.Sound("D:\\python\\pygame游戏制作\\游戏制作2\\image\\pick.wav")
			channel_2 = pygame.mixer.Channel(2)
			channel_2.play(music)

	screen.blit(background_image,(0,0))
	screen.blit(duan_image,(duan_x,duan_y))
	screen.blit(bing_image,(bing_x,bing_y))
	text = font.render("分数："+str(score),True,(255,255,255))
	screen.blit(text,(0,0))
	pygame.display.update()

pygame.quit()
