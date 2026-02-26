#CREATED AND PROGRAMMED BY JONATHAN BLYTH
#Illustrated by Kallum Morris
#MADE FOR YEAR 9 2024 DESIGN MECHANISMS AND ROBOTICS CLASS

#Abandoned Space Station Explorer v2.0.0

#Thanks to Danijel Zambo from Uppbeat for Game Music

'''Game Music License:
Music from #Uppbeat (free for Creators!):
https://uppbeat.io/t/danijel-zambo/stardust
'''

import pygame
import math
import os
import time
import random

pygame.init()
pygame.font.init()

pygame.mixer.init()
pygame.mixer.set_num_channels(3)
channelNum = 3
#Channels:
#0 Music (Music)
#1 Footsteps (SFX)
#2 Gun (SFX)

#Folder Roots
audioF = "Assets/Audio"
imagesF = "Assets/Images"
fontsF = "Assets/Fonts"

#Screen Parameters
FPS = 60
HEIGHT = 500
WIDTH = 500

#Colours
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
YELLOW = (255,255,0)
ORANGE = (250,90,0)

#Create Screen
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AbandonedSpaceStationExplorer")

#ALL MIGHTY STATES:
#-2 Options
#-1 Intro
#0 Menu
#1 Docking Bay
#2 Lobby
#2.5 (H/h) Hallway
#3 Officer's Quarters 1
#4 Officer's Quarters 2
#5 Ensuite
#6 Captain's Quarters
#7 Control Room
#8 Storage Room (END OF GAME)

#READ THESE INSTRUCTIONS FOR COMMAND PROMPT USE:
'''COMMAND PROMPTS:
Access by pressing BACKQUOTE (`) during game

Format:
state.key.command=value
----------------------------------
state
    key
        command
            value/possible values
----------------------------------
(Should be complete)
set
    door
        1locked
            true,false
        2locked1
            true,false
        2locked2
            true,false
        3locked
            true,false
        4locked
            true,false
    astronaut
        health
            >0
        speed
            >0
        x
            >0<WIDTH
        y
            >0<HEIGHT
        lives
            >0
        damage
            >0
        inventory
            0,1,2,3,23,4
    options
        mvb
            true,false
        sib
            true,false
    state
        load
            1,2,h,3,4,5,6,7,8
    injure
        faint
        die
add
    astronaut
        health
            >0
        speed
            >0
        x
            >0<WIDTH
        y
            >0<HEIGHT
        lives
            >0
        damage
            >0
----------------------------------
WHITE Screen = Default
GREEN Screen = Command has been Run
RED Screen = Error with entered Command 
^^^(Refer to Terminal for State,Key,Command of error)
'''

#Start Settings
MVB = True
SIB = False
ScrollSpeed = 40
VideoSpeed = 350

#Keys
characters = []
keys = {
    pygame.K_a: 'a',
    pygame.K_b: 'b',
    pygame.K_c: 'c',
    pygame.K_d: 'd',
    pygame.K_e: 'e',
    pygame.K_f: 'f',
    pygame.K_g: 'g',
    pygame.K_h: 'h',
    pygame.K_i: 'i',
    pygame.K_j: 'j',
    pygame.K_k: 'k',
    pygame.K_l: 'l',
    pygame.K_m: 'm',
    pygame.K_n: 'n',
    pygame.K_o: 'o',
    pygame.K_p: 'p',
    pygame.K_q: 'q',
    pygame.K_r: 'r',
    pygame.K_s: 's',
    pygame.K_t: 't',
    pygame.K_u: 'u',
    pygame.K_v: 'v',
    pygame.K_w: 'w',
    pygame.K_x: 'x',
    pygame.K_y: 'y',
    pygame.K_z: 'z',
    pygame.K_0: '0',
    pygame.K_1: '1',
    pygame.K_2: '2',
    pygame.K_3: '3',
    pygame.K_4: '4',
    pygame.K_5: '5',
    pygame.K_6: '6',
    pygame.K_7: '7',
    pygame.K_8: '8',
    pygame.K_9: '9',
    pygame.K_SPACE: ' ',
    pygame.K_EQUALS: '=',
    pygame.K_PERIOD: '.',
}

#Handle Monster Lists Creation
class Monster:
    def __init__(self, X, Y, face, id, on):
        self.facing = face
        self.position = pygame.Vector2(X,Y)
        self.image = pygame.transform.scale(self.facing, monsterRect)
        self.rect = pygame.Rect(self.position.x, self.position.y, monsterRect.x, monsterRect.y)
        self.id = id
        self.on = on

        self.health = 3
        self.speed = 5

    def turn(self, turn):
        #Change Image To Face Astronaut
        self.facing = turn
        self.image = pygame.transform.scale(self.facing, monsterRect)

def create_monsters(list):
    newList = []
    for item in list:
        monster = Monster(item[0], item[1], item[2], item[3], True)
        newList.append(monster)
    return newList

#Load Misc Images
if True:
    SpaceBackground1 = pygame.image.load(os.path.join(imagesF, "SpaceBackground1.png")).convert_alpha()
    titleImage = pygame.image.load(os.path.join(imagesF, "ASSETitle.png")).convert_alpha()
    startButtonImage1 = pygame.image.load(os.path.join(imagesF, "StartButton1.jpg")).convert_alpha()
    startButtonImage2 = pygame.image.load(os.path.join(imagesF, "StartButton2.jpg")).convert_alpha()
    optionsButtonImage1 = pygame.image.load(os.path.join(imagesF, "OptionsButton1.png")).convert_alpha()
    optionsButtonImage2 = pygame.image.load(os.path.join(imagesF, "OptionsButton2.png")).convert_alpha()
    backArrowImage = pygame.transform.scale(pygame.image.load(os.path.join(imagesF, "BackArrow.png")).convert_alpha(), (30,30))
    gunImage = pygame.image.load(os.path.join(imagesF, "Gun.png")).convert_alpha()
    deadBody1image = pygame.image.load(os.path.join(imagesF, "DeadBody1.png")).convert_alpha()
    deadBody1imageHighlighted = pygame.image.load(os.path.join(imagesF, "DeadBody1Highlighted.png")).convert_alpha()
    cupboardImage = pygame.transform.scale(pygame.image.load(os.path.join(imagesF, "Cupboard1.png")).convert_alpha(), (46,81))
    cupboardImageHighlighted = pygame.transform.scale(pygame.image.load(os.path.join(imagesF, "Cupboard2.png")).convert_alpha(), (46,81))
    bed2Image = pygame.transform.scale(pygame.image.load(os.path.join(imagesF, "Bed2.png")).convert_alpha(), (397*0.5,412*0.5))
    bed2ImageHighlighted = pygame.transform.scale(pygame.image.load(os.path.join(imagesF, "Bed2Highlighted.png")).convert_alpha(), (397*0.5,412*0.5))
    tableKImage = pygame.transform.scale(pygame.image.load(os.path.join(imagesF, "Table.png")).convert_alpha(), (86*1.7,44*1.7))
    tableKImageHighlighted = pygame.transform.scale(pygame.image.load(os.path.join(imagesF, "TableHighlighted.png")).convert_alpha(), (86*1.7,44*1.7))
    pauseImage = pygame.image.load(os.path.join(imagesF, "Pause.png")).convert_alpha()
    pauseRect = pygame.Rect(((WIDTH/2)-(pauseImage.get_width()/2)),((HEIGHT/2)-(pauseImage.get_height()/2)),pauseImage.get_width(),pauseImage.get_height())
#Load Tick Boxes
if True:
    tickBoxImage1 = pygame.image.load(os.path.join(imagesF, "TickBox1.png")).convert_alpha()
    tickBoxImage2 = pygame.image.load(os.path.join(imagesF, "TickBox2.png")).convert_alpha()
#Load Rooms
if True:
    Room1 = pygame.image.load(os.path.join(imagesF, "Room1.png")).convert_alpha() #Docking Bay
    Room2 = pygame.image.load(os.path.join(imagesF, "Room2.png")).convert_alpha() #Lobby
    RoomH = pygame.image.load(os.path.join(imagesF, "RoomH.png")).convert_alpha() #Hallway
    Room3 = pygame.image.load(os.path.join(imagesF, "Room3.png")).convert_alpha() #Officer's Quarters 1
    Room4 = pygame.image.load(os.path.join(imagesF, "Room4.png")).convert_alpha() #Officer's Quarters 2
    Room5 = pygame.image.load(os.path.join(imagesF, "Room5.png")).convert_alpha() #Ensuite
    Room6 = pygame.image.load(os.path.join(imagesF, "Room6.png")).convert_alpha() #Captain's Quarters
    Room7 = pygame.image.load(os.path.join(imagesF, "Room7.png")).convert_alpha() #Control Room
    Room8 = pygame.image.load(os.path.join(imagesF, "Room8.png")).convert_alpha() #Storage Room

    Rooms = [Room1,Room2,Room3,Room4,Room5,Room6,Room7,Room8]
#Load Astronaut Images and Sizes
if True:
    sideRect = pygame.Vector2(45*0.8,105*0.8)
    forwardRect = pygame.Vector2(52*0.8, 105*0.8)
    IN = pygame.image.load(os.path.join(imagesF, "Idle N.png")).convert_alpha()
    IE = pygame.image.load(os.path.join(imagesF, "Idle E.png")).convert_alpha()
    IS = pygame.image.load(os.path.join(imagesF, "Idle S.png")).convert_alpha()
    IW = pygame.image.load(os.path.join(imagesF, "Idle W.png")).convert_alpha()
    WN = pygame.image.load(os.path.join(imagesF, "Walk N.png")).convert_alpha()
    WE = pygame.image.load(os.path.join(imagesF, "Walk E.png")).convert_alpha()
    WS = pygame.image.load(os.path.join(imagesF, "Walk S.png")).convert_alpha()
    WW = pygame.image.load(os.path.join(imagesF, "Walk W.png")).convert_alpha()
#Handle Monsters
if True:
    monsterVelocity = 1
    monsterRect = pygame.Vector2(50,50)
    M1N = pygame.image.load(os.path.join(imagesF, "Monster1N.png")).convert_alpha()
    M1E = pygame.image.load(os.path.join(imagesF, "Monster1E.png")).convert_alpha()
    M1S = pygame.image.load(os.path.join(imagesF, "Monster1S.png")).convert_alpha()
    M1W = pygame.image.load(os.path.join(imagesF, "Monster1W.png")).convert_alpha()

    M2N = pygame.image.load(os.path.join(imagesF, "Monster2N.png")).convert_alpha()
    M2E = pygame.transform.rotate(pygame.image.load(os.path.join(imagesF, "Monster2N.png")).convert_alpha(), 90)
    M2S = pygame.transform.rotate(pygame.image.load(os.path.join(imagesF, "Monster2N.png")).convert_alpha(), 180)
    M2W = pygame.transform.rotate(pygame.image.load(os.path.join(imagesF, "Monster2N.png")).convert_alpha(), 270)
