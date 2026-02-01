import pygame

class Button:
    def __init__(self, display, text, position, size, next_state, default_image_path, hover_image_path):
               
        self.display = display

        self.text = text
        self.position = position
        self.size = size
        self.is_hover_on = False
        self.next_state = next_state

        self.default_img = pygame.image.load(default_image_path)
        self.hover_img = pygame.image.load(hover_image_path)
        self.current_button_img = self.default_img
        self.rect = (self.position[0], self.position[1], self.size[0], self.size[0])

    def update(self, display, mouse_pos): #updates the button graphics and 
        display.blit(self.current_button_img, self.rect)
        self.hover_on(mouse_pos)

    def pressed(self, mouse_p): 
        """checks if button is pressed, methode is called from main loop and uses self.hover_on for checking the mouse position"""
        if self.hover_on(mouse_p):
            return True

    def hover_on(self, m_position): 
        """checks if the mouse position is in the button surface, depending if it is or isnt, it changes the current image that is displayed"""
        if (m_position[0] in range(int(self.position[0]), int(self.position[0]+self.size[0])) and m_position[1] in range(int(self.position[1]), int(self.position[1]+self.size[1]))):
            self.current_button_img = self.hover_img
            return True
        else:
            self.current_button_img = self.default_img