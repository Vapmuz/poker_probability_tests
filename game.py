import sys
import pygame
import graphic_manager
from graphic_helper import GlobalGraphicsHelper

pygame.init()

class Game:
    def __init__(self, version):
        self.version = version
        self.display = pygame.display.set_mode((1920, 1080))
        self.graphic_manager = graphic_manager.GraphicManager(self.display)
        self.graphic_helper = GlobalGraphicsHelper()
        self.run()

    def run(self):

        """Main game loop that checks for all mouse and keyboard event"""

        pygame.display.init()
        running = True
        while running:
            self.mouse_pos = pygame.mouse.get_pos()
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                    self.quit_game()
                if event.type == pygame.MOUSEBUTTONUP:
                    self.mouse_pos = pygame.mouse.get_pos()
                    self.pressed_buttons(self.mouse_pos)
            self.update()

    def update(self):

        """update method that calls graphic_manager for displaying background and buttons, displays text"""

        self.graphic_manager.update_graphic_state(self.display, self.mouse_pos)
        self.graphic_helper.print_text(self.display, self.version, "white", 26, (20, 20)) #displays game version at corner
        pygame.display.update()

    def pressed_buttons(self, mouse_p):

        """this method interacts between the input events and the graphic manager, giving it the state that it has to display"""

        for i in self.graphic_manager.active_buttons:
            if self.graphic_manager.buttons[i].pressed(mouse_p):
                self.graphic_manager.switch_state(self.graphic_manager.buttons[i].next_state)
                
    def quit_game(self):
        """quits the game"""
        pygame.quit()
        sys.exit()

game = Game("pre-alpha v.0.1.0")
