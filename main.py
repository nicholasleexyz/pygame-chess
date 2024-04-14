import pygame
from checkerboard import CheckerBoard
from chess_pieces import ChessPieces
import colors

# NOTE:
# - [ x ] render every chess piece
# - [ ] chess piece behavior
# - [ ]

pygame.init()

screen = pygame.display.set_mode((128 * 8, 128 * 8))
pygame.display.set_caption("Chess")

clock = pygame.time.Clock()
running = True

graphic_checkerboard = CheckerBoard(128)
graphic_chess_pieces = ChessPieces()

piece_placement = {
    "pawn_black": [
        (0, 1),
        (1, 1),
        (2, 1),
        (3, 1),
        (4, 1),
        (5, 1),
        (6, 1),
        (7, 1),
    ],
    "queen_black": [(3, 0)],
    "king_black": [(4, 0)],
    "bishop_black": [(2, 0), (5, 0)],
    "knight_black": [(1, 0), (6, 0)],
    "rook_black": [(0, 0), (7, 0)],
    "pawn_white": [
        (0, 6),
        (1, 6),
        (2, 6),
        (3, 6),
        (4, 6),
        (5, 6),
        (6, 6),
        (7, 6),
    ],
    "queen_white": [(3, 7)],
    "king_white": [(4, 7)],
    "bishop_white": [(2, 7), (5, 7)],
    "knight_white": [(1, 7), (6, 7)],
    "rook_white": [(0, 7), (7, 7)],
}

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_pos = pygame.mouse.get_pos()

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    ####
    # RENDER YOUR GAME HERE

    screen.blit(graphic_checkerboard.draw(), (0, 0))

    scale = 128
    for key in piece_placement:
        for places in piece_placement[key]:
            pos = (places[0] * scale, places[1] * scale)
            screen.blit(graphic_chess_pieces.draw(key), pos)

    # draw a circle at mouse cursor position
    pygame.draw.circle(screen, colors.CYAN, mouse_pos, 5)

    ####

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
