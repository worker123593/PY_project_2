from info import tile_width, tile_height, load_level, load_image
import info
from subject import Subject
from camera import Camera
from level_generator import generate_level
from random import shuffle
import pygame


class Player(Subject):
    def __init__(self, x=0, y=0):
        super().__init__(x, y)
        player_image = load_image('warrior.png')
        self.image = player_image
        self.name = 'player'
        self.num_of_level = 1
        self.data_of_levels = {}
        x, y = generate_level(load_level('map1.txt'))
        self.overwriting_add_coord(x, y)
        self.overwriting_main_coord(x, y)
        info.player_group.add(self)
        info.all_sprites.add(self)
        self.camera = Camera()
        self.changing_level(0)

    def update(self):
        if self.a:
            motion = self.a.pop()
            self.rect.x -= (self.x - motion[0]) * tile_width
            self.rect.y -= (self.y - motion[1]) * tile_height
            self.overwriting_add_coord(motion[0], motion[1])
            for i in info.all_sprites:
                if i.get_add_coord() == motion and not self.a and i.name in ['stairs up', 'stairs down']:
                    if i.name == 'stairs up':
                        self.changing_level(-1)
                    else:
                        self.changing_level(1)
            self.camera.update(self)

    def changing_level(self, num):
        print(self.get_main_coord())
        self.data_of_levels[self.num_of_level] = [info.all_sprites, info.player_group, self.get_add_coord(), self.get_main_coord()]
        self.num_of_level += num
        info.player_group = pygame.sprite.Group()
        info.all_sprites = pygame.sprite.Group()
        if self.num_of_level in self.data_of_levels:
            info.player_group = self.data_of_levels[self.num_of_level][1]
            info.all_sprites = self.data_of_levels[self.num_of_level][0]
            x, y = self.data_of_levels[self.num_of_level][2]
        else:
            x, y = generate_level(load_level('map2.txt'))
            info.player_group.add(self)
            info.all_sprites.add(self)
        print(self.get_main_coord())
        self.overwriting_add_coord(x, y)
        self.overwriting_main_coord(x, y)

        self.camera.update(self)


