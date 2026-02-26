import pygame

pygame.init()
pygame.font.init()
pygame.mixer.init()

from chords import chords

FPS = 60
HEIGHT = 40
WIDTH = 900
BORDER_WIDTH = 3

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chording Keyboard")

topLeft = pygame.Vector2(10,10)

FONT = pygame.font.SysFont("sansserif", 30, False)

class Cursor:
    def __init__(self):
        self.position = pygame.Vector2(WIDTH/2,10)
        self.size = pygame.Vector2(2, 20)
        self.rect = pygame.Rect(self.position.x,self.position.y, self.size.x,self.size.y)
        self.colour = WHITE

    def dark(self, mode):
        if mode == 0:
            self.colour = BLACK
        if mode == 1:
            self.colour = BLUE

    def white(self):
        self.colour = WHITE

class Type:
    def __init__(self):
        self.type = ""
        self.colour = BLACK
        self.text = FONT.render(self.type, 1, self.colour)
        self.position = topLeft

    def update_chord(self, new_text):
        if len(self.type) > 0:
            self.type += " "
        self.type += new_text
        self.text = FONT.render(self.type, 1, self.colour)

    def backspace(self):
        self.type = self.type[:-1]
        self.text = FONT.render(self.type, 1, self.colour)

    def space(self):
        self.type += " "
        self.text = FONT.render(self.type, 1, self.colour)

    def clear(self):
        self.type = ""
        self.text = FONT.render(self.type, 1, self.colour)
    
    def punctuation(self, symbol):
        self.type += symbol
        self.text = FONT.render(self.type, 1, self.colour)

    def number(self, number):
        self.type += number
        self.text = FONT.render(self.type, 1, self.colour)

    def add_s(self):
        self.type += "s"
        self.text = FONT.render(self.type, 1, self.colour)

    def add_aps(self):
        self.type += "'s"
        self.text = FONT.render(self.type, 1, self.colour)

    def add_es(self):
        self.type += "es"
        self.text = FONT.render(self.type, 1, self.colour)

    def add_ing(self):
        self.type += "ing"
        self.text = FONT.render(self.type, 1, self.colour)

    def add_d(self):
        self.type += "d"
        self.text = FONT.render(self.type, 1, self.colour)

    def add_ed(self):
        self.type += "ed"
        self.text = FONT.render(self.type, 1, self.colour)
    
    def add_er(self):
        self.type += "er"
        self.text = FONT.render(self.type, 1, self.colour)

def keydown(letter, activeKeys, pressedKeys):
    activeKeys.add(letter)
    pressedKeys.add(letter)

def keyup(letter, activeKeys, pressedKeys, chords, type):
    pressedKeys.discard(letter)
    chordTuple = tuple(sorted(activeKeys))
    
    if not pressedKeys:
        if len(chordTuple) > 1:
            if chordTuple in chords:
                type.update_chord(chords[chordTuple])
            else:
                print(f"Chord {chordTuple} is not mapped")
            activeKeys.clear()
        elif len(chordTuple) == 1:
            if chordTuple == ('a',) or chordTuple == ('i',):
                type.update_chord(chords[chordTuple])
            else:
                print(f"Single letter {chordTuple} is not 'a' or 'I', not processed.")
            activeKeys.clear()
        else:
            print("Empty chord detected.")

def print_output(type, filename):
    with open(filename, 'a') as output:
        output.write("\n")
        output.write(type.type)

def draw_display(type, cursor, mode):
    window.fill(WHITE)

    if mode == 1:
        pygame.draw.rect(window, BLUE, (0,0,WIDTH,HEIGHT))
        pygame.draw.rect(window, WHITE, (BORDER_WIDTH,BORDER_WIDTH,WIDTH-BORDER_WIDTH*2,HEIGHT-BORDER_WIDTH*2))

    window.blit(type.text, (WIDTH/2 - type.text.get_width(), type.position.y))

    pygame.draw.rect(window, cursor.colour, cursor.rect)

    pygame.display.flip()

