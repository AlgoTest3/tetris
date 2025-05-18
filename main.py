import pygame
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

BLOCK_SIZE = 30
GRID_WIDTH = 10
GRID_HEIGHT = 20
SCREEN_WIDHT = BLOCK_SIZE * (GRID_WIDTH + 6)
SCREEN_HEIGHT = BLOCK_SIZE * GRID_HEIGHT

screen = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGHT))
pygame.display.set_caption('Тетрис')

clock = pygame.time.Clock()

running = True
font1 = pygame.font.SysFont(None, 36)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLACK)

    #Создаём игровую область
    pygame.draw.rect(screen, WHITE, (30, 0, 
            BLOCK_SIZE * GRID_WIDTH, BLOCK_SIZE * GRID_HEIGHT), 1)

    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            pygame.draw.rect(screen, GRAY,
            (30 + x * BLOCK_SIZE,
            y * BLOCK_SIZE,
            BLOCK_SIZE, BLOCK_SIZE), 1)
    
    score_text = font1.render(f"Счёт: score", True, WHITE)
    level_text = font1.render(f"Уровень: level", True, WHITE)
    screen.blit(score_text, (30 + GRID_WIDTH * BLOCK_SIZE + 20, 30))
    screen.blit(level_text, (30 + GRID_WIDTH * BLOCK_SIZE + 20, 70))
    pygame.display.update()
    clock.tick(60)
