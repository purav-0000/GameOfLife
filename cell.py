import pygame


class Cell:

    def __init__(self, size, x, y, col, row):
        self.size = size
        self.x = x
        self.y = y
        self.col = col
        self.row = row

    def draw(self, colour, screen):
        pygame.draw.rect(screen, colour, (self.x, self.y, self.size, self.size))

    def isOver(self, pos):
        if self.x < pos[0] < self.x + self.size:
            if self.y < pos[1] < self.y + self.size:
                return True

        return False
