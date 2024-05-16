import random
import numpy
import pygame
import cell

class Grid:

    def __init__(self, rows, cols, margin, size, alive, dead):
        self.rows = rows
        self.cols = cols
        self.margin = margin
        self.grid = numpy.ndarray(shape=(self.rows, self.cols))
        self.size = size
        self.total_size = size + margin
        self.alive = alive
        self.dead = dead
        self.grid_boxes = list()
        self.alive_cells = list(tuple())
        self.infinite_plane = False
        self.larger_grid = numpy.ndarray(shape=(self.rows+3, self.cols+3))

    def make2D_array(self):

        for i in range(self.rows):
            for j in range(self.cols):
                self.grid[i][j] = random.randint(0, 1)

    def game_of_life(self):

        next_grid = numpy.ndarray(shape=(self.rows, self.cols))

        for i in range(self.rows):
            for j in range(self.cols):
                if self.countNeighbours(i, j) == 3 and self.grid[i][j] == 0:
                    next_grid[i][j] = 1
                elif (self.countNeighbours(i, j) > 3 or self.countNeighbours(i, j) < 2) and self.grid[i][j] == 1:
                    next_grid[i][j] = 0
                else:
                    next_grid[i][j] = self.grid[i][j]

        return next_grid

    def draw_grid(self, screen):

        self.grid = self.game_of_life()

        for i in range(self.rows):
            for j in range(self.cols):

                if self.grid[i][j] == 1:
                    pygame.draw.rect(screen, self.alive, (j * self.total_size, i * self.total_size, self.size, self.size))

                else:
                    pygame.draw.rect(screen, self.dead, (j * self.total_size, i * self.total_size, self.size, self.size))

    def countNeighbours(self, i, j):

        total = 0
        x = 0
        y = 0
        if not self.infinite_plane:
            for p in range(i - 1, i + 2):
                for q in range(j - 1, j + 2):
                    y = p
                    x = q
                    if p < 0:
                        y = self.rows + p
                    if q < 0:
                        x = self.cols + q
                    if p >= self.rows:
                        y = p - self.rows
                    if q >= self.cols:
                        x = q - self.cols
                    if self.grid[y][x] == 1 and (i, j) != (y, x):
                        total = total + 1
        else:
            for p in range(i - 1, i + 2):
                for q in range(j - 1, j + 2):
                    if p < 0:
                        continue
                    if q < 0:
                        continue
                    if p >= self.rows:
                        continue
                    if q >= self.cols:
                        continue
                    if self.grid[p][q] == 1 and (i, j) != (p, q):
                        total = total + 1
        return total



    def configuration(self, screen):
        self.makeAGospelGun(10, 56, False)
        self.makeAGospelGun(10, 18, False,)
        self.makeA90GospelGun(30, 140, True)
        for i in range(self.rows):
            for j in range(self.cols):
                box = cell.Cell(self.size, j * self.total_size, i * self.total_size, j, i)
                if self.grid[i][j] == 1:
                    self.alive_cells.append((i, j))
                if (i, j) in self.alive_cells:
                    box.draw(self.alive, screen)
                    self.grid[i][j] = 1
                else:
                    box.draw(self.dead, screen)
                    self.grid[i][j] = 0
                self.grid_boxes.append(box)

    def checkIfOver(self, pos):

        for i in range(len(self.grid_boxes)):
            if self.grid_boxes[i].x <= pos[0] <= self.grid_boxes[i].x + self.size and self.grid_boxes[i].y <= pos[1] <= self.grid_boxes[i].y + self.size:
                self.alive_cells.append((self.grid_boxes[i].row, self.grid_boxes[i].col))
                break

    def makeAGospelGun(self, y, x, invert):

        def adjustY(b, i):
            return (b + i) % self.rows

        if not invert:
            def adjustX(a, i):
                return (a + i) % self.cols
        else:
            def adjustX(a, i):
                return (a - i) % self.cols

        self.grid[adjustY(y, 0)][adjustX(x, 0)] = 1
        self.grid[adjustY(y, 0)][adjustX(x, -1)] = 1
        self.grid[adjustY(y, +1)][adjustX(x, -1)] = 1
        self.grid[adjustY(y, -1)][adjustX(x, -1)] = 1
        self.grid[adjustY(y, 0)][adjustX(x, -3)] = 1
        self.grid[adjustY(y, 0)][adjustX(x, -7)] = 1
        self.grid[adjustY(y, 0)][adjustX(x, -16)] = 1
        self.grid[adjustY(y, 0)][adjustX(x, -17)] = 1
        self.grid[adjustY(y, -1)][adjustX(x, -16)] = 1
        self.grid[adjustY(y, -1)][adjustX(x, -17)] = 1
        self.grid[adjustY(y, -2)][adjustX(x, +17)] = 1
        self.grid[adjustY(y, -2)][adjustX(x, +18)] = 1
        self.grid[adjustY(y, -3)][adjustX(x, +17)] = 1
        self.grid[adjustY(y, -3)][adjustX(x, +18)] = 1
        self.grid[adjustY(y, +2)][adjustX(x, -2)] = 1
        self.grid[adjustY(y, -2)][adjustX(x, -2)] = 1
        self.grid[adjustY(y, -1)][adjustX(x, -7)] = 1
        self.grid[adjustY(y, +1)][adjustX(x, -7)] = 1
        self.grid[adjustY(y, +2)][adjustX(x, -6)] = 1
        self.grid[adjustY(y, -2)][adjustX(x, -6)] = 1
        self.grid[adjustY(y, +3)][adjustX(x, -5)] = 1
        self.grid[adjustY(y, +3)][adjustX(x, -4)] = 1
        self.grid[adjustY(y, -3)][adjustX(x, -5)] = 1
        self.grid[adjustY(y, -3)][adjustX(x, -4)] = 1
        self.grid[adjustY(y, 0)][adjustX(x, +5)] = 1
        self.grid[adjustY(y, 0)][adjustX(x, +7)] = 1
        self.grid[adjustY(y, +1)][adjustX(x, +7)] = 1
        self.grid[adjustY(y, -4)][adjustX(x, +7)] = 1
        self.grid[adjustY(y, -5)][adjustX(x, +7)] = 1
        self.grid[adjustY(y, -4)][adjustX(x, +5)] = 1
        self.grid[adjustY(y, -1)][adjustX(x, +3)] = 1
        self.grid[adjustY(y, -2)][adjustX(x, +3)] = 1
        self.grid[adjustY(y, -3)][adjustX(x, +3)] = 1
        self.grid[adjustY(y, -1)][adjustX(x, +4)] = 1
        self.grid[adjustY(y, -2)][adjustX(x, +4)] = 1
        self.grid[adjustY(y, -3)][adjustX(x, +4)] = 1

    def makeA90GospelGun(self, y, x, invert):

        def adjustY(b, i):
            return (b + i) % self.rows

        if not invert:
            def adjustX(a, i):
                return (a + i) % self.cols
        else:
            def adjustX(a, i):
                return (a - i) % self.cols

        self.grid[adjustY(y, 0)][adjustX(x, 0)] = 1
        self.grid[adjustY(y, -1)][adjustX(x, 0)] = 1
        self.grid[adjustY(y, -1)][adjustX(x, +1)] = 1
        self.grid[adjustY(y, -1)][adjustX(x, -1)] = 1
        self.grid[adjustY(y, -3)][adjustX(x, 0)] = 1
        self.grid[adjustY(y, -7)][adjustX(x, 0)] = 1
        self.grid[adjustY(y, -16)][adjustX(x, 0)] = 1
        self.grid[adjustY(y, -17)][adjustX(x, 0)] = 1
        self.grid[adjustY(y, -16)][adjustX(x, -1)] = 1
        self.grid[adjustY(y, -17)][adjustX(x, -1)] = 1
        self.grid[adjustY(y, 17)][adjustX(x, -2)] = 1
        self.grid[adjustY(y, 18)][adjustX(x, -2)] = 1
        self.grid[adjustY(y, 17)][adjustX(x, -3)] = 1
        self.grid[adjustY(y, 18)][adjustX(x, -3)] = 1
        self.grid[adjustY(y, -2)][adjustX(x, +2)] = 1
        self.grid[adjustY(y, -2)][adjustX(x, -2)] = 1
        self.grid[adjustY(y, -7)][adjustX(x, -1)] = 1
        self.grid[adjustY(y, -7)][adjustX(x, +1)] = 1
        self.grid[adjustY(y, -6)][adjustX(x, 2)] = 1
        self.grid[adjustY(y, -6)][adjustX(x, -2)] = 1
        self.grid[adjustY(y, -5)][adjustX(x, +3)] = 1
        self.grid[adjustY(y, -4)][adjustX(x, 3)] = 1
        self.grid[adjustY(y, -5)][adjustX(x, -3)] = 1
        self.grid[adjustY(y, -4)][adjustX(x, -3)] = 1
        self.grid[adjustY(y, 5)][adjustX(x, 0)] = 1
        self.grid[adjustY(y, 7)][adjustX(x, 0)] = 1
        self.grid[adjustY(y, +7)][adjustX(x, +1)] = 1
        self.grid[adjustY(y, 7)][adjustX(x, -4)] = 1
        self.grid[adjustY(y, 7)][adjustX(x, -5)] = 1
        self.grid[adjustY(y, +5)][adjustX(x, -4)] = 1
        self.grid[adjustY(y, 3)][adjustX(x, -1)] = 1
        self.grid[adjustY(y, +3)][adjustX(x, -2)] = 1
        self.grid[adjustY(y, +3)][adjustX(x, -3)] = 1
        self.grid[adjustY(y, +4)][adjustX(x, -1)] = 1
        self.grid[adjustY(y, +4)][adjustX(x, -2)] = 1
        self.grid[adjustY(y, +4)][adjustX(x, -3)] = 1


