import sys 
import pygame
import os
import scoreboard #From Me importing Scoreboard.py file
import time

# this is from a Youtube (https://www.youtube.com/watch?v=CLFdN2I2Feg&list=PLr-iRXN7HiJgjrUT-6NE1sSnMzNEGQAH_)
# creating scrolling background
WIDTH = 623
HEIGHT = 150

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Dash")

font = pygame.font.Font(None, 14)

class BG:

    def __init__(self, x):
        self.width = WIDTH
        self.height = HEIGHT
        self.x = x
        self.y = 0
        self.set_texture()
        self.meters_moved = 0

    def update(self, dx):
        self.x += dx
        self.meters_moved += abs(dx)
        if self.x <= -WIDTH:
            self.x = WIDTH

    def show(self, screen):
        screen.blit(self.texture, (self.x, self.y))
        scoreboard.draw_score_counter(self.meters_moved, screen, font)

    def set_texture(self):
        path  =  os.path.join("..","stimuli","assets", "images", "bg.png")
        self.texture = pygame.image.load(path)
        self.texture = pygame.transform.scale(self.texture, (self.width, self.height))

class Game:

    def __init__(self):
        self.bg = [BG(x=0), BG(x=WIDTH) ]
        self.speed = 0.6
        


def main():

    game = Game()
    meters = 0 # From Me! Importing the scoreboard 
    clock = pygame.time.Clock() #This was from Pygame
    
    while True:

        for bg in game.bg:
            bg.update(-game.speed)
            bg.show()
            meters += 0.1 #From ME! Now count in meters
            time.sleep(1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        
        scoreboard.draw_score_counter(meters, screen, font) #From Me! Importing the scoreboard
        clock.tick(80) # From pygames
        pygame.display.update()

if __name__ == "__main__":  
    main()