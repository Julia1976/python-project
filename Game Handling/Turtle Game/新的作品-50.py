import pygame
import sys


pygame.init()

window = pygame.display.set_mode([600,400])
turtles = [pygame.image.load("turtle_1.png"),
        pygame.image.load("turtle_2.png"),
          pygame.image.load("turtle_3.png"), ]
beach = pygame.image.load("beach.png")

index = 0
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    window.blit(beach,[0,0])
    window.blit(turtles[index % 3],[300,200])
    index = index + 1
    pygame.display.flip()
    clock.tick(10)
