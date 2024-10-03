import pygame
from spritesheet import Spritesheet

class Weapon(pygame.sprite.Sprite):
    def __init__(self,player,groups,player_center):
        super().__init__(groups)
        self.player = player
        self.direction = self.player.status.split('_')[0]
        
        self.weapon_graphics = Spritesheet("./graphics/player/Chris Sword 01.png")
        self.player_center = player_center
        self.image = pygame.Surface((1,1))
        self.rect = self.image.get_rect(center = self.player.rect.center)
        self.frame_index = 0
        
        self.animations = {
            'down':  [
                self.weapon_graphics.get_sprite(32,112,32,16),
                self.weapon_graphics.get_sprite(112,112,32,16),
                self.weapon_graphics.get_sprite(192,96,32,32),
                self.weapon_graphics.get_sprite(256,128,48,16),
                self.weapon_graphics.get_sprite(336,112,32,32),
                self.weapon_graphics.get_sprite(416,112,32,32),
                self.weapon_graphics.get_sprite(496,112,32,32),
                self.weapon_graphics.get_sprite(576,112,32,32),
                #self.weapon_graphics.get_sprite(656,112,48,48)
            ],'up':[
                  self.weapon_graphics.get_sprite(16,32,32,16),
                self.weapon_graphics.get_sprite(96,32,32,16),
                self.weapon_graphics.get_sprite(176,32,32,32),
                self.weapon_graphics.get_sprite(256,16,48,32),
                self.weapon_graphics.get_sprite(352,16,32,32),
                self.weapon_graphics.get_sprite(432,16,32,32),
                self.weapon_graphics.get_sprite(512,16,32,32),
                self.weapon_graphics.get_sprite(592,32,32,16),
            ], 'left':[
                        self.weapon_graphics.get_sprite(16,32,32,16),
                self.weapon_graphics.get_sprite(96,32,32,16),
                self.weapon_graphics.get_sprite(176,32,32,32),
                self.weapon_graphics.get_sprite(256,16,48,32),
                self.weapon_graphics.get_sprite(352,16,32,32),
                self.weapon_graphics.get_sprite(432,16,32,32),
                self.weapon_graphics.get_sprite(512,16,32,32),
                self.weapon_graphics.get_sprite(592,32,32,16),
                ]        
}

    
    def animate(self):
        if self.direction == 'down' :
           
            
            animation = self.animations[self.direction]

            if int(self.player.frame_index) < len(animation):
                  
                self.frame_index = int(self.player.frame_index)

                self.image = animation[int(self.player.frame_index)]

                if int(self.player.frame_index) in (0,1):
                        
                        self.rect = self.image.get_rect(center = (self.player_center[0] +8 ,self.player_center[1] ))
                    

                elif int(self.player.frame_index) == 2:
                        self.rect = self.image.get_rect(center = (self.player_center[0] +8 ,self.player_center[1] - 8 ))
                elif int(self.player.frame_index) == 3:
                        self.rect = self.image.get_rect(center = (self.player_center[0]  ,self.player_center[1] + 16 ))
                elif int(self.player.frame_index) in (4,5):
                        self.rect = self.image.get_rect(center = (self.player_center[0] - 6  ,self.player_center[1] +8 ))
                
        elif self.direction == 'up':
                animation = self.animations[self.direction]

                if int(self.player.frame_index) < len(animation):
                    
                    self.frame_index = int(self.player.frame_index)

                    self.image = animation[int(self.player.frame_index)]

                    if int(self.player.frame_index) in (0,1):
                            
                            self.rect = self.image.get_rect(center = (self.player_center[0] -8 ,self.player_center[1] ))
                        
                    elif int(self.player.frame_index) == 2:
                            self.rect = self.image.get_rect(center = (self.player_center[0] -8 ,self.player_center[1] + 8 ))
                    elif int(self.player.frame_index) == 3:
                            self.rect = self.image.get_rect(center = (self.player_center[0]  ,self.player_center[1] - 8 ))
                    elif int(self.player.frame_index) in (4,5):
                            self.rect = self.image.get_rect(center = (self.player_center[0] + 8  ,self.player_center[1] -8 ))
                    elif int(self.player.frame_index) in (6,7):
                            self.rect = self.image.get_rect(center = (self.player_center[0] + 8  ,self.player_center[1] ))

        elif self.direction == 'left':
                animation = self.animations[self.direction]

                if int(self.player.frame_index) < len(animation):
                    
                    self.frame_index = int(self.player.frame_index)

                    self.image = animation[int(self.player.frame_index)]

                    if int(self.player.frame_index) in (0,1):
                            
                            self.rect = self.image.get_rect(center = (self.player_center[0] -8 ,self.player_center[1] ))
                        
                    elif int(self.player.frame_index) == 2:
                            self.rect = self.image.get_rect(center = (self.player_center[0] -8 ,self.player_center[1] + 8 ))
                    elif int(self.player.frame_index) == 3:
                            self.rect = self.image.get_rect(center = (self.player_center[0]  ,self.player_center[1] - 8 ))
                    elif int(self.player.frame_index) in (4,5):
                            self.rect = self.image.get_rect(center = (self.player_center[0] + 8  ,self.player_center[1] -8 ))
                    elif int(self.player.frame_index) in (6,7):
                            self.rect = self.image.get_rect(center = (self.player_center[0] + 8  ,self.player_center[1] ))

                
    def update (self):
        self.animate()
      
        