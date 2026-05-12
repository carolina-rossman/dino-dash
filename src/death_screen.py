import pygame
import pygame.freetype
import sys


class Display:
    screen_size = (800, 600)

    def __init__(self, screen):
        pygame.init()
        font = pygame.freetype.SysFont("Arial", 65)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill((255, 255, 255))
            text_surface, rect = font.render("You Died", (0, 0, 0))
            screen.blit(text_surface, (40, 250))
            # font.render_to(screen, (40, 350), "You Died", (0, 0, 0))

            pygame.display.flip()

        pygame.quit()


def main():
    pygame.init()
    screen = pygame.display.set_mode(Display.screen_size)
    Display(screen)


if __name__ == "__main__":
    main()
