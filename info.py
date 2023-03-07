import sys
import os
from random import choice
import pygame

size = [1300, 1000]
maps = {}


def fs(num):
    if num not in maps:
        maps[num] = load_level(f'map{choice(range(1, 8))}.txt')
    return maps[num]


def sss_sprites(name):
    return {'board': [size[1] / 3, size[0] / 3, size[0] / 3, 160, 'cyan'],
            'play': [size[1] / 3 + 10, size[0] / 3, size[0] / 3, 40, 'grey'],
            'setting': [size[1] / 3 + 60, size[0] / 3, size[0] / 3, 40, 'grey'],
            'exit': [size[1] / 3 + 110, size[0] / 3, size[0] / 3, 40, 'grey']}[name]


def ess_sprites(name):
    return {'board': [size[1] // 3, size[0] // 3, size[0] // 3, 160, 'cyan'],
            'menu': [size[1] // 3 + 10, size[0] // 3, size[0] // 3, 40, 'grey'],
            'setting': [size[1] // 3 + 60, size[0] // 3, size[0] // 3, 40, 'grey'],
            'exit': [size[1] // 3 + 110, size[0] // 3, size[0] // 3, 40, 'grey']}[name]


def settings_sprites(name):
    return {'board': [size[1] // 3, size[0] // 3, size[0] // 3, 160, 'cyan'],
            'music': [size[1] // 3 + 10, size[0] // 3, size[0] // 3, 40, 'grey'],
            'back': [size[1] // 3 + 70, size[0] // 3, size[0] // 3, 40, 'grey']}[name]


def interface_sprites(name):
    return {'board': [size[1] // 3, size[0] // 3, size[0] // 3, 160, 'cyan'],
            'music': [size[1] // 3 + 10, size[0] // 3, size[0] // 3, 40, 'grey'],
            'back': [size[1] // 3 + 70, size[0] // 3, size[0] // 3, 40, 'grey']}[name]


def terminate():
    pygame.quit()
    sys.exit()


def load_image(name):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def load_level(filename):
    filename = os.path.join('maps', filename)
    filename = os.path.join('data', filename)
    if not os.path.isfile(filename):
        print(f"Файл с картой '{filename}' не найден")
        sys.exit()
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    for i in range(len(level_map)):
        if len(level_map[i]) != max_width:
            level_map[i] += '0' * (max_width - len(level_map[i]))
    return list(map(lambda x: x.ljust(max_width, '0'), level_map))


screen = pygame.display.set_mode(size, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
all_sprites = pygame.sprite.Group()
player_group = pygame.sprite.Group()
subject_group = pygame.sprite.Group()
enemys_group = pygame.sprite.Group()
tile_images = {
    'wall': load_image('wall.png'),
    'stairs up': load_image('stairs_up.png'),
    'stairs down': load_image('stairs_down.png'),
    'empty': load_image('floor.png')}
# mob_images = {
#    'rat': load_image('rat.png'),
#    'crab': load_image('crab.png'),
#    'gnoll': load_image('gnoll.png')}
player_image = load_image('warrior.png')
tile_width = tile_height = 50
clock = pygame.time.Clock()
FPS = 20
score = 0
music = True
grid = None
retry_path = False


def reset_settings():
    global tile_width, tile_height, score, act, all_sprites, player_group, subject_group, enemys_group, maps
    tile_width = tile_height = 50
    score = 0
    act = False
    all_sprites = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    subject_group = pygame.sprite.Group()
    enemys_group = pygame.sprite.Group()
    maps = {}



