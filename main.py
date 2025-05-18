import pygame
from random import randint
from copy import deepcopy
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

BLOCK_SIZE = 30
GRID_WIDTH = 10
GRID_HEIGHT = 20
SCREEN_WIDHT = BLOCK_SIZE * (GRID_WIDTH + 6)
SCREEN_HEIGHT = BLOCK_SIZE * GRID_HEIGHT

count = 0
speed = 60
limit = 2000

figures_pos = [[(-1, 0), (-2, 0), (0, 0), (1, 0)], #I
               [(0, -1), (-1, -1), (-1, 0), (0, 0)], #O
               [(-1, 0), (-1, 1), (0, 0), (0, -1)], #Z
               [(0, 0), (-1, 0), (0, 1), (-1, -1)], #S
               [(0, 0), (0, -1), (0, 1), (-1, -1)], #L
               [(0, 0), (0, -1), (0, 1), (1, -1)], #J
               [(0, 0), (0, -1), (0, 1), (-1, 0)]] #T


field = [[0 for i in range(GRID_WIDTH + 1)] for j in range(GRID_HEIGHT)]
figures = []
for fig_pos in figures_pos:
    figure = []
    for x, y in fig_pos:
        figure.append(pygame.Rect(x + GRID_WIDTH//2, y+1, 1, 1))
    figures.append(figure)
figure_rect = pygame.Rect(0, 0, BLOCK_SIZE - 1, BLOCK_SIZE - 1)
figure = deepcopy(figures[randint(0, 6)])

screen = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGHT))
pygame.display.set_caption('Тетрис')

clock = pygame.time.Clock()

running = True
font1 = pygame.font.SysFont(None, 36)

def border():
    if figure[i].x < 1 or figure[i].x > GRID_WIDTH:
        return True
    elif figure[i].y > GRID_HEIGHT - 1 or field[figure[i].y][figure[i].x]:
        return True
    return False

while running:
    dx = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -1
            elif event.key == pygame.K_RIGHT:
                dx = 1
            elif event.key == pygame.K_DOWN:
                limit = 100
            
    screen.fill(BLACK)

    figure_old = deepcopy(figure)
    for i in range(4):
        figure[i].x += dx
        if border():
            figure = deepcopy(figure_old)
            break

    count += speed
    if count > limit:
        count = 0
        figure_old = deepcopy(figure)
        for i in range(4):
            figure[i].y += 1
            if border():
                for i in range(4):
                    field[figure_old[i].y][figure_old[i].x] =  WHITE
                figure = deepcopy(figures[randint(0, 6)])
                limit = 2000
                break

    #Создаём игровую область
    pygame.draw.rect(screen, WHITE, (30, 0, 
            BLOCK_SIZE * GRID_WIDTH, BLOCK_SIZE * GRID_HEIGHT), 1)

    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            pygame.draw.rect(screen, GRAY,
            (30 + x * BLOCK_SIZE,
            y * BLOCK_SIZE,
            BLOCK_SIZE, BLOCK_SIZE), 1)

    for i in range(4):
        figure_rect.x = figure[i].x * BLOCK_SIZE
        figure_rect.y = figure[i].y * BLOCK_SIZE
        pygame.draw.rect(screen, WHITE, figure_rect)

    for y, raw in enumerate(field):
        for x, col in enumerate(raw):
            if col:
                figure_rect.x, figure_rect.y = x * BLOCK_SIZE, y * BLOCK_SIZE
                pygame.draw.rect(screen, col, figure_rect)
    
    score_text = font1.render(f"Счёт: score", True, WHITE)
    level_text = font1.render(f"Уровень: level", True, WHITE)
    screen.blit(score_text, (30 + GRID_WIDTH * BLOCK_SIZE + 20, 30))
    screen.blit(level_text, (30 + GRID_WIDTH * BLOCK_SIZE + 20, 70))
    pygame.display.update()
    clock.tick(60)
