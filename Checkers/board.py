from .piece import Piece
from .constants import *
from copy import deepcopy, copy


class Board:
    def __init__(self):
        self.board = []
        self.selected = 0
        self.black_left = self.white_left = 12
        self.black_kings = self.white_kings = 0
        self.create_board()

    @staticmethod
    def draw_squares(win):
        win.fill(BLACK)
        for row in range(ROWS):
            if row % 2 == 0:
                for col in range(ROWS):
                    if col % 2 == 0:
                        win.blit(texture03, (SQUARE_SIZE * col, SQUARE_SIZE * row))
                    else:
                        win.blit(texture04, (SQUARE_SIZE * col, SQUARE_SIZE * row))
            else:
                for col in range(ROWS):
                    if col % 2 != 0:
                        win.blit(texture03, (SQUARE_SIZE * col, SQUARE_SIZE * row))
                    else:
                        win.blit(texture04, (SQUARE_SIZE * col, SQUARE_SIZE * row))

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == (row + 1) % 2:
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, BLACK))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)


    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw_piece(win)

    def move(self, piece, row, col):
        if isinstance(piece, Piece):
            self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
            piece.move(row, col)
        if (row == ROWS - 1 or row == 0) and not piece.king:
            piece.make_king()
            if piece.color == WHITE:
                self.white_kings += 1
            elif piece.color == BLACK:
                self.black_kings += 1

    def get_piece(self, row, col):
        return self.board[row][col]

    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row
        if piece.color == BLACK or piece.king:
            moves.update(self._traverse_left(row - 1, max(row - 3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row - 1, max(row - 3, -1), -1, piece.color, right))
        if piece.color == WHITE or piece.king:
            moves.update(self._traverse_left(row + 1, min(row + 3, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row + 1, min(row + 3, ROWS), 1, piece.color, right))
        return moves

    def _traverse_left(self, start, stop, step, color, left, skipped=[]):  # Checks for Left Diagonal
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break
            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    if skipped:
                        moves.update(self._traverse_left(r + step, row, step, color, left - 1, skipped=last + skipped))
                        moves.update(self._traverse_right(r + step, row, step, color, left + 1, skipped=last + skipped))
                    else:
                        moves.update(self._traverse_left(r + step, row, step, color, left - 1, skipped=last))
                        moves.update(self._traverse_right(r + step, row, step, color, left + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]
            left -= 1
        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped=[]):  # Checks for the Right Diagonal
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break
            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)

                    if skipped:
                        moves.update(self._traverse_left(r + step, row, step, color, right - 1, skipped=last + skipped))
                        moves.update(
                            self._traverse_right(r + step, row, step, color, right + 1, skipped=last + skipped))
                    else:
                        moves.update(self._traverse_left(r + step, row, step, color, right - 1, skipped=last))
                        moves.update(self._traverse_right(r + step, row, step, color, right + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]
            right += 1
        return moves

    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == BLACK:
                    self.black_left -= 1
                elif piece.color == WHITE:
                    self.white_left -= 1

    def winner(self):
        if self.white_left == 0:
            return BLACK
        elif self.black_left == 0:
            return WHITE
        else:
            return None

    def evaluate(self):
        return self.white_left - self.black_left + (self.white_kings * 0.5 - self.black_kings * 0.5)

    def get_all_pieces(self, color):
        pieces = []
        for row in self.board:
            for cell in row:
                if isinstance(cell, Piece) and cell != 0 and cell.color == color:
                    pieces.append(cell)
        return pieces

    def __repr__(self):
        _str = f'[{id(self)}]\n'
        if self.board != []:
            for i in range(len(self.board)):
                for j in self.board[i]:
                    if isinstance(j, Piece):
                        if j.color == WHITE:
                            _str += f"[■]"
                        else:
                            _str += f'[●]'
                    else:
                        _str += "[ ]"
                _str += '\n'
            return _str

    #Alternatives to deepcopy

    def copy_board(self):
        board = []
        for r, row in enumerate(self.board):
            board.append([])
            for piece in row:
                if piece != 0:
                    board[r].append(piece.copy())
                else:
                    board[r].append(piece)
        return board

    def copy(self):
        copyobj = Board()
        for name, attr in self.__dict__.items():
            if name == 'board':
                board = self.copy_board()
                setattr(copyobj, 'board', board)
            elif hasattr(attr, 'copy') and callable(getattr(attr, 'copy')) and name != 'board':
                copyobj.__dict__[name] = copy(attr)
            else:
                copyobj.__dict__[name] = deepcopy(attr)
        return copyobj