#Monster Lists
if True:
    R0M = []
    R1OM = []
    R2OM = [
        [150,150,M1S,0],
        [250,150,M1S,1],
        [350,150,M1S,2],
    ]
    RHOM = [
        [350,100,M1S,0],
        [350,200,M1S,1],
        [350,300,M1S,2],
        [350,400,M1S,3],
        [250,250,M2S,4]
    ]
    R3OM = [
        [180,250,M2S,0],
        [320,250,M2S,1],
        [250,180,M2S,2],
        [250,320,M2S,3],
    ]
    R4OM = [
        [180,400,M2S,0],
        [320,400,M2S,1],
        [180,300,M2S,2],
        [320,300,M2S,3],
        [40,300,M2S,4],
        [460,300,M2S,5],
    ]
    R5OM = [
        [300,100,M2S,0],
        [160,100,M2S,1],
        [300,380,M2S,2],
        [160,380,M2S,3],
    ]
    R6OM = [
        [180,250,M1S,0],
        [320,250,M1S,1],
        [250,180,M1S,2],
        [250,320,M1S,3],
    ]
    R7OM = [
        [150,200,M1S,0],
        [250,200,M1S,1],
        [350,200,M1S,2],
    ]
    R8OM = []

    Room1Monsters = create_monsters(R1OM)
    Room2Monsters = create_monsters(R2OM)
    RoomHMonsters = create_monsters(RHOM)
    Room3Monsters = create_monsters(R3OM)
    Room4Monsters = create_monsters(R4OM)
    Room5Monsters = create_monsters(R5OM)
    Room6Monsters = create_monsters(R6OM)
    Room7Monsters = create_monsters(R7OM)
    Room8Monsters = create_monsters(R8OM)

    RoomMonsters = [R0M,Room1Monsters,Room2Monsters,Room3Monsters,Room4Monsters,Room5Monsters,Room5Monsters,Room7Monsters,Room8Monsters]
#Load Audio
if True:
    startSound = pygame.mixer.Sound(os.path.join(audioF, "StartButton.wav"))
    gunShoot1Sound = pygame.mixer.Sound(os.path.join(audioF, "GunShoot1.wav"))
    concreteFootstepsSound = pygame.mixer.Sound(os.path.join(audioF, "ConcreteFootsteps.wav"))

    gameMusic = pygame.mixer.music.load(os.path.join(audioF, "stardust-danijel-zambo-main-version-1372-03-13.mp3"))
#Bullet Parameters
if True: 
    bullets = []
    BULLET_VELOCITY = 10
    BULLET_COLOR = (255, 0, 0)
    BULLET_WIDTH = 7
    BULLET_HEIGHT = 7
#Heart Parameters And Health Bar
if True:
    hearts = []
    heartNumber = 3
    heartImage = pygame.image.load(os.path.join(imagesF, "Heart.png")).convert_alpha()
    heartSize = 15

    HealthBarImage = pygame.transform.scale(pygame.image.load(os.path.join(imagesF, "HealthBar.png")).convert_alpha(), (60, 6))
    HealthBarColours = [GREEN,YELLOW,ORANGE,RED]
#Door Flash Parameters
if True:
    doorFlashWidth = 4
#Load StartVideo Frames And Scroll Intro Image
if True:
    Frame1 = pygame.image.load(os.path.join(imagesF, "Frame1.png")).convert_alpha()
    Frame2 = pygame.image.load(os.path.join(imagesF, "Frame2.png")).convert_alpha()
    Frame3 = pygame.image.load(os.path.join(imagesF, "Frame3.png")).convert_alpha()
    Frame4 = pygame.image.load(os.path.join(imagesF, "Frame4.png")).convert_alpha()
    Frame5 = pygame.image.load(os.path.join(imagesF, "Frame5.png")).convert_alpha()
    Frame6 = pygame.image.load(os.path.join(imagesF, "Frame6.png")).convert_alpha()
    Frame7 = pygame.image.load(os.path.join(imagesF, "Frame7.png")).convert_alpha()
    Frame8 = pygame.image.load(os.path.join(imagesF, "Frame8.png")).convert_alpha()
    Frame9 = pygame.image.load(os.path.join(imagesF, "Frame9.png")).convert_alpha()
    Frame10 = pygame.image.load(os.path.join(imagesF, "Frame10.png")).convert_alpha()
    Frame11 = pygame.image.load(os.path.join(imagesF, "Frame11.png")).convert_alpha()
    Frame12 = pygame.image.load(os.path.join(imagesF, "Frame12.png")).convert_alpha()
    Frame13 = pygame.image.load(os.path.join(imagesF, "Frame13.png")).convert_alpha()
    Frame14 = pygame.image.load(os.path.join(imagesF, "Frame14.png")).convert_alpha()
    Frame15 = pygame.image.load(os.path.join(imagesF, "Frame15.png")).convert_alpha()
    Frame16 = pygame.image.load(os.path.join(imagesF, "Frame16.png")).convert_alpha()
    Frame17 = pygame.image.load(os.path.join(imagesF, "Frame17.png")).convert_alpha()
    Frame18 = pygame.image.load(os.path.join(imagesF, "Frame18.png")).convert_alpha()
    Frame19 = pygame.image.load(os.path.join(imagesF, "Frame19.png")).convert_alpha()
    Frame20 = pygame.image.load(os.path.join(imagesF, "Frame20.png")).convert_alpha()
    Frame21 = pygame.image.load(os.path.join(imagesF, "Frame21.png")).convert_alpha()

    ScrollIntroImage = pygame.image.load(os.path.join(imagesF, "ScrollIntro.png")).convert_alpha()
#StartVideo Frames List
if True:
    Frames = [Frame1,Frame2,Frame3,Frame4,Frame5,Frame6,Frame7,Frame8,Frame9,Frame10,Frame11,Frame12,Frame13,Frame14,Frame15,Frame16,Frame17,Frame18,Frame19,Frame20,Frame21]
    FrameNum = 21
#Events
if True:
    FAINTED = pygame.USEREVENT + 1
    DIED = pygame.USEREVENT + 2
#Fonts
if True:
    healthFont = pygame.font.Font(os.path.join(fontsF, "Nunito-VariableFont_wght.ttf"), 50)
    deathFont = pygame.font.Font(os.path.join(fontsF, "Nunito-VariableFont_wght.ttf"), 90)
    optionFont = pygame.font.Font(os.path.join(fontsF, "Nunito-VariableFont_wght.ttf"), 36)
    commandFont = pygame.font.Font(os.path.join(fontsF, "Inconsolata-VariableFont_wdth,wght.ttf"), 30)
    scoreFont = pygame.font.Font(os.path.join(fontsF, "Inconsolata-VariableFont_wdth,wght.ttf"), 50)
#Load Inventory Images
if True:
    InventoryFramePosition = pygame.Vector2(93,4)
    InventoryFrame = pygame.transform.scale(pygame.image.load(os.path.join(imagesF, "InventoryFrame.png")).convert_alpha(),(50, 50))
    Keycard1Image = pygame.transform.scale(pygame.image.load(os.path.join(imagesF, "Keycard1.png")).convert_alpha(),(28, 28))
    Keycard2Image = pygame.transform.scale(pygame.image.load(os.path.join(imagesF, "Keycard2.png")).convert_alpha(),(28, 28))
    Keycard3Image = pygame.transform.scale(pygame.image.load(os.path.join(imagesF, "Keycard3.png")).convert_alpha(),(28, 28))
    Keycard23Image = pygame.transform.scale(pygame.image.load(os.path.join(imagesF, "Keycard23.png")).convert_alpha(),(28, 28))
    Keycard4Image = pygame.transform.scale(pygame.image.load(os.path.join(imagesF, "Keycard4.png")).convert_alpha(),(28, 28))
    KeycardPosition = pygame.Vector2(103,13)

    #Inventory Flash Images
    InventoryFlashImage1 = pygame.image.load(os.path.join(imagesF, "InventoryFlash1.png")).convert_alpha()
    InventoryFlashImage2 = pygame.image.load(os.path.join(imagesF, "InventoryFlash2.png")).convert_alpha()
    InventoryFlashImage3 = pygame.image.load(os.path.join(imagesF, "InventoryFlash3.png")).convert_alpha()
    InventoryFlashImage4 = pygame.image.load(os.path.join(imagesF, "InventoryFlash4.png")).convert_alpha()
    InventoryFlashImage5 = pygame.image.load(os.path.join(imagesF, "InventoryFlash5.png")).convert_alpha()
#Load Furniture Images
if True:
    PotPlantImage = pygame.transform.scale(pygame.image.load(os.path.join(imagesF, "PotPlant1.png")).convert_alpha(),(36*1.4, 57*1.4))
    BarrelImage = pygame.transform.scale(pygame.image.load(os.path.join(imagesF, "Barrel1.png")).convert_alpha(),(97*0.5, 126*0.5))
    WallImage = pygame.transform.scale(pygame.image.load(os.path.join(imagesF, "Wall.png")).convert_alpha(), (300,75))
    SpaceWindowImage = pygame.transform.scale(pygame.image.load(os.path.join(imagesF, "SpaceWindow.png")).convert_alpha(), (200,46))
    GrandClockImage = pygame.transform.scale(pygame.image.load(os.path.join(imagesF, "GrandClock.png")).convert_alpha(), (166*0.3,380*0.3))

    CPSM = 0.7
    ControlPanel_1 = pygame.transform.scale(pygame.image.load(os.path.join(imagesF, "ControlPanel_1.png")).convert_alpha(),(98*CPSM,257*CPSM))
    ControlPanel_2 = pygame.transform.scale(pygame.image.load(os.path.join(imagesF, "ControlPanel_2.png")).convert_alpha(),(299*CPSM,154*CPSM))
    ControlPanel_2Highlighted = pygame.transform.scale(pygame.image.load(os.path.join(imagesF, "ControlPanel_2Highlighted.png")).convert_alpha(),(299*CPSM,154*CPSM))
    ControlPanel_3 = pygame.transform.scale(pygame.image.load(os.path.join(imagesF, "ControlPanel_3.png")).convert_alpha(),(301*CPSM,102*CPSM))
    ControlPanel_4 = pygame.transform.scale(pygame.image.load(os.path.join(imagesF, "ControlPanel_4.png")).convert_alpha(),(97*CPSM,257*CPSM))
    CPTL = pygame.Vector2(((WIDTH/2) - (494*CPSM/2)), 50)
    CP1P = pygame.Vector2(CPTL.x, CPTL.y)
    CP2P = pygame.Vector2(CPTL.x+98*CPSM, CPTL.y)
    CP3P = pygame.Vector2(CPTL.x+98*CPSM, CPTL.y+154*CPSM+1)
    CP4P = pygame.Vector2(CPTL.x+98*CPSM+299*CPSM, CPTL.y)

    Bed1 = pygame.transform.scale(pygame.image.load(os.path.join(imagesF, "Bed1.png")).convert_alpha(),(106*0.9,147*0.9))
    Bed1Pos1 = pygame.Vector2(WIDTH-(56*0.9)-30-(106*0.9),60)
    Bed1Pos2 = pygame.Vector2((56*0.9)+30,60)
    BST1 = pygame.transform.scale(pygame.image.load(os.path.join(imagesF, "BST1.png")).convert_alpha(),(56*0.9,83*0.9))
    BST1Pos1 = pygame.Vector2(WIDTH-(56*0.9)-30,60)
    BST1Pos2 = pygame.Vector2(30,60)

    KeycardPanel1Image = pygame.transform.scale(pygame.image.load(os.path.join(imagesF, "KeycardPanel1.png")).convert_alpha(), (36,18.9))
    KeycardPanel2Image = pygame.transform.scale(pygame.image.load(os.path.join(imagesF, "KeycardPanel2.png")).convert_alpha(), (18.9,36))

    ToiletImage = pygame.transform.scale(pygame.image.load(os.path.join(imagesF, "Toilet.png")).convert_alpha(), (79*0.6,174*0.6))
    BathImage = pygame.transform.scale(pygame.image.load(os.path.join(imagesF, "Bath.png")).convert_alpha(), (161*0.4,209*0.4))
