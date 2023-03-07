import pygame
from collections import deque
import info


class Subject(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__(info.subject_group, info.all_sprites)
        self.itr_name = 'p'
        self.graph = None
        self.x, self.y = x, y
        self.name_of_floor = '0'
        self.name = 'subject'
        self.health = 100
        self.damage = 10
        self.path = []
        self.recreate_grid()
        self.image = pygame.Surface(([50, 50]))
        self.rect = self.image.get_rect().move(info.tile_width * self.x + 15, info.tile_height * self.y + 5)

    def recreate_grid(self):
        info.grid = self.f(info.num_of_level)
        self.graph = {}
        for y, row in enumerate(info.grid):
            for x, col in enumerate(row):
                self.graph[(x, y)] = self.graph.get((x, y), []) + self.get_next_nodes(x, y)

    def overwriting_main_coord(self, x, y):
        self.rect.x, self.rect.y = x * info.tile_width, y * info.tile_height

    def f(self, num):
        if num not in info.maps:
            info.maps[num] = info.load_level(f'map{info.choice(range(1, 8))}.txt')
        return info.maps[num]

    def get_next_nodes(self, dx, dy):
        check_next_node = (lambda x, y: 0 <= x < len(info.grid[0]) and 0 <= y < len(
            info.grid) and info.grid[y][x] not in ['1'])
        ways = [-1, 0], [0, -1], [1, 0], [0, 1], [-1, 1], [-1, -1], [1, 1], [1, -1]
        return [(dx + x, dy + y) for x, y in ways if check_next_node(dx + x, dy + y)]

    def get_main_coord(self):
        return self.rect.x, self.rect.y

    def overwriting_add_coord(self, x, y):
        self.x, self.y = x, y

    def get_add_coord(self):
        return self.x, self.y

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
        if self.path:
            motion = self.path.pop(0)
            self.rect.x -= (self.x - motion[0]) * info.tile_width
            self.rect.y -= (self.y - motion[1]) * info.tile_height
            self.overwriting_coords(self.x - (self.x - motion[0]), self.y - (self.y - motion[1]))

    def moving(self, pos):
        visited = self.bfs(pos, self.graph)
        self.path = []
        path_head, path_segment = self.get_add_coord(), pos
        while path_segment in visited and visited[path_segment]:
            self.path.append(path_segment)
            path_segment = visited[path_segment]

    def get_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            info.subject_group.remove(self)
            info.all_sprites.remove(self)
            if self.name == 'player':
                pass
