from info import width, height, tile_height, tile_width
import info
import pygame


class Camera:
    def __init__(self):
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.dx = 0
        self.dy = 0

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - height // 2)
        for sprite in info.all_sprites:
            self.apply(sprite)

    def mouse_updating(self, coord):
        self.dx = coord[0]
        self.dy = coord[1]
        for sprite in info.all_sprites:
            self.apply(sprite)

    def changing_size(self, item):
        self.tile_width += item if 25 <= self.tile_width + item <= 60 else 0
        self.tile_height += item if 25 <= self.tile_height + item <= 60 else 0
        for sprite in info.all_sprites:
            self.f(sprite)

    def f(self, target):
        a = target.rect.w, target.rect.h
        target.rect.w, target.rect.h = self.tile_width, self.tile_height
        target.image = pygame.transform.scale(target.image, (target.rect.w, target.rect.h))
        target.rect.x -= a[0] - self.tile_width
        target.rect.y -= a[1] - self.tile_height
        print(target.rect)


