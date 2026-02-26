import pygame

pygame.init()
pygame.font.init()

FPS = 60
HEIGHT = 500
WIDTH = 700
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DSKY")

LGREY = (120, 120, 120)
GREY = (80, 80, 80)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

font = pygame.font.Font(None, 50)
smallFont = pygame.font.Font(None, 35)
digitalFont = pygame.font.Font("digital-7.ttf", 90)

numPos = pygame.Vector2(10, 229.5)
numSize = 57.5
numSep = 10

row2Text = ["+","-","V","N","D"]
row2Pos = pygame.Vector2(10, 297)
row2Size = 57.5
row2Sep = 10

prgRect = pygame.Rect(15,432, 97.5,57.5)
prgText = "PRG"

clrRect = pygame.Rect(122.5,432, 97.5,57.5)
clrText = "CLR"

entRect = pygame.Rect(230,432, 97.5,57.5)
entText = "ENT"

activeRect = pygame.Rect(395,35, 120,60)
activeText = "ACTIVE"

class Logic:
    def __init__(self):
        self.program = "00"
        self.verb = "00"
        self.noun = "00"
        self.register1 = "00000"
        self.register2 = "00000"
        self.register3 = "00000"
        self.registerSign1 = "+"
        self.registerSign2 = "+"
        self.registerSign3 = "+"

def get_centered_text_position(rect, text, font):
    text_surface = font.render(text, True, WHITE)
    text_width = text_surface.get_width()
    text_height = text_surface.get_height()

    x = rect.x + (rect.width - text_width) // 2
    y = rect.y + (rect.height - text_height) // 2

    return (x, y), text_surface

def rect_collide(rect):
    mousePos = pygame.mouse.get_pos()
    return rect.rect_collide(mousePos)            

def draw_display(logic):
    window.fill(LGREY)

    pygame.draw.line(window, WHITE, (350, 0), (350, 500), 3)
    pygame.draw.line(window, WHITE, (0, 285-67.5), (350, 285-67.5), 3)
    pygame.draw.rect(window, GREY, (0, 287-67.5, 348, 300))

    counter1, counter2, counter3 = 0, 0, 0

    for i in range(5):
        x = numPos.x + (numSize + numSep) * counter1
        y = numPos.y
        rect = pygame.Rect(x, y, numSize, numSize)
        pygame.draw.rect(window, BLACK, rect)

        text = str(counter1)
        (tx, ty), rendered_text = get_centered_text_position(rect, text, font)
        window.blit(rendered_text, (tx, ty))

        counter1 += 1

    for i in range(5):
        x = numPos.x + (numSize + numSep) * counter2
        y = numPos.y + numSize + numSep
        rect = pygame.Rect(x, y, numSize, numSize)
        pygame.draw.rect(window, BLACK, rect)

        text = str(counter2 + 5)
        (tx, ty), rendered_text = get_centered_text_position(rect, text, font)
        window.blit(rendered_text, (tx, ty))

        counter2 += 1

    for i in range(5):
        x = row2Pos.x + (row2Size + row2Sep) * counter3
        y = row2Pos.y + row2Size + row2Sep
        rect = pygame.Rect(x, y, row2Size, row2Size)
        pygame.draw.rect(window, BLACK, rect)

        text = str(row2Text[counter3])
        (tx, ty), rendered_text = get_centered_text_position(rect, text, font)
        window.blit(rendered_text, (tx, ty))

        counter3 += 1

    pygame.draw.rect(window, BLACK, prgRect)
    (tx, ty), rendered_text = get_centered_text_position(prgRect, prgText, font)
    window.blit(rendered_text, (tx, ty))

    pygame.draw.rect(window, BLACK, clrRect)
    (tx, ty), rendered_text = get_centered_text_position(clrRect, clrText, font)
    window.blit(rendered_text, (tx, ty))

    pygame.draw.rect(window, BLACK, entRect)
    (tx, ty), rendered_text = get_centered_text_position(entRect, entText, font)
    window.blit(rendered_text, (tx, ty))


    pygame.draw.rect(window, GREEN, activeRect)
    (tx, ty), rendered_text = get_centered_text_position(activeRect, activeText, smallFont)
    window.blit(rendered_text, (tx, ty))

    programText = smallFont.render("PROG", True, GREEN)
    window.blit(programText, (580,18))
    programNumText = digitalFont.render(logic.program, True, GREEN)
    window.blit(programNumText, (577,40))

    verbText = smallFont.render("VERB", True, GREEN)
    window.blit(verbText, (417,130))
    verbNumText = digitalFont.render(logic.verb, True, GREEN)
    window.blit(verbNumText, (414,152))

    nounText = smallFont.render("NOUN", True, GREEN)
    window.blit(nounText, (580,130))
    nounNumText = digitalFont.render(logic.noun, True, GREEN)
    window.blit(nounNumText, (577,152))


    registerSign1Text = digitalFont.render(logic.registerSign1, True, GREEN)
    window.blit(registerSign1Text, (390,250))
    registerSign2Text = digitalFont.render(logic.registerSign2, True, GREEN)
    window.blit(registerSign2Text, (390,320))
    registerSign3Text = digitalFont.render(logic.registerSign3, True, GREEN)
    window.blit(registerSign3Text, (390,390))

    register1Text = digitalFont.render(logic.register1, True, GREEN)
    window.blit(register1Text, (440,250))
    register2Text = digitalFont.render(logic.register2, True, GREEN)
    window.blit(register2Text, (440,320))
    register3Text = digitalFont.render(logic.register3, True, GREEN)
    window.blit(register3Text, (440,390))

    pygame.display.flip()

def main():
    clock = pygame.time.Clock()
    run = True

    logic = Logic()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                #if 0.rect_collide():
                    #pass
                pass

        draw_display(logic)

    pygame.quit()

if __name__ == "__main__":
    main()