import pygame, sys, os
from GUI.button import Button
from GUI.textures import *
from GUI.constants import *


def draw(WIN, winner, main_button, quit_button):
    pygame.font.init()
    WIN.fill((255, 255, 255))
    t_1 = pygame.font.Font(os.path.join('Assets', "RETRO_SPACE_INV.ttf"), 40)
    t_1_txt = f'{winner} WON!'
    t_1_w, t_1_h = t_1.size(t_1_txt)
    WIN.blit(t_1.render(t_1_txt, 1, (0,0,0)), (290,150))
    main_button.draw()
    quit_button.draw()


def main_winner(winner):
    FPS = 60
    WIN = pygame.display.set_mode((800,450))
    pygame.display.set_caption("Checkers")
    clock = pygame.time.Clock()
    run = True
    main_button = Button(WIN, (250, 350, 160, 50), state=1,
                         color=GREENW, corner_radius=10, hover_color=GREENWW, disabled_color=GRAY,
                         font=font_render('f_2', 30), font_values=("Play", 30, BLACK))
    quit_button = Button(WIN, (550, 350, 160, 50),
                         color=REDW, corner_radius=10, hover_color=REDWW, disabled_color=GRAY,
                         font=font_render('f_2', 30), font_values=("Quit", 30, BLACK))
    flag = False
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

        draw(WIN, winner, main_button, quit_button)
        pygame.display.update()
