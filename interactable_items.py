import pygame 
from spritesheet import Spritesheet
from settings import * 

class Interact(pygame.sprite.Sprite):
    def __init__(self,tile,groups):
         super().__init__(groups)
         self.tile = tile
         self.display_surface = pygame.display.get_surface()
         self.font = pygame.font.Font(UI_FONT,UI_INT_FONT_SIZE)

    def show_inter_icon(self,tile):
         text_surf = self.font.render(str('F'),False,'black')
         
