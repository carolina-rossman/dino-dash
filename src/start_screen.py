import pygame 
import pygame.freetype
from pygame.sprite import Sprite 
from pygame.rect import Rect 
import instructions_screen
import sys

class Display(): 
    screen_size = (800, 600)
    def __init__(self):
        pygame.init()
        self.screen_size_x = self.screen_size[0]
        self.screen_size_y = self.screen_size [1]
        self.canvas = pygame.display.set_mode(self.screen_size)
        self.background_image = pygame.image.load("../stimuli/start_screen_background.png")
        self.background_image = pygame.transform.scale(self.background_image, (self.screen_size))
        self.start_button = pygame.Rect(300, 250, 200, 50)
        self.quit_button = pygame.Rect(300, 350, 200, 50)
        pygame.display.set_caption("Start Screen")

    def init_window(self):
        self.canvas.blit(self.background_image, (0,0))
        self.title_font = pygame.font.SysFont("Arial", 65, bold = True)
        title = self.title_font.render("Dino Dash", True, (255, 255, 255))
        title_rect = title.get_rect(center = (self.screen_size_x/2, 100))
        self.canvas.blit(title, title_rect)


    def create_interface_buttons(self):
        pygame.draw.rect(self.canvas, (0, 200, 0), self.start_button)
        pygame.draw.rect(self.canvas,(200, 0, 0), self.quit_button)
        self.button_font = pygame.font.SysFont("Arial", 20, bold=True)
        start_text = self.button_font.render ("Start!", True, (255, 255, 255))
        quit_text = self.button_font.render ("Quit", True, (255, 255, 255))
        self.canvas.blit (start_text, (self.start_button.x, self.start_button.y))
        self.canvas.blit(quit_text, (self.quit_button.x, self.quit_button.y))

    def go(self):
        clock = pygame.time.Clock()
        running = True 
        while running: 
            self.init_window()
            self.create_interface_buttons()
            pygame.display.update()
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    sys.exit()   
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    new_screen = instructions_screen.Display()
                    new_screen.go()
                    if self.start_button.collidepoint(event.pos):
                        instructions_screen.Display.go()
                    if self.quit_button.collidepoint(event.pos): 
                        pygame.quit()
                        sys.exit()
            pygame.display.update
            clock.tick(120)

def main(): 
    my_display = Display()
    my_display.go()

if __name__ == "__main__":
    main()