import pygame
from config import COL_SECONDARY, COL_EXIT, VIEW_DIST


class Cell:

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, screen, player_pos):

        # Дальность прорисовки
        if abs(self.x - player_pos[0]) < VIEW_DIST and abs(self.y - player_pos[1]) < VIEW_DIST:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        elif self.color is not COL_EXIT:
            pygame.draw.rect(screen, COL_SECONDARY, (self.x, self.y, self.width, self.height))