#Furtniture Parameters And Lists
if True:
    furnitures = []
    
    RoomFurnitures = []
    R0F = []
    Room1Furnitures = [
        [310,20,KeycardPanel1Image,False],
    ]
    Room2Furnitures = [
        [35,20,PotPlantImage,True],
        [415,70,BarrelImage,True],
        [308,20,KeycardPanel1Image,False],
        [4,325,KeycardPanel2Image,False],
    ]
    RoomHFurnitures = [
        [35,25,PotPlantImage,True],
        [310,20,KeycardPanel1Image,False],
        [153,20,KeycardPanel1Image,False],
    ]
    Room3Furnitures = [
        [Bed1Pos1.x,Bed1Pos1.y,Bed1,True],
        [BST1Pos1.x,BST1Pos1.y,BST1,True],
        [Bed1Pos2.x,Bed1Pos2.y,Bed1,True],
        [BST1Pos2.x,BST1Pos2.y,BST1,True],
        [300,HEIGHT-75-20,tableKImage,True],
        ]
    Room4Furnitures = [
        [Bed1Pos1.x,Bed1Pos1.y,Bed1,True],
        [BST1Pos1.x,BST1Pos1.y,BST1,True],
        [Bed1Pos2.x,Bed1Pos2.y,Bed1,True],
        [BST1Pos2.x,BST1Pos2.y,BST1,True],
    ]
    Room5Furnitures = [
        [205,200,WallImage,True],
        [230,50,BathImage,True],
        [310,50,BathImage,True],
        [390,50,BathImage,True],
        [240,230,ToiletImage,True],
        [320,230,ToiletImage,True],
        [400,230,ToiletImage,True],
        [430,370,cupboardImage, True],
    ]
    Room6Furnitures = [
        [WIDTH/2-198.5/2,30,bed2Image,True],
        [30,10,GrandClockImage,True],
        [WIDTH/2+198.5/2+5,33,BST1,True],
    ]
    Room7Furnitures = [
        [CP1P.x,CP1P.y,ControlPanel_1,True],
        [CP2P.x,CP2P.y,ControlPanel_2,True],
        [CP3P.x,CP3P.y,ControlPanel_3,False],
        [CP4P.x,CP4P.y,ControlPanel_4,True],
        [150,3,SpaceWindowImage,False]
    ]
    Room8Furnitures = []

    RoomFurnitures = [R0F,Room1Furnitures,Room2Furnitures,Room3Furnitures,Room4Furnitures,Room5Furnitures,Room6Furnitures,Room7Furnitures,Room8Furnitures]
#Load Coin Images And List
if True:
    CM = 0.2
    Coin1 = pygame.transform.scale(pygame.image.load(os.path.join(imagesF, "Coin1.png")).convert_alpha(),(96*CM,96*CM))
    Coin2 = pygame.transform.scale(pygame.image.load(os.path.join(imagesF, "Coin2.png")).convert_alpha(),(96*CM,85*CM))
    Coin3 = pygame.transform.scale(pygame.image.load(os.path.join(imagesF, "Coin3.png")).convert_alpha(),(96*CM,49*CM))
    Coin4 = pygame.transform.scale(pygame.image.load(os.path.join(imagesF, "Coin4.png")).convert_alpha(),(96*CM,24*CM))
    Coin5 = pygame.transform.scale(pygame.image.load(os.path.join(imagesF, "Coin5.png")).convert_alpha(),(96*CM,49*CM))
    Coin6 = pygame.transform.scale(pygame.image.load(os.path.join(imagesF, "Coin6.png")).convert_alpha(),(96*CM,84*CM))
    
    coins = []
    coinAnimation = [Coin1,Coin2,Coin3,Coin4,Coin5,Coin6]
#Load Map Images And List
if True:
    Map1 = pygame.image.load(os.path.join(imagesF, "Map1.png")).convert_alpha()
    Map2 = pygame.image.load(os.path.join(imagesF, "Map2.png")).convert_alpha()
    MapH = pygame.image.load(os.path.join(imagesF, "MapH.png")).convert_alpha()
    Map3 = pygame.image.load(os.path.join(imagesF, "Map3.png")).convert_alpha()
    Map4 = pygame.image.load(os.path.join(imagesF, "Map4.png")).convert_alpha()
    Map5 = pygame.image.load(os.path.join(imagesF, "Map5.png")).convert_alpha()
    Map6 = pygame.image.load(os.path.join(imagesF, "Map6.png")).convert_alpha()
    Map7 = pygame.image.load(os.path.join(imagesF, "Map7.png")).convert_alpha()

    maps = [Map1,Map2,Map3,Map4,Map5,Map6,Map7]
#Load Help Image
if True:
    helpImage = pygame.image.load(os.path.join(imagesF, "Help.png")).convert_alpha()

class Background:
    def __init__(self, image, x, y):
        self.image = image
        self.position = pygame.Vector2(x,y)
        self.rect = self.image.get_rect()

class Astronaut:
    def __init__(self):
        self.facing = IS
        self.position = pygame.Vector2(250-26, 250-52)
        self.image = pygame.transform.scale(self.facing, forwardRect)
        self.rect = pygame.Rect(self.position.x, self.position.y, forwardRect.x, forwardRect.y)

        #Stats
        self.speed = 3
        self.health = 100
        self.lives = 3
        self.damage = 10
        self.inventory = 0

        #Door Lockssd
        self.door1locked = True #1 To Lobby
        self.door2locked1 = True #2 To Captain's Quarters 1
        self.door2locked2 = True #3 To Captain's Quarters 2
        self.door3locked = True #3 To Control Room
        self.door4locked = True #4 To Storage Room

        #Command Background Colour
        self.commandColour = WHITE

        #Scoring System
        self.score = 0
        self.kills = 0
        self.deaths = 0
        self.damage = 0
        self.timer = 0

        #Inventory Flash
        self.inventoryTimer = 0
        
    def calculate_score(self):
        #Calculate Score
        self.score = round(((self.kills) - (self.deaths * 3 + self.damage / 10))*100, 1)

        #Render Score Text
        self.scoreText = f"Score: {self.score}"
        self.scoreTextRender = pygame.font.Font.render(scoreFont, self.scoreText, 1, WHITE)
        self.timerText = f"Time: {self.timer // 60} sec"
        self.timerTextRender = pygame.font.Font.render(scoreFont, self.timerText, 1, WHITE)
        return self.scoreTextRender, self.timerTextRender

    def turn(self, turn):
        self.facing = turn
        if (self.facing == WN) or (self.facing == WS) or (self.facing == IN) or (self.facing == IS):
            self.image = pygame.transform.scale(self.facing, forwardRect)
        if (self.facing == WE) or (self.facing == WW) or (self.facing == IE) or (self.facing == IW):
            self.image = pygame.transform.scale(self.facing, sideRect)

    def hurt(self, damage):
        self.health -= damage
        self.damage += damage
        if self.health <= 0:
            self.lives -= 1
            self.deaths += 1
            self.health = 100
            if self.lives <= 0:
                pygame.event.post(pygame.event.Event(DIED))
            else:
                pygame.event.post(pygame.event.Event(FAINTED))

class Gun:
    def __init__(self, anchor):
        self.image = pygame.transform.scale(gunImage, (75*0.7, 23*0.7))
        self.anchor = anchor
        self.xOffset = 22.5
        self.yOffset = 50
        self.position = pygame.Vector2(anchor.position.x + self.xOffset, anchor.position.y + self.yOffset)
        self.rect = self.image.get_rect(center=self.position)
        self.colour = (0, 0, 255)

        self.visible = False

class Bullet:
    def __init__(self, position, angle):
        self.position = pygame.Vector2(position)
        self.angle = angle
        self.velocity = BULLET_VELOCITY
        self.colour = BULLET_COLOR
        self.rect = pygame.Rect(self.position.x, self.position.y, BULLET_WIDTH, BULLET_HEIGHT)
    def move(self):
        self.dx = self.velocity * math.cos(math.radians(self.angle))
        self.dy = self.velocity * math.sin(math.radians(self.angle))
        self.position.x += self.dx
        self.position.y += self.dy
        self.rect = pygame.Rect(self.position.x, self.position.y, BULLET_WIDTH, BULLET_HEIGHT)

class Title:
    def __init__(self, image):
        self.image = image
        self.scaledImage = pygame.transform.scale(self.image, (200*1.3,57*1.2))
        self.position = pygame.Vector2(150, 40)
        self.rect = pygame.Rect(150, 40, 200, 57)
        self.counter = 0
        self.timer = 0

    def scale(self):
        #Grow/Shrink Animation
        newX = 200*(1+self.counter)*1.5*1.2
        newY = 57*(1+self.counter)*1.5*1.2
        self.scaledImage = pygame.transform.scale(self.image, (newX, newY))
        self.position = pygame.Vector2((WIDTH/2)-newX/2, (HEIGHT/2)-newY/2-150)
        self.rect = pygame.Rect(self.position.x, self.position.y, newX, newY)

        #Animation Timer
        self.timer += 1
        if self.timer < 40:
            self.counter += 0.003
        elif self.timer >= 40 and self.timer < 80:
            self.counter -= 0.003
        elif self.timer >= 80:
            self.timer = 0

