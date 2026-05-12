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
        self.powerups_list = [self.jetpack, self.immunity, self.revival, self.nothing,self.nothing,self.nothing,self.nothing]
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
    
    def move(self, blocked):
        self.rect.x -= self.speed 
        if self.rect.right < 0: 
            if blocked:
                self.image = self.nothing
            else: 
                self.image = random.choice(self.powerups_list)
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)
            self.rect.x = self.screen_width + random.randint(100, 500)
            self.rect.y = 45
            return True
        return False  
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
class PowerDowns:
    def __init__(self, screen_width, screen_height):
        self.speed_up = pygame.transform.scale(pygame.image.load("../stimuli/double_time_token.png"), (50, 70))
        self.tiny_dino = pygame.transform.scale(pygame.image.load("../stimuli/tiny_dino_token.png"), (50, 70))
        self.nothing = pygame.transform.scale(pygame.image.load("../stimuli/white_screen.png"), (1, 1))
        self.powerdowns_list = [self.speed_up, self.tiny_dino,self.nothing, self.nothing, self.nothing]
        self.image = random.choice(self.powerdowns_list)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.screen_width = screen_width
        self.screen_height = screen_height 
        self.rect.x = screen_width + random.randint(100,300)
        self.rect.y = 45
        self.speed = 5
    def move(self, blocked): 
        self.rect.x -= self.speed 
        if self.rect.right < 0: 
            if blocked: 
                self.image = self.nothing 
            else: 
                self.image = random.choice(self.powerdowns_list)
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)
            self.rect.x = self.screen_width + random.randint(100, 500)
            self.rect.y = 45
            return True
        return False  
    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Obstacles:
    def __init__(self, screen_width, screen_height):
        #obstacle images loaded in
        self.fence = pygame.transform.scale(pygame.image.load("../stimuli/fence.png"), (50, 50))
        self.bush = pygame.transform.scale(pygame.image.load("../stimuli/bush.png"), (50, 70))
        self.obstacle_list = [self.bush, self.fence]
        self.image = random.choice(self.obstacle_list)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.rect.x = screen_width + random.randint(100,300)
        self.rect.y = 45
        self.speed = 5
        #speed of obstacle as it goes across the screen

    def move(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.rect.x = self.screen_width + random.randint(100, 500)
            self.image = random.choice(self.obstacle_list)
            self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
            return True
        return False
    def draw(self, screen):
        screen.blit(self.image, self.rect)


def main(): 
     pygame.init()
     screen = pygame.display.set_mode((screen_width, screen_height))
     clock = pygame.time.Clock()
     x_pos = 100
     ground = 95 
     y_pos = ground 
     jumping = False 
     y_gravity = 0.5
     jump_height = 8 
     y_vel = jump_height
     standing_dino = pygame.transform.scale(pygame.image.load("../stimuli/dino.png"), (25, 35))
     normal_dino = standing_dino
     jumping_surface = pygame.transform.scale(pygame.image.load("../stimuli/jumping_dino.png"), (25, 35))
     jumping_dino = jumping_surface
     jetpack_dino = pygame.transform.scale(pygame.image.load("../stimuli/jetpack_dino.png"), (25, 35))
     immunity_dino = pygame.transform.scale(pygame.image.load("../stimuli/shield_dino.png"), (25, 35))
     tiny_dino = pygame.transform.scale(pygame.image.load("../stimuli/tiny_dino.png"), (20, 30))
     tiny_dino_jumping = pygame.transform.scale(pygame.image.load("../stimuli/tiny_dino.png"), (20, 30))
     background = scrolling_background.Game()
     normal_speed = background.speed
     spawned_powerups = [PowerUps(screen_width, screen_height) for _ in range(1)]
     spawned_powerdown = [PowerDowns(screen_width, screen_height) for _ in range(1)]
     spawned_obstacles = [Obstacles(screen_width, screen_height) for _ in range(2)]
     running = True 
     jetpack_active = False 
     jetpack_time = 0 
     immunity_active = False 
     immunity_time = 0 
     revival_active = False 
     revival_time = 0 
     speedup_active = False 
     speedup_time = 0 
     tinydino_active = False 
     tinydino_time = 0 
     any_active_powerup_powerdown = False 
     while running: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_SPACE]: 
            if not jetpack_active:
                jumping = True
        if jetpack_active:
            jetpack_time -= 1
            if jetpack_time <= 0:
                jetpack_active = False
                normal_dino = standing_dino
                y_pos = 95
        if immunity_active: 
            immunity_time -= 1
            if immunity_time <= 0: 
                immunity_active = False 
                normal_dino = standing_dino
                #revert other changes 
        if revival_active: 
            revival_time -= 1
            if revival_time <= 0: 
                revival_active = False 
                normal_dino = standing_dino
        if speedup_active:
            speedup_time -= 1
            if speedup_time <= 0:
                speedup_active = False 
                normal_dino = standing_dino
                background.speed = normal_speed
        if tinydino_active:
            tinydino_time -= 1
            if tinydino_time <= 0:
                tinydino_active = False 
                normal_dino = standing_dino
                jumping_dino = jumping_surface
                ground = 95
                if not jumping: 
                    y_pos = ground 
        dino_rect = normal_dino.get_rect(center=(x_pos, y_pos))
        any_active_powerup_powerdown = (jetpack_time > 0 or  
                                        immunity_time > 0 or 
                                        revival_time > 0 or 
                                        speedup_time > 0 or 
                                        tinydino_time > 0)
        for bg in background.bg: 
            bg.update(-background.speed)
        if jumping: 
            dino_rect = jumping_dino.get_rect(center = (x_pos, y_pos))
        else: 
            dino_rect = normal_dino.get_rect (center = (x_pos, y_pos))
        for power in spawned_powerups: 
            power.move(any_active_powerup_powerdown)
            if not any_active_powerup_powerdown and power.image != power.nothing: 
                if dino_rect.colliderect(power.rect):
                    if power.image == power.jetpack:
                        jetpack_active = True
                        jetpack_time = 500
                        normal_dino = jetpack_dino
                        y_pos = 30 
                        jumping = False 
                        y_vel = jump_height
                    elif power.image == power.immunity:
                        immunity_active = True 
                        immunity_time = 500
                        normal_dino = immunity_dino
                        jumping_dino = immunity_dino
                    #can't die, use obstacles death variable once created
                    else:
                        revival_active = True 
                        revival_time = 500
                    #cause a reaction, revival 
                    power.rect.x = -100
        for power in spawned_powerdown:
            power.move(any_active_powerup_powerdown)
            if not any_active_powerup_powerdown and power.image != power.nothing:
                if dino_rect.colliderect(power.rect):
                    if power.image == power.speed_up:
                        speedup_active = True 
                        speedup_time = 500
                        background.speed = normal_speed * 5
            #cause a reaction
                    elif power.image == power.tiny_dino:
                        tinydino_active = True 
                        tinydino_time = 500
                        normal_dino = tiny_dino
                        jumping_dino = tiny_dino_jumping
                        ground = 100
                        if not jumping: 
                            y_pos = ground 
            #cause a reaction
                        power.rect.x = -100
        if jumping: 
            y_pos -= y_vel
            y_vel -= y_gravity
            if y_pos >= ground:
                y_pos = ground 
                jumping = False 
                y_vel = jump_height
            if y_vel < -jump_height:
                jumping = False
                y_vel = jump_height
        for obstacle in spawned_obstacles:
            obstacle.move()
            if dino_rect.colliderect(obstacle.rect):
                pass
        for bg in background.bg:
            bg.show(screen)
        for power in spawned_powerups: 
            power.draw(screen)
        for power in spawned_powerdown: 
            power.draw(screen)
        for obstacle in spawned_obstacles:
            obstacle.draw(screen)
        dino_rect = normal_dino.get_rect(center =(x_pos, y_pos))
        if jumping: 
            dino_rect = jumping_dino.get_rect(center = (x_pos, y_pos))
            screen.blit(jumping_dino, dino_rect)
        else: 
            dino_rect = normal_dino.get_rect(center = (x_pos, y_pos))
            screen.blit(normal_dino, dino_rect)
        pygame.display.flip()
        clock.tick(60)
     pygame.quit()


if __name__ == "__main__":
    main()