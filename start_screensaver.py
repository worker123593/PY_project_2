from info import size, terminate, clock, FPS, screen, load_image
import pygame

SSS_sprite_group = pygame.sprite.Group()
ESS_sprite_group = pygame.sprite.Group()


def start_screen():
    intro_text = [""]
    object_ = pygame.sprite.Sprite(SSS_sprite_group)

    object_.image = pygame.Surface(([30, 20]))
    object_.image.fill(pygame.Color('red'))
    object_.rect = object_.image.get_rect().move(200, 300)

    setting = pygame.sprite.Sprite(SSS_sprite_group)
    setting.image = load_image('setting.png')
    setting.rect = setting.image.get_rect().move(10, 10)

    fon = pygame.transform.scale(load_image('fon.jpg'), size)
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.VIDEORESIZE:
                pass
            elif event.type == pygame.KEYDOWN:
                pass
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in SSS_sprite_group:
                    if i.rect.collidepoint(event.pos):
                        return
        screen.blit(fon, (0, 0))
        SSS_sprite_group.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


def exit_screen():
    intro_text = ["game over"]

    fon = pygame.transform.scale(load_image('death.png'), size)
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                start_screen()
                return
        pygame.display.flip()
        clock.tick(FPS)
