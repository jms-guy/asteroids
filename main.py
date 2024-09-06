import pygame
from constants import *
from circleshape import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    x1 = SCREEN_WIDTH / 2
    y1 = SCREEN_HEIGHT / 2
    player = Player(x1, y1, PLAYER_RADIUS)

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0,0,0))
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()
        clock.tick(60)
        dt = (clock.tick(60)) / 1000


if __name__ == "__main__":
    main()