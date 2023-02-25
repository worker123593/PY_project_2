import info
from game_object import Object


class Tile(Object):
    def __init__(self, tile_type, x, y):
        super().__init__(x, y)
        self.image = info.tile_images[tile_type]
        self.rect = self.image.get_rect().move(info.tile_width * x, info.tile_height * y)
        self.name = tile_type


def generate_level(level):
    player_pos = (0, 0)
    c = 0
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '0':
                Tile('empty', x, y)
            elif level[y][x] == '1':
                Tile('wall', x, y)
            elif level[y][x] == '3':
                c += 1
                if c == 1:
                    Tile('stairs up', x, y)
                    player_pos = (x, y)
                else:
                    Tile('stairs down', x, y)
    return player_pos
