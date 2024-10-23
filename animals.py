#animals.py
import pygame
import time

class Animal:
    def __init__(self, x, y, image, product, production_time):
        self.image = pygame.transform.scale(image, (60, 60))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.product = product
        self.production_time = production_time
        self.last_production_time = time.time()

    def collect(self):
        if time.time() - self.last_production_time >= self.production_time:
            return self.product

class Chicken(Animal):
    def __init__(self, x, y):
        super().__init__(x, y, pygame.image.load("chicken.png").convert_alpha(), "egg", 10)

class Cow(Animal):
    def __init__(self, x, y):
        super().__init__(x, y, pygame.image.load("cow.png").convert_alpha(), "milk", 30)
