import pygame 
from spritesheet import Spritesheet
from settings import * 

class Interact(pygame.sprite.Sprite):
    def __init__(self,tile,groups,surface = pygame.Surface((TILESIZE,TILESIZE))):
         super().__init__(groups)
         self.tile = tile

         x = tile.rect.x
         y = tile.rect.y 
     
         self.image = surface

         self.rect = self.image.get_rect(center = (self.tile.rect.center[0],self.tile.rect.center[1]-16))

