import pygame
import os
from asset_utils import get_asset_path

class SoundManager:
    def __init__(self):
        try:
            pygame.mixer.pre_init(frequency=22050, size=-16, channels=2, buffer=512)
            pygame.mixer.init()
        except pygame.error:
            pass
        
        self.background_music = None
        self.move_sound = None
        self.capture_sound = None
        self.winning_sound = None
        self.click_sound = None
        self.load_sounds()
    
    def load_sounds(self):
        try:
            bg_music_path = get_asset_path('background.mp3')
            if os.path.exists(bg_music_path):
                try:
                    pygame.mixer.music.load(bg_music_path)
                except pygame.error:
                    pass
            
            move_sound_path = get_asset_path('move.wav')
            if os.path.exists(move_sound_path):
                self.move_sound = pygame.mixer.Sound(move_sound_path)
            
            capture_sound_path = get_asset_path('capture.wav')
            if os.path.exists(capture_sound_path):
                self.capture_sound = pygame.mixer.Sound(capture_sound_path)
            
            winning_sound_path = get_asset_path('winning.wav')
            if os.path.exists(winning_sound_path):
                self.winning_sound = pygame.mixer.Sound(winning_sound_path)
            
            click_sound_path = get_asset_path('click.wav')
            if os.path.exists(click_sound_path):
                self.click_sound = pygame.mixer.Sound(click_sound_path)
                
        except pygame.error:
            pass
    
    def play_background_music(self, volume=0.3):
        try:
            pygame.mixer.music.set_volume(volume)
            pygame.mixer.music.play(-1)
        except pygame.error:
            pass
    
    def stop_background_music(self):
        pygame.mixer.music.stop()
    
    def play_move_sound(self, volume=0.8):
        if self.move_sound:
            self.move_sound.set_volume(volume)
            self.move_sound.play()
    
    def play_capture_sound(self, volume=0.7):
        if self.capture_sound:
            self.capture_sound.set_volume(volume)
            self.capture_sound.play()
    
    def play_winning_sound(self, volume=0.8):
        if self.winning_sound:
            self.winning_sound.set_volume(volume)
            self.winning_sound.play()
    
    def play_click_sound(self, volume=0.8):
        if self.click_sound:
            self.click_sound.set_volume(volume)
            self.click_sound.play()
    
    def fade_out_music(self, time_ms=1000):
        pygame.mixer.music.fadeout(time_ms)