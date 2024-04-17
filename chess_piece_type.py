from enum import Enum, auto


class ChessPieceType(Enum):
    PAWN_BLACK = auto()
    KNIGHT_BLACK = auto()
    BISHOP_BLACK = auto()
    ROOK_BLACK = auto()
    QUEEN_BLACK = auto()
    KING_BLACK = auto()
    PAWN_WHITE = auto()
    KNIGHT_WHITE = auto()
    BISHOP_WHITE = auto()
    ROOK_WHITE = auto()
    QUEEN_WHITE = auto()
    KING_WHITE = auto()


# CHESS_SPRITES = {
#     "PAWN_BLACK": (0, 2),
#     "KNIGHT_BLACK": (1, 2),
#     "BISHOP_BLACK": (2, 2),
#     "ROOK_BLACK": (3, 2),
#     "QUEEN_BLACK": (4, 2),
#     "KING_BLACK": (5, 2),
#     "PAWN_WHITE": (0, 4),
#     "KNIGHT_WHITE": (1, 4),
#     "BISHOP_WHITE": (2, 4),
#     "ROOK_WHITE": (3, 4),
#     "QUEEN_WHITE": (4, 4),
#     "KING_WHITE": (5, 4),
# }
