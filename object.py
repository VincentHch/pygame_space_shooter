import pygame
import os
import numpy as np
import random

from misc import collide

FUEL = pygame.transform.scale(pygame.image.load(os.path.join("asset", "fuel.png")), (43, 30))
AMMO = pygame.transform.scale(pygame.image.load(os.path.join("asset", "ammo.png")), (35, 35))




class Object:

    def __init__(self, x, y):
        self.pos = np.array([float(x), float(y)])
        self.image = None
        self.mask = None

    def draw(self, window):
        if self.image is None:
            return None

        window.blit(self.image, self.pos)

    def randomize(self, width, height):
        self.set_x(random.randint(self.get_img().get_width(), width - self.get_img().get_width()))
        self.set_y(random.randint(self.get_img().get_height(), height - self.get_img().get_height()))
        return self

    def set_x(self, x):
        self.pos[0] = float(x)

    def set_y(self, y):
        self.pos[1] = float(y)

    def get_x(self):
        return self.pos[0]

    def get_y(self):
        return self.pos[1]

    def get_mask(self):
        return self.mask

    def collision(self, obj):
        return collide(self, obj)

    def get_img(self):
        return self.image

    def get_mask(self):
        return self.mask


class Fuel(Object):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = FUEL
        self.mask = pygame.mask.from_surface(self.image)


class Ammo(Object):

    def __init__(self, x, y, quantity=5):
        super().__init__(x, y)
        self.image = AMMO
        self.mask = pygame.mask.from_surface(self.image)
        self.quantity = quantity

class Background(Object):
    def __init__(self, width, height):
        super().__init__(0,0)
        self.image = pygame.transform.scale(pygame.image.load(os.path.join("asset", "space.png")), (width, height))
        self.mask = pygame.mask.from_surface(self.image)