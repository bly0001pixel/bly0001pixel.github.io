import pygame
import math
pygame.init()

FPS, WIDTH, HEIGHT = 60, 560, 560
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")

BLACK = (0,0,0)
WHITE = (255,255,255)
HIGHLIGHTCOLOUR = (0,0,255)
LTILECOLOUR = (227,193,111)
DTILECOLOUR = (184,139,74)
LPIECECOLOUR = (232,227,192)
DPIECECOLOUR = (21,21,21)

tileSize = pygame.Vector2(WIDTH/8, HEIGHT/8)
pieceRadius = (tileSize.x * 0.8) / 2
highlightWidth = 6
turnOutlineRect = pygame.Rect(0, 0, WIDTH, HEIGHT)
turnOutlineWidth = 4

LPieceList = []
DPieceList = []

class Piece:
    def __init__(self, colour, tile):
        self.colour = colour
        self.tile = tile
        self.monarch = False

def createPieces():
    for r in range(8):
        for c in range(8):
            if c <= 2:
                if r % 2 == 0:
                    if c % 2 != 0:
                        piece = Piece(DPIECECOLOUR, pygame.Vector2(r,c))
                        DPieceList.append(piece)
                else:
                    if c % 2 == 0:
                        piece = Piece(DPIECECOLOUR, pygame.Vector2(r,c))
                        DPieceList.append(piece)
            if c >= 5:
                if r % 2 == 0:
                    if c % 2 != 0:
                        piece = Piece(LPIECECOLOUR, pygame.Vector2(r,c))
                        LPieceList.append(piece)
                else:
                    if c % 2 == 0:
                        piece = Piece(LPIECECOLOUR, pygame.Vector2(r,c))
                        LPieceList.append(piece)

def mouseToTile(mousePos):
    tileSelected = pygame.Vector2()

    tileSelected.x = math.floor(mousePos[0] / tileSize.x)
    tileSelected.y = math.floor(mousePos[1] / tileSize.y)

    return tileSelected

def mouseSelect(tileOver, turn):
    tileSelected = False

    for piece in LPieceList if turn == 0 else DPieceList:
        if tileOver == piece.tile:
            tileSelected = tileOver

    return tileSelected

def possibleMoves(tileSelected, turn):
    for piece in LPieceList if turn == 0 else DPieceList:
        if tileSelected == piece.tile:
            if piece.monarch:
                possibleMoves = [
                    pygame.Vector2(-1,-1),
                    pygame.Vector2(1,-1),
                    pygame.Vector2(-1,1),
                    pygame.Vector2(1,1)
                ]
            else:
                possibleMoves = [
                    pygame.Vector2(-1,-1),
                    pygame.Vector2(1,-1)
                ]

    clearMoves = []
    possibleCaptureMoves = []

    for i in range(len(possibleMoves)):
        destination = tileSelected + possibleMoves[i]
        for piece in LPieceList if turn == 0 else DPieceList:
            if destination != piece.tile:
                clear = True
            else:
                clear = False
        for piece in DPieceList if turn == 1 else LPieceList:
            if destination == piece.tile:
                capture = True
            else:
                capture = False

        if clear:
            clearMoves.append(possibleMoves[i])
        if capture:
            possibleCaptureMoves.append(possibleMoves[i])

    captureMoves = []

    for move in possibleCaptureMoves:
        moveBranches = []
        
        destination = tileSelected + (possibleMoves[i] * 2)
        for piece in LPieceList if turn == 0 else DPieceList:
            if destination != piece.tile:
                clear = True
            else:
                clear = False
        for piece in DPieceList if turn == 1 else LPieceList:
            if destination != piece.tile:
                clear = True
            else:
                clear = False
        

    return clearMoves, captureMoves

def draw_display(tileSelected, turn, clearMoves, captureMoves):
    window.fill(BLACK)

    #Draw Tiles
    for r in range(8):
        for c in range(8):
            if r % 2 == 0:
                if c % 2 == 0:
                    tileColour = LTILECOLOUR
                else:
                    tileColour = DTILECOLOUR
            else:
                if c % 2 == 0:
                    tileColour = DTILECOLOUR
                else:
                    tileColour = LTILECOLOUR

            tileRect = pygame.Rect(r * tileSize.x, c * tileSize.y, tileSize.x, tileSize.y)

            pygame.draw.rect(window, tileColour, tileRect)

    #Draw Pieces
    for piece in LPieceList:
        pygame.draw.circle(window, piece.colour, (piece.tile.x * tileSize.x + (tileSize.x/2), piece.tile.y * tileSize.y + (tileSize.y/2)), pieceRadius)
    for piece in DPieceList:
        pygame.draw.circle(window, piece.colour, (piece.tile.x * tileSize.x + (tileSize.x/2), piece.tile.y * tileSize.y + (tileSize.y/2)), pieceRadius)

    #Draw Highlight
    if tileSelected:
        pygame.draw.circle(window, HIGHLIGHTCOLOUR, ((tileSelected.x * tileSize.x) + (tileSize.x / 2), (tileSelected.y * tileSize.y) + (tileSize.y / 2)), pieceRadius, highlightWidth)
        
    #Draw Turn Outline
    if turn == 0:
        turnOutlineColour = LPIECECOLOUR
    else:
        turnOutlineColour = DPIECECOLOUR

    #Draw Destinations
    for move in clearMoves:


    pygame.draw.rect(window, turnOutlineColour, turnOutlineRect, turnOutlineWidth)

def main():
    run = True
    clock = pygame.time.Clock()

    createPieces()

    tileSelected = pygame.Vector2(0,0)
    turn = 0

    while run:
        clock.tick(FPS)
        mousePos = pygame.mouse.get_pos()
        tileOver = mouseToTile(mousePos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    tileSelected = mouseSelect(tileOver, turn)
                elif event.button == 3:
                    tileSelected = False

        clearMoves, captureMoves = possibleMoves(tileSelected, turn)

        draw_display(tileSelected, turn, clearMoves, captureMoves)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()