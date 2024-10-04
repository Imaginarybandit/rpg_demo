import pygame 
from spritesheet import Spritesheet
from settings import * 

class Interact(pygame.sprite.Sprite):
    def __init__(self,tile,groups):
         super().__init__(groups)
         self.tile = tile
         #self.display_surface = pygame.display.get_surface()
         self.font = pygame.font.Font(UI_FONT,UI_INT_FONT_SIZE)
         self.health_bar_rect = pygame.Rect(10,10,HEALTH_BAR_WIDTH,BAR_HEIGHT)

         x = tile.rect.x
         y = tile.rect.y 
     
         self.image = pygame.Surface((15,15))
     #     text_surf = self.font.render('F',False,'black')
     #     self.rect = text_surf.get_rect(center = (x,y))
         self.rect = self.image.get_rect(center = (self.tile.rect.center[0],self.tile.rect.center[1]-16))



#     def show_inter_icon(self,tile):
#          text_surf = self.font.render('F',False,'black')
#          x = tile.rect.x
#          y = tile.rect.y 
#          text_rect = text_surf.get_rect(center = (x,y))
#          #pygame.draw.rect(surface = self.display_surface,rect = text_rect.inflate(15,10))
#          #self.display_surface.blit(text_surf,text_rect)
         

#     def display(self,tile):
#          self.show_inter_icon(tile)