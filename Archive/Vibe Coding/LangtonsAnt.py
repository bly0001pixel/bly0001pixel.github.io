import pygame
import sys

# Constants
GRID_WIDTH = 200
GRID_HEIGHT = 200
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ANT_COLOR = (255, 0, 0)

MIN_CELL_SIZE = 2
MAX_CELL_SIZE = 40

# Directions (Up, Right, Down, Left)
DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

class Ant:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dir = 0

    def turn_right(self):
        self.dir = (self.dir + 1) % 4

    def turn_left(self):
        self.dir = (self.dir - 1) % 4

    def move_forward(self):
        dx, dy = DIRS[self.dir]
        self.x = (self.x + dx) % GRID_WIDTH
        self.y = (self.y + dy) % GRID_HEIGHT

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Langton's Ant with Zoom, Drag, and Speed Control")
    clock = pygame.time.Clock()

    grid = [[0 for _ in range(GRID_HEIGHT)] for _ in range(GRID_WIDTH)]
    ant = Ant(GRID_WIDTH // 2, GRID_HEIGHT // 2)

    cell_size = 10
    offset_x = SCREEN_WIDTH // 2 - (ant.x * cell_size)
    offset_y = SCREEN_HEIGHT // 2 - (ant.y * cell_size)

    dragging = False
    drag_start = (0, 0)
    offset_start = (0, 0)

    sim_speed = 10

    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Start dragging
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                dragging = True
                drag_start = pygame.mouse.get_pos()
                offset_start = (offset_x, offset_y)

            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                dragging = False

            # Zoom with mouse wheel
            elif event.type == pygame.MOUSEWHEEL:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                old_cell_size = cell_size
                if event.y > 0:
                    cell_size = min(MAX_CELL_SIZE, cell_size + 1)
                elif event.y < 0:
                    cell_size = max(MIN_CELL_SIZE, cell_size - 1)

                if old_cell_size != cell_size:
                    scale = cell_size / old_cell_size
                    offset_x = mouse_x - (mouse_x - offset_x) * scale
                    offset_y = mouse_y - (mouse_y - offset_y) * scale

            # Speed control using number keys
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    sim_speed = 1
                elif event.key == pygame.K_2:
                    sim_speed = 3
                elif event.key == pygame.K_3:
                    sim_speed = 10
                elif event.key == pygame.K_4:
                    sim_speed = 30
                elif event.key == pygame.K_5:
                    sim_speed = 100
                elif event.key == pygame.K_6:
                    sim_speed = 300
                elif event.key == pygame.K_7:
                    sim_speed = 1000
                elif event.key == pygame.K_8:
                    sim_speed = 3000
                elif event.key == pygame.K_9:
                    sim_speed = 10000
                elif event.key == pygame.K_0:
                    sim_speed = 30000

        # Handle dragging
        if dragging:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            dx = mouse_x - drag_start[0]
            dy = mouse_y - drag_start[1]
            offset_x = offset_start[0] + dx
            offset_y = offset_start[1] + dy

        # Langton's Ant logic
        for _ in range(sim_speed):
            if grid[ant.x][ant.y] == 0:
                grid[ant.x][ant.y] = 1
                ant.turn_right()
            else:
                grid[ant.x][ant.y] = 0
                ant.turn_left()
            ant.move_forward()

        # Drawing
        screen.fill((0, 0, 0))  # Background grey

        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                colour = WHITE if grid[x][y] == 0 else BLACK
                px = x * cell_size + offset_x
                py = y * cell_size + offset_y
                if -cell_size < px < SCREEN_WIDTH and -cell_size < py < SCREEN_HEIGHT:
                    pygame.draw.rect(screen, colour, (px, py, cell_size, cell_size))

        # Draw Ant
        ant_px = ant.x * cell_size + offset_x
        ant_py = ant.y * cell_size + offset_y
        if -cell_size < ant_px < SCREEN_WIDTH and -cell_size < ant_py < SCREEN_HEIGHT:
            pygame.draw.rect(screen, ANT_COLOR, (ant_px, ant_py, cell_size, cell_size))

        # UI: speed display
        font = pygame.font.SysFont(None, 24)
        text = font.render(f"Speed: {sim_speed} steps/frame (1-0)", True, (255, 255, 255))
        screen.blit(text, (10, 10))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
