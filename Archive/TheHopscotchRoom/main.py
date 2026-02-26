#The Hopscotch Room v1.0.0
#Made By Jonathan Blyth
#Based on The Libarary / The Hopscotch Room in Arkanae, The Medoran Chronicles, by Lynentte Loni

#All Might States:
#MENU
#SCORE
#GAME

#Pieces of Light - Tobias Voigt
#Music from #Uppbeat (free for Creators!):
#https://uppbeat.io/t/tobias-voigt/pieces-of-light

import pygame
import random
import os

pygame.init()
pygame.font.init()
pygame.mixer.init()

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(ROOT_DIR, "assets")
FONTS_DIR = os.path.join(ASSETS_DIR, "fonts")
AUDIO_DIR = os.path.join(ASSETS_DIR, "audio")
IMAGES_DIR = os.path.join(ASSETS_DIR, "images")
LOGS_DIR = os.path.join(ASSETS_DIR, "logs")
MENU_DIR = os.path.join(ASSETS_DIR, "menu")

FPS = 60
HEIGHT = 560
WIDTH = 1260
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TheHopscotchRoom")

#Handle File Transfer
if True:
    def read_file(filename):
        output = {}
        with open(filename, "r") as file:
            for line in file:
                key = line.strip().split("=")[0]
                value = line.strip().split("=")[1]
                output[key] = value
        return output
    
    def write_to_line(filename, lineNum, data):
        write_data = {}

        with open(filename, "r") as file:
            for line in file:
                key = line.strip().split("=")[0]
                value = line.strip().split("=")[1]
                write_data[key] = value

        keys = list(write_data.keys())
        lineKey = keys[lineNum]
        write_data[lineKey] = int(float(data))

        with open(filename, "w") as file:
            for key, value in write_data.items():
                file.write(f"{key}={value}\n")
                print(f"{key}={value}")

COLOURS = {"BLACK": (0,0,0), "WHITE": (255,255,255), "GREEN": (0,255,0), "RED": (255,0,0), "BLUE": (0,0,255), "ENDS": (153, 102, 0), "GREY":(154, 160, 166), "BROWN":(103, 77, 48), "ORANGE":(255, 191, 128)}

titleFont = pygame.font.Font(os.path.join(FONTS_DIR, "EagleLake-Regular.ttf"), 70)
smallTitleFont = pygame.font.Font(os.path.join(FONTS_DIR, "EagleLake-Regular.ttf"), 30)
mediumTitleFont = pygame.font.Font(os.path.join(FONTS_DIR, "EagleLake-Regular.ttf"), 50)
timerFont = pygame.font.Font(os.path.join(FONTS_DIR, "Technology.ttf"), 200)

pygame.mixer.music.load(os.path.join(AUDIO_DIR, "pieces-of-light-tobias-voigt-main-version-19286-03-04.mp3"))

#Handle Ends
if True:
    EndsImage = pygame.image.load(os.path.join(IMAGES_DIR, "tiles", "Ends.png"))

    def draw_ends():
        for i in range(8):
            window.blit(EndsImage, (0,i*70))
        for i in range(8):
            window.blit(EndsImage, (WIDTH-70,i*70))

