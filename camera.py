import info
import pygame


class Camera:
    def __init__(self, x=0, y=0):
        self.tile_width = info.tile_width
        self.tile_height = info.tile_height
        self.dx = x
        self.dy = y
        for sprite in info.all_sprites:
            self.apply(sprite)

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - info.size[0] // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - info.size[1] // 2)
        for sprite in info.all_sprites:
            if target.name != 'player':
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


