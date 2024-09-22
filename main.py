import pygame
from main_board import main_board
from main_gui import main_gui
from main_winner import main_winner


def main():
    diff = main_gui()
    winner = main_board(diff)
    main_winner(winner)
    main()


if __name__ == '__main__':
    main()