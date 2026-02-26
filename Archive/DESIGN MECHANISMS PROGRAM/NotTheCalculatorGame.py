import pygame

pygame.init()
pygame.font.init()
pygame.mixer.init()

FPS = 60
HEIGHT = 500
WIDTH = 500

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Not The Calculator: The Game")

buttons = []

backgroundColour = (86, 191, 102)
buttonColour = (59, 128, 69)
fadedColour = (79, 148, 89)
WHITE = (255, 255, 255)

BUTTON_FONT = pygame.font.SysFont("comicsans", 40)
TOTAL_FONT = pygame.font.SysFont("comicsans", 60)
GOAL_FONT = pygame.font.SysFont("comicsans", 60)
MOVES_FONT = pygame.font.SysFont("comicsans", 35)

levelCounter = 1

totalDisplayPosition = pygame.Vector2(310,10)
totalDisplaySize = pygame.Vector2(180,80)
clearButtonPosition = pygame.Vector2(310,100)
clearButtonSize = pygame.Vector2(180,90)

oneGoal = 2
oneMove = 2
twoGoal = 8
twoMove = 3
threeGoal = 6
threeMove = 4
fourGoal = 200
fourMove = 4
fiveGoal = 1
fiveMove = 3

class Button:
    def __init__(self, x, y, w, h, colour, text, offset, number, operator):
        self.position = pygame.Vector2(x, y)
        self.size = pygame.Vector2(w, h)

        self.colour = colour
        self.rect = pygame.Rect(self.position.x, self.position.y, self.size.x, self.size.y)
        self.text = BUTTON_FONT.render(text, 1, WHITE)
        self.offset = pygame.Vector2(offset)

        self.number = number
        self.operator = operator

class TotalDisplay:
    def __init__(self, total):
        self.text = TOTAL_FONT.render(str(total), 1, WHITE)
        self.rect = pygame.Rect(totalDisplayPosition.x, totalDisplayPosition.y, totalDisplaySize.x, totalDisplaySize.y)

class ClearButton:
    def __init__(self):
        self.text = GOAL_FONT.render("Clear", 1, WHITE)
        self.rect = pygame.Rect(clearButtonPosition.x, clearButtonPosition.y, clearButtonSize.x, clearButtonSize.y)

def create_buttons(x, y, w, h, colour, text, offset, number, operator):
    button = Button(x, y, w, h, colour, text, offset, number, operator)
    buttons.append(button)

def draw_display(level, totalD, clearB):
    window.fill(backgroundColour)

    for button in buttons:
        pygame.draw.rect(window, button.colour, button.rect)
        window.blit(button.text, (button.position.x + button.size.x / 2 - button.offset.x,
                                  button.position.y + button.size.y / 2 - button.offset.y))

    pygame.draw.rect(window, buttonColour, totalD.rect)
    totalD.text = TOTAL_FONT.render(str(total), 1, WHITE)
    window.blit(totalD.text, (totalDisplayPosition.x + 30, totalDisplayPosition.y - 5, totalDisplaySize.x, totalDisplaySize.y))
    
    pygame.draw.rect(window, buttonColour, clearB.rect)
    totalD.text = TOTAL_FONT.render(str(total), 1, WHITE)
    window.blit(clearB.text, (clearButtonPosition.x + 20, clearButtonPosition.y - 0, clearButtonSize.x, clearButtonSize.y))

    if level == 1:
        goal = GOAL_FONT.render("Goal = " + str(oneGoal), 1, WHITE)
        window.blit(goal, (30,5))
        moves = MOVES_FONT.render("Moves = " + str(oneMove-moveCounter), 1, WHITE)
        window.blit(moves, (320, 215))
    if level == 2:
        goal = GOAL_FONT.render("Goal = " + str(twoGoal), 1, WHITE)
        window.blit(goal, (30,5))
        moves = MOVES_FONT.render("Moves = " + str(twoMove-moveCounter), 1, WHITE)
        window.blit(moves, (320, 215))
    if level == 3:
        goal = GOAL_FONT.render("Goal = " + str(threeGoal), 1, WHITE)
        window.blit(goal, (30,5))
        moves = MOVES_FONT.render("Moves = " + str(threeMove-moveCounter), 1, WHITE)
        window.blit(moves, (320, 215))
    if level == 4:
        goal = GOAL_FONT.render("Goal = " + str(fourGoal), 1, WHITE)
        window.blit(goal, (7,5))
        moves = MOVES_FONT.render("Moves = " + str(fourMove-moveCounter), 1, WHITE)
        window.blit(moves, (320, 215))
    if level == 5:
        goal = GOAL_FONT.render("Goal = " + str(fiveGoal), 1, WHITE)
        window.blit(goal, (30,5))
        moves = MOVES_FONT.render("Moves = " + str(fiveMove-moveCounter), 1, WHITE)
        window.blit(moves, (320, 215))

    pygame.display.flip()

