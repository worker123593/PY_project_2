import info
from subject import Subject
import pygame


class Rat(Subject):
    def __init__(self, x=0, y=0):
        super().__init__(x, y)
        self.itr_name = '@'
        self.player_pos = []
        self.image = pygame.transform.scale(info.load_image('rat.png'), (50, 50))
        self.name = 'rat'
        self.num_of_level = 1
        self.data_of_levels = {}
        self.overwriting_add_coord(x, y)
        self.overwriting_main_coord(x, y)
        info.enemys_group.add(self)

    def update(self):
        for i in info.player_group:
            if abs(self.x - i.x) <= 4 and abs(self.y - i.y) <= 4:
                self.player_pos = i.get_add_coord()
        if abs(self.x - i.x) > 1 or abs(self.y - i.y) > 1:
            if len(self.path) > 1 and self.player_pos == self.path[0]:
                motion = self.path.pop()
                self.change_name_of_grid()
                self.rect.x -= (self.x - motion[0]) * info.tile_width
                self.rect.y -= (self.y - motion[1]) * info.tile_height
                self.overwriting_add_coord(motion[0], motion[1])
                self.change_name_of_grid()
            elif not len(self.path) and self.player_pos or len(self.path) and self.player_pos != self.path[0]:
                self.moving(self.player_pos)
        else:
            pass




