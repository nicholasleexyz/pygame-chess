import pygame
from chess_piece_type import ChessPieceType


class ChessPiece:
    def __init__(self, chess_piece_type: ChessPieceType, x: int, y: int):
        self.chess_piece_type = chess_piece_type
        self.pos_x = x
        self.pos_y = y

    def move(self):
        pass
