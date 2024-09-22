import pygame
import os
from .constants import SCREEN_WIDTH, SCREEN_HEIGHT

pygame.font.init()

fonts = {"f_1": "RETRO_SPACE.ttf", "f_2": "RETRO_SPACE_INV.ttf"}


def texture_resize(texture, factor):
    ratio = texture.get_width(), texture.get_height()
    size = int(factor*ratio[0]), int(factor*ratio[1])
    return pygame.transform.scale(texture, size)


def font_render(file_code, size=40):
    return pygame.font.Font(os.path.join('Assets', fonts[file_code]), size)


factor1 = 0.4

t_bg = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'bg.png')), (SCREEN_WIDTH, SCREEN_HEIGHT))
t_easy = texture_resize(pygame.image.load(os.path.join("Assets", 'easy.png')), factor1)
t_okay = texture_resize(pygame.image.load(os.path.join("Assets", 'okay.png')), factor1)
t_hard = texture_resize(pygame.image.load(os.path.join("Assets", 'hard.png')), factor1)
t_easy_d = texture_resize(pygame.image.load(os.path.join("Assets", 'easy_d.png')), factor1)
t_okay_d = texture_resize(pygame.image.load(os.path.join("Assets", 'okay_d.png')), factor1)
t_hard_d = texture_resize(pygame.image.load(os.path.join("Assets", 'hard_d.png')), factor1)