class StartButton:
    def __init__(self, image):
        self.image = image
        self.scaledImage = pygame.transform.scale(self.image, (225*0.6*1.3, 86*0.6*1.3))
        self.position = pygame.Vector2((WIDTH/2-(225*0.6*1.3)/2), 250)
        self.rect = pygame.Rect(WIDTH/2-(225*0.6*1.3)/2, 250, 225, 86)
        self.counter = 0
        self.timer = 0

    def scale(self):
        #Grow/Shrink Animation
        newX = 225*0.6*(1+self.counter)*1.3
        newY = 86*0.6*(1+self.counter)*1.3
        self.scaledImage = pygame.transform.scale(self.image, (newX, newY))
        self.position = pygame.Vector2((WIDTH/2)-newX/2, (HEIGHT/2)-newY/2+10)
        self.rect = pygame.Rect(self.position.x, self.position.y, newX, newY)

        #Animation Timer
        self.timer += 1
        if self.timer < 40:
            self.counter += 0.003
        elif self.timer >= 40 and self.timer < 80:
            self.counter -= 0.003
        elif self.timer >= 80:
            self.timer = 0

    def mouseOver(self, image):
        self.image = image

class OptionsButton:
    def __init__(self, image):
        self.image = image
        self.scaledImage = pygame.transform.scale(self.image, (225*0.6*1.3, 86*0.6*1.3))
        self.position = pygame.Vector2((WIDTH/2-(225*0.6*1.3)/2), 400)
        self.rect = pygame.Rect(WIDTH/2-(225*0.6*1.3)/2, 400, 225, 86)
        self.counter = 0
        self.timer = 0

    def scale(self):
        #Grow/Shrink Animation
        newX = 225*0.6*(1+self.counter)*1.3
        newY = 86*0.6*(1+self.counter)*1.3
        self.scaledImage = pygame.transform.scale(self.image, (newX, newY))
        self.position = pygame.Vector2((WIDTH/2)-newX/2, (HEIGHT/2)-newY/2+120)
        self.rect = pygame.Rect(self.position.x, self.position.y, newX, newY)

        #Animation Timer
        self.timer += 1
        if self.timer < 40:
            self.counter += 0.003
        elif self.timer >= 40 and self.timer < 80:
            self.counter -= 0.003
        elif self.timer >= 80:
            self.timer = 0

    def mouseOver(self, image):
        self.image = image

class BackArrow:
    def __init__(self):
        self.position = pygame.Vector2(20,20)
        self.image = backArrowImage
        self.rect = pygame.Rect(self.position.x,self.position.y, self.image.get_width(), self.image.get_height())

class TickBox:
    def __init__(self, X, Y, ticked, text):
        self.position = pygame.Vector2(X,Y)
        self.ticked = ticked
        if ticked:
            self.image = tickBoxImage1
        else:
            self.image = tickBoxImage2
        self.rect = pygame.Rect(self.position.x,self.position.y, self.image.get_width(), self.image.get_height())

        self.text = text
        self.textRender = pygame.font.Font.render(optionFont, self.text, 1, WHITE)
        self.textRect = pygame.Rect(self.position.x+60, self.position.y-5, self.textRender.get_width(), self.textRender.get_height())

    def switch(self):
        if self.ticked:
            self.image = tickBoxImage2
            self.ticked = False
        else:
            self.image = tickBoxImage1
            self.ticked = True

class DoorFlash:
    def __init__(self, direction):
        #Direction Presets
        self.direction = direction
        if self.direction == 1 or self.direction == 5:
            self.point1 = (193,0)
            self.point2 = (303,0)
            self.point3 = (297,58)
            self.point4 = (198,58)
        elif self.direction == 2 or self.direction == 6:
            self.point1 = (498,190)
            self.point2 = (498,307)
            self.point3 = (470,297)
            self.point4 = (470,200)
        elif self.direction == 3 or self.direction == 7:
            self.point1 = (193,498)
            self.point2 = (302,498)
            self.point3 = (299,485)
            self.point4 = (199,485)
        elif self.direction == 4 or self.direction == 8:
            self.point1 = (0,190)
            self.point2 = (0,307)
            self.point3 = (27,297)
            self.point4 = (27,200)

        if self.direction in [1,2,3,4]:
            self.colour = WHITE
        else:
            self.colour = RED

class StartVideo:
    def __init__(self):
        self.frame = 0
        self.image = Frames[self.frame]

class DeadBody1:
    def __init__(self):
        self.position = pygame.Vector2(250,250)
        self.velocity = pygame.Vector2(0.2,0.4)
        self.angle = 0
        self.image = pygame.transform.scale(deadBody1image, (100,100))
        self.rotatedImage = pygame.transform.rotate(self.image, self.angle)
        self.rect = pygame.Rect(self.position.x, self.position.y, self.rotatedImage.get_width(), self.rotatedImage.get_height())
        self.highlighted = False

    def move(self):
        #Move
        self.position += self.velocity
        # Bounce off the walls
        if self.position.x <= 0 or self.position.x >= 500-self.image.get_width():
            self.velocity.x = -self.velocity.x
        if self.position.y <= 0 or self.position.y >= 500-self.image.get_height():
            self.velocity.y = -self.velocity.y
        #Update Rect And Rotate Image
        self.angle += 0.1
        self.rotatedImage = pygame.transform.rotate(self.image, self.angle)
        self.rect = pygame.Rect(self.position.x, self.position.y, self.rotatedImage.get_width(), self.rotatedImage.get_height())

    def highlight(self, astronaut):
        #Highlight Body When Close To Astronaut
        distanceToAstronaut = math.sqrt(((self.position.x - astronaut.position.x) ** 2) + ((self.position.y - astronaut.position.y) ** 2))
        if distanceToAstronaut < 70 and astronaut.door1locked == True:
            self.image = deadBody1imageHighlighted
            self.highlighted = True
        else:
            self.image = deadBody1image
            self.highlighted = False

class Heart:
    def __init__(self, X, Y):
        self.position = pygame.Vector2(X,Y)
        self.image = pygame.transform.scale(heartImage, (heartSize,heartSize))
        self.rect = pygame.Rect(self.position.x, self.position.y, self.image.get_width(), self.image.get_height())

class Furniture:
    def __init__(self, X, Y, image, collide):
        self.position = pygame.Vector2(X,Y)
        self.image = image
        self.rect = pygame.Rect(self.position.x, self.position.y, self.image.get_width(), self.image.get_height()/2)
        self.collide = collide

class Cupboard:
    def __init__(self):
        self.position = pygame.Vector2(430,370)
        self.image = cupboardImage
        self.rect = pygame.Rect(self.position.x,self.position.y,self.image.get_width(),self.image.get_height())
        self.highlighted = False

    def highlight(self, astronaut):
        #Highlight Cupboard When Close To Astronaut
        distanceToAstronaut = math.sqrt(((self.position.x - astronaut.position.x) ** 2) + ((self.position.y - astronaut.position.y) ** 2))
        if distanceToAstronaut < 70 and astronaut.door2locked1 == True:
            self.image = cupboardImageHighlighted
            self.highlighted = True
        else:
            self.image = cupboardImage
            self.highlighted = False

class Bed2:
    def __init__(self):
        self.position = pygame.Vector2(WIDTH/2-198.5/2,30)
        self.image = bed2Image
        self.rect = pygame.Rect(self.position.x,self.position.y,self.image.get_width(),self.image.get_height())
        self.highlighted = False

    def highlight(self, astronaut):
        #Highlight Bed When Close To Astronaut
        distanceToAstronaut = math.sqrt(((self.position.x+200 - astronaut.position.x) ** 2) + ((self.position.y - astronaut.position.y) ** 2))
        if distanceToAstronaut < 70 and astronaut.door3locked == True:
            self.image = bed2ImageHighlighted
            self.highlighted = True
        else:
            self.image = bed2Image
            self.highlighted = False

class ControlPanel:
    def __init__(self):
        self.position = pygame.Vector2(CP2P.x,CP2P.y)
        self.image = ControlPanel_2
        self.rect = pygame.Rect(self.position.x,self.position.y,self.image.get_width(),self.image.get_height())
        self.highlighted = False

    def highlight(self, astronaut):
        #Highlight Control Panel When Close To Astronaut
        distanceToAstronaut = math.sqrt(((self.position.x+100 - astronaut.position.x) ** 2) + ((self.position.y+20 - astronaut.position.y) ** 2))
        if distanceToAstronaut < 50 and astronaut.door4locked == True:
            self.image = ControlPanel_2Highlighted
            self.highlighted = True
        else:
            self.image = ControlPanel_2
            self.highlighted = False

class TableK:
    def __init__(self):
        self.position = pygame.Vector2(300,HEIGHT-75-20)
        self.image = tableKImage
        self.rect = pygame.Rect(self.position.x,self.position.y,self.image.get_width(),self.image.get_height())
        self.highlighted = False

    def highlight(self, astronaut):
        #Highlight Table When Close To Astronaut
        distanceToAstronaut = math.sqrt(((self.position.x+120 - astronaut.position.x) ** 2) + ((self.position.y - astronaut.position.y) ** 2))
        if distanceToAstronaut < 100 and astronaut.door2locked2 == True:
            self.image = tableKImageHighlighted
            self.highlighted = True
        else:
            self.image = tableKImage
            self.highlighted = False

class Coin:
    def __init__(self):
        self.position = pygame.Vector2(random.randint(0,WIDTH),random.randint(1,700)*-1)
        self.velocity = 0.5
        self.stage = random.randint(1,6)
        self.image = coinAnimation[self.stage-1]
        self.rect = pygame.Rect(self.position.x, self.position.y, self.image.get_width(), self.image.get_height())
        self.timer = 0
    
    def step(self):
        #Move Down, Coin Flipping Animation
        self.timer += 1
        self.position.y += self.velocity
        if self.timer >= 100:
            if self.stage >= 6:
                self.stage = 0
            self.stage += 1
            self.timer = 0
        self.image = coinAnimation[self.stage-1]
        self.rect = pygame.Rect(self.position.x, self.position.y, self.image.get_width(), self.image.get_height())

class HealthBar:
    def __init__(self, astronaut):
        self.image = HealthBarImage
        self.position = pygame.Vector2((astronaut.position.x + (forwardRect.x/2)) - (self.image.get_width()/2), astronaut.position.y - heartSize - self.image.get_height() - 2)
        self.rect = pygame.Rect(self.position.x, self.position.y, self.image.get_width(), self.image.get_height())

        self.colour = GREEN
        self.barRect = self.rect
        self.stage = 0

    def update(self, astronaut):
        if astronaut.health >= 75:
            self.stage = 0
        elif astronaut.health >= 50:
            self.stage = 1
        elif astronaut.health >= 25:
            self.stage = 2
        else:
            self.stage = 3
        self.colour = HealthBarColours[self.stage]
        self.position = pygame.Vector2((astronaut.position.x + (forwardRect.x/2)) - (self.image.get_width()/2), astronaut.position.y - heartSize - self.image.get_height() - 2)
        self.rect = pygame.Rect(self.position.x, self.position.y, self.image.get_width(), self.image.get_height())
        self.barRect = self.rect
        self.barRect.width = astronaut.health*0.6

