import pygame
import sys
from constants import FPS, SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print(f"Screen size: {SCREEN_WIDTH}x{SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    font = pygame.font.Font(None, 32)

    clock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = updateable
    Shot.containers = (updateable, drawable, shots)
    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updateable.update(dt)

        for asteroid in asteroids:
            if asteroid.collide(player):
                print("Game over!")
                pygame.quit()
                sys.exit()

        for shot in shots:
            for asteroid in asteroids:
                if shot.collide(asteroid):
                    score += 1
                    asteroid.split()
                    shot.kill()

        screen.fill("black")
        score_text = font.render(f"Score: {score}", True, "white")
        screen.blit(score_text, (10, 10))
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = clock.tick(FPS) / 1000


if __name__ == "__main__":
    main()
