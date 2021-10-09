import pygame
import sys


pygame.init()

window = pygame.display.set_mode([600, 400])
beach = pygame.image.load("beach.png")
turtle = pygame.image.load("turtle.png")
rectangle = turtle.get_rect()
displacement = [-2,2]

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    rectangle = rectangle.move(displacement)
    if rectangle.left < 0:
        displacement[0] = -displacement[0]
        turtle = pygame.transform.flip(turtle,True,False)
    if rectangle.right > 600:
        displacement[0] = -displacement[0]
        turtle = pygame.transform.flip(turtle,True,False)
    if rectangle.top < 0:
        displacement[1] = -displacement[1]
    if rectangle.bottom > 400:
        displacement[1] = -displacement[1]


    window.blit(beach, [0, 0])
    window.blit(turtle,rectangle)
    pygame.display.flip()
    clock.tick
