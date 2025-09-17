import pygame, sys
from GUI.constants import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE
from GUI.textures import *
from GUI.gui import GUI


def main_gui(screen, clock):
    FPS = 60
    pygame.display.set_caption("Checkers")
    main_gui = GUI(screen)
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if main_gui.quit or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        if main_gui.play:
            run = False
            return main_gui.difficulty
        
        main_gui.run()
        main_gui.draw()
        main_gui.update()
        pygame.display.update()

    return None


if __name__ == '__main__':
    main_gui()
