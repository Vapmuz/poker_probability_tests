import pygame

class GlobalGraphicsHelper:

    """this class can be used to simplify some complicated pygame functions: like displaying text"""

    def __init__(self):
        self.fonts = ["assets/fonts/casio-fx-9860gii.ttf"] #array to save various fonts

    def print_text(self, display, text, color, size, position):
        font = pygame.font.Font(self.fonts[0], size) # for now there's a default font, maybe can be customized in future.
        text_surface = font.render(text, True, color)
        display.blit(text_surface, position)