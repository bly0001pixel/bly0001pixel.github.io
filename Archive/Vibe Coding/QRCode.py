import pygame
import qrcode
import io
from PIL import Image
import sys

# --- Config ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BG_COLOR = (30, 30, 30)
TEXT_COLOR = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("QR Code Generator")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 28)

# --- Input and State ---
user_input = ""
qr_surface = None
zoom = 1.0
offset = [0, 0]
dragging = False
drag_start = (0, 0)
offset_start = (0, 0)

def generate_qr_surface(text):
    if not text:
        return None
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=10,
        border=2
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img_io = io.BytesIO()
    img.save(img_io, format="PNG")
    img_io.seek(0)
    qr_img = pygame.image.load(img_io, "qr.png").convert()
    return qr_img

running = True
while running:
    clock.tick(60)
    screen.fill(BG_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Text input
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            elif event.key == pygame.K_RETURN:
                qr_surface = generate_qr_surface(user_input)
            elif event.key == pygame.K_s:
                if qr_surface:
                    pygame.image.save(qr_surface, "qr_output.png")
                    print("QR code saved as qr_output.png")
            else:
                user_input += event.unicode

        # Zoom with mouse wheel
        elif event.type == pygame.MOUSEWHEEL:
            old_zoom = zoom
            zoom *= 1.1 if event.y > 0 else 0.9
            zoom = max(0.1, min(zoom, 10))
            mx, my = pygame.mouse.get_pos()
            offset[0] = mx - (mx - offset[0]) * (zoom / old_zoom)
            offset[1] = my - (my - offset[1]) * (zoom / old_zoom)

        # Start dragging
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            dragging = True
            drag_start = pygame.mouse.get_pos()
            offset_start = list(offset)

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            dragging = False

    # Drag logic
    if dragging:
        mx, my = pygame.mouse.get_pos()
        dx = mx - drag_start[0]
        dy = my - drag_start[1]
        offset[0] = offset_start[0] + dx
        offset[1] = offset_start[1] + dy

    # Draw QR code
    if qr_surface:
        qr_scaled = pygame.transform.smoothscale(
            qr_surface,
            (int(qr_surface.get_width() * zoom), int(qr_surface.get_height() * zoom))
        )
        screen.blit(qr_scaled, qr_scaled.get_rect(center=(SCREEN_WIDTH//2 + offset[0], SCREEN_HEIGHT//2 + offset[1])))

    # Draw input field
    input_text = font.render("Input: " + user_input, True, TEXT_COLOR)
    screen.blit(input_text, (10, SCREEN_HEIGHT - 35))

    pygame.display.flip()

pygame.quit()
sys.exit()
