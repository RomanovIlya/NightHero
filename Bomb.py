from Object import GameObject
import math


class Bomb(GameObject):
    def __init__(self, x, y):
        super().__init__("source/bomb.png", x, y, speed=1, scales = (36, 13))
    
    def update(self, target):
        if not self.exploding:
            dx, dy = target.x - self.x, target.y - self.y
            self.target_angle = math.degrees(math.atan2(-dy, dx))
            self.rotate_towards_target()
            self.move()