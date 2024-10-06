import pygame
from settings import *
from spritesheet import Spritesheet

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups,sprite_type,surface = pygame.Surface((TILESIZE,TILESIZE)),itemName  = None):
        super().__init__(groups)

        self.sprite_type = sprite_type
        self.name = itemName
      
        self.image = surface
        if sprite_type == 'object':
            self.rect = self.image.get_rect(topleft = (pos[0],pos[1] - TILESIZE))
        else:
            self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,0)
