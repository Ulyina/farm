#plants.py
import pygame
import time

cell_size = 60

class Crop:
    def __init__(self, x, y, image, wet_image, grown_image, grow_time):
        self.image = pygame.transform.scale(image, (cell_size, cell_size))
        self.wet_image = pygame.transform.scale(wet_image, (cell_size, cell_size))
        self.grown_image = pygame.transform.scale(grown_image, (cell_size, cell_size))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.watered = False
        self.grown = False
        self.grow_time = grow_time
        self.watered_time = None

    def water(self):
        if not self.watered:
            self.watered = True
            self.watered_time = time.time()

    def update(self):
        if self.watered and not self.grown:
            if time.time() - self.watered_time >= self.grow_time:
                self.grown = True

    def draw(self, surface):
        if self.grown:
            surface.blit(self.grown_image, self.rect)
        elif self.watered:
            surface.blit(self.wet_image, self.rect)
        else:
            surface.blit(self.image, self.rect)

    def can_harvest(self):
        return self.grown

class Corn(Crop):
    def __init__(self, x, y):
        super().__init__(x, y, pygame.image.load("corn.png").convert_alpha(),
                         pygame.image.load("wet_corn.png").convert_alpha(),
                         pygame.image.load("grown_corn.png").convert_alpha(), 15)  # Время роста 15 секунд при поливе

class Potato(Crop):
    def __init__(self, x, y):
        super().__init__(x, y, pygame.image.load("potato.png").convert_alpha(),
                         pygame.image.load("wet_potato.png").convert_alpha(),
                         pygame.image.load("grown_potato.png").convert_alpha(), 15)  # Время роста 15 секунд при поливе

class Carrot(Crop):
    def __init__(self, x, y):
        super().__init__(x, y, pygame.image.load("carrot.png").convert_alpha(),
                         pygame.image.load("wet_carrot.png").convert_alpha(),
                         pygame.image.load("grown_carrot.png").convert_alpha(), 15)  # Время роста 15 секунд при поливе
