import pygame
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'

WIDTH_WIN, HEIGHT_WIN = 400, 400
collide = False
n = 0
block = False
pygame.font.Font(None, 32)
FPS = 60
clock = pygame.time.Clock()
#квадрат
rect_size = w, h = 70, 70
rect_pos = ((WIDTH_WIN - w) // 2, (HEIGHT_WIN - h) // 2)
#круг
circle_radius = 35
circle_pos = (0,0)
#счет
score_pos = (10,10)
#цвета
red = (255,0,0)
blue = (0,0,255)
yellow = (255,255,0)
BG = (128,128,128)

pygame.init()
pygame.display.set_caption('DRAW AND COLIDE')
screen = pygame.display.set_mode((WIDTH_WIN, HEIGHT_WIN))

surface = pygame.Surface((circle_radius * 2, circle_radius * 2), pygame.SRCALPHA)


run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.MOUSEMOTION:
            circle_pos = e.pos
    
    screen.fill(BG)

    rect1 = pygame.draw.circle(screen, yellow, circle_pos, circle_radius)
    rect2 = pygame.draw.rect(screen, red if collide else blue ,(rect_pos, rect_size))
    if rect1.colliderect(rect2):
        collide = True
        if not block:
            n += 1
        block = True
    else:
        collide = False
        block = False
    screen.blit(font.render(str(n), 1, red, (10,10)))
    pygame.display.update()
    clock.tick(FPS)