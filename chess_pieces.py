import pygame


class ChessPieces:
    def __init__(self) -> None:
        sprite_sheet = pygame.image.load("chess.png")

        def get_image(col: int, row: int) -> pygame.Surface:
            img = pygame.Surface((128, 128))
            x = col * 128
            y = row * 128
            img.blit(sprite_sheet, (0, 0), (x, y, x + 128, y + 128))
            img.set_colorkey((0, 0, 0))
            return img

        self.dict = {
            "pawn_black": get_image(0, 2),
            "knight_black": get_image(1, 2),
            "bishop_black": get_image(2, 2),
            "rook_black": get_image(3, 2),
            "queen_black": get_image(4, 2),
            "king_black": get_image(5, 2),
            "pawn_white": get_image(0, 4),
            "knight_white": get_image(1, 4),
            "bishop_white": get_image(2, 4),
            "rook_white": get_image(3, 4),
            "queen_white": get_image(4, 4),
            "king_white": get_image(5, 4),
        }

    def draw(self, key: str) -> pygame.Surface:
        return self.dict[key]
