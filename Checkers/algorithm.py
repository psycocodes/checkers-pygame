from .constants import WHITE, BLACK, RED
import pygame
flag = False


def minimax(position, depth, max_player, game):
    if depth == 0 or position.winner() is not None:
        return position.evaluate(), position
    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, WHITE, game):
            evaluation = minimax(move, depth-1, False, game)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, BLACK, game):
            evaluation = minimax(move, depth-1, True, game)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move
        return minEval, best_move


def get_all_moves(board, color, game):
    moves = []
    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            if flag:
                draw_moves(game, board, piece)
            temp_board = board.copy()
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)

    return moves


def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)
    return board


def draw_moves(game, board, piece):
    valid_moves = board.get_valid_moves(piece)
    board.draw(game.win)
    pygame.draw.circle(game.win, RED, (piece.x, piece.y), 30, 2)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()
    pygame.time.delay(10)


def move_minimax(old_board, new_board):
    i_pieces = old_board.get_all_pieces(WHITE)
    f_pieces = new_board.get_all_pieces(WHITE)
    i_moves = [(x.row, x.col) for x in i_pieces]
    f_moves = [(x.row, x.col) for x in f_pieces]
    piece_pos = [x for x in i_moves if x not in f_moves]
    diff = [x for x in f_moves if x not in i_moves]
    if diff and piece_pos:
        move = diff[0]
        piece = piece_pos[0]
    return piece[0], piece[1], move[0], move[1]








