import pygame
import os
import sys
from asset_utils import get_asset_path
from GUI.constants import SCREEN_WIDTH, SCREEN_HEIGHT, GREENW, GREENWW, REDW, REDWW, GRAY, BLACK
from GUI.infinite_bg import InfiniteBackground
from GUI.particle_system import ParticleManager
from GUI.particle_utils import load_data
from GUI.gui import GUI
from GUI.button import Button
from GUI.textures import *
from GUI.sound_manager import SoundManager
from Checkers.constants import *
from Checkers.game import Game
from Checkers.algorithm import minimax, move_minimax

class ScreenManager:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Checkers")
        
        icon_path = get_asset_path('black_piece.png')
        try:
            icon = pygame.image.load(icon_path)
            pygame.display.set_icon(icon)
        except Exception:
            pass
        
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = "menu"
        self.difficulty = None
        self.winner = None
        
        self.infinite_bg = InfiniteBackground(scroll_speed=0.3)
        self.bg_offset_x = -20
        self.bg_offset_y = 0
        
        DISPLAY_SCALE = 2
        self.particle_surface = pygame.Surface((SCREEN_WIDTH // DISPLAY_SCALE, SCREEN_HEIGHT // DISPLAY_SCALE))
        data_file_path = get_asset_path('particle_data.json')
        preset_file_path = get_asset_path('presets.json')
        self.particle_manager = ParticleManager(self.particle_surface, load_data(data_file_path), preset_file_path)
        self.screen_bleed_w = self.screen_bleed_h = 10

        self.sound_manager = SoundManager()
        
        self.init_menu()
        self.init_game()
        self.init_winner()
        
        self.sound_manager.play_background_music(volume=0.1)

    def init_menu(self):
        self.gui = GUI(self.screen)
        self.gui.set_sound_manager(self.sound_manager)

    def init_game(self):
        self.game = None
        self.flag = 1

    def init_winner(self):
        self.main_button = None
        self.quit_button = None

    def render_background(self):
        try:
            self.infinite_bg.update(self.screen.get_size())
            
            self.particle_surface.fill(pygame.Color('black'))
            self.particle_manager.render()
            
            self.infinite_bg.draw(self.screen, self.bg_offset_x, self.bg_offset_y)
            
            scaled_particle_surface = pygame.transform.scale(
                self.particle_surface, 
                (self.screen.get_width() + self.screen_bleed_w, self.screen.get_height() + self.screen_bleed_h)
            )
            self.infinite_bg.render_dynamic_surface(self.screen, scaled_particle_surface, self.bg_offset_x, self.bg_offset_y, pygame.BLEND_RGBA_ADD)
        except Exception:
            self.screen.fill((40, 40, 80))

    def handle_menu(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                return "quit"
        
        if self.gui.quit or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            return "quit"
        
        if self.gui.play:
            self.difficulty = self.gui.difficulty
            self.game = Game(self.screen)
            self.game.set_sound_manager(self.sound_manager)
            return "game"
        
        overlay = pygame.Surface((800, 450))
        overlay.set_alpha(150)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))
        
        self.gui.run()
        self.gui.draw()
        self.gui.update()
        return "menu"

    def handle_game(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = self.get_mouse_pos(pos)
                if row is not None and col is not None:
                    self.game.select(row, col)

        if self.game.turn == WHITE and self.flag:
            value, new_board = minimax(self.game.get_board(), self.difficulty, True, self.game)
            piece_row, piece_col, row, col = move_minimax(self.game.get_board(), new_board)
            
            # Check if we got valid coordinates
            if piece_row is not None and piece_col is not None and row is not None and col is not None:
                piece = self.game.get_board().get_piece(piece_row, piece_col)
                if piece != 0 and hasattr(piece, 'col'):  # Ensure it's a valid piece object
                    self.game.ai_move(piece, row, col)
        
        if self.game.winner():
            self.winner = self.game.winner()
            self.sound_manager.play_winning_sound()
            self.init_winner_buttons()
            return "winner"
        
        overlay = pygame.Surface((800, 450))
        overlay.set_alpha(120)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))
        
        self.game.update()
        return "game"

    def init_winner_buttons(self):
        self.main_button = Button(self.screen, (250, 350, 160, 50), state=1,
                                 color=GREENW, corner_radius=10, hover_color=GREENWW, disabled_color=GRAY,
                                 font=font_render('f_2', 30), font_values=("Play", 30, BLACK))
        self.quit_button = Button(self.screen, (550, 350, 160, 50),
                                 color=REDW, corner_radius=10, hover_color=REDWW, disabled_color=GRAY,
                                 font=font_render('f_2', 30), font_values=("Quit", 30, BLACK))

    def handle_winner(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                return "quit"
        
        if self.quit_button.get_action() or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            if self.quit_button.get_action():
                self.sound_manager.play_click_sound()
            return "quit"
        
        if self.main_button.get_action():
            self.sound_manager.play_click_sound()
            self.init_menu()
            return "menu"
        
        overlay = pygame.Surface((800, 450))
        overlay.set_alpha(180)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))
        
        pygame.font.init()
        try:
            t_1 = pygame.font.Font(get_asset_path("RETRO_SPACE_INV.ttf"), 60)
        except Exception:
            t_1 = pygame.font.Font(None, 60)
        t_1_txt = f'{self.winner} WON!'
        
        try:
            text_surface = t_1.render(t_1_txt, True, (255,255,255))
        except Exception:
            text_surface = t_1.render(t_1_txt, False, (255,255,255))
        text_width = text_surface.get_width()
        text_x = (SCREEN_WIDTH - text_width) // 2
        text_y = 150
        
        self.screen.blit(text_surface, (text_x, text_y))
        self.main_button.draw()
        self.quit_button.draw()
        
        return "winner"

    def get_mouse_pos(self, pos):
        x, y = pos
        x -= BOARD_X
        y -= BOARD_Y
        row = int(y // SQUARE_SIZE)
        col = int(x // SQUARE_SIZE)
        if row < 0 or row >= ROWS or col < 0 or col >= COLS:
            return None, None
        return row, col

    def run(self):
        while self.running:
            self.clock.tick(60)
            
            self.render_background()
            
            events = pygame.event.get()
            
            if self.state == "menu":
                self.state = self.handle_menu(events)
            elif self.state == "game":
                self.state = self.handle_game(events)
            elif self.state == "winner":
                self.state = self.handle_winner(events)
            elif self.state == "quit":
                self.running = False
            
            pygame.display.update()
