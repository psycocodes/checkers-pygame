import os
import sys

def get_asset_path(filename):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
        return os.path.join(base_path, 'Assets', filename)
    else:
        return os.path.join('Assets', filename)