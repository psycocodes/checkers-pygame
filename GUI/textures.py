import pygame
import os
from asset_utils import get_asset_path

pygame.font.init()

fonts = {"f_1": "RETRO_SPACE.ttf", "f_2": "RETRO_SPACE_INV.ttf"}

def texture_resize(texture, factor):
    ratio = texture.get_width(), texture.get_height()
    size = int(factor*ratio[0]), int(factor*ratio[1])
    return pygame.transform.scale(texture, size)

def font_render(file_code, size=40):
    try:
        font_path = get_asset_path(fonts[file_code])
        return pygame.font.Font(font_path, size)
    except Exception:
        return pygame.font.Font(None, size)

factor1 = 0.4

def import_bg(width, height, factor=(0, 0)):
    try:
        bg_path = get_asset_path('infinite_bg.png')
        bg_image = pygame.image.load(bg_path)
        t_bg = pygame.transform.scale(bg_image, (width+factor[0], height+factor[1]))
        return t_bg
    except Exception:
        fallback = pygame.Surface((width+factor[0], height+factor[1]))
        fallback.fill((20, 30, 60))
        return fallback

def blit_asset(display, texture: pygame.Surface, coordinates=(0, 0), special_flags=0):
    try:
        display.blit(texture, coordinates, special_flags=special_flags)
    except FileNotFoundError:
        pygame.draw.rect(display, 'purple', pygame.Rect(coordinates, (40, 40)))

def texture_load(name, parent_dir='Assets', file_ext='png'):
    return pygame.image.load(get_asset_path(f'{name}.{file_ext}'))

def dynamic_texture(texture, size, factor=1):
    return pygame.transform.scale(texture, (size[0]*factor, size[1]*factor))

from .constants import SCREEN_WIDTH, SCREEN_HEIGHT
from Checkers.constants import BOARD_SIZE, BOARD_X, BOARD_Y

def safe_load_texture(filename, fallback_color=(255, 0, 255)):
    try:
        return pygame.image.load(get_asset_path(filename))
    except Exception:
        surface = pygame.Surface((100, 50))
        surface.fill(fallback_color)
        return surface

t_bg = pygame.transform.scale(safe_load_texture('bg.png'), (SCREEN_WIDTH, SCREEN_HEIGHT))
t_easy = texture_resize(safe_load_texture('easy.png'), factor1)
t_okay = texture_resize(safe_load_texture('okay.png'), factor1)
t_hard = texture_resize(safe_load_texture('hard.png'), factor1)
t_easy_d = texture_resize(safe_load_texture('easy_d.png'), factor1)
t_okay_d = texture_resize(safe_load_texture('okay_d.png'), factor1)
t_hard_d = texture_resize(safe_load_texture('hard_d.png'), factor1)

tile_size = int(BOARD_SIZE * 1.05)
t_tile = pygame.transform.scale(safe_load_texture('tile.png'), (tile_size, tile_size))
tile_x = BOARD_X - (tile_size - BOARD_SIZE) // 2
tile_y = BOARD_Y - (tile_size - BOARD_SIZE) // 2

