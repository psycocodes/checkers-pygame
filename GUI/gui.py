import pygame
from .textures import *
from .constants import *
from .button import Button, RadioGroupElement, RadioGroup


class GUI:
    s_h = SCREEN_HEIGHT
    s_w = SCREEN_WIDTH

    def __init__(self, win):
        self.win = win
        self.quit = False
        self.play = 0
        self.difficulty = 1
        self._init()

    def _init(self):
        self.play_button = Button(self.win, (250, 350, 160, 50), state=0,
                                  color=WHITEW, corner_radius=10, hover_color=GREENW, disabled_color=GRAY,
                                  font=font_render('f_2', 30), font_values=("Play", 30, BLACK))
        self.quit_button = Button(self.win, (550, 350, 160, 50),
                                  color=WHITEW, corner_radius=10, hover_color=REDW, disabled_color=GRAY,
                                  font=font_render('f_2', 30), font_values=("Quit", 30, BLACK))
        self.easy = RadioGroupElement(self.win, 1, t_easy_d, t_easy, t_easy)
        self.okay = RadioGroupElement(self.win, 2, t_okay_d, t_okay, t_okay)
        self.hard = RadioGroupElement(self.win, 3, t_hard_d, t_hard, t_hard)
        self.difficulties = [self.easy, self.okay, self.hard]
        self.difficulties_group = RadioGroup(self.difficulties, 325, 253, 150)

    def draw(self):
        self.draw_window()
        # Title Rendering
        title = font_render('f_2', 40)
        title_txt = "C H E C K E R S"
        title_w, title_h = title.size(title_txt)
        self.win.blit(title.render(title_txt, 1, WHITE), ((self.s_w - title_w)//2,
                                                                 100 + title_h//2))
        title_sub = font_render('f_2', 20)
        title_sub_txt = "AI Implemented"
        title_sub_w, title_sub_h = title_sub.size(title_sub_txt)
        self.win.blit(title_sub.render(title_sub_txt, 1, WHITE), ((self.s_w - title_sub_w)//2,
                                                                 150 + title_sub_h//2))
        # Text Rendering
        t_1 = font_render('f_2', 25)
        t_1_txt = 'Difficulty: '
        t_1_w, t_1_h = title_sub.size(t_1_txt)
        self.win.blit(t_1.render(t_1_txt, 1, WHITE), (150-t_1_w//2, 235+t_1_h//2))

        self.play_button.draw()
        self.quit_button.draw()
        self.difficulties_group.draw()

    def update(self):
        pygame.display.update()

    def draw_window(self):
        self.win.blit(t_bg, (0, 0))

    def run(self):
        self.play_button_f()
        self.quit_button_f()
        self.radio_group_f()
        if self.difficulties_group.selected is not None:
            self.play_button.state = 1
        else:
            self.play_button.state = 0

    def play_button_f(self):
        if self.play_button.get_action():
            self.play = 1

    def quit_button_f(self):
        if self.quit_button.get_action():
            self.quit = True

    def radio_group_f(self):
        selected = self.difficulties_group.get_selected()
        if selected == 1:
            self.difficulty = 1
        elif selected == 2:
            self.difficulty = 2
        elif selected == 3:
            self.difficulty = 3
        else:
            self.difficulty = 1

    def return_v(self):
        return self.difficulty
