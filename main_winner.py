import pygame, sys, os
from asset_utils import get_asset_path
from GUI.button import Button
from GUI.textures import *
from GUI.constants import *


def draw(screen, winner, main_button, quit_button):
    pygame.font.init()
    overlay = pygame.Surface((800, 450))
    overlay.set_alpha(180)
    overlay.fill((0, 0, 0))
    screen.blit(overlay, (0, 0))
    
    t_1 = pygame.font.Font(get_asset_path("RETRO_SPACE_INV.ttf"), 40)
    t_1_txt = f'{winner} WON!'
    t_1_w, t_1_h = t_1.size(t_1_txt)
    screen.blit(t_1.render(t_1_txt, True, (255,255,255)), (290,150))
    main_button.draw()
    quit_button.draw()


def main_winner(winner, screen, clock):
    FPS = 60
    pygame.display.set_caption("Checkers")
    run = True
    main_button = Button(screen, (250, 350, 160, 50), state=1,
                         color=GREENW, corner_radius=10, hover_color=GREENWW, disabled_color=GRAY,
                         font=font_render('f_2', 30), font_values=("Play", 30, BLACK))
    quit_button = Button(screen, (550, 350, 160, 50),
                         color=REDW, corner_radius=10, hover_color=REDWW, disabled_color=GRAY,
                         font=font_render('f_2', 30), font_values=("Quit", 30, BLACK))
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if quit_button.get_action() or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        if main_button.get_action():
            run = False
            return True

        draw(screen, winner, main_button, quit_button)
        pygame.display.update()

    return None

