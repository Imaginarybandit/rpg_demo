import pygame
from settings import *
from entity import Entity
from support import * 
from spritesheet import Spritesheet

class Enemy(Entity):
    def __init__(self,monster_name,pos,groups,obstacle_sprites,damage_player):

        super().__init__(groups)
        self.sprite_type = 'enemy'
        self.animation_speed = 0.10

        self.spritesheet = Spritesheet('./graphics/enemies/Slime 01.png')
        self.import_graphics(monster_name)
        self.status = 'idle'
        self.image =  self.spritesheet.get_sprite(16,0,16,16)

        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-10)
        self.obstacles_sprites = obstacle_sprites

        self.monster_name = monster_name
        monster_info = monster_data[self.monster_name]
        self.health = monster_info['health']
        self.speed = monster_info['speed']
        self.attack_damage = monster_info['damage']
        self.resistance = monster_info['resistance']
        self.attack_radius = monster_info['attack_radius']
        self.notice_radius = monster_info['notice_radius']
        self.attack_type = monster_info['attack_type']

        self.attacking = False

        self.can_attack = True
        self.attack_time = None
        self.attack_cooldown = 200
        self.damage_player = damage_player

        self.vulnerable = True
        self.hit_time = None
        self.invincibility_duration = 400

    def import_graphics(self,name):
            self.animations = {
                'idle':[
                self.spritesheet.get_sprite(0,0,16,16),
                self.spritesheet.get_sprite(16,0,16,16),
                self.spritesheet.get_sprite(32,0,16,16),
                self.spritesheet.get_sprite(48,0,16,16),
                self.spritesheet.get_sprite(0,64,16,16),
                self.spritesheet.get_sprite(16,64,16,16),
                self.spritesheet.get_sprite(32,64,16,16),
                self.spritesheet.get_sprite(48,64,16,16)
            ],
            'move':[
               self.spritesheet.get_sprite(0,0,16,16),
                self.spritesheet.get_sprite(16,0,16,16),
                self.spritesheet.get_sprite(32,0,16,16),
                self.spritesheet.get_sprite(48,0,16,16),
                self.spritesheet.get_sprite(0,64,16,16),
                self.spritesheet.get_sprite(16,64,16,16),
                self.spritesheet.get_sprite(32,64,16,16),
                self.spritesheet.get_sprite(48,64,16,16)
                ],
                'attack':[
               self.spritesheet.get_sprite(0,0,16,16),
                self.spritesheet.get_sprite(16,0,16,16),
                self.spritesheet.get_sprite(32,0,16,16),
                self.spritesheet.get_sprite(48,0,16,16),
                self.spritesheet.get_sprite(0,64,16,16),
                self.spritesheet.get_sprite(16,64,16,16),
                self.spritesheet.get_sprite(32,64,16,16),
                self.spritesheet.get_sprite(48,64,16,16)
                ]}
    
    
    def get_player_distance_direction(self,player):
        enemy_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(player.rect.center)
        distance = (player_vec - enemy_vec).magnitude()

        if distance > 0:
            direction = (player_vec - enemy_vec).normalize()
        else:
            direction = pygame.math.Vector2()
        
        return (distance,direction)

    def get_status(self, player):
        
        distance = self.get_player_distance_direction(player)[0]

        if distance <= self.attack_radius and self.can_attack:
            if self.status != 'attack':
                self.frame_index = 0
                self.status = 'attack'
        elif distance <= self.notice_radius:
            self.status = 'move'
        else:
            self.status = 'idle'

    def actions(self,player):
        
        if self.status == 'attack':
            self.attack_time = pygame.time.get_ticks()
            self.direction = self.get_player_distance_direction(player)[1]
            self.damage_player(self.attack_damage,self.attack_type)
        elif self.status == 'move':
            self.direction = self.get_player_distance_direction(player)[1]
        else:
            self.direction = pygame.math.Vector2()

    def animate(self):
        
        animation = self.animations[self.status]
		
        self.frame_index += self.animation_speed
        
        if self.frame_index >= len(animation):
            if self.status == 'attack':
                self.can_attack = False
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

        if not self.vulnerable:
             alpha = self.wave_value()
             self.image.set_alpha(alpha)
        else:
          self.image.set_alpha(255)

    def cooldowns(self):
          current_time = pygame.time.get_ticks()
          if not self.can_attack:
             
             if current_time - self.attack_time >= self.attack_cooldown:
                  self.can_attack = True

          if not self.vulnerable:
              if current_time - self.hit_time >= self.invincibility_duration:
                  self.vulnerable = True
                  self.hit_react = True

    def get_damage(self,player,attack_type):
        if self.vulnerable:
            if attack_type == 'weapon':
                self.health -= player.get_full_weapon_damage()
                self.hit_time = pygame.time.get_ticks()
            self.vulnerable = False

    def check_death(self): 
        if self.health <= 0:
            self.kill()

    def hit_reaction(self):

        if not self.vulnerable:
            
            self.direction *= -self.resistance
           
            
            

    def update(self):
        self.hit_reaction()
        self.move(self.speed)
        self.animate()
        self.cooldowns()
        self.check_death()


    def enemy_update(self,player):
        self.get_status(player)
        self.actions(player)