#Handle Tiles
if True:
    # Ends
    EndsImage = pygame.transform.scale(
        pygame.image.load(os.path.join(IMAGES_DIR, "tiles", "Ends.png")).convert_alpha(), (70,70)
    )

    # Tiles
    RedImage = pygame.transform.scale(pygame.image.load(os.path.join(IMAGES_DIR, "tiles", "Red.png")).convert_alpha(),(70,70))
    GreyImage = pygame.transform.scale(pygame.image.load(os.path.join(IMAGES_DIR, "tiles", "Grey.png")).convert_alpha(),(70,70))
    BlueImage = pygame.transform.scale(pygame.image.load(os.path.join(IMAGES_DIR, "tiles", "Blue.png")).convert_alpha(),(70,70))
    BrownImage = pygame.transform.scale(pygame.image.load(os.path.join(IMAGES_DIR, "tiles", "Brown.png")).convert_alpha(),(70,70))
    BlackImage = pygame.transform.scale(pygame.image.load(os.path.join(IMAGES_DIR, "tiles", "Black.png")).convert_alpha(),(70,70))

    # Player
    PlayerImage = pygame.image.load(os.path.join(IMAGES_DIR, "player", "Player.png")).convert_alpha()

    # Menu
    InstructionsImage = pygame.transform.scale(
        pygame.image.load(os.path.join(IMAGES_DIR, "menu", "Instructions.png")).convert_alpha(), (634*0.7,625*0.7)
    )
    ControlsImage = pygame.transform.scale(
        pygame.image.load(os.path.join(IMAGES_DIR, "menu", "Controls.png")).convert_alpha(), (509*0.5,508*0.5)
    )
    VolumeButtonImage = pygame.transform.scale(
        pygame.image.load(os.path.join(IMAGES_DIR, "menu", "Volume.jpg")).convert_alpha(), (271*0.15, 289*0.15)
    )
    VolumeMuteButtonImage = pygame.transform.scale(
        pygame.image.load(os.path.join(IMAGES_DIR, "menu", "VolumeMute.jpg")).convert_alpha(), (290*0.15, 290*0.15)
    )


    List_Tiles = []
    TILE_TYPES = ["RED", "GREY", "BLUE", "BROWN", "BLACK"]
    TILE_IMAGES = {"RED":RedImage, "GREY":GreyImage, "BLUE":BlueImage, "BROWN":BrownImage, "BLACK":BlackImage}
    TILE_SIZE = 70

    class Tile:
        def __init__(self, x, y, difficulty, settings):
            newChance = random.randint(0, 99)
            if difficulty["EASY"]:
                if 0 <= newChance < int(settings["easy_brownChance"]):
                    newType = "BROWN"
                if int(settings["easy_brownChance"]) <= newChance < int(settings["easy_brownChance"]) + int(settings["easy_greyChance"]):
                    newType = "GREY"
                if int(settings["easy_brownChance"]) + int(settings["easy_greyChance"]) <= newChance < int(settings["easy_brownChance"]) + int(settings["easy_greyChance"]) + int(settings["easy_blueChance"]):
                    newType = "BLUE"
                if int(settings["easy_brownChance"]) + int(settings["easy_greyChance"]) + int(settings["easy_blueChance"]) <= newChance < int(settings["easy_brownChance"]) + int(settings["easy_greyChance"]) + int(settings["easy_blueChance"]) + int(settings["easy_redChance"]):
                    newType = "RED"
                if int(settings["easy_brownChance"]) + int(settings["easy_greyChance"]) + int(settings["easy_blueChance"]) + int(settings["easy_redChance"]) <= newChance < 100:
                    newType = "BLACK"

            if difficulty["MEDIUM"]:
                if 0 <= newChance < int(settings["medium_brownChance"]):
                    newType = "BROWN"
                if int(settings["medium_brownChance"]) <= newChance < int(settings["medium_brownChance"]) + int(settings["medium_greyChance"]):
                    newType = "GREY"
                if int(settings["medium_brownChance"]) + int(settings["medium_greyChance"]) <= newChance < int(settings["medium_brownChance"]) + int(settings["medium_greyChance"]) + int(settings["medium_blueChance"]):
                    newType = "BLUE"
                if int(settings["medium_brownChance"]) + int(settings["medium_greyChance"]) + int(settings["medium_blueChance"]) <= newChance < int(settings["medium_brownChance"]) + int(settings["medium_greyChance"]) + int(settings["medium_blueChance"]) + int(settings["medium_redChance"]):
                    newType = "RED"
                if int(settings["medium_brownChance"]) + int(settings["medium_greyChance"]) + int(settings["medium_blueChance"]) + int(settings["medium_redChance"]) <= newChance < 100:
                    newType = "BLACK"

            if difficulty["HARD"]:
                if 0 <= newChance < int(settings["hard_brownChance"]):
                    newType = "BROWN"
                if int(settings["hard_brownChance"]) <= newChance < int(settings["hard_brownChance"]) + int(settings["hard_greyChance"]):
                    newType = "GREY"
                if int(settings["hard_brownChance"]) + int(settings["hard_greyChance"]) <= newChance < int(settings["hard_brownChance"]) + int(settings["hard_greyChance"]) + int(settings["hard_blueChance"]):
                    newType = "BLUE"
                if int(settings["hard_brownChance"]) + int(settings["hard_greyChance"]) + int(settings["hard_blueChance"]) <= newChance < int(settings["hard_brownChance"]) + int(settings["hard_greyChance"]) + int(settings["hard_blueChance"]) + int(settings["hard_redChance"]):
                    newType = "RED"
                if int(settings["hard_brownChance"]) + int(settings["hard_greyChance"]) + int(settings["hard_blueChance"]) + int(settings["hard_redChance"]) <= newChance < 100:
                    newType = "BLACK"


            self.type = newType
            self.position = pygame.Vector2(x*70, y*70)
            self.image = TILE_IMAGES[self.type]
            self.rect = pygame.Rect(self.position.x, self.position.y, TILE_SIZE, TILE_SIZE)

            self.outlineRect = pygame.Rect(self.position.x, self.position.y, TILE_SIZE, TILE_SIZE)
            self.changeTimer = 0
            self.changing = False

        def start_change(self, newType):
            self.changeTimer = 0
            self.newType = newType
            self.changing = True

        def change(self, player):
            if self.changing:
                self.changeTimer += 1
                pygame.draw.rect(window, COLOURS["ORANGE"], self.outlineRect, 3)
                if self.changeTimer >= player.tileChangeTime:
                    self.type = self.newType
                    self.image = TILE_IMAGES[self.type]
                    self.changing = False

    def create_tiles(difficulty, settings):
        List_Tiles.clear()
        for x in range(1,17):
            List_Tiles_x = []
            for y in range(0,8):
                tile = Tile(x, y, difficulty, settings)
                List_Tiles_x.append(tile)
            List_Tiles.append(List_Tiles_x)

    def draw_tiles(player):
        for List_Tiles_x in List_Tiles:
            for tile in List_Tiles_x:
                window.blit(tile.image, tile.rect)
                tile.change(player)

    def change_tiles(player, difficulty, settings):
        for List_Tiles_x in List_Tiles:
            for tile in List_Tiles_x:
                if random.randint(0,player.tileChangeChance) == 0 and not tile.changing:
                    newChance = random.randint(0, 99)
                    if difficulty["EASY"]:
                        if 0 <= newChance < int(settings["easy_brownChance"]):
                            newType = "BROWN"
                        if int(settings["easy_brownChance"]) <= newChance < int(settings["easy_brownChance"]) + int(settings["easy_greyChance"]):
                            newType = "GREY"
                        if int(settings["easy_brownChance"]) + int(settings["easy_greyChance"]) <= newChance < int(settings["easy_brownChance"]) + int(settings["easy_greyChance"]) + int(settings["easy_blueChance"]):
                            newType = "BLUE"
                        if int(settings["easy_brownChance"]) + int(settings["easy_greyChance"]) + int(settings["easy_blueChance"]) <= newChance < int(settings["easy_brownChance"]) + int(settings["easy_greyChance"]) + int(settings["easy_blueChance"]) + int(settings["easy_redChance"]):
                            newType = "RED"
                        if int(settings["easy_brownChance"]) + int(settings["easy_greyChance"]) + int(settings["easy_blueChance"]) + int(settings["easy_redChance"]) <= newChance < 100:
                            newType = "BLACK"

                    if difficulty["MEDIUM"]:
                        if 0 <= newChance < int(settings["medium_brownChance"]):
                            newType = "BROWN"
                        if int(settings["medium_brownChance"]) <= newChance < int(settings["medium_brownChance"]) + int(settings["medium_greyChance"]):
                            newType = "GREY"
                        if int(settings["medium_brownChance"]) + int(settings["medium_greyChance"]) <= newChance < int(settings["medium_brownChance"]) + int(settings["medium_greyChance"]) + int(settings["medium_blueChance"]):
                            newType = "BLUE"
                        if int(settings["medium_brownChance"]) + int(settings["medium_greyChance"]) + int(settings["medium_blueChance"]) <= newChance < int(settings["medium_brownChance"]) + int(settings["medium_greyChance"]) + int(settings["medium_blueChance"]) + int(settings["medium_redChance"]):
                            newType = "RED"
                        if int(settings["medium_brownChance"]) + int(settings["medium_greyChance"]) + int(settings["medium_blueChance"]) + int(settings["medium_redChance"]) <= newChance < 100:
                            newType = "BLACK"

                    if difficulty["HARD"]:
                        if 0 <= newChance < int(settings["hard_brownChance"]):
                            newType = "BROWN"
                        if int(settings["hard_brownChance"]) <= newChance < int(settings["hard_brownChance"]) + int(settings["hard_greyChance"]):
                            newType = "GREY"
                        if int(settings["hard_brownChance"]) + int(settings["hard_greyChance"]) <= newChance < int(settings["hard_brownChance"]) + int(settings["hard_greyChance"]) + int(settings["hard_blueChance"]):
                            newType = "BLUE"
                        if int(settings["hard_brownChance"]) + int(settings["hard_greyChance"]) + int(settings["hard_blueChance"]) <= newChance < int(settings["hard_brownChance"]) + int(settings["hard_greyChance"]) + int(settings["hard_blueChance"]) + int(settings["hard_redChance"]):
                            newType = "RED"
                        if int(settings["hard_brownChance"]) + int(settings["hard_greyChance"]) + int(settings["hard_blueChance"]) + int(settings["hard_redChance"]) <= newChance < 100:
                            newType = "BLACK"

                    tile.start_change(newType)

