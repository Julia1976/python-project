import pygame
import random

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

class Block(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
class  Game():
    def __init__(self):
        self.block_list = pygame.sprite.Group()
        self.all_sprite_list = pygame.sprite.Group()

        for i in range(50):
            block = Block(BLACK,20,20)
            
            block.rect.x = random.randrange(SCREEN_WIDTH)
            block.rect.y = random.randrange(SCREEN_WIDTH)
            
            self.block_list.add(block)
            self.all_sprite_list.add(block)
        self.player = Player(RED, 20, 20)
        self.all_sprite_list.add(self.player)
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True 
        return False
    def run_logic(self):
        self.player.update()
        pygame.sprite.spritecollide(self.player, self.block_list, True)
    def display_frame(self,screen):
        screen.fill(WHITE)
        self.all_sprite_list.draw(screen)
        pygame.display.flip()
        



def main():
    pygame.init()
    screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
    pygame.display.set_caption("收集方块")
    pygame.mouse.set_visible(False)

    game = Game()
    done = False
    clock = pygame.time.Clock()
    while not done:
        done = game.process_events()
        game.run_logic()
        game.display_frame(screen)
        
        clock.tick(60)

    pygame.quit()

main()