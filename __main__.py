from config import SCR_WIDTH, SCR_HEIGHT, COL_BACKGROUND
from maze import Maze
import pygame
import time


pygame.init()
screen = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))


def main():

    maze = Maze()

    while True:

        screen.fill(COL_BACKGROUND)
        maze.think()
        maze.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()
        time.sleep(0.1)


if __name__ == "__main__":
    main()
