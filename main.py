import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver} \nScreen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock, dt = pygame.time.Clock(), 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2


    updatable, drawable = pygame.sprite.Group(), pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player(x, y)

    while True:
        dt = clock.tick(60)/1000

        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for elem in updatable:
            elem.update(dt)
        for elem in drawable:
            elem.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()
