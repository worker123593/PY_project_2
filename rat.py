import info
from subject import Subject
from camera import Camera
from random import choice
import pygame


class Rat(Subject):
    def __init__(self, x=0, y=0):
        super().__init__(x, y)
        self.image = pygame.transform.scale(info.load_image('rat.png'), (50, 50))
        self.name = 'rat'
        self.num_of_level = 1
        self.data_of_levels = {}
        self.overwriting_add_coord(x, y)
        self.overwriting_main_coord(x, y)
        info.enemys_group.add(self)


    def update(self):
        pass