def rotate_pivot(image, angle, pivot, origin):
    #Rotate the image around a given pivot
    surf = pygame.transform.rotate(image, angle)
    offset = pivot + (origin - pivot).rotate(angle)
    rect = surf.get_rect(center=offset)
    return surf, rect

def move_gun(gun):
    #Entire Gun Rotate/Move Function
    gun.position = pygame.Vector2(gun.anchor.position.x + gun.xOffset, gun.anchor.position.y + gun.yOffset)
    mousePosition = pygame.Vector2(pygame.mouse.get_pos())

    mouseOffset = mousePosition - gun.position
    mouseAngle = -math.degrees(math.atan2(mouseOffset.y, mouseOffset.x))
    gun.angle = -math.degrees(math.atan2(-mouseOffset.y, mouseOffset.x))

    gun.rotatedImage, gun.rect = rotate_pivot(gun.image, mouseAngle, gun.position, gun.position)

    if gun.visible:
        window.blit(gun.rotatedImage, gun.rect)

def create_bullet(gun):
    #Create Bullet at end of gun
    end_x = gun.position.x + 30 * math.cos(math.radians(gun.angle))
    end_y = gun.position.y + 30 * math.sin(math.radians(gun.angle))

    bullet = Bullet((end_x, end_y), gun.angle)
    bullets.append(bullet)

def mouseOver_check(mx, my, rectToCheck, offsetXD, offsetXM, offsetYD, offsetYM):
    #Check if mouse is over any rect value
    if mx >= rectToCheck.position.x and mx <= rectToCheck.position.x+rectToCheck.rect.right/offsetXD-offsetXM \
    and my >= rectToCheck.position.y and my <= rectToCheck.position.y+rectToCheck.rect.bottom/offsetYD-offsetYM:
        return True
    else:
        return False

def handle_keys(keysPressed, astronaut):
    #Resets new delta for each frame
    delta = pygame.Vector2()

    #Footsteps sound effect
    if (keysPressed[pygame.K_w] or keysPressed[pygame.K_a] or keysPressed[pygame.K_s] or keysPressed[pygame.K_d]):
        if not pygame.mixer.Channel(1).get_busy():
            pygame.mixer.Channel(1).play(pygame.mixer.Sound(concreteFootstepsSound))

    #Movement & Walking Animation
    if keysPressed[pygame.K_w]:
        delta.y -= astronaut.speed
        astronaut.turn(WN)
    if keysPressed[pygame.K_a]:
        delta.x -= astronaut.speed
        astronaut.turn(WW)
    if keysPressed[pygame.K_s]:
        delta.y += astronaut.speed
        astronaut.turn(WS)
    if keysPressed[pygame.K_d]:
        delta.x += astronaut.speed
        astronaut.turn(WE)

    #Stop Moving Animation
    if (delta.x == 0) and (delta.y == 0):
        pygame.mixer.Channel(1).stop()
        if astronaut.facing == WN:
            astronaut.facing = IN
            astronaut.image = pygame.transform.scale(astronaut.facing, forwardRect)
        if astronaut.facing == WE:
            astronaut.facing = IE
            astronaut.image = pygame.transform.scale(astronaut.facing, sideRect)
        if astronaut.facing == WS:
            astronaut.facing = IS
            astronaut.image = pygame.transform.scale(astronaut.facing, forwardRect)
        if astronaut.facing == WW:
            astronaut.facing = IW
            astronaut.image = pygame.transform.scale(astronaut.facing, sideRect)

    #Update Astronaut Position/Rect, Test For Collisions
    astronaut_collisions(astronaut, delta)

def door_selector(astronaut, state):
    #Return direction of selected door
    if astronaut.position.x < 290 and astronaut.position.x > 150 and astronaut.position.y < 58:
        if state == 1:
            if astronaut.door1locked == False:
                return 1
            else:
                return 5
        elif state == 2.5:
            if astronaut.door2locked1 == False and astronaut.door2locked2 == False:
                return 1
            else:
                return 5
        elif state == 2:
            if astronaut.door3locked == False:
                return 1
            else:
                return 5
        else:
            return 1
    if astronaut.position.y < 290 and astronaut.position.y > 150 and astronaut.position.x > 430:
        return 2
    if astronaut.position.x < 290 and astronaut.position.x > 150 and astronaut.position.y > 400:
        return 3
    if astronaut.position.y < 290 and astronaut.position.y > 150 and astronaut.position.x < 30:
        if state == 2:
            if astronaut.door4locked == False:
                return 4
            else:
                return 8
        else:
            return 4
    else:
        return 0

def draw_doorFlash(doorFlashState):
    #Draw Door Flash
    doorFlash = DoorFlash(doorFlashState)
    pygame.draw.line(window, doorFlash.colour, doorFlash.point1, doorFlash.point2, doorFlashWidth)
    pygame.draw.line(window, doorFlash.colour, doorFlash.point2, doorFlash.point3, doorFlashWidth)
    pygame.draw.line(window, doorFlash.colour, doorFlash.point3, doorFlash.point4, doorFlashWidth)
    pygame.draw.line(window, doorFlash.colour, doorFlash.point4, doorFlash.point1, doorFlashWidth)

def monster_move(monster, astronaut):
    #Move Monsters Towards Astronaut
    direction = astronaut.position - monster.position
    if direction.length() > 0:
        movement = direction.normalize() * monsterVelocity
    else:
        movement = pygame.Vector2(0, 0)

    newPos = monster.position + movement
    newRect = pygame.Rect(newPos.x, newPos.y, monsterRect.x, monsterRect.y)
    collideCondition1 = False

    #Check For Collisions
    if newPos.x < 500 - sideRect.x and newPos.x > 0 and newPos.y < 500 - sideRect.y and newPos.y > 0:
        for furniture in furnitures:
            if furniture.collide:
                if pygame.Rect.colliderect(newRect, furniture.rect):
                    collideCondition1 = True
        if not collideCondition1:
            monster.position = newPos
            monster.rect = newRect

    #Change Image Based On Direction
    if abs(direction.x) > abs(direction.y):
        if direction.x > 0:
            monster.turn(M1E)
        else:
            monster.turn(M1W)
    else:
        if direction.y > 0:
            monster.turn(M1S)
        else:
            monster.turn(M1N)

def kill_monsters(astronaut):
    #Test For Coliisions of and Removing Monsters and Bullets
    if state == 2.5:
        for monster in RoomHMonsters:
            if monster.on:
                for bullet in bullets:
                    if pygame.Rect.colliderect(monster.rect, bullet.rect):
                        monster.health -= astronaut.damage
                        bullets.remove(bullet)
                        if monster.health <= 0:
                            if state == 2.5:
                                if len(RoomHMonsters) > 0:
                                    RoomHMonsters[monster.id].on = False
                            else:
                                if len(RoomMonsters[state]) > 0:
                                    RoomMonsters[state][monster.id].on = False
                            astronaut.kills += 1
    else:
        for monster in RoomMonsters[state]:
            if monster.on:
                for bullet in bullets:
                    if pygame.Rect.colliderect(monster.rect, bullet.rect):
                        monster.health -= astronaut.damage
                        bullets.remove(bullet)
                        if monster.health <= 0:
                            if state == 2.5:
                                RoomHMonsters[monster.id].on = False
                            else:
                                RoomMonsters[state][monster.id].on = False
                            astronaut.kills += 1

def loading_screen(astronaut, direction, state):
    #Loading Screen Black
    step = 0
    frames = 80
    pygame.display.flip()
    for i in range(frames):
        time.sleep(0.3/frames)
        step += 1/frames
        pygame.draw.rect(window, BLACK, (0,0, WIDTH*step, HEIGHT))
        pygame.display.flip()

    if direction == 1:
        astronaut.position = pygame.Vector2(WIDTH/2-sideRect.x/2,5)
    if direction == 2:
        astronaut.position = pygame.Vector2(WIDTH-sideRect.x-20,HEIGHT/2-sideRect.y/2)
    if direction == 3:
        astronaut.position = pygame.Vector2(WIDTH/2-sideRect.x/2,HEIGHT-sideRect.y-10)
    if direction == 4:
        astronaut.position = pygame.Vector2(20,HEIGHT/2-sideRect.y/2)

    spawn_furnitures(state)
    bullets.clear()

def start_loading_screen():
    #Loading Screen with Bar
    step = 0
    frames = 60
    window.fill(BLACK)
    pygame.display.flip()
    for i in range(frames):
        step += 1
        pygame.draw.rect(window, WHITE, (WIDTH/2-100,HEIGHT/2-20, 200,40), 3)
        pygame.draw.rect(window, WHITE, (WIDTH/2-100,HEIGHT/2-20, (200/frames)*step, 40))
        pygame.display.flip()
        time.sleep(0.5/frames)

    spawn_furnitures(1)
    bullets.clear()

def opening_scene(startVideo):
    #Play Scroll Intro
    counter = 0
    for i in range(ScrollIntroImage.get_height()-HEIGHT):
        window.blit(ScrollIntroImage, (0,counter, 500,1500))
        counter -= 1
        pygame.display.flip()
        pygame.time.delay(ScrollSpeed)

        #Test For Quit Game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()

    #Play Start Video
    for i in range(FrameNum):
        startVideo.image = Frames[startVideo.frame]
        window.blit(startVideo.image, (0,0))
        startVideo.frame += 1
        pygame.display.flip()
        pygame.time.delay(VideoSpeed)

        #Test For Quit Game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()

def create_hearts(number, astronaut):
    #Calculate Position of and Spawn Hearts
    hearts.clear()
    counter = 0
    for i in range(number):
        X = ((astronaut.position.x + (forwardRect.x/2)) - (heartSize * (heartNumber/2))) + (heartSize * (counter))
        Y = astronaut.position.y - heartSize - 1
        heart = Heart(X,Y)
        hearts.append(heart)
        counter += 1

