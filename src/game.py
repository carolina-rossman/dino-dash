# code is based on this youtube video: https://www.youtube.com/watch?v=6zRqd-gyO4c
import random
import pygame
import scrolling_background
import death_screen

screen_width = 800
screen_height = 150


class Powers:
    def __init__(self, screen_width, screen_height):
        # loading images for powerups
        self.jetpack = pygame.transform.scale(
            pygame.image.load("../stimuli/jetpack_token.png"), (30, 30)
        )
        self.immunity = pygame.transform.scale(
            pygame.image.load("../stimuli/shield_token.png"), (30, 30)
        )
        self.nothing = pygame.transform.scale(
            pygame.image.load("../stimuli/white_screen.png"), (1, 1)
        )
        self.speed_up = pygame.transform.scale(
            pygame.image.load("../stimuli/double_time_token.png"), (30, 30)
        )
        self.tiny_dino = pygame.transform.scale(
            pygame.image.load("../stimuli/tiny_dino_token.png"), (30, 30)
        )
        # loads all powerups and powerdown in a list and selects a random power up/power down, or nothing/free pass of no power-up or power-down
        self.all_powers = [
            self.jetpack,
            self.immunity,
            self.speed_up,
            self.tiny_dino,
            self.nothing,
            self.nothing,
            self.nothing,
        ]
        self.image = random.choice(self.all_powers)
        # registers outline of the image, so we can code a function as the dino passes through a power
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        # setting up screen size
        self.screen_width = screen_width
        self.screen_height = screen_height
        # powers spawn, at random x position, set y position, and go across the screen at a set speed
        self.rect.x = screen_width + random.randint(100, 300)
        self.rect.y = 85
        self.speed = 5

    def move(self, blocked):
        # Moves the power to the left
        self.rect.x -= self.speed
        # checks to see if the power is off the screen, to the left
        if self.rect.right < 0:
            # if another power is active, the image will always be nothing
            if blocked:
                self.image = self.nothing
            # if not then the image is randomly picked from the all_powers list
            else:
                self.image = random.choice(self.all_powers)
            # recalculating the hitbox, added to avoid bugs that were occuring
            self.rect = self.image.get_rect()
            # generates the collision mask for the image
            self.mask = pygame.mask.from_surface(self.image)
            # Spawns and respawns the image/power to the right of the screen randomly between (100 and 500) pixels
            self.rect.x = self.screen_width + random.randint(100, 500)
            # the height of the image is 85, so it's on the ground
            self.rect.y = 85
            # items succesfully spawned as if off the screen
            return True
        # item is still on the screen
        return False

    def draw(self, screen):
        # draw the power image in the game given it's position
        screen.blit(self.image, self.rect)


