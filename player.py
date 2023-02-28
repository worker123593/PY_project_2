import info
from subject import Subject
from camera import Camera
from level_generator import generate_level
import pygame


class Player(Subject):
    def __init__(self, x=0, y=0):
        super().__init__(x, y)
        self.count_of_enemys = []
        self.p = 0
        self.q = True
        self.w = False
        player_image = info.load_image('warrior.png')
        self.image = player_image
        self.name = 'player'
        self.num_of_level = 1
        self.data_of_levels = {}
        x, y = generate_level(info.load_level(f'map4.txt'))
        self.overwriting_add_coord(x, y)
        self.overwriting_main_coord(x, y)
        info.player_group.add(self)
        self.camera = Camera()
        self.changing_level(0)

    def update(self):
        self.count_of_enemys = []
        for i in info.enemys_group:
            if abs(self.x - i.x) <= 2 and abs(self.y - i.y) <= 2:
                print(abs(self.x - i.x), abs(self.y - i.y))
                self.count_of_enemys.append(i)
                if not self.w and len(self.count_of_enemys):
                    self.q = False
                    self.w = True
        if not len(self.count_of_enemys) and self.w:
            self.w = False

        if self.p:
            self.changing_level(self.p)
            self.p = 0

        if self.a and self.q:
            motion = self.a.pop()
            self.rect.x -= (self.x - motion[0]) * info.tile_width
            self.rect.y -= (self.y - motion[1]) * info.tile_height
            self.overwriting_add_coord(motion[0], motion[1])
            for i in info.all_sprites:
                if i.get_add_coord() == motion:
                    if not self.a and i.name in ['stairs up', 'stairs down']:
                        if i.name == 'stairs up':
                            pass
                            # self.p = -1
                        else:
                            self.p = 1
            # self.camera.update(self)

    def changing_level(self, num):
        self.data_of_levels[self.num_of_level] = [info.all_sprites, info.player_group, info.subject_group]
        self.num_of_level += num
        info.player_group = pygame.sprite.Group()
        info.all_sprites = pygame.sprite.Group()
        info.subject_group = pygame.sprite.Group()
        if self.num_of_level in self.data_of_levels and False:
            info.subject_group = self.data_of_levels[self.num_of_level][2]
            info.player_group = self.data_of_levels[self.num_of_level][1]
            info.all_sprites = self.data_of_levels[self.num_of_level][0]
        x, y = generate_level(info.load_level(f'map3.txt'))
        info.player_group.add(self)
        info.all_sprites.add(self)
        self.overwriting_main_coord(x, y)
        self.overwriting_add_coord(x, y)
        # self.camera.update(self)
        info.score += 1

    def dead_check(self):
        info.player_group.remove(self)
