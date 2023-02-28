import info
import pygame

settings_sprite_group = pygame.sprite.Group()


class Buttons(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, h=0, w=0, color='cyan', name='board'):
        super().__init__(settings_sprite_group)
        self.name = name
        self.image = pygame.Surface(([h, w]))
        self.image.fill(pygame.Color(color))
        self.rect = self.image.get_rect().move(y, x)
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
        if self.name == 'music':
            info.music = False


def setting():
    spos = [info.size[0] / 3, info.size[1] / 3]
    a = {'board': [spos[1], spos[0], spos[0], 160],
        'music': [spos[1] + 10, spos[0], spos[0], 40, 'grey']}
    for i in a.keys():
        Buttons(*a[i], name=i)
        settings_sprite_group.draw(info.screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                info.terminate()
            elif event.type == pygame.VIDEORESIZE:
                pass
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for i in settings_sprite_group:
                    if i.rect.collidepoint(mouse_pos):
                        i.action()
                    else:
                        return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in settings_sprite_group:
                    if i.rect.collidepoint(event.pos):
                        return
            elif event.type == pygame.VIDEORESIZE:
                info.size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        settings_sprite_group.draw(info.screen)
        pygame.display.flip()
        info.clock.tick(info.FPS)
