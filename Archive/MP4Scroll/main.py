import cv2
import pygame
import sys

# Setup
video_path = "Succession (HBO TV Series) - Main Title [Piano Version].mp4"
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Error: Cannot open video.")
    sys.exit()

total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Pygame init
pygame.init()
window = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("MP4Scroll")

frame_index = 136

def get_frame(index):
    cap.set(cv2.CAP_PROP_POS_FRAMES, index)
    ret, frame = cap.read()
    if not ret:
        return None
    frame = cv2.resize(frame, (1080, 720))
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    return pygame.surfarray.make_surface(frame.swapaxes(0, 1))

running = True
clock = pygame.time.Clock()

while running:
    clock.tick(30)  # Limit refresh rate

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Scroll to navigate frames
        elif event.type == pygame.MOUSEWHEEL:
            frame_index += event.y * 4 #Adjust sensitivity here
            frame_index = max(0, min(total_frames - 1, frame_index))

        elif event.type == pygame.MOUSEWHEEL and event.type == pygame.K_LSHIFT:
            frame_index += event.y * 1 #Adjust sensitivity here
            frame_index = max(0, min(total_frames - 1, frame_index))

        elif event.type == pygame.MOUSEWHEEL and event.type == pygame.K_LCTRL:
            frame_index += event.y * 8 #Adjust sensitivity here
            frame_index = max(0, min(total_frames - 1, frame_index))

    frame_surface = get_frame(frame_index)
    if frame_surface:
        window.blit(frame_surface, (0, 0))
        pygame.display.flip()

    print(frame_index)

pygame.quit()
cap.release()