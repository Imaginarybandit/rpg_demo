from typing import Iterable
import pygame
from pygame.sprite import AbstractGroup
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import import_csv_layout
from spritesheet import Spritesheet
from details import details

class Level:
    def __init__(self):
        
        #get the display surface
        self.display_surface = pygame.display.get_surface()
        #sprtie group setup
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        self.details = details

        #Sprite Setup
        self.create_map()

    def create_map(self):
        layout ={
            'boundary' : import_csv_layout('./map/Map._FloorBlocks.csv'),
            'details': import_csv_layout('./map/Map._Details.csv'),
            'extra_details': import_csv_layout('./map/Map._Details 2.csv'),
            'objects':import_csv_layout('./map/Map._Objects.csv')
        }

        for style,layout in layout.items():
            for row_index,row in enumerate(layout):
                for col_index,col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'boundary':
                            spritesheet = Spritesheet('./graphics/objects/Solaria Demo Tiles.png')
                            image = spritesheet.get_sprite(288,96,16,16)
                            Tile((x,y),[self.obstacle_sprites],'invisible',image)

                        if style == 'objects':
                            if col == '7':
                                 #details = self.details['mushrooms']
                                 spritesheet = Spritesheet('./graphics/objects/Solaria Demo Tiles.png')
                                 image = spritesheet.get_sprite(112,0,48,48)
                                 Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'objects',image)
                            if col == '10':
                                spritesheet = Spritesheet('./graphics/objects/Solaria Demo Tiles.png')
                                image = spritesheet.get_sprite(160,0,16,16)
                                Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'objects',image)
                            if col == '11':
                                spritesheet = Spritesheet('./graphics/objects/Solaria Demo Tiles.png')
                                image = spritesheet.get_sprite(176,0,16,16)
                                Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'objects',image)
                            if col == '12':
                                spritesheet = Spritesheet('./graphics/objects/Solaria Demo Tiles.png')
                                image = spritesheet.get_sprite(192,0,16,16)
                                Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'objects',image)
                            if col == '289':
                                spritesheet = Spritesheet('./graphics/objects/Solaria Demo Tiles.png')
                                image = spritesheet.get_sprite(144,160,16,32)
                                Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'objects',image)
                            if col == '91':
                                spritesheet = Spritesheet('./graphics/objects/Solaria Demo Tiles.png')
                                image = spritesheet.get_sprite(112,48,16,32)
                                Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'objects',image)

                            if col == '286':
                                spritesheet = Spritesheet('./graphics/objects/Solaria Demo Tiles.png')
                                image = spritesheet.get_sprite(96,160,48,80)
                                Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'objects',image)

                            if col == '147':
                                spritesheet = Spritesheet('./graphics/objects/Solaria Demo Tiles.png')
                                image = spritesheet.get_sprite(112,80,32,32)
                                Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'objects',image)
                            if col == '150':
                                spritesheet = Spritesheet('./graphics/objects/Solaria Demo Tiles.png')
                                image = spritesheet.get_sprite(160,80,16,16)
                                Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'objects',image)
                            if col == '311':
                                spritesheet = Spritesheet('./graphics/objects/Solaria Demo Tiles.png')
                                image = spritesheet.get_sprite(48,176,16,16)
                                Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'objects',image)
                            if col == '90':
                                spritesheet = Spritesheet('./graphics/objects/Solaria Demo Tiles.png')
                                image = spritesheet.get_sprite(96,48,16,32)
                                Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'objects',image)
                            if col == '260':
                                spritesheet = Spritesheet('./graphics/objects/Solaria Demo Tiles.png')
                                image = spritesheet.get_sprite(128,144,16,16)
                                Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'objects',image)
                            if col == '304':
                                spritesheet = Spritesheet('./graphics/objects/Solaria Demo Tiles.png')
                                image = spritesheet.get_sprite(384,160,16,16)
                                Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'objects',image)

        self.player = Player((192,560),[self.visible_sprites],self.obstacle_sprites)
       
    
        
    def run(self):

        #update and draw the game
       
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
       

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):

        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 4
        self.half_height = self.display_surface.get_size()[1] // 4

        self.offset = pygame.math.Vector2(50,100)

        #creating the floor
        self.floor_surf = pygame.image.load('./graphics/map/Map.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))
        

    def custom_draw(self,player):

            
        self.offset.x = player.rect.centerx - self.half_width 
        self.offset.y = player.rect.centery - self.half_height
        
        if player.status == 'left_attack' and int(player.frame_index) in range(3, 8): 
            self.offset.x = self.offset.x + 8

        elif player.status == 'down_attack' and int(player.frame_index) in range(3, 8):
           
           if int(player.frame_index) in [3,4]:
                
                self.offset.x = self.offset.x + 8
                self.offset.y = self.offset.y - 8
           else:
                self.offset.y = self.offset.y - 8
        
        elif player.status == 'up_attack'  and int(player.frame_index) in range(1, 8):
           
           if int(player.frame_index) in [1,2]:
                
                self.offset.y = self.offset.y - 8
           else:
                
                self.offset.y = self.offset.y + 8
                
        floor_offset_pos = self.floor_rect.topleft - self.offset

        self.display_surface.blit(self.floor_surf,floor_offset_pos)

        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)
                 