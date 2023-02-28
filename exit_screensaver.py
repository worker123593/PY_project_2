import info
import pygame
from settings import setting
from start_screensaver import start_screen


ESS_sprite_group = pygame.sprite.Group()


class Buttons(pygame.sprite.Sprite):
    def __init__(self, name='board'):
        super().__init__(ESS_sprite_group)
        inf = info.ess_sprites()[name]
        self.name = name
        self.image = pygame.Surface(([inf[2], inf[3]]))
        self.image.fill(pygame.Color(inf[4]))
        self.rect = self.image.get_rect().move(inf[1], inf[0])
        font = pygame.font.Font(None, 30)
        text_coord = 10
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
        elif self.name == 'menu':
            return 1
        elif self.name == 'setting':
            setting()


def exit_screen():
    info.score -= 1
    if info.score > 0:
        with open('data/score', 'a') as w:
            w.write(str(info.score) + '\n')
    with open('data/score') as r:
        best_score = max(list(map(int, r.readlines())))
    global ESS_sprite_group
    intro_text = ["game over", f'your score ' + str(info.score), 'the best score ' + str(best_score)]
    font = pygame.font.Font(None, 80)
    text_coord = 50
    items = ['board', 'menu', 'setting', 'exit']
    text = []
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = info.size[0] // 3
        text_coord += intro_rect.height
        text.append((string_rendered, intro_rect))

    for i in items:
        Buttons(name=i)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                info.terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in ESS_sprite_group:
                    mouse_pos = event.pos
                    if i.rect.collidepoint(mouse_pos):
                        a = i.action()
                        if a:
                            return start_screen()
                ESS_sprite_group = pygame.sprite.Group()
                for i in items:
                    Buttons(name=i)
            elif event.type == pygame.VIDEORESIZE:
                info.size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
                for i in text:
                    i[1].x = info.size[0] // 2 - 180
                ESS_sprite_group = pygame.sprite.Group()
                for i in items:
                    Buttons(name=i)
        fon = pygame.transform.scale(info.load_image('death.png'), info.size)
        info.screen.blit(fon, (0, 0))
        for i in text:
            info.screen.blit(*i)
        ESS_sprite_group.draw(info.screen)
        pygame.display.flip()
        info.clock.tick(info.FPS)
