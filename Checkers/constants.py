
import pygame
import os
import sys
from asset_utils import get_asset_path

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 450
ROWS, COLS = 8, 8
SQUARE_SIZE = int(SCREEN_HEIGHT * 0.8) // ROWS
BOARD_SIZE = SQUARE_SIZE * ROWS
BOARD_X = (SCREEN_WIDTH - BOARD_SIZE) // 2
BOARD_Y = (SCREEN_HEIGHT - BOARD_SIZE) // 2
IMAGE_SIZE = (SQUARE_SIZE * 4) // 5, (SQUARE_SIZE * 4) // 5
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
texture01 = pygame.transform.scale(pygame.image.load(get_asset_path("white_piece.png")), IMAGE_SIZE)
texture02 = pygame.transform.scale(pygame.image.load(get_asset_path("black_piece.png")), IMAGE_SIZE)
texture03 = pygame.transform.scale(pygame.image.load(get_asset_path("texture01.png")), (SQUARE_SIZE, SQUARE_SIZE))
texture04 = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(get_asset_path("texture02.png")), (SQUARE_SIZE, SQUARE_SIZE)), 90)
texture05 = pygame.transform.scale(pygame.image.load(get_asset_path("white_piece_king.png")), IMAGE_SIZE)
texture06 = pygame.transform.scale(pygame.image.load(get_asset_path("black_piece_king.png")), IMAGE_SIZE)
