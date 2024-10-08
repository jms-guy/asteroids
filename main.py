import pygame
import random 
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import * 

def main():
    #Game screen initialization
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    #Container groups for classes
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    x1 = SCREEN_WIDTH / 2
    y1 = SCREEN_HEIGHT / 2
    player = Player(x1, y1, PLAYER_RADIUS)

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for obj in updatable:
            if obj == player:
                obj.shoot_timer -= (dt)
                if obj.shoot_timer < 0:
                    obj.shoot_timer = 0
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.is_colliding(player):
                print("Game over!")
                return
            for shot in shots:
                if asteroid.is_colliding(shot):
                    asteroid.split()
                    shot.kill() 

        pygame.Surface.fill(screen, "black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        clock.tick(60)
        dt = (clock.tick(60)) / 1000


if __name__ == "__main__":
    main()