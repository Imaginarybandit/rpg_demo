import pygame, sys
from settings import *
from level1 import Level

class Game:
    def __init__(self):

        pygame.init()
        game_world_width, game_world_height = WIDTH // ZOOM_FACTOR, HEIGTH // ZOOM_FACTOR
        self.screen = pygame.display.set_mode((game_world_width,game_world_height))

       

        pygame.display.set_caption('RPG DEMO')

        self.clock = pygame.time.Clock()

        self.level = Level()

    def run(self):
        
        while True: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            self.level.run()
            zoomed_surface = pygame.transform.scale(self.screen, (WIDTH, HEIGTH))
            self.screen.blit(zoomed_surface, (0, 0))
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()