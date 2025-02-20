import pygame
from constants import *
from player import *
def main():
    pygame.init()
    clock = pygame.time.Clock()
    framerate = 60
    dt = 0
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0,0,0))
        updateable.update(dt)
        for entities in drawable:
            entities.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        dt = ((clock.tick(60))/1000)

if __name__ == "__main__":
    main()