import pygame
import pygame.freetype
import sys
import game


class Display:
    def __init__(self):
        pygame.init()
        pygame.freetype.init()
        # setting screen size and creating the window
        self.window = pygame.display.set_mode((800, 600))
        self.font = pygame.freetype.SysFont("Arial", 65, bold=True)
        self.background = pygame.Surface(self.window.get_size())
        # background color
        self.blue = [100, 149, 237]
        self.background.fill(self.blue)
        # setting the position of the buttons
        self.play_again_button = pygame.Rect(80, 500, 200, 50)
        self.quit_button = pygame.Rect(520, 500, 200, 50)
        self.window.blit(self.background, (0, 0))
        # creating the text and setting its position
        text_one, rect = self.font.render("Congrats!")
        text_two, rect = self.font.render("You Escaped Jurassic Park!")
        self.window.blit(text_one, (250, 200))
        self.window.blit(text_two, (50, 300))
        pygame.display.flip()

    def create_buttons(self):
        # creates the buttons
        pygame.draw.rect(self.window, (0, 200, 0), self.play_again_button)
        pygame.draw.rect(self.window, (200, 0, 0), self.quit_button)
        self.button_font = pygame.font.SysFont("Arial", 20, bold=True)
        play_again_text = self.button_font.render("Play Again", True, (255, 255, 255))
        quit_text = self.button_font.render("Quit", True, (255, 255, 255))
        self.window.blit(
            play_again_text, (self.play_again_button.x, self.play_again_button.y)
        )
        self.window.blit(quit_text, (self.quit_button.x, self.quit_button.y))

    def play_again(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            self.__init__
            self.create_buttons()
            pygame.display.update()
            for event in pygame.event.get():
                # when you quit the screen, everything else quits too
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # when you press the play again button with your mouse you are taken back the the beginning of game.py
                    if self.play_again_button.collidepoint(event.pos):
                        print("Play Again!")
                        new_screen = game.main()
                        new_screen.play_again
                    # when you press the quit button with your mouse, everything else quits too
                    if self.quit_button.collidepoint(event.pos):
                        print("Quit")
                        pygame.quit()
                        sys.exit()
            pygame.display.update()
            clock.tick(120)


def main():
    my_display = Display()
    my_display.play_again()


if __name__ == "__main__":
    main()
