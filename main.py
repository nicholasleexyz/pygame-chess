# Example file showing a basic pygame "game loop"
import pygame
from checkerboard import CheckerBoard
from chess_pieces import ChessPieces

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
running = True
graphic_checkerboard = CheckerBoard(100)
graphic_chess_pieces = ChessPieces()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE

    screen.blit(graphic_checkerboard.draw(), (0, 0))
    screen.blit(graphic_chess_pieces.draw("pawn_black"), (0, 0))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