def monster_collisions(astronaut):
    #Test For Collisions Of Monster and Astronaut
    if state == 2.5:
        for monster in RoomHMonsters:
            if monster.on:
                if pygame.Rect.colliderect(astronaut.rect, monster.rect):
                    astronaut.hurt(0.3)
                    newposition = pygame.Vector2(-1,-1)
                    while newposition.x < 0 and newposition.y < 0 or newposition.x > 500 and newposition.y > 500:
                        newposition = pygame.Vector2(random.randint(-1,1)*50, random.randint(-1,1)*50)
                    monster.rect = pygame.Rect(newposition.x, newposition.y, monsterRect.x, monsterRect.y)
    else:
        for monster in RoomMonsters[state]:
            if monster.on:
                if pygame.Rect.colliderect(astronaut.rect, monster.rect):
                    astronaut.hurt(0.3)
                    newposition = pygame.Vector2(-1,-1)
                    while newposition.x < 0 and newposition.y < 0 or newposition.x > 500 and newposition.y > 500:
                        newposition = pygame.Vector2(random.randint(-1,1)*50, random.randint(-1,1)*50)
                    monster.rect = pygame.Rect(newposition.x, newposition.y, monsterRect.x, monsterRect.y)

def faint():
    #Fainting Animation
    counter = 0
    for i in range(251):
        pygame.draw.rect(window, BLACK, (0,0, WIDTH, counter))
        pygame.draw.rect(window, BLACK, (0,0, counter, HEIGHT))
        pygame.draw.rect(window, BLACK, (WIDTH-counter,0, counter, HEIGHT))
        pygame.draw.rect(window, BLACK, (0,HEIGHT-counter, WIDTH, counter))
        counter += 1
        pygame.time.delay(5)
        pygame.display.flip()

    bullets.clear()
    
def die():
    #Dying Animation
    counter = 0
    for i in range(251):
        pygame.draw.rect(window, RED, (0,0, WIDTH, counter))
        pygame.draw.rect(window, RED, (0,0, counter, HEIGHT))
        pygame.draw.rect(window, RED, (WIDTH-counter,0, counter, HEIGHT))
        pygame.draw.rect(window, RED, (0,HEIGHT-counter, WIDTH, counter))

        counter += 1

        pygame.display.flip()
        pygame.time.delay(5)
    
    deathText = "YOU DIED"
    deathTextRender = pygame.font.Font.render(deathFont, deathText, 1, BLACK)
    window.blit(deathTextRender, ((WIDTH/2)-(deathTextRender.get_width()/2), (HEIGHT/2)-(deathTextRender.get_height()/2)))

    pygame.display.flip()
    pygame.time.delay(7000)

    pygame.quit()

def create_furniture(X, Y, image, collide):
    #Create Furniture Instance
    furniture = Furniture(X, Y, image, collide)
    furnitures.append(furniture)

def spawn_furnitures(state):
    #Spawn Furnitures For Each Room
    furnitures.clear()
    if state == 2.5:
        for list in RoomHFurnitures:
            create_furniture(list[0], list[1], list[2], list[3])
    else:
        for list in RoomFurnitures[state]:
                create_furniture(list[0], list[1], list[2], list[3])

def astronaut_collisions(astronaut, delta):
    #Test For Collisions Between Wall And Furniture
    newPos = astronaut.position + delta
    newRect = pygame.Rect(newPos.x, newPos.y, 40, 70)
    collideCondition1 = False

    if newPos.x < 500 - sideRect.x and newPos.x > 0 and newPos.y < 500 - sideRect.y and newPos.y > 0:
        for furniture in furnitures:
            if furniture.collide:
                if pygame.Rect.colliderect(newRect, furniture.rect):
                    collideCondition1 = True
        if not collideCondition1:
            astronaut.position = newPos
            astronaut.rect = newRect

def MVB_switch(MasterVolumeButton):
    #When MVB is clicked, mute or unmute all volume
    MasterVolumeButton.switch()
    if MasterVolumeButton.ticked:
        MVBset = 1.0
    else:
        MVBset = 0.0
    [channel.set_volume(MVBset) for channel in [pygame.mixer.Channel(i) for i in [0, 1, 2]]]
    pygame.mixer.music.set_volume(MVBset)

def SIB_switch(SkipIntroButton):
    #When SIB is clicked, don't play start video or scroll intro
    SkipIntroButton.switch()

def end_scene(astronaut):
    #Calculate Time and Score
    scoreTextRender, timerTextRender = astronaut.calculate_score()

    #Spawn Starting Coins
    if len(coins) == 0:
        for i in range(1000):
            coin = Coin()
            coins.append(coin)

    #Quit Timer
    QuitTimer = 0
    
    #Run Animation Loop
    while True:
        #Draw Background and Astronaut
        window.fill(BLACK)
        window.blit(Room8, (0,0,500,500))
        window.blit(pygame.transform.scale(IS, forwardRect), (250-26, 250-52))

        #Move, Animate, and Delete Coins
        for coin in coins:
            coin.step()
            if coin.position.y > HEIGHT:
                coins.remove(coin)
                coin1 = Coin()
                coins.append(coin1)
            window.blit(coin.image, coin.rect)

        #Render Quit Message Text
        quitText = "THE END"
        quitTextRender = pygame.font.Font.render(scoreFont, quitText, 1, WHITE)

        #Draw Score, Time, and Quit Message
        window.blit(scoreTextRender, ((WIDTH/2)-(scoreTextRender.get_width()/2), 320))
        window.blit(timerTextRender, ((WIDTH/2)-(timerTextRender.get_width()/2), 370))
        window.blit(quitTextRender, ((WIDTH/2)-(quitTextRender.get_width()/2), 120))

        #Test For Quit Game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()

        #Handle Quit Timer
        QuitTimer += 1
        if QuitTimer > 5000:
            pygame.quit()

        pygame.display.flip()

def show_map(state):
    #Set Map State
    if state == 2.5:
        img = MapH
    else:
        img = maps[state-1]
    
    #Calculate Map Positions
    pos = pygame.Vector2(WIDTH/2-img.get_width()/2, HEIGHT/2-img.get_height()/2)
    rect = pygame.Rect(pos.x,pos.y, img.get_width(),img.get_height())

    #Draw Map
    window.blit(img, rect)
    pygame.display.flip()

def run_command(characters, astronaut, MasterVolumeButton, SkipIntroButton, background):
    #Split Entered Command in to Value, State, Key, and Command
    cmd = "".join(characters)
    if "=" not in cmd:
        astronaut.commandColour = RED
        return
    valueSplit = cmd.split("=")
    if len(valueSplit) < 2:
        astronaut.commandColour = RED
        return
    value = valueSplit[1]
    mainSplit = valueSplit[0].split(".")
    if len(mainSplit) < 3:
        astronaut.commandColour = RED
        return
    state = mainSplit[0]
    key = mainSplit[1]
    command = mainSplit[2]
    
    #Translate and Complete Corresponding Function
    if state == "set":
        if key == "door":
            if command == "1locked":
                if value == "true":
                    astronaut.door1locked = True
                    astronaut.commandColour = GREEN
                elif value == "false":
                    astronaut.door1locked = False
                    astronaut.commandColour = GREEN
                else:
                    astronaut.commandColour = RED
                    print("Error: set.door.1locked")
            elif command == "2locked1":
                if value == "true":
                    astronaut.door2locked1 = True
                    astronaut.commandColour = GREEN
                elif value == "false":
                    astronaut.door2locked1 = False
                    astronaut.commandColour = GREEN
                else:
                    astronaut.commandColour = RED
                    print("Error: set.door.2locked1")
            elif command == "2locked2":
                if value == "true":
                    astronaut.door2locked2 = True
                    astronaut.commandColour = GREEN
                elif value == "false":
                    astronaut.door2locked2 = False
                    astronaut.commandColour = GREEN
                else:
                    astronaut.commandColour = RED
                    print("Error: set.door.2locked2")
            elif command == "3locked":
                if value == "true":
                    astronaut.door3locked = True
                    astronaut.commandColour = GREEN
                elif value == "false":
                    astronaut.door3locked = False
                    astronaut.commandColour = GREEN
                else:
                    astronaut.commandColour = RED
                    print("Error: set.door.3locked")
            elif command == "4locked":
                if value == "true":
                    astronaut.door4locked = True
                    astronaut.commandColour = GREEN
                elif value == "false":
                    astronaut.door4locked = False
                    astronaut.commandColour = GREEN
                else:
                    astronaut.commandColour = RED
                    print("Error: set.door.4locked")
            else:
                    astronaut.commandColour = RED
                    print("Error: set.door")
        elif key == "astronaut":
            if command == "health":
                if int(value) > 0:
                    astronaut.health = int(value)
                    astronaut.commandColour = GREEN
                else:
                    astronaut.commandColour = RED
                    print("Error: set.astronaut.health")
            elif command == "speed":
                if int(value) > 0:
                    astronaut.speed = int(value)
                    astronaut.commandColour = GREEN
                else:
                    astronaut.commandColour = RED
                    print("Error: set.astronaut.speed")
            elif command == "x":
                if int(value) > 0 and int(value) < WIDTH:
                    astronaut.position.x = int(value)
                    astronaut.rect.x = int(value)
                    astronaut.commandColour = GREEN
                else:
                    astronaut.commandColour = RED
                    print("Error: set.astronaut.x")
            elif command == "y":
                if int(value) > 0 and int(value) < HEIGHT:
                    astronaut.position.y = int(value)
                    astronaut.rect.y = int(value)
                    astronaut.commandColour = GREEN
                else:
                    astronaut.commandColour = RED
                    print("Error: set.astronaut.y")
            elif command == "lives":
                if int(value) > 0:
                    astronaut.lives = int(value)
                    astronaut.commandColour = GREEN
                else:
                    astronaut.commandColour = RED
                    print("Error: set.astronaut.lives")
            elif command == "damage":
                if int(value) > 0:
                    astronaut.damage = int(value)
                    astronaut.commandColour = GREEN
                else:
                    astronaut.commandColour = RED
                    print("Error: set.astronaut.damage")
            elif command == "inventory":
                if value in ["0","1","2","3","23","4"]:
                    astronaut.inventory = int(value)
                    astronaut.commandColour = GREEN
                else:
                    astronaut.commandColour = RED
                    print("Error: set.astronaut.inventory")
            else:
                astronaut.commandColour = RED
                print("Error: set.astronaut")
        elif key == "options":
            if command == "mvb":
                if value == "true":
                    if not MasterVolumeButton.ticked:
                        MVB_switch(MasterVolumeButton)
                    astronaut.commandColour = GREEN
                elif value == "false":
                    if MasterVolumeButton.ticked:
                        MVB_switch(MasterVolumeButton)
                    astronaut.commandColour = GREEN
                else:
                    astronaut.commandColour = RED
                    print("Error: set.options.mvb")
            elif command == "sib":
                if value == "true":
                    if not SkipIntroButton.ticked:
                        SIB_switch(SkipIntroButton)
                    astronaut.commandColour = GREEN
                elif value == "false":
                    if SkipIntroButton.ticked:
                        SIB_switch(SkipIntroButton)
                    astronaut.commandColour = GREEN
                else:
                    astronaut.commandColour = RED
                    print("Error: set.options.sib")
            else:
                astronaut.commandColour = RED
                print("Error: set.options")
                astronaut.commandColour = RED
                print("Error: set.list")
        elif key == "state":
            if command == "load":
                if value in ["1","2","3","h","4","5","6","7","8"]:
                    if value == "h":
                        state = 2.5
                        background.image = RoomH
                        loading_screen(astronaut, 3, 2.5)
                        astronaut.commandColour = GREEN
                        return 2.5
                    else:
                        state = int(value)
                        background.image = Rooms[state-1]
                        loading_screen(astronaut, 3, int(value))
                        astronaut.commandColour = GREEN
                        return int(value)
                else:
                    astronaut.commandColour = RED
                    print("Error: set.state.load")
            else:
                astronaut.commandColour = RED
                print("Error: set.load")
        elif key == "injure":
            if command == "faint":
                if value == "astronaut":
                    faint()
                    astronaut.health = 100
                    spawn_furnitures(1)
                    astronaut.commandColour = GREEN
                    return 1
                else:
                    astronaut.commandColour = RED
                    print("Error: set.injure.faint")
            elif command == "die":
                if value == "astronaut":
                    astronaut.commandColour = GREEN
                    return "Die"
                else:
                    astronaut.commandColour = RED
                    print("Error: set.injure.die")
            else:
                astronaut.commandColour = RED
                print("Error: set.injure")
    elif state == "add":
        if key == "astronaut":
            if command == "health":
                if int(value) > 0:
                    astronaut.health += int(value)
                    astronaut.commandColour = GREEN
                else:
                    astronaut.commandColour = RED
                    print("Error: add.astronaut.health")
            elif command == "speed":
                if int(value) > 0:
                    astronaut.speed += int(value)
                    astronaut.commandColour = GREEN
                else:
                    astronaut.commandColour = RED
                    print("Error: add.astronaut.speed")
            elif command == "x":
                if int(value) > 0 and int(value) < WIDTH:
                    astronaut.position.x += int(value)
                    astronaut.rect.x += int(value)
                    astronaut.commandColour = GREEN
                else:
                    astronaut.commandColour = RED
                    print("Error: add.astronaut.x")
            elif command == "y":
                if int(value) > 0 and int(value) < HEIGHT:
                    astronaut.position.y += int(value)
                    astronaut.rect.y += int(value)
                    astronaut.commandColour = GREEN
                else:
                    astronaut.commandColour = RED
                    print("Error: add.astronaut.y")
            elif command == "lives":
                if int(value) > 0:
                    astronaut.lives += int(value)
                    astronaut.commandColour = GREEN
                else:
                    astronaut.commandColour = RED
                    print("Error: add.astronaut.lives")
            elif command == "damage":
                if int(value) > 0:
                    astronaut.damage += int(value)
                    astronaut.commandColour = GREEN
                else:
                    astronaut.commandColour = RED
                    print("Error: add.astronaut.damage")
            else:
                astronaut.commandColour = RED
                print("Error: add.astronaut")
        else:
            astronaut.commandColour = RED
            print("Error: add")
    else:
        astronaut.commandColour = RED
        print("Error: state")
    