def check_mouse_click(clearB):
    mousex, mousey = pygame.mouse.get_pos()
    for button in buttons:
        if button.rect.collidepoint(mousex, mousey):
            return button
    if clearB.rect.collidepoint(mousex, mousey):
            return clearB
    return None

def clear_buttons():
    global buttons
    buttons = []

def level_one():
    clear_buttons()
    create_buttons(10, 100, 90, 90, buttonColour, "+1", (20, 30), 1, "+")
    create_buttons(110, 100, 90, 90, fadedColour, "", (20, 30), 0, "")
    create_buttons(210, 100, 90, 90, fadedColour, "", (20, 30), 0, "")
    create_buttons(10, 200, 90, 90, fadedColour, "", (20, 30), 0, "")
    create_buttons(110, 200, 90, 90, fadedColour, "", (20, 30), 0, "")
    create_buttons(210, 200, 90, 90, fadedColour, "", (20, 30), 0, "")
    create_buttons(10, 300, 90, 90, fadedColour, "", (20, 30), 0, "")
    create_buttons(110, 300, 90, 90, fadedColour, "", (20, 30), 0, "")
    create_buttons(210, 300, 90, 90, fadedColour, "", (20, 30), 0, "")
    create_buttons(110, 400, 90, 90, fadedColour, "", (20, 30), 0, "")

def level_two():
    clear_buttons()
    create_buttons(10, 100, 90, 90, buttonColour, "+2", (20, 30), 2, "+")
    create_buttons(110, 100, 90, 90, buttonColour, "+3", (20, 30), 3, "+")
    create_buttons(210, 100, 90, 90, fadedColour, "", (20, 30), 0, "")
    create_buttons(10, 200, 90, 90, fadedColour, "", (20, 30), 0, "")
    create_buttons(110, 200, 90, 90, fadedColour, "", (20, 30), 0, "")
    create_buttons(210, 200, 90, 90, fadedColour, "", (20, 30), 0, "")
    create_buttons(10, 300, 90, 90, fadedColour, "", (20, 30), 0, "")
    create_buttons(110, 300, 90, 90, fadedColour, "", (20, 30), 0, "")
    create_buttons(210, 300, 90, 90, fadedColour, "", (20, 30), 0, "")
    create_buttons(110, 400, 90, 90, fadedColour, "", (20, 30), 0, "")

def level_three():
    clear_buttons()
    create_buttons(10, 100, 90, 90, buttonColour, "+1", (20, 30), 1, "+")
    create_buttons(110, 100, 90, 90, buttonColour, "x2", (20, 30), 2, "*")
    create_buttons(210, 100, 90, 90, fadedColour, "", (20, 30), 0, "")
    create_buttons(10, 200, 90, 90, fadedColour, "", (20, 30), 0, "")
    create_buttons(110, 200, 90, 90, fadedColour, "", (20, 30), 0, "")
    create_buttons(210, 200, 90, 90, fadedColour, "", (20, 30), 0, "")
    create_buttons(10, 300, 90, 90, fadedColour, "", (20, 30), 0, "")
    create_buttons(110, 300, 90, 90, fadedColour, "", (20, 30), 0, "")
    create_buttons(210, 300, 90, 90, fadedColour, "", (20, 30), 0, "")
    create_buttons(110, 400, 90, 90, fadedColour, "", (20, 30), 0, "")

