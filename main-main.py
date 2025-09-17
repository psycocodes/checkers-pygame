import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from screen_manager import ScreenManager

def main():
    manager = ScreenManager()
    manager.run()

if __name__ == "__main__":
    main()