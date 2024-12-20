import pygame 
from settings import * 

class UI:
    def __init__(self):
        
        
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT,UI_FONT_SIZE)

        self.health_bar_rect = pygame.Rect(10,10,HEALTH_BAR_WIDTH,BAR_HEIGHT)

    def show_bar(self,current,max_amount,bg_rect,color):
        pygame.draw.rect(self.display_surface,UI_BG_COLOR,bg_rect)

        # text_surf = self.font.render(str(int(current)),False,TEXT_COLOR)
        # x = (self.display_surface.get_size()[0] - 20) // 44
        # y = (self.display_surface.get_size()[1] - 20)  // 36

        ratio = current / max_amount
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width

        #text_rect = text_surf.get_rect(topleft = (x,y))
        # pygame.draw.rect(self.display_surface,UI_BG_COLOR,text_rect.inflate(15,10))
        # self.display_surface.blit(text_surf,text_rect)
        pygame.draw.rect(self.display_surface,color,current_rect)
        pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,bg_rect,1)


    def display(self,player):
        self.show_bar(player.health,player.stats['health'],self.health_bar_rect,HEALTH_COLOR)