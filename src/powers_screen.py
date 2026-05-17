import pygame 
import sys
import game

class Display(): 
    # setting screen size 
    screen_size = (800, 600)
    def __init__(self):
        pygame.init()
        self.screen_size_x = self.screen_size[0]
        self.screen_size_y = self.screen_size [1]
        # creating the canvas/display given the screen size
        self.canvas = pygame.display.set_mode(self.screen_size)
        # loading the background image and then scaling it to screen size 
        self.background_image = pygame.image.load("../stimuli/powers_screen.png")
        self.background_image = pygame.transform.scale(self.background_image, (self.screen_size))
        # sets the position of the start and quit buttons 
        self.start_button = pygame.Rect(80, 500, 200, 50)
        self.quit_button = pygame.Rect(520, 500, 200, 50)
        # captions what the screen is in this case the powers screen 
        pygame.display.set_caption("Powers Screen")
                
    def init_window(self):
        # creates the backround image
        self.canvas.blit(self.background_image, (0,0))

    def create_interface_buttons(self): 
        # creates 2 buttons a start and quit button 
        pygame.draw.rect(self.canvas, (0, 200, 0), self.start_button)
        pygame.draw.rect(self.canvas,(200, 0, 0), self.quit_button)
        # sets a font for the buttons 
        self.button_font = pygame.font.SysFont("Arial", 20, bold=True)
        # creates the text for the buttons, bolds it and makes the text white 
        start_text = self.button_font.render ("Start!", True, (255, 255, 255))
        quit_text = self.button_font.render ("Quit", True, (255, 255, 255))
        # finished creating th ebuttons visually, no function yet 
        self.canvas.blit (start_text, (self.start_button.x, self.start_button.y))
        self.canvas.blit(quit_text, (self.quit_button.x, self.quit_button.y))
    
    def go(self):
        running = True 
        # while running, the initalized window and create interface buttons def statements run first
        while running: 
            self.init_window()
            self.create_interface_buttons()
            pygame.display.update()
            for event in pygame.event.get(): 
                # if you quit the screen, everything exits/quits with your input 
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    sys.exit()  
                # if you press the start button, game.py runs beggining the game 
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    if self.start_button.collidepoint(event.pos):
                        game.main()
                    # if you press the provided quit button, you are exited out of the game 
                    if self.quit_button.collidepoint(event.pos): 
                        pygame.quit()
                        sys.exit()
            pygame.display.update

# main runs the class Display above
def main():
    my_display = Display()
    my_display.go()

#runs the main function above 
if __name__ == "__main__":
    main()