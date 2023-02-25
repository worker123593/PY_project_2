import info
import pygame

from player import Player
from settings import setting

SSS_sprite_group = pygame.sprite.Group()


class Buttons(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, h=0, w=0, color='cyan',  image='', name='board'):
        super().__init__(SSS_sprite_group)
        self.name = name
        self.image = pygame.Surface(([h, w]))
        self.image.fill(pygame.Color(color))
        self.rect = self.image.get_rect().move(y, x)
        font = pygame.font.Font(None, 30)
        text_coord = 10
        if image:
            self.image.blit(info.load_image('warrior.png'), [10, 10])
        if name != 'board':
            line = name
            string_rendered = font.render(line, 1, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = text_coord
            intro_rect.x = self.rect.w / 7 * 3
            self.image.blit(string_rendered, intro_rect)

    def action(self):
        if self.name == 'exit':
            info.terminate()
        elif self.name == 'play':
            return 1
        elif self.name == 'setting':
            setting()


def start_screen():
    fon = pygame.transform.scale(info.load_image('fon.jpg'), info.size)
    info.screen.blit(fon, (0, 0))
    spos = [info.size[0] / 3, info.size[1] / 3]
    a = {'board': [spos[1], spos[0], spos[0], 160],
        'play': [spos[1] + 10, spos[0], spos[0], 40, 'grey'],
        'setting': [spos[1] + 60, spos[0], spos[0], 40, 'grey'],
        'exit': [spos[1] + 110, spos[0], spos[0], 40, 'grey']}
    for i in a.keys():
        Buttons(*a[i], name=i)
        SSS_sprite_group.draw(info.screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                info.terminate()
            elif event.type == pygame.VIDEORESIZE:
                pass
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in SSS_sprite_group:
                    mouse_pos = event.pos
                    if i.rect.collidepoint(mouse_pos):
                        a = i.action()
                        if a:
                            info.player_group = pygame.sprite.Group()
                            info.all_sprites = pygame.sprite.Group()
                            return Player()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in SSS_sprite_group:
                    if i.rect.collidepoint(event.pos):
                        return
            elif event.type == pygame.VIDEORESIZE:
                info.size = (pygame.display.Info().current_w, pygame.display.Info().current_h)

        info.screen.blit(fon, (0, 0))
        SSS_sprite_group.draw(info.screen)
        pygame.display.flip()
        info.clock.tick(info.FPS)
