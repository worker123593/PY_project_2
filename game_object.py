import pygame
from info import tile_width, tile_height, player_image
import info


class Object(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__(info.all_sprites)
        self.name = 'Object'
        self.coord = self.x, self.y = x, y
        self.image = player_image
        self.rect = self.image.get_rect().move(tile_width * x + 15, tile_height * y + 5)

    def overwriting_main_coord(self, x, y):
        self.rect.x, self.rect.y = x * tile_width, y * tile_height

    def get_main_coord(self):
        return self.rect.x, self.rect.y

    def overwriting_add_coord(self, x, y):
        self.coord = self.x, self.y = x, y

    def get_add_coord(self):
        return self.coord