def command(astronaut):
    #Variables
    global text
    typeHeight = 30
    typeY = HEIGHT-typeHeight
    cursorBorder = 4
    cursorWidth = 3

    #Character List to Text, Render, Calculate Cursor X
    text = "".join(characters)
    textRender = pygame.font.Font.render(commandFont, text, True, WHITE)
    textWidth = textRender.get_width() + cursorBorder

    #Draw Command Screen
    window.fill(astronaut.commandColour)
    pygame.draw.rect(window, BLACK, (0, typeY, WIDTH, typeHeight))  # Clear the input area
    pygame.draw.rect(window, WHITE, (textWidth, typeY + cursorBorder, cursorWidth, typeHeight - cursorBorder * 2))
    window.blit(textRender, (0, typeY))

    pygame.display.flip()

def show_help():
    window.blit(helpImage, (0,0))
    pygame.display.flip()

def inventory_flash(astronaut):
    astronaut.inventoryTimer += 1
    if astronaut.inventoryTimer < 200:
        if astronaut.inventory == 1:
            window.blit(InventoryFlashImage1, (0,0))
        elif astronaut.inventory == 2:
            window.blit(InventoryFlashImage2, (0,0))
        elif astronaut.inventory == 3:
            window.blit(InventoryFlashImage3, (0,0))
        elif astronaut.inventory == 4:
            window.blit(InventoryFlashImage4, (0,0))
        elif astronaut.inventory == 5:
            window.blit(InventoryFlashImage5, (0,0))
    if astronaut.inventory >= 100:
        return True

def draw_display(state, astronaut, gun, background, shootingTimer, title, startButton, optionsButton, 
                doorFlashState, deadBody1, backArrow, MasterVolumeButton, SkipIntroButton, cupboard1, 
                bed2, controlPanel, tableK, healthBar):
    window.fill((0,0,0))   

    #Menu
    if state == 0:
        #Background
        window.blit(SpaceBackground1, SpaceBackground1.get_rect())

        #Title
        window.blit(title.scaledImage, title.rect)
        title.scale()

        #Start Button
        window.blit(startButton.scaledImage, startButton.rect)
        startButton.scale()

        #Options Button
        window.blit(optionsButton.scaledImage, optionsButton.rect)
        optionsButton.scale()

    #Options
    if state == -2:
        #Background
        window.blit(SpaceBackground1, SpaceBackground1.get_rect())

        #Title
        window.blit(title.scaledImage, title.rect)
        title.scale()

        #Back Arrow
        window.blit(backArrow.image, backArrow.rect)

        #Tick Boxes and Labels
        window.blit(MasterVolumeButton.image, MasterVolumeButton.rect)
        window.blit(MasterVolumeButton.textRender, MasterVolumeButton.textRect)

        window.blit(SkipIntroButton.image, SkipIntroButton.rect)
        window.blit(SkipIntroButton.textRender, SkipIntroButton.textRect)

    #Game
    elif state != 0 and state != -1 and state != -2:
        #Draw Background
        if state == 1:
            background.image = Room1
            background.rect = background.image.get_rect()
        window.blit(background.image, background.rect)

        #Draw Landing Pad Detail
        if state == 1:
            pygame.draw.rect(window, (255,255,0), (WIDTH/2-5,HEIGHT/2-100, 10,200))
            pygame.draw.rect(window, (255,255,0), (WIDTH/2-100,HEIGHT/2-5, 200,10))

        #Draw Inventory Frame and Items
        window.blit(InventoryFrame, InventoryFramePosition)
        if astronaut.inventory == 1:
            window.blit(Keycard1Image, KeycardPosition)
        elif astronaut.inventory == 2:
            window.blit(Keycard2Image, KeycardPosition)
        elif astronaut.inventory == 3:
            window.blit(Keycard3Image, KeycardPosition) 
        elif astronaut.inventory == 23:
            window.blit(Keycard23Image, KeycardPosition)
        elif astronaut.inventory == 4:
            window.blit(Keycard4Image, KeycardPosition)

        #Highlight And Draw DeadBody1
        if state == 1:
            deadBody1.highlight(astronaut)
            window.blit(deadBody1.rotatedImage, deadBody1.rect)
            deadBody1.move()

        #Calculate and Draw DoorFlash
        if doorFlashState in [1,5]:
            if state in [1, 2, 2.5, 4]:
                draw_doorFlash(doorFlashState)
        if doorFlashState in [2,6]:
            if state in [2, 2.5, 4, 8]:
                draw_doorFlash(doorFlashState)
        if doorFlashState in [3,7]:
            if state in [2, 2.5, 6, 7]:
                draw_doorFlash(doorFlashState)
        if doorFlashState in [4,8]:
            if state in [2, 2.5, 3, 5]:
                draw_doorFlash(doorFlashState)

        #Draw Monsters And Move Towards Astronaut
        if state == 2.5:
            for monster in RoomHMonsters:
                if monster.on:
                    window.blit(monster.image, (monster.position.x, monster.position.y, monster.rect.x, monster.rect.y))
                    monster_move(monster, astronaut)
        else:
            for monster in RoomMonsters[state]:
                if monster.on:
                    window.blit(monster.image, (monster.position.x, monster.position.y, monster.rect.x, monster.rect.y))
                    monster_move(monster, astronaut)

        #Draw Furniture
        for furniture in furnitures:
            window.blit(furniture.image, furniture.rect)

        #Draw Small Inventory Icons
        if not astronaut.door1locked and astronaut.inventory != 1:
            window.blit(pygame.transform.scale(Keycard1Image, (10,10)), (93+50+5, 4))
        if not astronaut.door2locked1 and astronaut.inventory not in [2,23]:
            window.blit(pygame.transform.scale(Keycard2Image, (10,10)), (93+50+5, 16))
        if not astronaut.door2locked2 and astronaut.inventory not in [3,23]:
            window.blit(pygame.transform.scale(Keycard3Image, (10,10)), (93+50+5, 28))
        if not astronaut.door3locked and astronaut.inventory != 4:
            window.blit(pygame.transform.scale(Keycard4Image, (10,10)), (93+50+5, 40))

        #Highlight And Draw Bed2
        if state == 6:
            bed2.highlight(astronaut)
            window.blit(bed2.image, bed2.rect)

        #Highlight And Draw Cupboard
        if state == 5:
            cupboard1.highlight(astronaut)
            window.blit(cupboard1.image, cupboard1.rect)

        #Highlight And Draw Control Panel
        if state == 7:
            controlPanel.highlight(astronaut)
            window.blit(controlPanel.image, controlPanel.rect)

        #Highlight And Draw TableK
        if state == 3:
            tableK.highlight(astronaut)
            window.blit(tableK.image, tableK.rect)

        #Draw Astronaut Behind Gun
        if (astronaut.facing != IN) or (astronaut.facing != WN):
            window.blit(astronaut.image, astronaut.rect)

        #Draw And Move Gun, Gun Visible Timer
        if shootingTimer >= 200:
            gun.visible = False
            shootingTimer = 0
        move_gun(gun)

        #Draw Bullets
        for bullet in bullets:
            pygame.draw.rect(window, bullet.colour, bullet.rect)
            bullet.move()

        #Draw Astronaut In Front Of Gun
        if (astronaut.facing == IN) or (astronaut.facing == WN):
            window.blit(astronaut.image, astronaut.rect)

        #Create And Draw Hearts
        create_hearts(astronaut.lives, astronaut)
        for heart in hearts:
            window.blit(heart.image, heart.rect)

        #Update And Draw Health Bar
        healthBar.update(astronaut)
        pygame.draw.rect(window, healthBar.colour, healthBar.barRect)
        window.blit(healthBar.image, healthBar.rect)

