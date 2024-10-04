import pygame
from settings import *
from spritesheet import Spritesheet

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups,sprite_type,surface = pygame.Surface((TILESIZE,TILESIZE))):
        super().__init__(groups)

        self.sprite_type = sprite_type
      
        self.image = surface
        if sprite_type == 'object':
            self.rect = self.image.get_rect(topleft = (pos[0],pos[1] - TILESIZE))
        else:
            self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,0)

    # def get_player_distance_direction(self,player):
    #     enemy_vec = pygame.math.Vector2(self.rect.center)
    #     player_vec = pygame.math.Vector2(player.rect.center)
    #     distance = (player_vec - enemy_vec).magnitude()

    #     if distance > 0:
    #         direction = (player_vec - enemy_vec).normalize()
    #     else:
    #         direction = pygame.math.Vector2()

    #     return (distance,direction)