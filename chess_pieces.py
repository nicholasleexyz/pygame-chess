import pygame


class ChessPieces:
    def __init__(self) -> None:
        sprite_sheet = pygame.image.load("chess.png")

        def get_image() -> pygame.Surface:
            img = pygame.Surface((128, 128))
            img.blit(sprite_sheet, (-16, -16), (0, 0, 128, 128))
            img.set_colorkey((0, 0, 0))
            return img

        self.dict = {"pawn_black": get_image()}
        pass

    def draw(self, key: str) -> pygame.Surface:
        return self.dict[key]
