import pygame
import sys
import grid
import button

width = 1400
height = 900

pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
fps = 30

square_size = 7
margin = 1
total_size = square_size + margin

rows = height//total_size
cols = int(width/1.1)//total_size


cyan = (0, 255, 255)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
magenta = (255, 0, 255)

grid = grid.Grid(rows, cols, margin, square_size, magenta, white)


start = button.Button(cyan, width/1.1, 90, 100, 50, 'start')
infinite_plane = button.Button(cyan, width/1.1, 130, 100, 50, 'infinite plane')

def main():

    run = False

    while True:

        clock.tick(fps)

        screen.fill((0, 0, 0))
        start.draw(screen)
        infinite_plane.draw(screen)

        if not run:
            grid.configuration(screen)
        else:
            grid.draw_grid(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            pos = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start.isOver(pos):
                    run = True
                grid.checkIfOver(pos)
                if infinite_plane.isOver(pos):
                    grid.infinite_plane = True


        pygame.display.update()

main()
