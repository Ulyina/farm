# player.py
import pygame
from plants import Corn, Potato, Carrot

class Player:
    def __init__(self, screen_height):
        self.money = 100
        self.water = 100
        self.plants = []
        self.selected_crop = 'Кукуруза'
        self.inventory = {"Кукуруза": 5, "Картошка": 5, "Морковка": 5}
        self.screen_height = screen_height

    def plant(self, x, y):
        # Ограничиваем посадку только на игровом поле
        if y > self.screen_height - 80 or x >= 500:  # Запрет на правую часть
            return

        # Приведение координат к центру клеток
        grid_x = (x // 60) * 60 + 30
        grid_y = (y // 60) * 60 + 30

        # Проверяем, находится ли клетка в разрешенной зоне
        if (grid_x // 60) % 2 == 0 or (grid_y // 60) % 2 == 0:
            return  # Клетка не разрешена для посадки

        # Проверяем, можно ли посадить растение
        if all(not plant.rect.collidepoint(grid_x, grid_y) for plant in self.plants):
            if self.selected_crop == 'Кукуруза' and self.inventory["Кукуруза"] > 0:
                self.plants.append(Corn(grid_x - 30, grid_y - 30))
                self.inventory["Кукуруза"] -= 1
            elif self.selected_crop == 'Картошка' and self.inventory["Картошка"] > 0:
                self.plants.append(Potato(grid_x - 30, grid_y - 30))
                self.inventory["Картошка"] -= 1
            elif self.selected_crop == 'Морковка' and self.inventory["Морковка"] > 0:
                self.plants.append(Carrot(grid_x - 30, grid_y - 30))
                self.inventory["Морковка"] -= 1

    def water_plant(self, x, y):
        for plant in self.plants:
            if plant.rect.collidepoint(x, y) and self.water > 0:
                plant.water()
                self.water -= 1
                break

    def harvest_plant(self, x, y):
        for plant in self.plants[:]:
            if plant.rect.collidepoint(x, y) and plant.can_harvest():
                self.money += 20  # Добавляем деньги за урожай
                self.plants.remove(plant)  # Удаляем собранное растение

    def collect_water(self):
        self.water += 1  # Увеличиваем количество воды

    def draw(self, surface):
        for plant in self.plants:
            plant.update()  # Обновляем состояние растения
            plant.draw(surface)  # Рисуем растение

    def draw_inventory(self, surface):
        font = pygame.font.Font(None, 30)
        x_offset = 105
        for item, count in self.inventory.items():
            item_text = font.render(f"{count}", True, (0, 0, 0))  # Отображаем количество
            surface.blit(item_text, (x_offset, 580))
            x_offset += 150
        water_text = font.render(f"Вода: {self.water}", True, (0, 0, 0))  # Отображаем количество воды
        surface.blit(water_text, (680, 125))
