import pygame
import settings
import game

pygame.init()

resolution = (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption(settings.CAPTION)


def main():

    _game = game.Game()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        _game.update()
        _game.draw(screen)

    pygame.quit()


if __name__ == "__main__":
    main()
