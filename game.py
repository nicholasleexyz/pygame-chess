import pygame
from chess_board import ChessBoard


class Game:
    def __init__(self) -> None:
        self.clock = pygame.time.Clock()
        self.chess_board = ChessBoard()
        self.mouse_position = pygame.mouse.get_pos()

        self.current_cell_index: int = 0

    def update(self):
        self.mouse_position = pygame.mouse.get_pos()
        self.clock.tick(60)

    def draw(self, screen: pygame.Surface):
        screen.fill("purple")

        screen.blit(self.chess_board.draw(), (0, 0))

        # Define the square size
        square_size = 128

        # Calculate the square's top-left corner position
        square_top_left = (
            ((self.mouse_position[0] - (square_size // 2) + 64) // 128) * 128,
            ((self.mouse_position[1] - (square_size // 2) + 64) // 128) * 128,
        )

        square_dimensions = (square_size, square_size)
        square_rect = (square_top_left, square_dimensions)

        square_color = (0, 255, 255)

        # Draw a square at the mouse position
        pygame.draw.rect(screen, square_color, square_rect, 4)

        pygame.display.flip()

    def cell_coords_to_index(self, x: int, y: int):
        pass
