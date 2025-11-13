import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen size: {SCREEN_WIDTH}x{SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        pygame.display.flip()


if __name__ == "__main__":
    main()
