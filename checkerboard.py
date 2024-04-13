import pygame


class CheckerBoard:
    def __init__(self, cell_size) -> None:
        self.squares = []
        self.colors = []
        self.cell_size = cell_size

        def gen_color(x, y):
            return (255, 255, 255) if x % 2 == y % 2 else (0, 0, 0)

        def gen_square(x, y):
            xPos = x * self.cell_size
            yPos = y * self.cell_size
            height = self.cell_size
            width = self.cell_size

            return pygame.Rect(xPos, yPos, width, height)

        for y in range(8):
            for x in range(8):
                self.colors.append(gen_color(x, y))
                self.squares.append(gen_square(x, y))

    def draw(self) -> pygame.Surface:
        surf = pygame.Surface((8 * self.cell_size, 8 * self.cell_size))

        for i in range(64):
            pygame.draw.rect(surf, self.colors[i], self.squares[i])

        return surf