class Obstacles:
    def __init__(self, screen_width, screen_height, spawn_range, obstacle_type=None):
        # obstacle images loaded in
        self.fence = pygame.transform.scale(
            pygame.image.load("../stimuli/fence.png"), (30, 30)
        )
        self.bush = pygame.transform.scale(
            pygame.image.load("../stimuli/bush.png"), (30, 30)
        )
        self.obstacle_list = [self.bush, self.fence]
        self.obstacle_type = obstacle_type
        self.obstacle_type = obstacle_type
        if self.obstacle_type is not None:
            self.image = self.obstacle_list[self.obstacle_type]
        else:
            self.image = random.choice(self.obstacle_list)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.spawn_range = spawn_range
        self.rect.x = screen_width + random.randint(spawn_range[0], spawn_range[1])
        self.rect.y = 85
        self.speed = 5
        # speed of obstacle as it goes across the screen

    def move(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.rect.x = self.screen_width + random.randint(
                self.spawn_range[0], self.spawn_range[1]
            )
            if self.obstacle_type is not None:
                self.image = self.obstacle_list[self.obstacle_type]
            else:
                # selects an image at random from obstacles list
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
    # setting x_position, y_position for dino, and used for other things as well
    x_pos = 100
    ground = 95
    y_pos = ground
    # importing variables so the dino jumps, and so it can be manipulated in the effect of powerups and powerdowns
    # all dino movement code is based from this YouTube Video https://www.youtube.com/watch?v=ST-Qq3WBZBE
    jumping = False
    y_gravity = 0.5
    jump_height = 8
    y_vel = jump_height
    # imporing all stimuli for powerups and powerdowns, and setting variables so they can easily be manipulated
    standing_dino = pygame.transform.scale(
        pygame.image.load("../stimuli/dino.png"), (25, 35)
    )
    normal_dino = standing_dino
    jumping_surface = pygame.transform.scale(
        pygame.image.load("../stimuli/jumping_dino.png"), (25, 35)
    )
    jumping_dino = jumping_surface
    jetpack_dino = pygame.transform.scale(
        pygame.image.load("../stimuli/jetpack_dino.png"), (25, 35)
    )
    immunity_dino = pygame.transform.scale(
        pygame.image.load("../stimuli/shield_dino.png"), (25, 35)
    )
    tiny_dino = pygame.transform.scale(
        pygame.image.load("../stimuli/tiny_dino.png"), (20, 30)
    )
    tiny_dino_jumping = pygame.transform.scale(
        pygame.image.load("../stimuli/tiny_dino.png"), (20, 30)
    )
    # runs scrolling_background.py as the background for the game
    background = scrolling_background.Game()
    normal_speed = background.speed
    game_progression = (
        1.0  # this tracks the game speed and progesses the game time overtime
    )
    acceleration_rate = 0.003
    # selects 1 powers and 2 obstacles and spawns them in
    spawned_powers = [Powers(screen_width, screen_height) for _ in range(1)]
    #  spawned_obstacles = [Obstacles(screen_width, screen_height) for _ in range(2)]
    spawned_obstacles = [
        Obstacles(screen_width, screen_height, (100, 250), obstacle_type=0),
        Obstacles(screen_width, screen_height, (400, 550), obstacle_type=1),
    ]
    # setting variables to manipulate for powerups and powerdowns
    running = True
    god_mode = False
    jetpack_active = False
    jetpack_time = 0
    immunity_active = False
    immunity_time = 0
    speedup_active = False
    speedup_time = 0
    tinydino_active = False
    tinydino_time = 0
    any_active_powerup_powerdown = False
    # allowing you to quit the game, and enter god mode if press the 0 key
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    god_mode = True
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_SPACE]:
            if not jetpack_active:
                jumping = True
        # counts down the time of the powerup/power down being active and when the time is out undos the effect from the various powerups/powerdowns
        if jetpack_active:
            # counts time down
            jetpack_time -= 1
            if jetpack_time <= 0:
                jetpack_active = False
                normal_dino = standing_dino
                # reactivates jumping logic so dino goes down slowly like when jumping instead of instant
                jumping = True
                y_vel = 0
        if immunity_active:
            immunity_time -= 1
            if immunity_time <= 0:
                immunity_active = False
                normal_dino = standing_dino
                jumping_dino = jumping_surface
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
        # gets a variable to check if any powerup/powerdown is active, to prevent one from spawning while another is active
        any_active_powerup_powerdown = (
            jetpack_time > 0
            or immunity_time > 0
            or speedup_time > 0
            or tinydino_time > 0
        )
        if not speedup_active:
            game_progression += acceleration_rate
            normal_speed = 0.6 * game_progression
            background.speed = normal_speed
        for bg in background.bg:
            bg.update(-background.speed)
        if jumping:
            dino_rect = jumping_dino.get_rect(center=(x_pos, y_pos))
        else:
            dino_rect = normal_dino.get_rect(center=(x_pos, y_pos))
        for power in spawned_powers:
            power.move(any_active_powerup_powerdown)
            # checks to make sure the image isn't power.nothing, so that remains having no effect
            if power.image != power.nothing:
                # if the dino collides with the powerup/powerdown then the following code takes effect
                if dino_rect.colliderect(power.rect):
                    # check what power is ran into, and then causes the power's effect through variable manipulation
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
                    elif power.image == power.speed_up:
                        speedup_active = True
                        speedup_time = 500
                        background.speed = normal_speed * 2
                 # when dino reaches 2x icon the background will speed up.
                    elif power.image == power.tiny_dino:
                        tinydino_active = True
                        tinydino_time = 500
                        normal_dino = tiny_dino
                        jumping_dino = tiny_dino_jumping
                        ground = 100
                        if not jumping:
                            y_pos = ground
                    # if the dino runs into a power, it send the power off the screen so it gives the effect of being activated
                    power.rect.x = -100
        # makes the dino jump, logic based on YouTube Video https://www.youtube.com/watch?v=ST-Qq3WBZBE
        if jumping:
            y_pos -= y_vel
            y_vel -= y_gravity
            # checks to make sure the dino returns to the ground, done so to fix bugs from jetpack and tiny dino powers
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
                # checks to see if god_mode is active, and if it is makes the dino immune by passing this function
                if god_mode:
                    pass
                # check to see if immunity powerup is active, and if it is makes the dino immune by passing this function
                elif immunity_active:
                    pass
                # if dino isn't in god_mode or the imunity powerup isn't active then if the obstacle is hit the death.screen.py runs
                else:
                    death_screen.main()
                    return
        for bg in background.bg:
            bg.show(screen)
        for power in spawned_powers:
            power.draw(screen)
        for obstacle in spawned_obstacles:
            obstacle.draw(screen)
        dino_rect = normal_dino.get_rect(center=(x_pos, y_pos))
        if jumping:
            dino_rect = jumping_dino.get_rect(center=(x_pos, y_pos))
            screen.blit(jumping_dino, dino_rect)
        else:
            dino_rect = normal_dino.get_rect(center=(x_pos, y_pos))
            screen.blit(normal_dino, dino_rect)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


# runs main
if __name__ == "__main__":
    main()