def main():
    activeKeys = set()
    pressedKeys = set()

    type = Type()
    cursor = Cursor()

    timer = 0
    mode = 0

    clock = pygame.time.Clock()
    run = True
    while run:

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.KEYDOWN:
                mods = pygame.key.get_mods()
                is_shift_pressed = mods & pygame.KMOD_SHIFT

                if 1 == 1:
                    if mode == 1:
                        if event.key == pygame.K_a:
                            if is_shift_pressed:
                                type.type += "A"
                                type.text = FONT.render(type.type, 1, type.colour)
                            else:
                                type.type += "a"
                                type.text = FONT.render(type.type, 1, type.colour)
                        if event.key == pygame.K_b:
                            if is_shift_pressed:
                                type.type += "B"
                                type.text = FONT.render(type.type, 1, type.colour)
                            else:
                                type.type += "b"
                                type.text = FONT.render(type.type, 1, type.colour)
                        if event.key == pygame.K_c:
                            if is_shift_pressed:
                                type.type += "C"
                                type.text = FONT.render(type.type, 1, type.colour)
                            else:
                                type.type += "c"
                                type.text = FONT.render(type.type, 1, type.colour)
                        if event.key == pygame.K_d:
                            if is_shift_pressed:
                                type.type += "D"
                                type.text = FONT.render(type.type, 1, type.colour)
                            else:
                                type.type += "d"
                                type.text = FONT.render(type.type, 1, type.colour)
                        if event.key == pygame.K_e:
                            if is_shift_pressed:
                                type.type += "E"
                                type.text = FONT.render(type.type, 1, type.colour)
                            else:
                                type.type += "e"
                                type.text = FONT.render(type.type, 1, type.colour)
                        if event.key == pygame.K_f:
                            if is_shift_pressed:
                                type.type += "F"
                                type.text = FONT.render(type.type, 1, type.colour)
                            else:
                                type.type += "f"
                                type.text = FONT.render(type.type, 1, type.colour)
                        if event.key == pygame.K_g:
                            if is_shift_pressed:
                                type.type += "G"
                                type.text = FONT.render(type.type, 1, type.colour)
                            else:
                                type.type += "g"
                                type.text = FONT.render(type.type, 1, type.colour)
                        if event.key == pygame.K_h:
                            if is_shift_pressed:
                                type.type += "H"
                                type.text = FONT.render(type.type, 1, type.colour)
                            else:
                                type.type += "h"
                                type.text = FONT.render(type.type, 1, type.colour)
                        if event.key == pygame.K_i:
                            if is_shift_pressed:
                                type.type += "I"
                                type.text = FONT.render(type.type, 1, type.colour)
                            else:
                                type.type += "i"
                                type.text = FONT.render(type.type, 1, type.colour)
                        if event.key == pygame.K_j:
                            if is_shift_pressed:
                                type.type += "J"
                                type.text = FONT.render(type.type, 1, type.colour)
                            else:
                                type.type += "j"
                                type.text = FONT.render(type.type, 1, type.colour)
                        if event.key == pygame.K_k:
                            if is_shift_pressed:
                                type.type += "K"
                                type.text = FONT.render(type.type, 1, type.colour)
                            else:
                                type.type += "k"
                                type.text = FONT.render(type.type, 1, type.colour)
                        if event.key == pygame.K_l:
                            if is_shift_pressed:
                                type.type += "L"
                                type.text = FONT.render(type.type, 1, type.colour)
                            else:
                                type.type += "l"
                                type.text = FONT.render(type.type, 1, type.colour)
                        if event.key == pygame.K_m:
                            if is_shift_pressed:
                                type.type += "M"
                                type.text = FONT.render(type.type, 1, type.colour)
                            else:
                                type.type += "m"
                                type.text = FONT.render(type.type, 1, type.colour)
                        if event.key == pygame.K_n:
                            if is_shift_pressed:
                                type.type += "N"
                                type.text = FONT.render(type.type, 1, type.colour)
                            else:
                                type.type += "n"
                                type.text = FONT.render(type.type, 1, type.colour)
                        if event.key == pygame.K_o:
                            if is_shift_pressed:
                                type.type += "O"
                                type.text = FONT.render(type.type, 1, type.colour)
                            else:
                                type.type += "o"
                                type.text = FONT.render(type.type, 1, type.colour)
                        if event.key == pygame.K_p:
                            if is_shift_pressed:
                                type.type += "P"
                                type.text = FONT.render(type.type, 1, type.colour)
                            else:
                                type.type += "p"
                                type.text = FONT.render(type.type, 1, type.colour)
                        if event.key == pygame.K_q:
                            if is_shift_pressed:
                                type.type += "Q"
                                type.text = FONT.render(type.type, 1, type.colour)
                            else:
                                type.type += "q"
                                type.text = FONT.render(type.type, 1, type.colour)
                        if event.key == pygame.K_r:
                            if is_shift_pressed:
                                type.type += "R"
                                type.text = FONT.render(type.type, 1, type.colour)
                            else:
                                type.type += "r"
                                type.text = FONT.render(type.type, 1, type.colour)
                        if event.key == pygame.K_s:
                            if is_shift_pressed:
                                type.type += "S"
                                type.text = FONT.render(type.type, 1, type.colour)
                            else:
                                type.type += "s"
                                type.text = FONT.render(type.type, 1, type.colour)
                        if event.key == pygame.K_t:
                            if is_shift_pressed:
                                type.type += "T"
                                type.text = FONT.render(type.type, 1, type.colour)
                            else:
                                type.type += "t"
                                type.text = FONT.render(type.type, 1, type.colour)
                        if event.key == pygame.K_u:
                            if is_shift_pressed:
                                type.type += "U"
                                type.text = FONT.render(type.type, 1, type.colour)
                            else:
                                type.type += "u"
                                type.text = FONT.render(type.type, 1, type.colour)
                        if event.key == pygame.K_v:
                            if is_shift_pressed:
                                type.type += "V"
                                type.text = FONT.render(type.type, 1, type.colour)
                            else:
                                type.type += "v"
                                type.text = FONT.render(type.type, 1, type.colour)
                        if event.key == pygame.K_w:
                            if is_shift_pressed:
                                type.type += "W"
                                type.text = FONT.render(type.type, 1, type.colour)
                            else:
                                type.type += "w"
                                type.text = FONT.render(type.type, 1, type.colour)
                        if event.key == pygame.K_x:
                            if is_shift_pressed:
                                type.type += "X"
                                type.text = FONT.render(type.type, 1, type.colour)
                            else:
                                type.type += "x"
                                type.text = FONT.render(type.type, 1, type.colour)
                        if event.key == pygame.K_y:
                            if is_shift_pressed:
                                type.type += "Y"
                                type.text = FONT.render(type.type, 1, type.colour)
                            else:
                                type.type += "y"
                                type.text = FONT.render(type.type, 1, type.colour)
                        if event.key == pygame.K_z:
                            if is_shift_pressed:
                                type.type += "Z"
                                type.text = FONT.render(type.type, 1, type.colour)
                            else:
                                type.type += "z"
                                type.text = FONT.render(type.type, 1, type.colour)
                    elif mode == 0:
                        if event.key == pygame.K_a:
                            keydown("a", activeKeys, pressedKeys)
                        if event.key == pygame.K_b:
                            keydown("b", activeKeys, pressedKeys)
                        if event.key == pygame.K_c:
                            keydown("c", activeKeys, pressedKeys)
                        if event.key == pygame.K_d:
                            keydown("d", activeKeys, pressedKeys)
                        if event.key == pygame.K_e:
                            keydown("e", activeKeys, pressedKeys)
                        if event.key == pygame.K_f:
                            keydown("f", activeKeys, pressedKeys)
                        if event.key == pygame.K_g:
                            keydown("g", activeKeys, pressedKeys)
                        if event.key == pygame.K_h:
                            keydown("h", activeKeys, pressedKeys)
                        if event.key == pygame.K_i:
                            keydown("i", activeKeys, pressedKeys)
                        if event.key == pygame.K_j:
                            keydown("j", activeKeys, pressedKeys)
                        if event.key == pygame.K_k:
                            keydown("k", activeKeys, pressedKeys)
                        if event.key == pygame.K_l:
                            keydown("l", activeKeys, pressedKeys)
                        if event.key == pygame.K_m:
                            keydown("m", activeKeys, pressedKeys)
                        if event.key == pygame.K_n:
                            keydown("n", activeKeys, pressedKeys)
                        if event.key == pygame.K_o:
                            keydown("o", activeKeys, pressedKeys)
                        if event.key == pygame.K_p:
                            keydown("p", activeKeys, pressedKeys)
                        if event.key == pygame.K_q:
                            keydown("q", activeKeys, pressedKeys)
                        if event.key == pygame.K_r:
                            keydown("r", activeKeys, pressedKeys)
                        if event.key == pygame.K_s:
                            keydown("s", activeKeys, pressedKeys)
                        if event.key == pygame.K_t:
                            keydown("t", activeKeys, pressedKeys)
                        if event.key == pygame.K_u:
                            keydown("u", activeKeys, pressedKeys)
                        if event.key == pygame.K_v:
                            keydown("v", activeKeys, pressedKeys)
                        if event.key == pygame.K_w:
                            keydown("w", activeKeys, pressedKeys)
                        if event.key == pygame.K_x:
                            keydown("x", activeKeys, pressedKeys)
                        if event.key == pygame.K_y:
                            keydown("y", activeKeys, pressedKeys)
                        if event.key == pygame.K_z:
                            keydown("z", activeKeys, pressedKeys)

                if event.key == pygame.K_LALT:
                    keydown("lalt", activeKeys, pressedKeys)
                if event.key == pygame.K_RALT:
                    keydown("ralt", activeKeys, pressedKeys)
                if event.key == pygame.K_MINUS:
                    keydown("-", activeKeys, pressedKeys)

                if event.key == pygame.K_BACKSPACE:
                    type.backspace()
                if event.key == pygame.K_SPACE:
                    type.space()
                if event.key == pygame.K_RETURN:
                    print_output(type, "Output.txt")
                    type.clear()
                if event.key == pygame.K_DELETE:
                    type.clear()
                if event.key == pygame.K_PERIOD:
                    type.punctuation(".")
                if event.key == pygame.K_COMMA:
                    type.punctuation(",")

                if event.key == pygame.K_SLASH:
                    if is_shift_pressed:
                        type.punctuation("?")
                    else:
                        type.punctuation("/")

                if 1 == 1:
                    if event.key == pygame.K_1:
                        if is_shift_pressed:
                            type.punctuation("!")
                        else:
                            type.number("1")
                    if event.key == pygame.K_2:
                        if is_shift_pressed:
                            type.punctuation("@")
                        else:
                            type.number("2")
                    if event.key == pygame.K_3:
                        if is_shift_pressed:
                            type.punctuation("#")
                        else:
                            type.number("3")
                    if event.key == pygame.K_4:
                        if is_shift_pressed:
                            type.punctuation("$")
                        else:
                            type.number("4")
                    if event.key == pygame.K_5:
                        if is_shift_pressed:
                            type.punctuation("%")
                        else:
                            type.number("5")
                    if event.key == pygame.K_6:
                        if is_shift_pressed:
                            type.punctuation("^")
                        else:
                            type.number("6")
                    if event.key == pygame.K_7:
                        if is_shift_pressed:
                            type.punctuation("&")
                        else:
                            type.number("7")
                    if event.key == pygame.K_8:
                        if is_shift_pressed:
                            type.punctuation("*")
                        else:
                            type.number("8")
                    if event.key == pygame.K_9:
                        if is_shift_pressed:
                            type.punctuation("(")
                        else:
                            type.number("9")
                    if event.key == pygame.K_0:
                        if is_shift_pressed:
                            type.punctuation(")")
                        else:
                            type.number("0")

            elif event.type == pygame.KEYUP:
                if 1 == 1:
                    if event.key == pygame.K_a:
                        keyup("a", activeKeys, pressedKeys, chords, type)
                    if event.key == pygame.K_b:
                        keyup("b", activeKeys, pressedKeys, chords, type)
                    if event.key == pygame.K_c:
                        keyup("c", activeKeys, pressedKeys, chords, type)
                    if event.key == pygame.K_d:
                        keyup("d", activeKeys, pressedKeys, chords, type)
                    if event.key == pygame.K_e:
                        keyup("e", activeKeys, pressedKeys, chords, type)
                    if event.key == pygame.K_f:
                        keyup("f", activeKeys, pressedKeys, chords, type)
                    if event.key == pygame.K_g:
                        keyup("g", activeKeys, pressedKeys, chords, type)
                    if event.key == pygame.K_h:
                        keyup("h", activeKeys, pressedKeys, chords, type)
                    if event.key == pygame.K_i:
                        keyup("i", activeKeys, pressedKeys, chords, type)
                    if event.key == pygame.K_j:
                        keyup("j", activeKeys, pressedKeys, chords, type)
                    if event.key == pygame.K_k:
                        keyup("k", activeKeys, pressedKeys, chords, type)
                    if event.key == pygame.K_l:
                        keyup("l", activeKeys, pressedKeys, chords, type)
                    if event.key == pygame.K_m:
                        keyup("m", activeKeys, pressedKeys, chords, type)
                    if event.key == pygame.K_n:
                        keyup("n", activeKeys, pressedKeys, chords, type)
                    if event.key == pygame.K_o:
                        keyup("o", activeKeys, pressedKeys, chords, type)
                    if event.key == pygame.K_p:
                        keyup("p", activeKeys, pressedKeys, chords, type)
                    if event.key == pygame.K_q:
                        keyup("q", activeKeys, pressedKeys, chords, type)
                    if event.key == pygame.K_r:
                        keyup("r", activeKeys, pressedKeys, chords, type)
                    if event.key == pygame.K_s:
                        keyup("s", activeKeys, pressedKeys, chords, type)
                    if event.key == pygame.K_t:
                        keyup("t", activeKeys, pressedKeys, chords, type)
                    if event.key == pygame.K_u:
                        keyup("u", activeKeys, pressedKeys, chords, type)
                    if event.key == pygame.K_v:
                        keyup("v", activeKeys, pressedKeys, chords, type)
                    if event.key == pygame.K_w:
                        keyup("w", activeKeys, pressedKeys, chords, type)
                    if event.key == pygame.K_x:
                        keyup("x", activeKeys, pressedKeys, chords, type)
                    if event.key == pygame.K_y:
                        keyup("y", activeKeys, pressedKeys, chords, type)
                    if event.key == pygame.K_z:
                        keyup("z", activeKeys, pressedKeys, chords, type)

                if event.key == pygame.K_LALT:
                    keyup("lalt", activeKeys, pressedKeys, chords, type)
                if event.key == pygame.K_RALT:
                    keyup("ralt", activeKeys, pressedKeys, chords, type)
                if event.key == pygame.K_MINUS:
                    keyup("-", activeKeys, pressedKeys, chords, type)

                if event.key == pygame.K_SEMICOLON:
                    type.add_s()
                if event.key == pygame.K_QUOTE:
                    type.add_aps()
                if event.key == pygame.K_LEFTBRACKET:
                    type.add_d()
                if event.key == pygame.K_BACKSLASH:
                    type.add_ing()
                if event.key == pygame.K_RIGHTBRACKET:
                    type.add_ed()
                if event.key == pygame.K_EQUALS:
                    type.add_es()      
                if event.key == pygame.K_BACKQUOTE:
                    type.add_er()      
                
                if event.key == pygame.K_LCTRL:
                    mode = (mode + 1) % 2

        timer += 1
        if timer >= 33:
            cursor.dark(mode)
        if timer >= 66:
            cursor.white()
            timer = 0

        draw_display(type, cursor, mode)

    pygame.quit()

if __name__ == "__main__":
    main()