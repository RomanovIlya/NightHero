import pygame
import random
from Bomb import Bomb
from Player import Player

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 540, 790
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("NightHero")

# Камера
camera_x, camera_y = 0, 0
score = 0

player = Player(WIDTH//2, HEIGHT//2)
bombs = []

running = True
clock = pygame.time.Clock()
mouse_held = False

next_bomb_time = pygame.time.get_ticks()

font = pygame.font.Font(None, 80)

def spawn_bomb():
    x = 0
    y =0
    while x < player.x - 500 or x > player.x + 500 or y > player.y + 500 or y < player.y - 500:
        x = random.randint(int(player.x)-500, int(player.x)+500)
        y = random.randint(int(player.y)-500, int(player.y)+500)
    bombs.append(Bomb(x, y))

while running:
    screen.fill((135, 206, 235)) 
    text = font.render(str(score//16), True, (255, 255, 255)) 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_held = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_held = False
    
    if player.alive:
        player.update(mouse_held, pygame.mouse.get_pos(), camera_x, camera_y)
        if pygame.time.get_ticks() > next_bomb_time:
            spawn_bomb()
            next_bomb_time = pygame.time.get_ticks() + 3000  

    for bomb in bombs:
        if bomb.alive:
            bomb.update(player)
    
    for bomb in bombs:
        for other_bomb in bombs:
            if bomb != other_bomb and bomb.check_collision(other_bomb):
                bomb.explode()
                other_bomb.explode()
                score += 10
        if player.check_collision(bomb):
            player.explode()
            bomb.explode()


    camera_x = player.x - WIDTH // 2
    camera_y = player.y - HEIGHT // 2
    
    player.draw(screen, camera_x, camera_y)
    for bomb in bombs:
        bomb.draw(screen, camera_x, camera_y)
    
    screen.blit(text, (WIDTH // 2, 0))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()