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

player = Player(WIDTH//2, HEIGHT//2)
bomb = Bomb(random.randint(player.x - 600, player.x + 600), random.randint(player.y - 600, player.y + 600))

running = True
clock = pygame.time.Clock()
mouse_held = False

while running:
    screen.fill((135, 206, 235))  
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_held = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_held = False
    
    if player.alive:
        player.update(mouse_held, pygame.mouse.get_pos(), camera_x, camera_y)
    if bomb.alive:
        bomb.update(player)
    
    
    if player.check_collision(bomb):
        player.explode()
        bomb.explode()


    camera_x = player.x - WIDTH // 2
    camera_y = player.y - HEIGHT // 2
    
    player.draw(screen, camera_x, camera_y)
    bomb.draw(screen, camera_x, camera_y)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()