import pygame
from config import COL_PRIMARY, COL_SECONDARY, COL_EXIT

class Cell:

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, screen, player_pos):

        # Only draw cells that are not farther than 5 cells from player_pos

        if abs(self.x - player_pos[0]) < 100 and abs(self.y - player_pos[1]) < 100:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        elif self.color is not COL_EXIT:
            pygame.draw.rect(screen, COL_SECONDARY, (self.x, self.y, self.width, self.height))
