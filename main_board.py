import pygame, sys
import os
from Checkers.constants import *
from Checkers.board import *
from Checkers.piece import *
from Checkers.game import *
from Checkers.algorithm import minimax, move_minimax


def get_mouse_pos(pos):
    x, y = pos
    x -= BOARD_X
    y -= BOARD_Y
    row = int(y // SQUARE_SIZE)
    col = int(x // SQUARE_SIZE)
    if row < 0 or row >= ROWS or col < 0 or col >= COLS:
        return None, None
    return row, col



def main_board(diff, screen, clock):
    FPS = 60
    pygame.display.set_caption("Checkers")
    run = True
    winner = None
    game = Game(screen)
    flag = 1
    
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_mouse_pos(pos)
                if row is not None and col is not None:
                    game.select(row, col)

        if game.turn == WHITE and flag:
            value, new_board = minimax(game.get_board(), diff, True, game)
            piece_row, piece_col, row, col = move_minimax(game.get_board(), new_board)
            game.ai_move(game.get_board().get_piece(piece_row, piece_col), row, col)
        if game.winner():
            run = False
            winner = game.winner()
            
        game.update()
        pygame.display.update()

    return winner

if __name__ == '__main__':
    main_board()