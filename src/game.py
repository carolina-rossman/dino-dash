# code is based on this youtube video: https://www.youtube.com/watch?v=6zRqd-gyO4c
import random
import pygame
import base_dino
import scrolling_background

screen_width = 800
screen_height = 150 

class PowerUps:
    def __init__(self, screen_width, screen_height):
        #loading images for powerups 
        self.jetpack = pygame.transform.scale(pygame.image.load("../stimuli/jetpack_token.png"), (50, 70))
        self.immunity = pygame.transform.scale(pygame.image.load("../stimuli/shield_token.png"), (50, 70))
        self.revival = pygame.transform.scale(pygame.image.load("../stimuli/life_token.png"), (50, 70))
        self.nothing = pygame.transform.scale(pygame.image.load("../stimuli/white_screen.png"), (1, 1))
        #selecting random image 
        self.powerups_list = [self.jetpack, self.immunity, self.revival, self.nothing,self.nothing,self.nothing,self.nothing,self.nothing,self.nothing,self.nothing,self.nothing,self.nothing, self.nothing]
        # to increase number of jetpacks likelihood to spawn, just add more self.jetpack above 
        self.image = random.choice(self.powerups_list)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.screen_width = screen_width
        self.screen_height = screen_height 
        self.rect.x = screen_width + random.randint(100,300)
        self.rect.y = 45
        self.speed = 5
        #speed of power-up, as it passes
    
    def move(self):
        self.rect.x -= self.speed 
        if self.rect.right < 0: 
            self.rect.x = self.screen_width + random.randint(100, 500)
            self.image = random.choice(self.powerups_list)
            self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
            return True
        return False  
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def jetpack(self):
        pass
    def immunity(self): 
        pass 

    def revival(self):
        pass
        #look at code for shield power-up)

class PowerDowns:
    def __init__(self, screen_width, screen_height):
        self.speed_up = pygame.transform.scale(pygame.image.load("../stimuli/double_time_token.png"), (50, 70))
        self.tiny_dino = pygame.transform.scale(pygame.image.load("../stimuli/tiny_dino_token.png"), (50, 70))
        self.nothing = pygame.transform.scale(pygame.image.load("../stimuli/white_screen.png"), (1, 1))
        self.powerdowns_list = [self.speed_up, self.tiny_dino, self.nothing, self.nothing, self.nothing, self.nothing, self.nothing, self.nothing, self.nothing]
        self.image = random.choice(self.powerdowns_list)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.screen_width = screen_width
        self.screen_height = screen_height 
        self.rect.x = screen_width + random.randint(100,300)
        self.rect.y = 45
        self.speed = 5
    def move(self): 
        self.rect.x -= self.speed 
        if self.rect.right < 0: 
            self.rect.x = self.screen_width + random.randint(100, 500)
            self.image = random.choice(self.powerdowns_list)
            self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
            return True
        return False  
    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Obstacles:
    def create_obstacles(self): 
        self.fence = pygame.image.load("../stimuli/fence.png")
        self.bush = pygame.image.load("../stimuli/bush.png")
        self.selected_obstacles = random.choice (self.bush, self.fence)
        # generate those images as background scrolls 
        # use pygame


def main(): 
     pygame.init()
     screen = pygame.display.set_mode((screen_width, screen_height))
     clock = pygame.time.Clock()
     x_pos, y_pos = 100, 95
     jumping = False 
     y_gravity = 0.5
     jump_height = 8 
     y_vel = jump_height
     standing_surface = pygame.transform.scale(pygame.image.load("../stimuli/dino.png"), (25, 35))
     jumping_surface = pygame.transform.scale(pygame.image.load("../stimuli/jumping_dino.png"), (25, 35))
     background = scrolling_background.Game()
     spawned_powerups = [PowerUps(screen_width, screen_height) for _ in range(1)]
     spawned_powerdown = [PowerDowns(screen_width, screen_height) for _ in range(1)]
     running = True 
     while running: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_SPACE]: 
            jumping = True
        for bg in background.bg: 
            bg.update(-background.speed)
        for power in spawned_powerups: 
            power.move()
        for power in spawned_powerdown:
            power.move()
        if jumping: 
            y_pos -= y_vel
            y_vel -= y_gravity
            if y_vel < -jump_height:
                jumping = False
                y_vel = jump_height
        for bg in background.bg:
            bg.show(screen)
        for power in spawned_powerups: 
            power.draw(screen)
        for power in spawned_powerdown: 
            power.draw(screen)
        dino_rect = standing_surface.get_rect(center =(x_pos, y_pos))
        if jumping: 
            screen.blit(jumping_surface, dino_rect)
        else: 
            screen.blit(standing_surface, dino_rect)
        pygame.display.flip()
        clock.tick(60)
     pygame.quit()


if __name__ == "__main__":
    main()