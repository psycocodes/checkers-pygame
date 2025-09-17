import pygame
import sys
from screen_manager import ScreenManager

def main():
    pygame.init()
    manager = ScreenManager()
    manager.run()

if __name__ == "__main__":
    main()