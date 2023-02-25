import info
import pygame
from start_screensaver import start_screen

ESS_sprite_group = pygame.sprite.Group()


class Buttons(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, name='board', image=''):
        super().__init__(ESS_sprite_group)
        self.name = name
        self.image = pygame.Surface(([100, 100]))
        self.image.fill(pygame.Color('red'))
        self.rect = self.image.get_rect().move(y, x)
        font = pygame.font.Font(None, 30)
        text_coord = 20
        if image:
            self.image.blit(info.load_image('warrior.png'), [10, 10])
        if name != 'board':
            line = name
            string_rendered = font.render(line, 1, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            self.image.blit(string_rendered, intro_rect)

    def action(self):
        if self.name == 'exit':
            info.terminate()
        elif self.name == 'menu':
            return 1


def exit_screen():
    intro_text = ["game over"]
    fon = pygame.transform.scale(info.load_image('death.png'), info.size)
    info.screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50

    sprites_pos = [info.size[0] // 2, info.size[1] // 2]
    board = Buttons(sprites_pos[0], sprites_pos[1])
    menu = Buttons(sprites_pos[0] - 200, sprites_pos[1], name='menu')
    exit = Buttons(sprites_pos[0], sprites_pos[1], name='exit')
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        info.screen.blit(string_rendered, intro_rect)

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
            elif event.type == pygame.VIDEORESIZE:
                info.size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        info.screen.blit(fon, (0, 0))
        ESS_sprite_group.draw(info.screen)
        pygame.display.flip()
        info.clock.tick(info.FPS)
