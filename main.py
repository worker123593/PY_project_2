import pygame
import info
from player import Player
from start_screensaver import start_screen
from exit_screensaver import exit_screen
from info import screen, clock, FPS

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('1level')
    player = Player()
    start_screen()
    f = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_screen()
            elif event.type == pygame.MOUSEBUTTONUP:
                f = False
                if event.button == 4 and False:
                    player.camera.changing_size(1)
                if event.button == 5 and False:
                    player.camera.changing_size(-1)
                if event.button == 1:
                    for i in info.all_sprites:
                        if i.rect.collidepoint(event.pos):
                            player.moving(i.get_add_coord())
                            break

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3 and not f:
                    f = True
                    first_coord = event.pos
            elif event.type == pygame.MOUSEMOTION and f:
                change = [event.pos[0] - first_coord[0], event.pos[1] - first_coord[1]]
                first_coord = event.pos
                player.camera.mouse_updating(change)
        info.all_sprites.update()
        screen.fill(pygame.Color('black'))
        info.all_sprites.draw(screen)
        info.player_group.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)