#Hangle Grid
if True:
    def draw_grid():
        for x in range(0, WIDTH, 70):
            pygame.draw.line(window, COLOURS["BLACK"], (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, 70):
            pygame.draw.line(window, COLOURS["BLACK"], (0, y), (WIDTH, y))

#Handle Player
PlayerImage = pygame.image.load(os.path.join(IMAGES_DIR, "player", "Player.png")).convert_alpha()
class Player:
    def __init__(self, settings):
        self.size = pygame.Vector2(50, 50)
        self.position = pygame.Vector2((TILE_SIZE-self.size.x)/2, (TILE_SIZE*4)+((TILE_SIZE-self.size.y)/2))
        self.image = PlayerImage
        self.rect = pygame.Rect(self.position.x, self.position.y, self.size.x, self.size.y)
        self.tileOn = None
        self.tileOnPosition = None
        self.numb = False
        self.greyTimer = 0
        self.blueTimer = 0
        self.deaths = 0

        self.greySpeed = int(settings["easy_greySpeed"])
        self.tileChangeChance = int(settings["easy_tileChangeChance"])
        self.tileChangeTime = FPS*int(settings["easy_tileChangeTime"])
        self.blueFreezeTime = FPS*int(settings["easy_blueFreezeTime"])

    def draw(self):
        window.blit(self.image, self.rect)

    def floor_logic(self, difficulty, settings):
        if self.tileOn == "RED":
            red_touched(self)
        elif self.tileOn == "BLUE":
            blue_touched(self)
        elif self.tileOn == "GREY":
            grey_touched(self, difficulty, settings)
        elif self.tileOn == "BLACK":
            black_touched(self)

        if difficulty["EASY"]:
            key = "easy_greySpeed"
        elif difficulty["MEDIUM"]:
            key = "medium_greySpeed"
        elif difficulty["HARD"]:
            key = "hard_greySpeed"

        if self.tileOn != "GREY":
            self.greyTimer = 0
        if self.tileOn != "BLUE":
            self.numb = False

        if self.greyTimer >= float(settings[key])-0.1:
            self.greyTimer = 0
            self.reset()

    def collisions(self):
        if self.position.x > TILE_SIZE and self.position.x < (WIDTH-TILE_SIZE):
            countery = 0
            for List_Tiles_x in List_Tiles:
                counterx = 0
                for tile in List_Tiles_x:
                    if self.rect.colliderect(tile.rect):
                        self.tileOn = tile.type
                        self.tileOnPosition = pygame.Vector2(counterx, countery)
                    counterx += 1
                countery += 1
        else:
            self.tileOn = None
            self.tileOnPosition = None

    def move(self, direction):
        dx = direction.x * TILE_SIZE 
        dy = direction.y * TILE_SIZE
        if 0 <= (self.position.x + dx) <= WIDTH and 0 <= (self.position.y + dy) <= HEIGHT:
            self.position += pygame.Vector2(dx, dy)
        self.rect = pygame.Rect(self.position.x, self.position.y, self.size.x, self.size.y)

        self.collisions()

    def reset(self):
        self.position = pygame.Vector2((TILE_SIZE-self.size.x)/2, (TILE_SIZE*4)+((TILE_SIZE-self.size.y)/2))
        self.rect = pygame.Rect(self.position.x, self.position.y, self.size.x, self.size.y)
        self.tileOn = None
        self.deaths += 1

#Floor Logic
if True:
    def red_touched(player):
        player.reset()

    def blue_touched(player):
        player.blueTimer += 1
        player.numb = True
        if player.blueTimer >= player.blueFreezeTime:
            x = int(player.tileOnPosition.x)
            y = int(player.tileOnPosition.y)
            currentTile = List_Tiles[y][x]

            currentTile.type = "BROWN"
            currentTile.image = TILE_IMAGES["BROWN"]

            player.blueTimer = 0

    def grey_touched(player, difficulty, settings):
        player.greyTimer += 1/FPS
        if difficulty["EASY"]:
            key = "easy_greySpeed"
        elif difficulty["MEDIUM"]:
            key = "medium_greySpeed"
        elif difficulty["HARD"]:
            key = "hard_greySpeed"
        GreyTimerText = str(round(float(settings[key]) - player.greyTimer,2))
        GreyTimerRender = pygame.font.Font.render(timerFont, GreyTimerText, 1, COLOURS["WHITE"])
        window.blit(GreyTimerRender, ((WIDTH/2)-150, 400))

    def black_touched(player):
        if player.position.x > TILE_SIZE * 3:
            player.move(pygame.Vector2(-3, 0))
        elif player.position.x > TILE_SIZE * 2:
            player.move(pygame.Vector2(-2, 0))
        elif player.position.x > TILE_SIZE * 1:
            player.move(pygame.Vector2(-1, 0))

#Handle Menu
if True:
    InstructionsImage = pygame.transform.scale(
    pygame.image.load(os.path.join(MENU_DIR, "Instructions.png")).convert_alpha(), (634*0.7, 625*0.7)
    )
    ControlsImage = pygame.transform.scale(
    pygame.image.load(os.path.join(MENU_DIR, "Controls.png")).convert_alpha(), (509*0.5, 508*0.5)
    )
    VolumeButtonImage = pygame.transform.scale(
    pygame.image.load(os.path.join(MENU_DIR, "Volume.jpg")).convert_alpha(), (271*0.15, 289*0.15)
    )
    VolumeMuteButtonImage = pygame.transform.scale(
    pygame.image.load(os.path.join(MENU_DIR, "VolumeMute.jpg")).convert_alpha(), (290*0.15, 290*0.15)
    )
    VolumeButtonRect = pygame.Rect(1120,45, 290*0.15,290*0.15)

    EasyButtonRect = pygame.Rect(WIDTH/2+200, 150, 350, 105)
    MediumButtonRect = pygame.Rect(WIDTH/2+200, 150+125, 350, 105)
    HardButtonRect = pygame.Rect(WIDTH/2+200, 150+250, 350, 105)

    def draw_menu(difficulty, volume):
        #Title
        window.blit(TitleTextRender, ((WIDTH/2)-(TitleTextRender.get_width()/2), 5))

        #Mouse Hover
        mousePos = pygame.mouse.get_pos()
        StartButtonColour = COLOURS["BLUE"] if StartButtonRect.collidepoint(mousePos) else COLOURS["BLACK"]

        if not difficulty["EASY"]:
            EasyButtonColour = COLOURS["BLUE"] if EasyButtonRect.collidepoint(mousePos) else COLOURS["BLACK"]
        else:
            EasyButtonColour = COLOURS["GREEN"]

        if not difficulty["MEDIUM"]:
            MediumButtonColour = COLOURS["BLUE"] if MediumButtonRect.collidepoint(mousePos) else COLOURS["BLACK"]
        else:
            MediumButtonColour = COLOURS["GREEN"]

        if not difficulty["HARD"]:
            HardButtonColour = COLOURS["BLUE"] if HardButtonRect.collidepoint(mousePos) else COLOURS["BLACK"]
        else:
            HardButtonColour = COLOURS["GREEN"]

        #Start Button
        pygame.draw.rect(window, StartButtonColour, StartButtonRect, 5)
        StartButtonTextRender = pygame.font.Font.render(titleFont,"Start", 1, StartButtonColour)
        window.blit(StartButtonTextRender, ((WIDTH/2)-(StartButtonTextRender.get_width()/2), StartButtonRect.y + (StartButtonRect.height/2) - (StartButtonTextRender.get_height()/2)))

        #Easy Button
        pygame.draw.rect(window, EasyButtonColour, EasyButtonRect, 5)
        EasyButtonTextRender = pygame.font.Font.render(titleFont,"Easy", 1, EasyButtonColour)
        window.blit(EasyButtonTextRender, ((EasyButtonRect.x+(EasyButtonRect.width/2))-(EasyButtonTextRender.get_width()/2), (EasyButtonRect.y + (EasyButtonRect.height/2)) - (EasyButtonTextRender.get_height()/2)))

        #Medium Button
        pygame.draw.rect(window, MediumButtonColour, MediumButtonRect, 5)
        MediumButtonTextRender = pygame.font.Font.render(titleFont,"Medium", 1, MediumButtonColour)
        window.blit(MediumButtonTextRender, ((MediumButtonRect.x+(MediumButtonRect.width/2))-(MediumButtonTextRender.get_width()/2), (MediumButtonRect.y + (MediumButtonRect.height/2)) - (MediumButtonTextRender.get_height()/2)))

        #Hard Button
        pygame.draw.rect(window, HardButtonColour, HardButtonRect, 5)
        HardButtonTextRender = pygame.font.Font.render(titleFont,"Hard", 1, HardButtonColour)
        window.blit(HardButtonTextRender, ((HardButtonRect.x+(HardButtonRect.width/2))-(HardButtonTextRender.get_width()/2), (HardButtonRect.y + (HardButtonRect.height/2)) - (HardButtonTextRender.get_height()/2)))

        #Instructions
        window.blit(InstructionsImage, (34,108))

        #Controls
        window.blit(ControlsImage, ((WIDTH/2)-(ControlsImage.get_width()/2),150))

        #Volume Button
        if volume:
            window.blit(VolumeButtonImage, VolumeButtonRect)
        else:
            window.blit(VolumeMuteButtonImage, VolumeButtonRect)

    def start_game(player, difficulty, settings):
        create_tiles(difficulty, settings)
        player = Player(settings)
        if difficulty["EASY"]:
            player.greySpeed = float(settings["easy_greySpeed"])
            player.tileChangeChance = int(settings["easy_tileChangeChance"])
            player.tileChangeTime = FPS*int(settings["easy_tileChangeTime"])
            player.blueFreezeTime = FPS*int(settings["easy_blueFreezeTime"])
        elif difficulty["MEDIUM"]:
            player.greySpeed = float(settings["medium_greySpeed"])
            player.tileChangeChance = int(settings["medium_tileChangeChance"])
            player.tileChangeTime = FPS*int(settings["medium_tileChangeTime"])
            player.blueFreezeTime = FPS*int(settings["medium_blueFreezeTime"])
        elif difficulty["HARD"]:
            player.greySpeed = float(settings["hard_greySpeed"])
            player.tileChangeChance = int(settings["hard_tileChangeChance"])
            player.tileChangeTime = FPS*int(settings["hard_tileChangeTime"])
            player.blueFreezeTime = FPS*int(settings["hard_blueFreezeTime"])

#Handle Score Screen
if True:
    class HighScoreLogic:
        def __init__(self):
            self.written = False
            self.highScoreBeaten = False
            self.oldHighScore = 0
            self.difficultyText = ""

    PlayAgainButtonRect = pygame.Rect(WIDTH/2-250, HEIGHT/2-60, 500, 120)
    MainMenuButtonRect = pygame.Rect(WIDTH/2-250, HEIGHT/2+100, 500, 120)

    def draw_score_screen(time, difficulty, scores, highScoreLogic, player):
        window.fill(COLOURS["WHITE"])

        #Score
        minutes = int(time // 60)
        seconds = int(time - (minutes * 60))
        ScoreTextRender = pygame.font.Font.render(titleFont, "Your Time:  " + str(minutes)+"m "+str(seconds)+"s", 1, COLOURS["BLACK"])
        window.blit(ScoreTextRender, ((WIDTH/2)-(ScoreTextRender.get_width()/2), 15))

        #High Score
        if not highScoreLogic.written:
            if difficulty["EASY"]:
                highScoreLogic.oldHighScore = int(scores["easyHighScoreSec"])
                highScoreLogic.difficultyText = "Easy"
                line = 0
            elif difficulty["MEDIUM"]:
                highScoreLogic.oldHighScore = int(scores["mediumHighScoreSec"])
                highScoreLogic.difficultyText = "Medium"
                line = 1
            elif difficulty["HARD"]:
                highScoreLogic.oldHighScore = int(scores["hardHighScoreSec"])
                highScoreLogic.difficultyText = "Hard"
                line = 2
        highScore = highScoreLogic.oldHighScore
        difficultyText = highScoreLogic.difficultyText
        
        highScoreLogic.highScoreBeaten = True if time < highScore else False
        if highScoreLogic.highScoreBeaten:
            highScoreTextRender = pygame.font.Font.render(mediumTitleFont, "New "+difficultyText+" High Score!!!", 1, COLOURS["BLACK"])
            window.blit(highScoreTextRender, ((WIDTH/2)-(highScoreTextRender.get_width()/2), 120))
            pygame.draw.rect(window, COLOURS["GREEN"], (0, 0, WIDTH, HEIGHT), 8)
            if not highScoreLogic.written:
                write_to_line(os.path.join(LOGS_DIR, "scores.txt"), line, str(time))
                highScoreLogic.written = True
        else:
            highScoreTextRender = pygame.font.Font.render(mediumTitleFont, difficultyText+" High Score:  "+str(highScore // 60)+"m "+str(highScore-((highScore//60) * 60))+"s", 1, COLOURS["BLACK"])
            window.blit(highScoreTextRender, ((WIDTH/2)-(highScoreTextRender.get_width()/2), 120))
            pygame.draw.rect(window, COLOURS["RED"], (0, 0, WIDTH, HEIGHT), 8)

        #Mouse Hover
        mousePos = pygame.mouse.get_pos()
        PlayAgainButtonColour = COLOURS["BLUE"] if PlayAgainButtonRect.collidepoint(mousePos) else COLOURS["BLACK"]
        MainMenuButtonColour = COLOURS["BLUE"] if MainMenuButtonRect.collidepoint(mousePos) else COLOURS["BLACK"]

        #Play Again Button
        pygame.draw.rect(window, PlayAgainButtonColour, PlayAgainButtonRect, 5)
        PlayAgainButtonTextRender = pygame.font.Font.render(titleFont,"Play Again", 1, PlayAgainButtonColour)
        window.blit(PlayAgainButtonTextRender, ((WIDTH/2)-(PlayAgainButtonTextRender.get_width()/2), PlayAgainButtonRect.y + (PlayAgainButtonRect.height/2) - (PlayAgainButtonTextRender.get_height()/2)))

        #Play Again Difficulty
        if difficulty["EASY"]:
            currentDifficultyText = "Easy"
        elif difficulty["MEDIUM"]:
            currentDifficultyText = "Medium"
        elif difficulty["HARD"]:
            currentDifficultyText = "Hard"
        currentDifficultyTextRender1 = pygame.font.Font.render(smallTitleFont, "Current Difficulty:", 1, COLOURS["BLACK"])
        currentDifficultyTextRender2 = pygame.font.Font.render(smallTitleFont, currentDifficultyText, 1, COLOURS["BLACK"])
        window.blit(currentDifficultyTextRender1, (910, 225))
        window.blit(currentDifficultyTextRender2, (910, 225+5+currentDifficultyTextRender1.get_height()))

        #Deaths
        DeathsText = str(player.deaths)
        DeathsTextRender = pygame.font.Font.render(mediumTitleFont, "Deaths = "+DeathsText, 1, COLOURS["BLACK"])
        window.blit(DeathsTextRender, (40,235))

        #Main Menu Button
        pygame.draw.rect(window, MainMenuButtonColour, MainMenuButtonRect, 5)
        MainMenuButtonTextRender = pygame.font.Font.render(titleFont,"Main Menu", 1, MainMenuButtonColour)
        window.blit(MainMenuButtonTextRender, ((WIDTH/2)-(MainMenuButtonTextRender.get_width()/2), MainMenuButtonRect.y + (MainMenuButtonRect.height/2) - (MainMenuButtonTextRender.get_height()/2)))

def draw_display(player, state, difficulty, settings):
    window.fill(COLOURS["WHITE"])
    if state == "MENU":
        draw_menu(difficulty, settings)
    elif state == "GAME":
        draw_ends()
        draw_tiles(player)
        draw_grid()
        player.draw()

def main():
    clock = pygame.time.Clock()
    run = True
    settings = read_file("assets/logs/settings.txt")
    scores = read_file("assets/logs/scores.txt")
    state = "MENU"
    difficulty = {"EASY": True, "MEDIUM": False, "HARD": False}
    player = Player(settings)
    highScoreLogic = HighScoreLogic()
    volume = True

    startTicks = pygame.time.get_ticks()

    pygame.mixer.music.play(-1)

    while run:
        clock.tick(FPS)
        settings = read_file(os.path.join(LOGS_DIR, "settings.txt"))
        scores = read_file(os.path.join(LOGS_DIR, "scores.txt"))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.mixer.music.stop()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                state = "MENU"
                player.position = pygame.Vector2((TILE_SIZE-player.size.x)/2, (TILE_SIZE*2)+((TILE_SIZE-player.size.y)/2))
                player.rect = pygame.Rect(player.position.x, player.position.y, player.size.x, player.size.y)

            if event.type == pygame.KEYDOWN and not player.numb:
                if event.key == pygame.K_q:
                    player.move(pygame.Vector2(-1, -1))
                elif event.key == pygame.K_e:
                    player.move(pygame.Vector2(1, -1))
                elif event.key == pygame.K_z:
                    player.move(pygame.Vector2(-1, 1))
                elif event.key == pygame.K_c:
                    player.move(pygame.Vector2(1, 1))

                elif event.key == pygame.K_w:
                    player.move(pygame.Vector2(0, -1))
                elif event.key == pygame.K_s:
                    player.move(pygame.Vector2(0, 1))
                elif event.key == pygame.K_a:
                    player.move(pygame.Vector2(-1, 0))
                elif event.key == pygame.K_d:
                    player.move(pygame.Vector2(1, 0))

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if state == "MENU":
                    if StartButtonRect.collidepoint(pygame.mouse.get_pos()):
                        start_game(player, difficulty, settings)
                        state = "GAME"
                        startTicks = pygame.time.get_ticks()

                    elif VolumeButtonRect.collidepoint(pygame.mouse.get_pos()):
                        volume = False if volume else True             

                    elif EasyButtonRect.collidepoint(pygame.mouse.get_pos()):
                        difficulty["EASY"] = True
                        difficulty["MEDIUM"] = False
                        difficulty["HARD"] = False
                    elif MediumButtonRect.collidepoint(pygame.mouse.get_pos()):
                        difficulty["EASY"] = False
                        difficulty["MEDIUM"] = True
                        difficulty["HARD"] = False
                    elif HardButtonRect.collidepoint(pygame.mouse.get_pos()):
                        difficulty["EASY"] = False
                        difficulty["MEDIUM"] = False
                        difficulty["HARD"] = True
                if state == "SCORE":
                    if PlayAgainButtonRect.collidepoint(pygame.mouse.get_pos()):
                        player.position = pygame.Vector2((TILE_SIZE-player.size.x)/2, (TILE_SIZE*2)+((TILE_SIZE-player.size.y)/2))
                        player.rect = pygame.Rect(player.position.x, player.position.y, player.size.x, player.size.y)
                        startTicks = pygame.time.get_ticks()
                        start_game(player, difficulty, settings)
                        state = "GAME"
                    elif MainMenuButtonRect.collidepoint(pygame.mouse.get_pos()):
                        main()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKQUOTE:
                player.move(pygame.Vector2(17, 0))

        if run:
            if not state == "SCORE":
                draw_display(player, state, difficulty, volume)
            else:
                draw_score_screen(round(time,0), difficulty, scores, highScoreLogic, player)
            
            if state == "GAME":
                player.floor_logic(difficulty, settings)
                change_tiles(player, difficulty, settings)
                player.collisions()
                time = (pygame.time.get_ticks() - startTicks) / 1000
            
            if player.position.x > WIDTH-TILE_SIZE:
                state = "SCORE"

        pygame.display.flip()

        if volume:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()

    pygame.quit()

if __name__ == "__main__":
    main()