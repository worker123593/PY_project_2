import info
import pygame

from settings import setting

SSS_sprite_group = pygame.sprite.Group()


class Buttons(pygame.sprite.Sprite):
    def __init__(self, name='board'):
        super().__init__(SSS_sprite_group)
        inf = info.sss_sprites(name)
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
        elif self.name == 'play':
            return 1
        elif self.name == 'setting':
            setting()


def recreate_buttons():
    global SSS_sprite_group
    items = ['board', 'setting', 'play', 'exit']
    SSS_sprite_group = pygame.sprite.Group()
    for i in items:
        Buttons(name=i)


def start_screen():
    recreate_buttons()
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                info.terminate()
            elif event.type == pygame.VIDEORESIZE:
                info.size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
                recreate_buttons()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in SSS_sprite_group:
                    if i.rect.collidepoint(event.pos):
                        if i.action():
                            # info.reset_settings()
                            return
                recreate_buttons()
        fon = pygame.transform.scale(info.load_image('fon.jpg'), info.size)
        info.screen.blit(fon, (0, 0))
        SSS_sprite_group.draw(info.screen)
        pygame.display.flip()
        info.clock.tick(info.FPS)
