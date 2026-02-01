import button
import pygame

class GraphicManager:
    def __init__(self, display):
        self.display = display
        self.current_state = 0
        self.center = (pygame.display.get_window_size()[0]/2, pygame.display.get_window_size()[1]/2) #get screen center for positioning use
        self.size = (pygame.display.get_window_size()[0], pygame.display.get_window_size()[1])

        self.buttons = [] #list of all buttons in the game
        self.active_buttons = [0, 1] # array that contains the active buttons to display

        """creating all buttons with attributes: (name, default_color, hover_colore, font, position, size, next_state, default_image, hover_image)"""
        """name, colors and font is in revision if it is usefull..."""

        self.buttons.append(button.Button(self.display, "singleplayer", (self.center[0]-200, self.center[1]), (400, 75), 1
                            , "assets/buttons/button_single_p.png", #default button image
                              "assets/buttons/button_single_p_hov.png")) #image when mouse is hovering on button
        self.buttons.append(button.Button(self.display, "exit", (self.center[0]-200, self.center[1]+85), (400, 75), -1
                            , "assets/buttons/button_quit.png",
                              "assets/buttons/button_quit_hov.png"))
        self.buttons.append(button.Button(self.display, "back to main menu", (self.center[0]-900, self.center[1]+350), (150, 75), 0
                            , "assets/buttons/button_back.png",
                              "assets/buttons/button_back_hov.png"))
        self.buttons.append(button.Button(self.display, "start game", (self.center[0]-200, self.center[1]), (400, 75), 2
                            , "assets/buttons/button_startgame.png",
                              "assets/buttons/button_startgame_hov.png"))
        self.buttons.append(button.Button(self.display, "quit game", (self.center[0]-900, self.center[1]+350), (150, 75), 0
                            , "assets/buttons/button_qcurgame.png",
                              "assets/buttons/button_qcurgame_hov.png"))

        self.bg_main = pygame.image.load("assets/bg_menu.png").convert()
        self.bg_single_p_set = pygame.image.load("assets/bg_menu.png").convert()
        self.bg_single_p_game = pygame.image.load("assets/bg_menu.png").convert()

    def update_graphic_state(self, display, mouse_pos): 

        """switches graphic state for every current_state value"""

        match self.current_state:
            case -1:
                self.quit_game()
            case 0:
                self.display_main_menu(display, mouse_pos)
            case 1:
                self.display_singleplayer_settings(display, mouse_pos)
            case 2:
                self.display_singleplayer(display, mouse_pos)
            case 3:
                self.display_exit(display, mouse_pos)

    def switch_state(self, state_id): 

        """switches the graphic  state to the next_state attribute of every button object"""

        self.current_state = state_id

    """every display methode sets the own backgroung, and sets the active buttons for the specific game state"""

    def display_main_menu(self, display, mouse_pos): 
        display.fill("blue") #blue screen if the system can't load the image correctly
        self.display_background(self.display, self.bg_main)
        self.active_buttons = [0, 1]
        self.display_buttons(self.active_buttons, display, mouse_pos)

    def display_singleplayer_settings(self, display, mouse_pos):
        display.fill("blue")
        self.display_background(self.display, self.bg_single_p_set)
        self.active_buttons = [2, 3]
        self.display_buttons(self.active_buttons, display, mouse_pos)

    def display_singleplayer(self, display, mouse_pos):
        display.fill("blue")
        self.display_background(self.display, self.bg_single_p_game)
        self.active_buttons = [4]
        self.display_buttons(self.active_buttons, display, mouse_pos)

    def display_buttons(self, active_buttons, display, mouse_pos): # displays only the active butttons
        for i in active_buttons:
            self.buttons[i].update(display, mouse_pos)

    def display_background(self, display, file): 

        """displays the loaded image for every background"""

        display.blit(pygame.transform.scale(file, self.size), file.get_rect())

    def quit_game(self): # quits the graphics and the game
        pygame.quit()
    