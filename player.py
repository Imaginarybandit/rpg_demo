import pygame
from settings import *
from spritesheet import Spritesheet
from weapons import Weapon
from entity import Entity


class Player(Entity):
    def __init__(self,pos,groups,obstacle_sprites,create_attack,destroy_attack,get_item):
        super().__init__(groups)

        self.movementgraphics = Spritesheet("./graphics/player/Chris Walk.png")
        self.idlegraphics = Spritesheet("./graphics/player/Chris Idle.png")
        self.attackgraphics = Spritesheet("./graphics/player/Chris Attack (One Hand Weapons).png")

        self.spritesheet = Spritesheet('./graphics/player/Chris Idle.png')
        self.image = self.spritesheet.get_sprite(32,112,16,16)
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-5)
        self.original_position = None
        
        self.import_player_assets()
        self.status = 'down'
        

        self.obstacles_sprites =obstacle_sprites

        
        self.can_interact = False

        self.attacking = False
        self.attack_cooldown = 400
        self.attack_time = None
        self.create_attack = create_attack
        self.destroy_attack = destroy_attack
        self.get_item = get_item

        self.stats = {'health': 100, 'attack': 5,'speed': 2}
        self.weapons = []
        self.weapon = weapon_data['sword']
        self.items = []
        self.health = self.stats['health']
        self.speed = self.stats['speed']

        self.vulnerable = True
        self.hurt_time = None
        self.invulnerability_duration = 400

    def import_player_assets(self):
        self.animations = {

                'up': [
                    self.movementgraphics.get_sprite(32,32,16,16),
                    self.movementgraphics.get_sprite(112,32,16,16),
                    self.movementgraphics.get_sprite(192,32,16,16),
                    self.movementgraphics.get_sprite(272,32,16,16),
                    self.movementgraphics.get_sprite(352,32,16,16),
                    self.movementgraphics.get_sprite(432,32,16,16)
                ],
                'down':[
                    self.movementgraphics.get_sprite(32,112,16,16),
                    self.movementgraphics.get_sprite(112,112,16,16),
                    self.movementgraphics.get_sprite(192,112,16,16),
                    self.movementgraphics.get_sprite(272,112,16,16),
                    self.movementgraphics.get_sprite(352,112,16,16),
                    self.movementgraphics.get_sprite(432,112,16,16)
                ],
                'left':[
                    self.movementgraphics.get_sprite(32,192,16,16),
                    self.movementgraphics.get_sprite(112,192,16,16),
                    self.movementgraphics.get_sprite(192,192,16,16),
                    self.movementgraphics.get_sprite(272,192,16,16),
                    self.movementgraphics.get_sprite(352,192,16,16),
                    self.movementgraphics.get_sprite(432,192,16,16)
                ],
                'right':[
                    self.movementgraphics.get_sprite(32,272,16,16),
                    self.movementgraphics.get_sprite(112,272,16,16),
                    self.movementgraphics.get_sprite(192,272,16,16),
                    self.movementgraphics.get_sprite(272,272,16,16),
                    self.movementgraphics.get_sprite(352,272,16,16),
                    self.movementgraphics.get_sprite(432,272,16,16)
                ],'up_idle': [
                    self.idlegraphics.get_sprite(32,32,16,16),
                    self.idlegraphics.get_sprite(112,32,16,16),
                    self.idlegraphics.get_sprite(192,32,16,16),
                    self.idlegraphics.get_sprite(272,32,16,16),
                    self.idlegraphics.get_sprite(352,32,16,16),
                    self.idlegraphics.get_sprite(432,32,16,16)
                ],
                'down_idle':[
                    self.idlegraphics.get_sprite(32,112,16,16),
                    self.idlegraphics.get_sprite(112,112,16,16),
                    self.idlegraphics.get_sprite(192,112,16,16),
                    self.idlegraphics.get_sprite(272,112,16,16),
                    self.idlegraphics.get_sprite(352,112,16,16),
                    self.idlegraphics.get_sprite(432,112,16,16)
                ],
                'left_idle':[
                    self.idlegraphics.get_sprite(32,192,16,16),
                    self.idlegraphics.get_sprite(112,192,16,16),
                    self.idlegraphics.get_sprite(192,192,16,16),
                    self.idlegraphics.get_sprite(272,192,16,16),
                    self.idlegraphics.get_sprite(352,192,16,16),
                    self.idlegraphics.get_sprite(432,192,16,16)
                ],
                'right_idle':[
                    self.idlegraphics.get_sprite(32,272,16,16),
                    self.idlegraphics.get_sprite(112,272,16,16),
                    self.idlegraphics.get_sprite(192,272,16,16),
                    self.idlegraphics.get_sprite(272,272,16,16),
                    self.idlegraphics.get_sprite(352,272,16,16),
                    self.idlegraphics.get_sprite(432,272,16,16)
                ],'up_attack':[
                    self.attackgraphics.get_sprite(32,32,16,16),
                    self.attackgraphics.get_sprite(112,32,16,32),
                    self.attackgraphics.get_sprite(192,32,16,32),
                    self.attackgraphics.get_sprite(272,16,16,32),
                    self.attackgraphics.get_sprite(352,16,16,32),
                    self.attackgraphics.get_sprite(432,16,16,32),
                    self.attackgraphics.get_sprite(512,16,16,32),
                    self.attackgraphics.get_sprite(592,16,16,32),
                    self.attackgraphics.get_sprite(672,32,16,16)
                ],'down_attack':[
                    self.attackgraphics.get_sprite(32,112,16,16),
                    self.attackgraphics.get_sprite(112,112,16,16),
                    self.attackgraphics.get_sprite(192,112,16,16),
                    self.attackgraphics.get_sprite(256,112,32,32),
                    self.attackgraphics.get_sprite(336,112,32,32),
                    self.attackgraphics.get_sprite(432,112,16,32),
                    self.attackgraphics.get_sprite(512,112,16,32),
                    self.attackgraphics.get_sprite(592,112,16,32),
                    self.attackgraphics.get_sprite(672,112,16,16)
                ],'left_attack':[
                    self.attackgraphics.get_sprite(32,192,16,16),
                    self.attackgraphics.get_sprite(112,192,16,16),
                    self.attackgraphics.get_sprite(192,192,16,16),
                    self.attackgraphics.get_sprite(256,192,32,16),
                    self.attackgraphics.get_sprite(336,192,32,16),
                    self.attackgraphics.get_sprite(416,192,32,16),
                    self.attackgraphics.get_sprite(496,192,32,16),
                    self.attackgraphics.get_sprite(576,192,32,16),
                    self.attackgraphics.get_sprite(672,192,16,16)],
                    'right_attack':[
                    self.attackgraphics.get_sprite(32,272,16,16),
                    self.attackgraphics.get_sprite(112,272,16,16),
                    self.attackgraphics.get_sprite(192,272,16,16),
                    self.attackgraphics.get_sprite(272,272,32,16),
                    self.attackgraphics.get_sprite(352,272,32,16),
                    self.attackgraphics.get_sprite(432,272,32,16),
                    self.attackgraphics.get_sprite(512,272,32,16),
                    self.attackgraphics.get_sprite(592,272,32,16),
                    self.attackgraphics.get_sprite(672,272,16,16)
                    ]

            }
                                
    def inputs(self):

        if not self.attacking:

            keys = pygame.key.get_pressed()

            if keys[pygame.K_w]:
                self.direction.y = -1
                self.status = 'up'
            elif keys[pygame.K_s]:
                self.direction.y = 1
                self.status = 'down'
            else:
                self.direction.y= 0
                
            if keys[pygame.K_a]:
                self.direction.x = -1
                self.status = 'left'
            elif keys[pygame.K_d]:
                self.direction.x = 1
                self.status = 'right'
            else:
                self.direction.x= 0 


            if keys[pygame.K_f]:
                self.interact = True

                self.get_item()
                
            if keys[pygame.K_SPACE]:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()
                
                self.create_attack()
                

    def get_status(self):
        if self.direction.x == 0 and self.direction.y == 0:
            if not '_idle' in self.status and not '_attack' in self.status:
                self.status = self.status + '_idle'
        
        if self.attacking:
            self.direction.x = 0
            self.direction.y = 0

            if not 'attack' in self.status:
                if 'idle' in self.status:
                    self.status = self.status.replace('_idle','_attack')
                else:   
                    self.status = self.status + '_attack'
            
            
        else:
            if 'attack' in self.status:
                self.status = self.status.replace('_attack','')

    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking =False
                self.frame_index = 0
                self.destroy_attack()

        if not self.vulnerable:
            if current_time - self.hurt_time >= self.invulnerability_duration:
                self.vulnerable = True

    def animate(self):
       
       animation = self.animations[self.status]
       
       self.frame_index += self.animation_speed
    
       if self.frame_index >= len(animation):
            self.frame_index = 0
        
       self.image = animation[int(self.frame_index)]

       previous_center = self.rect.center
       previous_hitbox_center = self.hitbox.center

       if 'right_attack' in self.status and int(self.frame_index) in range(3, 8):  # Attack frames
            if self.original_position is None:
                self.original_position = previous_center

            
       elif 'left_attack' in self.status and int(self.frame_index) in range(3, 8):

            self.rect = self.image.get_rect(center=(self.hitbox.center[0] - 8,self.hitbox.center[1]))

       elif 'down_attack' in self.status and int(self.frame_index) in range(3, 8):
           
           if int(self.frame_index) in [3,4]:
                self.rect = self.image.get_rect(center=(self.hitbox.center[0] - 8,self.hitbox.center[1] +8))

           else:
                self.rect = self.image.get_rect(center=(self.hitbox.center[0] ,self.hitbox.center[1] + 8  ))
            
       elif 'up_attack' in self.status and int(self.frame_index) in range(1, 8):
           
           if int(self.frame_index) in [1,2]:
                self.rect = self.image.get_rect(center=(self.hitbox.center[0] ,self.hitbox.center[1] + 8  ))

           else:
                 self.rect = self.image.get_rect(center=(self.hitbox.center[0] ,self.hitbox.center[1] - 8  ))
       else:
            # Restore original position for non-attack states
            self.rect = self.image.get_rect(center=previous_hitbox_center)

        
    
    def get_full_weapon_damage(self):
        base_damage = self.stats['attack']
        weapon_damage = self.weapon['damage'] 
        
        return base_damage + weapon_damage

    def update(self):

        self.inputs()
        self.cooldowns()
        self.get_status()
        self.animate()
        self.move(self.speed)