def level_four():
    clear_buttons()
    create_buttons(10, 100, 90, 90, buttonColour, "+10", (30, 30), 10, "+")
    create_buttons(110, 100, 90, 90, buttonColour, "x4", (25, 30), 4, "*")
    create_buttons(210, 100, 90, 90, fadedColour, "", (20, 30), 0, "")
    create_buttons(10, 200, 90, 90, fadedColour, "", (20, 30), 0, "")
    create_buttons(110, 200, 90, 90, fadedColour, "", (20, 30), 0, "")
    create_buttons(210, 200, 90, 90, fadedColour, "", (20, 30), 0, "")
    create_buttons(10, 300, 90, 90, fadedColour, "", (20, 30), 0, "")
    create_buttons(110, 300, 90, 90, fadedColour, "", (20, 30), 0, "")
    create_buttons(210, 300, 90, 90, fadedColour, "", (20, 30), 0, "")
    create_buttons(110, 400, 90, 90, fadedColour, "", (20, 30), 0, "")

def level_five():
    clear_buttons()
    create_buttons(10, 100, 90, 90, buttonColour, "<<", (17, 30), 0, "<<")
    create_buttons(110, 100, 90, 90, fadedColour, "", (20, 30), 0, "")
    create_buttons(210, 100, 90, 90, fadedColour, "", (20, 30), 0, "")
    create_buttons(10, 200, 90, 90, fadedColour, "", (20, 30), 0, "")
    create_buttons(110, 200, 90, 90, fadedColour, "", (20, 30), 0, "")
    create_buttons(210, 200, 90, 90, fadedColour, "", (20, 30), 0, "")
    create_buttons(10, 300, 90, 90, fadedColour, "", (20, 30), 0, "")
    create_buttons(110, 300, 90, 90, fadedColour, "", (20, 30), 0, "")
    create_buttons(210, 300, 90, 90, fadedColour, "", (20, 30), 0, "")
    create_buttons(110, 400, 90, 90, fadedColour, "", (20, 30), 0, "")

def main():
    clock = pygame.time.Clock()
    run = True

    global total
    total = 0

    global moveCounter
    moveCounter = 0

    mouse_pressed_last_frame = False

    totalDisplay = TotalDisplay(total)
    clearButton = ClearButton()

    levelCounter = 1

    while run:
        clock.tick(FPS)

        mouse_pressed = pygame.mouse.get_pressed()[0]  # Check if left mouse button is pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False

        if levelCounter == 1:
            if total != oneGoal:
                if moveCounter < oneMove:
                    level_one()
                else:
                    total = 0
                    moveCounter = oneMove
            else:
                levelCounter = 2
                total = 0
                moveCounter = 0
        elif levelCounter == 2:
            if total != twoGoal:
                if moveCounter < twoMove:
                    level_two()
                else:
                    total = 0
                    moveCounter = 0
            else:
                levelCounter = 3
                total = 0
                moveCounter = 0
        elif levelCounter == 3:
            if total != threeGoal:
                if moveCounter < threeMove:
                    level_three()
                else:
                    total = 0
                    moveCounter = 0
            else:
                levelCounter = 4
                total = 0
                moveCounter = 0
        elif levelCounter == 4:
            if total != fourGoal:
                if moveCounter < fourMove:
                    level_four()
                else:
                    total = 0
                    moveCounter = 0
            else:
                levelCounter = 5
                total = 1234
                moveCounter = 0
        elif levelCounter == 5:
            if total != fiveGoal:
                if moveCounter < fiveMove:
                    level_five()
                else:
                    total = 0
                    moveCounter = 0
            else:
                levelCounter = 6
                total = 0
                moveCounter = 0

        if mouse_pressed and not mouse_pressed_last_frame:
            clicked_button = check_mouse_click(clearButton)
            if clicked_button != clearButton:
                if clicked_button.operator == '+':
                    total = total + clicked_button.number
                if clicked_button.operator == '-':
                    total = total - clicked_button.number
                if clicked_button.operator == '*':
                    total = total * clicked_button.number
                if clicked_button.operator == '<<':
                    total = int(str(total)[:-1])
                moveCounter += 1
            else:
                total = 0
                moveCounter = 0

        mouse_pressed_last_frame = mouse_pressed

        draw_display(levelCounter, totalDisplay, clearButton)

    pygame.quit()

if __name__ == "__main__":
    main()
