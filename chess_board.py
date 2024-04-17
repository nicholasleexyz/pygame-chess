import pygame
import sprite_sheet
from chess_piece_type import ChessPieceType
from chess_piece import ChessPiece


class ChessBoard:
    def __init__(self):
        resolution = (128 * 8, 128 * 8)
        self.surf = pygame.Surface(resolution)

        self.checkerboard = pygame.image.load("checkerboard.png")

        sprites = sprite_sheet.SpriteSheet("chess.png", 6, 12)

        self.textures = {
            ChessPieceType.PAWN_BLACK: sprites.get_sprite(0, 2),
            ChessPieceType.KNIGHT_BLACK: sprites.get_sprite(1, 2),
            ChessPieceType.BISHOP_BLACK: sprites.get_sprite(2, 2),
            ChessPieceType.ROOK_BLACK: sprites.get_sprite(3, 2),
            ChessPieceType.QUEEN_BLACK: sprites.get_sprite(4, 2),
            ChessPieceType.KING_BLACK: sprites.get_sprite(5, 2),
            ChessPieceType.PAWN_WHITE: sprites.get_sprite(0, 4),
            ChessPieceType.KNIGHT_WHITE: sprites.get_sprite(1, 4),
            ChessPieceType.BISHOP_WHITE: sprites.get_sprite(2, 4),
            ChessPieceType.ROOK_WHITE: sprites.get_sprite(3, 4),
            ChessPieceType.QUEEN_WHITE: sprites.get_sprite(4, 4),
            ChessPieceType.KING_WHITE: sprites.get_sprite(5, 4),
        }

        self.chess_pieces = [
            ChessPiece(ChessPieceType.ROOK_BLACK, 0, 0),
            ChessPiece(ChessPieceType.KNIGHT_BLACK, 1, 0),
            ChessPiece(ChessPieceType.BISHOP_BLACK, 2, 0),
            ChessPiece(ChessPieceType.QUEEN_BLACK, 3, 0),
            ChessPiece(ChessPieceType.KING_BLACK, 4, 0),
            ChessPiece(ChessPieceType.BISHOP_BLACK, 5, 0),
            ChessPiece(ChessPieceType.KNIGHT_BLACK, 6, 0),
            ChessPiece(ChessPieceType.ROOK_BLACK, 7, 0),
            ChessPiece(ChessPieceType.PAWN_BLACK, 0, 1),
            ChessPiece(ChessPieceType.PAWN_BLACK, 1, 1),
            ChessPiece(ChessPieceType.PAWN_BLACK, 2, 1),
            ChessPiece(ChessPieceType.PAWN_BLACK, 3, 1),
            ChessPiece(ChessPieceType.PAWN_BLACK, 4, 1),
            ChessPiece(ChessPieceType.PAWN_BLACK, 5, 1),
            ChessPiece(ChessPieceType.PAWN_BLACK, 6, 1),
            ChessPiece(ChessPieceType.PAWN_BLACK, 7, 1),
            ChessPiece(ChessPieceType.ROOK_WHITE, 0, 7),
            ChessPiece(ChessPieceType.KNIGHT_WHITE, 1, 7),
            ChessPiece(ChessPieceType.BISHOP_WHITE, 2, 7),
            ChessPiece(ChessPieceType.QUEEN_WHITE, 3, 7),
            ChessPiece(ChessPieceType.KING_WHITE, 4, 7),
            ChessPiece(ChessPieceType.BISHOP_WHITE, 5, 7),
            ChessPiece(ChessPieceType.KNIGHT_WHITE, 6, 7),
            ChessPiece(ChessPieceType.ROOK_WHITE, 7, 7),
            ChessPiece(ChessPieceType.PAWN_WHITE, 0, 6),
            ChessPiece(ChessPieceType.PAWN_WHITE, 1, 6),
            ChessPiece(ChessPieceType.PAWN_WHITE, 2, 6),
            ChessPiece(ChessPieceType.PAWN_WHITE, 3, 6),
            ChessPiece(ChessPieceType.PAWN_WHITE, 4, 6),
            ChessPiece(ChessPieceType.PAWN_WHITE, 5, 6),
            ChessPiece(ChessPieceType.PAWN_WHITE, 6, 6),
            ChessPiece(ChessPieceType.PAWN_WHITE, 7, 6),
        ]

    def draw(self) -> pygame.Surface:
        self.surf.blit(self.checkerboard, (0, 0))

        for p in self.chess_pieces:
            texture = self.textures[p.chess_piece_type]
            pos = (p.pos_x * 128, p.pos_y * 128)
            self.surf.blit(texture, pos)

        return self.surf
