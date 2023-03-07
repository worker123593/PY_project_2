import pygame
import info


class Object(pygame.sprite.Sprite):
    """класс объектов"""
    def __init__(self, x=0, y=0):
        super().__init__(info.all_sprites)
        self.name = 'Object'
        self.coord = self.x, self.y = x, y
        self.image = info.player_image
        self.rect = self.image.get_rect().move(info.tile_width * x + 15, info.tile_height * y + 5)

    def overwriting_main_coord(self, x, y):
        self.rect.x, self.rect.y = x * info.tile_width, y * info.tile_height

    def get_main_coord(self):
        return self.rect.x, self.rect.y

    def overwriting_add_coord(self, x, y):
        self.coord = self.x, self.y = x, y

    def get_add_coord(self):
        return self.coord

