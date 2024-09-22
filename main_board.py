import pygame, sys
from Checkers.constants import *
from Checkers.board import *
from Checkers.piece import *
from Checkers.game import *
from Checkers.algorithm import minimax, move_minimax


def get_mouse_pos(pos):
    x, y = pos
    row = int(y // SQUARE_SIZE)
    col = int(x // SQUARE_SIZE)
    return row, col


def main_board(diff):
    FPS = 60
    WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Checkers")
    clock = pygame.time.Clock()
    run = True
    winner = None
    game = Game(WIN)
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
                game.select(row, col)

        if game.turn == WHITE and flag:
            value, new_board = minimax(game.get_board(), diff, True, game)
            piece_row, piece_col, row, col = move_minimax(game.get_board(), new_board)
            game.ai_move(game.get_board().get_piece(piece_row, piece_col), row, col)
        if game.winner():
            run = False
            winner = game.winner()
        game.update()

    return winner

if __name__ == '__main__':
    main_board()



