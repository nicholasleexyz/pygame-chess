# constants
SCREEN_WIDTH = 128 * 8
SCREEN_HEIGHT = 128 * 8
CAPTION = "Chess"

PIECE_PLACEMENT = {
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

CHESS_SPRITES = {
    "pawn_black": (0, 2),
    "knight_black": (1, 2),
    "bishop_black": (2, 2),
    "rook_black": (3, 2),
    "queen_black": (4, 2),
    "king_black": (5, 2),
    "pawn_white": (0, 4),
    "knight_white": (1, 4),
    "bishop_white": (2, 4),
    "rook_white": (3, 4),
    "queen_white": (4, 4),
    "king_white": (5, 4),
}
