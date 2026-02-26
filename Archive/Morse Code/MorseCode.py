import pygame
import os
pygame.init()

FPS = 60
WIDTH, HEIGHT = 100, 100
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MorseDeCode")

BLACK = (0, 0, 0)

morseList = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    ".-.": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
}

def draw_display(finalText, elapsedTime):
    window.fill(BLACK)
    os.system('cls')
    print(finalText)
    print(elapsedTime)

def currentText(ctm):
    if ctm in morseList:
        ct = morseList[ctm]
    else:
        return "*"

    return ct

def main():
    run = True
    clock = pygame.time.Clock()

    leftClicked = False
    rightClicked = False
    finalText = ""
    currentTextM = ""
    startTime = 0
    elapsedTime = 0
    spaced = False

    while run:
        elapsedTime += clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and not leftClicked:
                    currentTextM += "."
                    leftClicked = True
                    startTime = elapsedTime
                    spaced = False
                elif event.button == 3 and not rightClicked:
                    currentTextM += "-"
                    rightClicked = True
                    startTime = elapsedTime
                    spaced = False

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    leftClicked = False
                elif event.button == 3:
                    rightClicked = False

        if (elapsedTime - startTime) >= 1000 and not spaced:
            finalText += currentText(currentTextM) + " "
            startTime = elapsedTime
            currentTextM = ""
            spaced = True

        draw_display(finalText, elapsedTime)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()