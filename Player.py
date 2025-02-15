from Object import GameObject
import math


class Player(GameObject):
    def __init__(self, x, y):
        super().__init__("source/player.png", x, y, speed=3.5, scales = (57, 48))
    
    def update(self, mouse_held, mouse_pos, camera_x, camera_y):
        if not self.exploding:
            if mouse_held:
                mx, my = mouse_pos
                dx, dy = mx - (self.x - camera_x), my - (self.y - camera_y)
                self.target_angle = math.degrees(math.atan2(-dy, dx))
            self.rotate_towards_target()
            self.move()