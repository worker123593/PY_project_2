import pygame
from collections import deque
import info


class Subject(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__(info.all_sprites)
        self.x, self.y = x, y
        self.a = []
        self.name = 'subject'
        self.grid = info.level_map
        self.graph = {}
        for y, row in enumerate(self.grid):
            for x, col in enumerate(row):
                self.graph[(x, y)] = self.graph.get((x, y), []) + self.get_next_nodes(x, y)
        self.image = info.player_image
        self.rect = self.image.get_rect().move(info.tile_width * self.x + 15, info.tile_height * self.y + 5)

    def overwriting_main_coord(self, x, y):
        self.rect.x, self.rect.y = x * info.tile_width, y * info.tile_height

    def get_main_coord(self):
        return self.rect.x, self.rect.y

    def overwriting_add_coord(self, x, y):
        self.x, self.y = x, y

    def get_add_coord(self):
        return (self.x, self.y)

    def get_next_nodes(self, x, y):
        check_next_node = lambda x, y: True if 0 <= x < len(self.grid[0]) and 0 <= y < len(self.grid)\
                                               and self.grid[y][x] != '1' else False
        ways = [-1, 0], [0, -1], [1, 0], [0, 1], [-1, 1], [-1, -1], [1, 1], [1, -1]
        return [(x + dx, y + dy) for dx, dy in ways if check_next_node(x + dx, y + dy)]

    def bfs(self, goal, graph):
        queue = deque([(self.x, self.y)])
        visited = {(self.x, self.y): None}
        while queue:
            cur_node = queue.popleft()
            if cur_node == goal:
                break
            next_nodes = graph[cur_node]
            for next_node in next_nodes:
                if next_node not in visited:
                    queue.append(next_node)
                    visited[next_node] = cur_node
        return visited

    def update(self):
        # rfrfz-nj abuyz
        if self.a:
            motion = self.a.pop(0)
            self.rect.x -= (self.x - motion[0]) * info.tile_width
            self.rect.y -= (self.y - motion[1]) * info.tile_height
            self.overwriting_coords(self.x - (self.x - motion[0]), self.y - (self.y - motion[1]))

    def moving(self, pos):
        visited = self.bfs(pos, self.graph)
        self.a = []
        path_head, path_segment = self.get_add_coord(), pos
        while path_segment in visited:
            self.a.append(path_segment)
            path_segment = visited[path_segment]

