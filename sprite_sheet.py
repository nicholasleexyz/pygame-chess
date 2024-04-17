import pygame
from typing import List


class SpriteSheet:
    def __init__(self, path: str, cols: int, rows: int):
        img: pygame.Surface = pygame.image.load(path)
        width = img.get_width()
        height = img.get_height()

        self.sprite_width = width / cols
        self.sprite_height = height / rows
        sprite_resolution = (self.sprite_width, self.sprite_height)

        self.sprites: List[pygame.Surface] = []
        self.cols = cols
        self.rows = rows

        for row in range(rows):
            for col in range(cols):
                sprite_surf = pygame.Surface(sprite_resolution)

                x = col * self.sprite_width
                y = row * self.sprite_height

                pos = (x, y, x + self.sprite_width, y + self.sprite_height)
                sprite_surf.blit(img, (0, 0), pos)
                sprite_surf.set_colorkey((0, 0, 0))

                self.sprites.append(sprite_surf)

    def get_sprite(self, col: int, row: int) -> pygame.Surface:
        return self.sprites[(row * self.cols) + col]
