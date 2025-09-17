from .board import *
from .piece import *
from .constants import *


class Game:
    def __init__(self, win):
        self._init()
        self.win = win
        self.sound_manager = None

    def set_sound_manager(self, sound_manager):
        self.sound_manager = sound_manager

    def _init(self):
        self.selected = None
        self.turn = BLACK
        self.board = Board()
        self.valid_moves = {}

    def reset(self):
        self._init()

    def update(self):
        self.board.draw(self.win)
        if self.selected is not None and self.turn == self.selected.color:
            self.draw_valid_moves(self.valid_moves)
        if self.selected is not None and self.selected != 0 and isinstance(self.selected, Piece) and self.turn == self.selected.color:
            pygame.draw.circle(self.win, GREEN, self.selected.rect.center, self.selected.rect.w//2+3, 2)
        pygame.display.update()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            skipped = self.valid_moves[(row, col)]
            self.board.move(self.selected, row, col)
            
            if self.sound_manager:
                if skipped:
                    self.sound_manager.play_capture_sound()
                else:
                    self.sound_manager.play_move_sound()
            
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False
        return True

    def change_turn(self):
        self.valid_moves = {}
        self.selected = None
        if self.turn == BLACK:
            self.turn = WHITE
        else:
            self.turn = BLACK

    def draw_valid_moves(self, moves):
        from .constants import BOARD_X, BOARD_Y
        for move in moves:
            row, col = move
            center_x = BOARD_X + col * SQUARE_SIZE + SQUARE_SIZE//2
            center_y = BOARD_Y + row * SQUARE_SIZE + SQUARE_SIZE//2
            pygame.draw.circle(self.win, BLUE, (center_x, center_y), 8)

    def winner(self):
        if self.board.winner() == WHITE:
            return 'AI'
        if self.board.winner() == BLACK:
            return 'YOU'

    def get_board(self):
        return self.board

    def ai_move(self, piece, row, col):
        _piece = self.board.get_piece(row, col)
        _valid_moves = self.board.get_valid_moves(piece)
        if _piece == 0 and (row, col) in _valid_moves:
            skipped = _valid_moves[(row, col)]
            self.board.move(piece, row, col)
            
            if self.sound_manager:
                if skipped:
                    self.sound_manager.play_capture_sound()
                else:
                    self.sound_manager.play_move_sound()
            
            if skipped:
                self.board.remove(skipped)
            self.change_turn()

