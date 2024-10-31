import random
import pygame
from config import MAZE_SIZE, SCR_WIDTH, SCR_HEIGHT
from config import COL_SECONDARY, COL_EXIT, COL_PLAYER
from config import COL_PRIMARY
from cell import Cell


class Maze:
    def __init__(self):

        self.player_pos = None
        self.cells = [
            Cell(x * MAZE_SIZE, y * MAZE_SIZE, MAZE_SIZE, MAZE_SIZE, COL_PRIMARY)
            for x in range(0, SCR_WIDTH // MAZE_SIZE)
            for y in range(0, SCR_HEIGHT // MAZE_SIZE)
        ]

        for _ in range(300):
            cell = self.cells.pop(random.randint(0, len(self.cells) - 1))
            cell.color = COL_SECONDARY

        # Place player
        self.player = random.choice(self.cells)
        self.player.color = COL_EXIT
        self.player_pos = self.player.x, self.player.y

        # Place exit
        self.exit = random.choice(self.cells)
        self.exit.color = COL_PLAYER

    def think(self):
        keys = pygame.key.get_pressed()

        # Calculate the new position based on the current position and the key pressed
        new_x, new_y = self.player.x, self.player.y

        if keys[pygame.K_LEFT] and self.player.x > 0:
            new_x -= MAZE_SIZE
        elif keys[pygame.K_RIGHT] and self.player.x < SCR_WIDTH - MAZE_SIZE:
            new_x += MAZE_SIZE
        elif keys[pygame.K_UP] and self.player.y > 0:
            new_y -= MAZE_SIZE
        elif keys[pygame.K_DOWN] and self.player.y < SCR_HEIGHT - MAZE_SIZE:
            new_y += MAZE_SIZE

        # Check if the new position is a wall
        for cell in self.cells:
            if cell.x == new_x and cell.y == new_y:
                if cell.color == COL_PRIMARY:  # Check if the cell is a wall
                    return  # Do not move if it's a wall

        # Check if player touches exit
        if self.exit.x == new_x and self.exit.y == new_y:
            pygame.quit()

        # Update player position if the new position is valid
        self.player.x, self.player.y = new_x, new_y
        self.player_pos = self.player.x, self.player.y

    def draw(self, screen):
        for idx, cell in enumerate(self.cells):
            cell.draw(screen, self.player_pos)
