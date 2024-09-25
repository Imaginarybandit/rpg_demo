import pygame
from spritesheet import Spritesheet

movement = Spritesheet("./graphics/player/Chris Walk.png")
idle = Spritesheet("./graphics/player/Chris Idle.png")
attack = Spritesheet("./graphics/player/Chris Attack (One Hand Weapons).png")

movementIdle ={

    'up': [
        movement.get_sprite(32,32,16,16),
        movement.get_sprite(112,32,16,16),
        movement.get_sprite(192,32,16,16)
    ]
}

attack ={

}