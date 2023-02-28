import pygame
import info
from start_screensaver import start_screen
from exit_screensaver import exit_screen

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('remake of pixel dungeon')
    player = start_screen()
    f = False
    act = True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_screen()

            elif event.type == pygame.MOUSEBUTTONUP:
                f = False
                if event.button == 4 and False:
                    player.camera.changing_size(1)
                elif event.button == 5 and False:
                    player.camera.changing_size(-1)
                elif event.button == 1:

                    for i in info.all_sprites:
                        if i.rect.collidepoint(event.pos):
                            if not player.q:
                                player.q = True
                            player.moving(i.get_add_coord())
                            break
                    act = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3 and not f:
                    f = True
                    first_coord = event.pos

            elif event.type == pygame.VIDEORESIZE:
                info.size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
            elif event.type == pygame.MOUSEMOTION and f:
                change = [event.pos[0] - first_coord[0], event.pos[1] - first_coord[1]]
                first_coord = event.pos
                player.camera.mouse_updating(change)

        info.screen.fill(pygame.Color('black'))
        if act:
            info.all_sprites.update()

        info.all_sprites.draw(info.screen)

        info.subject_group.draw(info.screen)
        pygame.display.flip()
        info.clock.tick(info.FPS)
