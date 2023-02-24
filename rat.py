import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)

    def moving(self, derection):
        x, y = (self.rect.x - 15) // tile_width, (self.rect.y - 5) // tile_height
        if derection == 'up':
            if y > 0 and (level_map[y - 1][x] == '.' or level_map[y - 1][x] == '@'):
                self.rect.y -= tile_height
        elif derection == 'down':
            print(width // tile_width - 1)
            if y < width // tile_width - 1 and (level_map[y + 1][x] == '.' or level_map[y + 1][x] == '@'):
                self.rect.y += tile_height
        elif derection == 'left':
            if x > 0 and (level_map[y][x - 1] == '.' or level_map[y][x - 1] == '@'):
                self.rect.x -= tile_width
        elif derection == 'right':
            if x < height // tile_height - 1 and (level_map[y][x + 1] == '.' or level_map[y][x + 1] == '@'):
                self.rect.x += tile_width