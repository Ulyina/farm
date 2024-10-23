# inventory.py
import pygame

def draw_inventory(screen, inventory, font, button_rect):
    inventory_surface = pygame.Surface((200, 150))  # Фон инвентаря
    inventory_surface.fill((255, 255, 255))  # Белый фон

    # Позиция фона под кнопкой инвентаря
    x_pos = button_rect.x
    y_pos = button_rect.y + button_rect.height

    screen.blit(inventory_surface, (x_pos, y_pos))  # Позиция фона

    x_offset = 10
    y_offset = 10
    for item, count in inventory.items():
        item_text = font.render(f"{item.capitalize()}: {count}", True, (0, 0, 0))
        screen.blit(item_text, (x_pos + x_offset, y_pos + y_offset))
        y_offset += 30  # Смещение по вертикали для следующего элемента
