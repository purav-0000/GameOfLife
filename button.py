import pygame


class Button:

    def __init__(self, colour, x, y, length, breadth, text=' '):
        self.colour = colour
        self.x = x
        self.y = y
        self.length = length
        self.breadth = breadth
        self.text = text

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.length, self.breadth), 0)

        if self.text != ' ':
            font = pygame.font.SysFont('arial', 20)
            text = font.render(self.text, True, (0, 0, 0))
            screen.blit(text, (self.x + (self.length/2 - text.get_width()/2), self.y + (self.breadth/2 - text.get_height()/2)))

    def isOver(self, pos):
        if self.x < pos[0] < self.x + self.length:
            if self.y < pos[1] < self.y + self.breadth:
                return True

        return False

