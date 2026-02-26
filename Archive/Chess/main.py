import pygame
import math
import random
import os
import time

pygame.init()
pygame.font.init()

FPS = 60
HEIGHT = 900
WIDTH = 800

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

#Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LBROWN = (242,227,129)
DBROWN = (162, 142, 11)
YELLOW = (255, 255, 0)

imagesF = "images"

BOARD_SIZE = pygame.Vector2(8, 8)

#Piece Parameters
if True:
    pieces = []

    KING_NUM = 1 #K
    QUEEN_NUM = 1 #Q
    KNIGHT_NUM = 2 #N
    BISHOP_NUM = 2 #B
    ROOK_NUM = 2 #R
    PAWN_NUM = 8 #P

    KING_MOVES = [
    [1, 0], [-1, 0], [0, 1], [0, -1], 
    [1, 1], [-1, -1], [1, -1], [-1, 1]
    ]

    QUEEN_DIR = [
        [1, 0], [-1, 0], [0, 1], [0, -1], 
        [1, 1], [-1, -1], [1, -1], [-1, 1]
    ]

    KNIGHT_MOVES = [
        [2, 1], [2, -1], [-2, 1], [-2, -1], 
        [1, 2], [1, -2], [-1, 2], [-1, -2]
    ]

    BISHOP_DIR = [
        [1, 1], [-1, -1], [1, -1], [-1, 1]
    ]

    ROOK_DIR = [
        [1, 0], [-1, 0], [0, 1], [0, -1]
    ]

    WHITE_PAWN_MOVES = [
        [0, 1], [0, 2], [-1, 1], [1, 1]
    ]

    BLACK_PAWN_MOVES = [
        [0, -1], [0, -2], [-1, -1], [1, -1]
    ]

    PIECE_MOVES = {
        "K" : KING_MOVES,
        "Q" : QUEEN_DIR,
        "N" : KNIGHT_MOVES,
        "B" : BISHOP_DIR,
        "R" : ROOK_DIR,
        "P" : [WHITE_PAWN_MOVES, BLACK_PAWN_MOVES]
    }

#Piece Images
if True:
    Image_King_White = pygame.image.load(os.path.join(imagesF, "WK.png")).convert_alpha()
    Image_Queen_White = pygame.image.load(os.path.join(imagesF, "WQ.png")).convert_alpha()
    Image_Knight_White = pygame.image.load(os.path.join(imagesF, "WN.png")).convert_alpha()
    Image_Bishop_White = pygame.image.load(os.path.join(imagesF, "WB.png")).convert_alpha()
    Image_Rook_White = pygame.image.load(os.path.join(imagesF, "WR.png")).convert_alpha()
    Image_Pawn_White = pygame.image.load(os.path.join(imagesF, "WP.png")).convert_alpha()

    Image_King_Black = pygame.image.load(os.path.join(imagesF, "BK.png")).convert_alpha()
    Image_Queen_Black = pygame.image.load(os.path.join(imagesF, "BQ.png")).convert_alpha()
    Image_Knight_Black = pygame.image.load(os.path.join(imagesF, "BN.png")).convert_alpha()
    Image_Bishop_Black = pygame.image.load(os.path.join(imagesF, "BB.png")).convert_alpha()
    Image_Rook_Black = pygame.image.load(os.path.join(imagesF, "BR.png")).convert_alpha()
    Image_Pawn_Black = pygame.image.load(os.path.join(imagesF, "BP.png")).convert_alpha()

class Logic:
    def __init__(self):
        self.mousePos = pygame.mouse.get_pos()
        self.pieceOver = None
        self.pieceClicked = None
        self.outerRect = pygame.Rect(0, 800, WIDTH, 100)
        self.allowedMoves = []
        self.allowedMovesRects = []

class Piece:
    def __init__(self, colour, piece, tx, ty):
        self.colour = colour
        self.piece = piece
        self.tPosition = pygame.Vector2(tx, ty)
        self.position = pygame.Vector2((tx*100)-100, (ty*100)-100)

        if self.colour == 0:
            if self.piece == "K":
                self.image = Image_King_White
            if self.piece == "Q":
                self.image = Image_Queen_White
            if self.piece == "N":
                self.image = Image_Knight_White
            if self.piece == "B":
                self.image = Image_Bishop_White
            if self.piece == "R":
                self.image = Image_Rook_White
            if self.piece == "P":
                self.image = Image_Pawn_White
        elif self.colour == 1:
            if self.piece == "K":
                self.image = Image_King_Black
            if self.piece == "Q":
                self.image = Image_Queen_Black
            if self.piece == "N":
                self.image = Image_Knight_Black
            if self.piece == "B":
                self.image = Image_Bishop_Black
            if self.piece == "R":
                self.image = Image_Rook_Black
            if self.piece == "P":
                self.image = Image_Pawn_Black

        self.rect = pygame.Rect(self.position.x, self.position.y, self.image.get_width(), self.image.get_height())

        self.firstMove = True

    def move(self, move):
        if self.firstMove:
            self.tPosition += 1
            self.firstMove = False

def add_piece(colour, piece, tx, ty):
    piece = Piece(colour, piece, tx, ty)
    pieces.append(piece)

