import pygame
from .textures import import_bg

class InfiniteBackground:
    def __init__(self, scroll_speed=0.1):
        self.scroll = 0  # Matching Graphics SCROLL = 0
        self.base_scroll_vx = scroll_speed  # Store base speed (Graphics SCROLL_VX = 0.1)
        self.scroll_vx = scroll_speed  # Current speed (will be updated each frame)
        self.screen_bleed_w = 10  # Matching Graphics values
        self.screen_bleed_h = 10
        self.original_size = (800, 450)  # Base screen size for factor calculation

    def update(self, window_size):
        # Calculate screen factor exactly like Graphics does
        screen_factor_x = window_size[0] / self.original_size[0]
        # Update scroll_vx each frame with screen factor (matching Graphics implementation)
        self.scroll_vx = self.base_scroll_vx * screen_factor_x

    def render_dynamic_surface(self, window, surface, offset_x=0, offset_y=0, special_flags=0):
        start = 0
        width = surface.get_width()
        if self.scroll >= 0:
            self.scroll = 0 if self.scroll >= width else self.scroll
        elif self.scroll < 0:
            self.scroll = 0 if self.scroll <= -width else self.scroll
        self.scroll = self.scroll + self.scroll_vx
        
        first_image_x = start + self.scroll + offset_x
        second_image_x = start + self.scroll + (width * (1 if self.scroll_vx <= 0 else -1)) + offset_x
        window.blit(surface, (first_image_x, offset_y), special_flags=special_flags)
        window.blit(surface, (second_image_x, offset_y), special_flags=special_flags)

    def draw(self, window, offset_x=0, offset_y=0):
        # Get window size and create background surface
        width, height = window.get_size()
        bg_surface = import_bg(width, height, (self.screen_bleed_w, self.screen_bleed_h))
        self.render_dynamic_surface(window, bg_surface, offset_x, offset_y)
