import math
import pygame

explosion_images = [pygame.image.load(f"source/explosion{i}.png") for i in range(1, 8)]


class GameObject:
    def __init__(self, image_path, x, y, speed, scales):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, scales)
        self.x = x
        self.y = y
        self.speed = speed
        self.angle = 0
        self.target_angle = 0
        self.rotation_speed = 5
        self.rect = self.image.get_rect(center=(self.x, self.y))    
        self.exploding = False
        self.explosion_frame = 0
        self.alive = True
    
    def rotate_towards_target(self):
        angle_diff = (self.target_angle - self.angle + 180) % 360 - 180
        if abs(angle_diff) > self.rotation_speed:
            self.angle += self.rotation_speed * (1 if angle_diff > 0 else -1)
        else:
            self.angle = self.target_angle
    
    def move(self):
        if not self.exploding:
            self.x += self.speed * math.cos(math.radians(self.angle))
            self.y -= self.speed * math.sin(math.radians(self.angle))
            self.rect.center = (self.x, self.y)
    
    def draw(self, surface, camera_x, camera_y):
        if self.exploding:
            if self.explosion_frame < len(explosion_images):
                explosion_image = pygame.transform.scale(explosion_images[self.explosion_frame], (100, 100))
                surface.blit(explosion_image, (self.x - camera_x - 25, self.y - camera_y - 25))
                self.explosion_frame = self.explosion_frame + 1
            else:
                self.alive = False
        elif self.alive:
            rotated_image = pygame.transform.rotate(self.image, self.angle)
            new_rect = rotated_image.get_rect(center=(self.x - camera_x, self.y - camera_y))
            surface.blit(rotated_image, new_rect.topleft)
    
    def check_collision(self, other):
        return self.rect.colliderect(other.rect) and self.alive and other.alive
    
    def explode(self):
        if not self.exploding:
            self.exploding = True
            self.explosion_frame = 0
            self.image = pygame.Surface((0, 0), pygame.SRCALPHA)