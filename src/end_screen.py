import pygame
import pygame.freetype
import sys
import game


class Display:
    def __init__(self):
        pygame.init()
        pygame.freetype.init()
        self.window = pygame.display.set_mode((800, 600))
        self.font = pygame.freetype.SysFont("Arial", 65, bold=True)
        self.background = pygame.Surface(self.window.get_size())
        self.blue = [100, 149, 237]
        self.background.fill(self.blue)
        self.restart_button = pygame.Rect(80, 500, 200, 50)
        self.quit_button = pygame.Rect(520, 500, 200, 50)
        self.window.blit(self.background, (0, 0))
        text_one, rect = self.font.render("Congrats!")
        text_two, rect = self.font.render("You Escaped Jurassic Park!")
        self.window.blit(text_one, (250, 200))
        self.window.blit(text_two, (50, 300))
        pygame.display.flip()

    def create_buttons(self):
        pygame.draw.rect(self.window, (0, 200, 0), self.restart_button)
        pygame.draw.rect(self.window, (200, 0, 0), self.quit_button)
        self.button_font = pygame.font.SysFont("Arial", 20, bold=True)
        restart_text = self.button_font.render("Play Again", True, (255, 255, 255))
        quit_text = self.button_font.render("Quit", True, (255, 255, 255))
        self.window.blit(restart_text, (self.restart_button.x, self.restart_button.y))
        self.window.blit(quit_text, (self.quit_button.x, self.quit_button.y))

    def restart(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            self.__init__
            self.create_buttons()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("Restart!")
                    if self.restart_button.collidepoint(event.pos):
                        new_screen = game.main()
                        new_screen.restart
                    if self.quit_button.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
            pygame.display.update()
            clock.tick(120)


def main():
    my_display = Display()
    my_display.restart()


if __name__ == "__main__":
    main()
