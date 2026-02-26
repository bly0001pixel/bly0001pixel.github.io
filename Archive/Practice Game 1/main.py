import pygame
pygame.init()
pygame.font.init()
pygame.mixer.init()

WINDOW_HEIGHT = 500
WINDOW_WIDTH = 900
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Practice Space Ship Game")

FPS = 60
WHITE = (255,255,255)
RED = (255,0,0)
YELLOW = (255,255,0)

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
SHIP_VELOCITY = 4
BULLET_VELOCITY = 7
MAX_BULLETS = 3
BORDER = pygame.Rect(445, 0, 10, WINDOW_WIDTH)

HEALTH_FONT = pygame.font.SysFont("comicsans", 30)
WINNER_FONT = pygame.font.SysFont("comicsans", 100)

BULLET_FIRE_SOUND = pygame.mixer.Sound("Assets_GUN+Silencer.mp3")
BULLET_HIT_SOUND = pygame.mixer.Sound("Assets_Grenade+1.mp3")

RED_HIT = pygame.USEREVENT + 1
YELLOW_HIT = pygame.USEREVENT + 2

redSpaceshipImage = pygame.image.load("spaceship_red.png")
redSpaceship = pygame.transform.rotate(pygame.transform.scale(redSpaceshipImage, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
yellowSpaceshipImage = pygame.image.load("spaceship_yellow.png")
yellowSpaceship = pygame.transform.rotate(pygame.transform.scale(yellowSpaceshipImage, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)
SPACE = pygame.transform.scale(pygame.image.load("space.png"), (WINDOW_WIDTH, WINDOW_HEIGHT))

def draw_window(red, yellow, redBullets, yellowBullets, redHealth, yellowHealth):
    window.blit(SPACE, (0,0))

    redHealthText = HEALTH_FONT.render("Health: " + str(redHealth), 1, WHITE)
    yellowHealthText = HEALTH_FONT.render("Health: " + str(yellowHealth), 1, WHITE)
    window.blit(redHealthText, (10,10))
    window.blit(yellowHealthText, (WINDOW_WIDTH - 160, 10))

    window.blit(redSpaceship,(red.x, red.y))
    window.blit(yellowSpaceship,(yellow.x, yellow.y))

    pygame.draw.rect(window, (0,0,0), BORDER)

    for bullet in redBullets:
        pygame.draw.rect(window, RED, bullet)

    for bullet in yellowBullets:
        pygame.draw.rect(window, YELLOW, bullet)

def red_movement(keys_pressed, red):
        if keys_pressed[pygame.K_w] and red.y - SHIP_VELOCITY > 0: #UP R
            red.y -= SHIP_VELOCITY
        if keys_pressed[pygame.K_a] and red.x - SHIP_VELOCITY > 0: #LEFT R
            red.x -= SHIP_VELOCITY
        if keys_pressed[pygame.K_s] and red.y + SHIP_VELOCITY + SPACESHIP_HEIGHT+14 < WINDOW_HEIGHT: #DOWN R
            red.y += SHIP_VELOCITY
        if keys_pressed[pygame.K_d] and red.x + SHIP_VELOCITY + SPACESHIP_WIDTH-16 < BORDER.x: #RIGHT R
            red.x += SHIP_VELOCITY

def yellow_movement(keys_pressed, yellow):
        if keys_pressed[pygame.K_UP] and yellow.y - SHIP_VELOCITY > 0: #UP Y
            yellow.y -= SHIP_VELOCITY
        if keys_pressed[pygame.K_LEFT] and yellow.x - SHIP_VELOCITY > BORDER.x + BORDER.width-3: #LEFT Y
            yellow.x -= SHIP_VELOCITY
        if keys_pressed[pygame.K_DOWN] and yellow.y + SHIP_VELOCITY < WINDOW_HEIGHT-51: #DOWN Y
            yellow.y += SHIP_VELOCITY
        if keys_pressed[pygame.K_RIGHT] and yellow.x + SHIP_VELOCITY + SPACESHIP_WIDTH-16 < WINDOW_WIDTH: #RIGHT Y
            yellow.x += SHIP_VELOCITY

def handle_bullets(redBullets, yellowBullets, red, yellow):
    for bullet in redBullets:
        bullet.x += BULLET_VELOCITY
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            redBullets.remove(bullet)
        elif bullet.x > WINDOW_WIDTH:
            redBullets.remove(bullet)            
    for bullet in yellowBullets:
        bullet.x -= BULLET_VELOCITY
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellowBullets.remove(bullet)
        elif bullet.x < 0:
            yellowBullets.remove(bullet)

def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    window.blit(draw_text, (WINDOW_WIDTH/2 - draw_text.get_width()/2, WINDOW_HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.flip()
    pygame.time.delay(5000)

def main():
    red = pygame.Rect(225,205,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    yellow = pygame.Rect(625,205,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)

    redBullets = []
    yellowBullets = []

    redHealth = 10
    yellowHealth = 10

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.QUIT()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(redBullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x + red.width, red.y + red.height/2 - 2.5, 10, 5)
                    redBullets.append(bullet)
                    pygame.mixer.Sound.play(BULLET_FIRE_SOUND)
                if event.key == pygame.K_RCTRL  and len(yellowBullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x, yellow.y + yellow.height/2 - 2.5, 10, 5)
                    yellowBullets.append(bullet)
                    pygame.mixer.Sound.play(BULLET_FIRE_SOUND)

            if event.type == RED_HIT:
                redHealth -= 1
                pygame.mixer.Sound.play(BULLET_HIT_SOUND)
            if event.type == YELLOW_HIT:
                yellowHealth -= 1
                pygame.mixer.Sound.play(BULLET_HIT_SOUND)

        winnerText = ""
        if redHealth <= 0:
            winnerText = "Yellow Wins!"
        if yellowHealth <= 0:
            winnerText = "Red Wins!"
        if winnerText != "":
            draw_winner(winnerText)
            break

        keys_pressed = pygame.key.get_pressed()
        red_movement(keys_pressed, red)
        yellow_movement(keys_pressed, yellow)
        draw_window(red, yellow, redBullets, yellowBullets, redHealth, yellowHealth)
        handle_bullets(redBullets, yellowBullets, red, yellow)

        pygame.display.flip()
    main()

if __name__ == "__main__":
    main()