def create_pieces():
        #Create White Pieces
        for i in range(KING_NUM):
            add_piece(0, "K", 4, 8)
        for i in range(QUEEN_NUM):
            add_piece(0, "Q", 5, 8)
        for i in range(KNIGHT_NUM):
            add_piece(0, "N", 3 if i == 0 else 6, 8)
        for i in range(BISHOP_NUM):
            add_piece(0, "B", 2 if i == 0 else 7, 8)
        for i in range(ROOK_NUM):
            add_piece(0, "R", 1 if i == 0 else 8, 8)
        for i in range(PAWN_NUM):
            add_piece(0, "P", i+1, 7)

        #Create Black Pieces
        for i in range(KING_NUM):
            add_piece(1, "K", 4, 1)
        for i in range(QUEEN_NUM):
            add_piece(1, "Q", 5, 1)
        for i in range(KNIGHT_NUM):
            add_piece(1, "N", 3 if i == 0 else 6, 1)
        for i in range(BISHOP_NUM):
            add_piece(1, "B", 2 if i == 0 else 7, 1)
        for i in range(ROOK_NUM):
            add_piece(1, "R", 1 if i == 0 else 8, 1)
        for i in range(PAWN_NUM):
            add_piece(1, "P", i+1, 2)

def draw_board():
    for row in range(8):
        for col in range(8):
            if (row + col) % 2 == 0:
                pygame.draw.rect(window, DBROWN, (col * 100, row * 100, 100, 100))
            else:
                pygame.draw.rect(window, LBROWN, (col * 100, row * 100, 100, 100))

def draw_pieces():
    for piece in pieces:
        window.blit(piece.image, piece.rect)

def check_pieceCollide(logic):
    for piece in pieces:
        if piece.rect.collidepoint(logic.mousePos):
            return piece

def allowed_moves_rect(logic):
    allowedMovesRects = []
    for move in logic.allowedMoves:
        allowedMovesRects.append(pygame.Rect((move.x-1)*100, (move.y-1)*100, 100, 100))
    logic.allowedMovesRects = allowedMovesRects

def allowed_moves(logic):
    # Initialize List
    allowedMoves = []

    # King and Knight Moves (No Block Check Needed)
    if logic.pieceClicked.piece in ["K", "N"]:
        for move in PIECE_MOVES[logic.pieceClicked.piece]:
            delta = pygame.Vector2(*move)
            newPos = logic.pieceClicked.tPosition + delta
            if 0 < newPos.x <= BOARD_SIZE.x and 0 < newPos.y <= BOARD_SIZE.y:
                allowedMoves.append(newPos)

    # Pawn Moves (Block Check and Rules)
    elif logic.pieceClicked.piece == "P":
        if logic.pieceClicked.colour == 0: 
            pawnMoves = WHITE_PAWN_MOVES
            print("White selected")
        elif logic.pieceClicked.colour == 1:
            pawnMoves = BLACK_PAWN_MOVES
            print("Black selected")

        # Forward Moves
        for i in range(2 if logic.pieceClicked.firstMove else 1):
            delta = pygame.Vector2(*pawnMoves[i])
            newPos = logic.pieceClicked.tPosition + delta
            if 0 < newPos.x <= BOARD_SIZE.x and 0 < newPos.y <= BOARD_SIZE.y:
                isOccupied = False
                for piece in pieces:
                    if piece.tPosition == newPos:
                        isOccupied = True
                        break
                
                if not isOccupied:
                    allowedMoves.append(newPos)
                    print("Forward move added")
                else:
                    break

        # Diagonal Capture Moves
        for i in range(2, 4):
            delta = pygame.Vector2(*pawnMoves[i])
            newPos = logic.pieceClicked.tPosition + delta
            if 0 < newPos.x <= BOARD_SIZE.x and 0 < newPos.y <= BOARD_SIZE.y:
                for piece in pieces:
                    if piece.tPosition == newPos and piece.colour != logic.pieceClicked.colour:
                        allowedMoves.append(newPos)
                        print("Diagonal capture move added")

    logic.allowedMoves = allowedMoves
    allowed_moves_rect(logic)

def draw_display(logic):
    window.fill(BLACK)

    draw_board()
    draw_pieces()

    #Draw Square Highlight For Clicked And Over
    logic.pieceOver = check_pieceCollide(logic)

    if logic.pieceOver:
        pygame.draw.rect(window, GREEN, logic.pieceOver.rect, 5)

    if logic.pieceClicked:
        pygame.draw.rect(window, BLUE, logic.pieceClicked.rect, 5)

        #Draw Allowed Moves
        for move in logic.allowedMoves:
            pygame.draw.circle(window, YELLOW, ((move.x-1)*100+50, (move.y-1)*100+50), 40, 5)

    pygame.display.flip()

def main():
    clock = pygame.time.Clock()
    run = True

    #Permanent Instances
    if True:
        logic = Logic()

        create_pieces()

    while run:
        clock.tick(FPS)
        keysPressed = pygame.key.get_pressed()
        logic.mousePos = pygame.mouse.get_pos()

        #Quit Game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        if keysPressed[pygame.K_ESCAPE]:
            pygame.quit()

        #Handle Mouse Clicks
        if pygame.mouse.get_pressed()[0]:
            if not logic.pieceOver:
                logic.pieceClicked = None
            else:
                logic.pieceClicked = logic.pieceOver
            if logic.pieceClicked:
                allowed_moves(logic)

        draw_display(logic)

    pygame.quit()

if __name__ == "__main__":
    main()