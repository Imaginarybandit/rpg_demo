WIDTH    = 1450
HEIGTH   = 950
FPS      = 60
TILESIZE = 16
ZOOM_FACTOR = 2.0

# ui 
BAR_HEIGHT = 10
HEALTH_BAR_WIDTH = 10
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = './graphics/font/joystix.ttf'
UI_FONT_SIZE = 14
UI_INT_FONT_SIZE = 8

WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

weapon_data = {
    'sword': {'cooldown':100,'damage':15,'graphics':'./graphics/player/Chris Sword 01.png'}
}

monster_data = {
   'blob':{ 'health': 30,'damage':1,'attack_type':'contact','speed':1,'resistance':1.5,'attack_radius':60,'notice_radius':120}
}