def main():
    #Clock Object, Run Condition, Pause Flag
    clock = pygame.time.Clock()
    running = True
    Paused = False
    Command = False
    timerOn = False
    inventoryFlash = False

    #Startup And Intitialise
    if True:
        #Inititalise The All Mighty Game State
        global state
        state = 0

        #Create Timers
        shootingTimer = 0
        doorFlashState = 0

        #Create Permanent Instances
        startVideo = StartVideo()
        title = Title(titleImage)
        startButton = StartButton(startButtonImage1)
        optionsButton = OptionsButton(optionsButtonImage1)
        backArrow = BackArrow()
        background = Background(Room1, 0, 0)
        astronaut = Astronaut()
        gun = Gun(astronaut)
        deadBody1 = DeadBody1()
        cupboard1 = Cupboard()
        bed2 = Bed2()
        controlPanel = ControlPanel()
        tableK = TableK()
        healthBar = HealthBar(astronaut)

        #Tick Boxes
        MasterVolumeButton = TickBox(110,220,MVB,"Master Volume")
        SkipIntroButton = TickBox(110,280,SIB,"Skip Intro")

        #Turn Master Volume "On and Off"
        MVB_switch(MasterVolumeButton)
        MVB_switch(MasterVolumeButton)

        #Map Showing Flag
        map_showing = False
        help_showing = False

    while running:
        clock.tick(FPS)
        #Previous Inventory State
        prevInventory = astronaut.inventory

        #While Game is Playing
        if not Paused and not Command:
            #Mouse Positions Per Frame
            mx, my = pygame.mouse.get_pos()

            #Key And Mouse Presses
            for event in pygame.event.get():
                #Quit Game
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                
                #MouseRightButton Functions
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if state != 0 and state != -1 and state != -2: #Shoot Gun/Create Bullets/Reset Gun Visible Timer
                        create_bullet(gun)
                        shootingTimer = 0
                        gun.visible = True
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound(gunShoot1Sound))
                    elif state == 0: #Start Game
                        if mouseOver_check(mx, my, startButton, 2, 20, 4, 20):
                            pygame.mixer.Channel(2).play(pygame.mixer.Sound(startSound))
                            state = -1
                            start_loading_screen()
                        if mouseOver_check(mx, my, optionsButton, 2, 20, 4, 20):
                            state = -2
                    elif state == -2: #Options
                        if mouseOver_check(mx, my, backArrow, 1,0,1,0):
                            state = 0

                        if mouseOver_check(mx, my, MasterVolumeButton, 1,100,4,30):
                            MVB_switch(MasterVolumeButton)
                        if mouseOver_check(mx, my, SkipIntroButton, 1,100,4,30):
                            SIB_switch(SkipIntroButton)

                #SpaceBar Functions
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    if state == 1: #Docking Bay
                        if doorFlashState == 1: #North
                            state = 2 #Lobby
                            background.image = Room2
                            loading_screen(astronaut, 3, state)
                            astronaut.inventory = 0
                        if deadBody1.highlighted == True and astronaut.door1locked == True:
                            astronaut.door1locked = False
                            astronaut.inventory = 1
                    elif state == 2: #Lobby
                        if doorFlashState == 1: #North
                            state = 7 #Control Room
                            background.image = Room7
                            loading_screen(astronaut, 3, state)
                            astronaut.inventory = 0
                        elif doorFlashState == 2: #East
                            state = 2.5 #Hallway
                            background.image = RoomH
                            loading_screen(astronaut, 4, state)
                        elif doorFlashState == 3: #South
                            state = 1 #Docking Bay
                            background.image = Room1
                            loading_screen(astronaut, 1, state)
                        elif doorFlashState == 4: #West
                            state = 8 #Storage Room
                            background.image = Room8
                            loading_screen(astronaut, 2, state)
                    elif state == 2.5: #Hallway
                        if doorFlashState == 1: #North
                            state = 6 #Captain's Quarters
                            background.image = Room6
                            loading_screen(astronaut, 3, state)
                        elif doorFlashState == 2: #East
                            state = 3 #Officer's Quarters 1
                            background.image = Room3
                            loading_screen(astronaut, 4, state)
                        elif doorFlashState == 3: #South
                            state = 4 #Officer's Quarters 2
                            background.image = Room4
                            loading_screen(astronaut, 1, state)
                        elif doorFlashState == 4: #West
                            state = 2 #Lobby
                            background.image = Room2
                            loading_screen(astronaut, 2, state)
                    elif state == 3: #Officer's Quarters 1
                        if doorFlashState == 4: #West
                            state = 2.5 #Hallway
                            background.image = RoomH
                            loading_screen(astronaut, 2, state)
                        
                        if tableK.highlighted == True and astronaut.door2locked2 == True:
                            astronaut.door2locked2 = False
                            astronaut.inventory = 3
                    elif state == 4: #Officer's Quarters 2
                        if doorFlashState == 1: #North
                            state = 2.5 #Hallway
                            background.image = RoomH
                            loading_screen(astronaut, 3, state)
                        elif doorFlashState == 2: #East
                            state = 5 #Ensuite
                            background.image = Room5
                            loading_screen(astronaut, 4, state)
                    elif state == 5: #Ensuite
                        if doorFlashState == 4: #West
                            state = 4 #Officer's Quarters 2
                            background.image = Room4
                            loading_screen(astronaut, 2, state)

                        if cupboard1.highlighted == True and astronaut.door2locked1 == True:
                            astronaut.door2locked1 = False
                            astronaut.inventory = 2
                    elif state == 6: #Captain's Quarters
                        if doorFlashState == 3: #South
                            state = 2.5 #Hallway
                            background.image = RoomH
                            loading_screen(astronaut, 1, state)

                        if bed2.highlighted == True and astronaut.door3locked == True:
                            astronaut.door3locked = False
                            astronaut.inventory = 4
                    elif state == 7: #Control Room
                        if doorFlashState == 3: #South
                            state = 2 #Lobby
                            background.image = Room2
                            loading_screen(astronaut, 1, state)

                        if controlPanel.highlighted == True and astronaut.door4locked == True:
                            astronaut.door4locked = False
                            astronaut.inventory = 5
                    elif state == 8: #Storage Room
                        if doorFlashState == 2: #East
                            state = 2 #Lobby
                            background.image = Room2
                            loading_screen(astronaut, 4, state)

                #Letter Presses DOWN
                if event.type == pygame.KEYDOWN:
                    #Enable Map
                    if event.key == pygame.K_m and state not in [0,-1,-2]:
                        map_showing = True

                    #Enable Help
                    if event.key == pygame.K_h and state not in [0,-1,-2]:
                        help_showing = True
                        
                    #Pause (Mute)
                    if event.key == pygame.K_p and state not in [0,-1,-2]:
                        Paused = True
                        MVB_switch(MasterVolumeButton)

                    #Command
                    if event.key == pygame.K_BACKQUOTE and state not in [0,-1,-2]:
                        Command = True

                #Letter Presses UP
                if event.type == pygame.KEYUP:
                    #Disable Map
                    if event.key == pygame.K_m and state not in [0,-1,-2]:
                        map_showing = False

                    #Disable Help
                    if event.key == pygame.K_h and state not in [0,-1,-2]:
                        help_showing = False

            #Start Inventroy Flash
            if prevInventory != astronaut.inventory:
                astronaut.inventoryTimer = 0
                inventoryFlash = True

            #Set Double Keycard Inventory
            if not astronaut.door2locked1 and not astronaut.door2locked2 and astronaut.door3locked:
                astronaut.inventory = 23

            #Menu Screen Hover
            if state == 0:
                #Start Button MouseHover Animation
                if mouseOver_check(mx, my, startButton, 2, 20, 4, 20):
                    startButton.mouseOver(startButtonImage2)
                else:
                    startButton.mouseOver(startButtonImage1)

                if mouseOver_check(mx, my, optionsButton, 2, 20, 4, 20):
                    optionsButton.mouseOver(optionsButtonImage2)
                else:
                    optionsButton.mouseOver(optionsButtonImage1)

            #Play Game Music
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.play(-1)

            #Handle Monsters
            monster_collisions(astronaut)
            kill_monsters(astronaut)

            #Key Presses
            keysPressed = pygame.key.get_pressed()
            handle_keys(keysPressed, astronaut)
        
            #Update
            shootingTimer += 1
            doorFlashState = door_selector(astronaut, state)

            #Map Or Display
            if map_showing:
                show_map(state)
            elif help_showing:
                show_help()
            else:
                draw_display(state, astronaut, gun, background, shootingTimer, title, startButton, optionsButton, 
                            doorFlashState, deadBody1, backArrow, MasterVolumeButton, SkipIntroButton, cupboard1, 
                            bed2, controlPanel, tableK, healthBar)

            #Draw Inventory Flash
            if inventoryFlash:
                if inventory_flash(astronaut):
                    inventoryFlash = False

            #Die And Faint
            for event in pygame.event.get():
                if event.type == FAINTED:
                    faint()
                    state = 1
                    astronaut.health = 100
                    spawn_furnitures(1)
                    pygame.event.clear(FAINTED)

                if event.type == DIED:
                    die()
                    pygame.event.clear(DIED)

            #Start Video And Scroll Intro
            if state == -1:
                if not SkipIntroButton.ticked:
                    opening_scene(startVideo)
                state = 1
                timerOn = True

            #End Scene
            if state == 8:
                end_scene(astronaut)

            #Increment Timer
            if timerOn:
                astronaut.timer += 1

            pygame.display.flip()

        #While Game is Paused
        else:
            for event in pygame.event.get():
                #When Game is Paused
                if Paused:
                    #Unpause (Unmute)
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_p and Paused:
                        Paused = False
                        MVB_switch(MasterVolumeButton)

                    #Quit Game
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        pygame.quit()

                    window.blit(pauseImage, pauseRect)
                    pygame.display.flip()

                #When in Command Prompt
                if Command:
                    #Command Quit
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKQUOTE and Command:
                        Command = False

                    #Quit Game
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        pygame.quit()

                    #Command Prompt Actions
                    if event.type == pygame.KEYDOWN:
                        #Enter and Run Command
                        if event.key == pygame.K_RETURN:
                            newState = run_command(characters, astronaut, MasterVolumeButton, SkipIntroButton, background)
                            #If Change State Command is Run
                            if newState:
                                if newState == "Die":
                                    Command = False
                                    die()
                                else:
                                    state = newState
                                    Command = False

                        #Backspace
                        elif event.key == pygame.K_BACKSPACE:
                            astronaut.commandColour = WHITE
                            if len(characters) > 0:
                                characters.pop()

                        #Add Key when Key in List is Pressed
                        elif event.key in keys:
                            astronaut.commandColour = WHITE
                            characters.append(keys[event.key])

                    command(astronaut)

    pygame.quit()

if __name__ == "__main__":
    main()