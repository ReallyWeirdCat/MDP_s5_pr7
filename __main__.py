from config import SCR_WIDTH, SCR_HEIGHT
import pygame


pygame.init()
screen = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()


if __name__ == "__main__":
    main()
