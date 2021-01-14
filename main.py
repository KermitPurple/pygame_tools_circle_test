import pygame, math
from pygame.locals import *
from pygame_tools import *

class Block:

    def __init__(self, center: Point, radius: int):
        self.center = Point._make(center)
        self.radius = radius
        self.angle = 0
        self.surface = pygame.Surface((50, 50), flags = SRCALPHA)
        self.surface.fill('grey')

    def update(self):
        self.angle += 0.03

    def draw(self, screen: pygame.Surface):
        transformed = pygame.transform.rotate(self.surface, -self.angle / math.pi * 180)
        transformed_size = transformed.get_size()
        pos = self.radius * math.cos(self.angle) + self.center.x - transformed_size[0] / 2, self.radius * math.sin(self.angle) + self.center.y - transformed_size[1] / 2
        screen.blit(transformed, pos)

class CircleTest(GameScreen):

    def __init__(self):
        pygame.init()
        size = Point(600, 600)
        super().__init__(pygame.display.set_mode(size), size, (size.x // 2, size.y // 2))
        radius = 125
        center = self.window_size.x // 2, self.window_size.y // 2
        self.block = Block(center, radius)
        self.static_circle = Circle(center, radius, 'white', 10)
        self.changing_circle = Circle(center, radius, 'green', 1)
        self.run()

    def update(self):
        self.screen.fill('black')
        self.block.update()
        self.block.draw(self.screen)
        self.static_circle.draw(self.screen)
        mouse = self.get_scaled_mouse_pos()
        pos = int(Point.distance(self.changing_circle.center, mouse))
        self.changing_circle.radius = pos
        self.changing_circle.draw(self.screen)
        if self.static_circle.collide_point(mouse, True):
            print('border')
        elif self.static_circle.collide_point(mouse):
            print('all')
        else:
            print('none')

    def mouse_button_down(self, event: pygame.event.Event):
        if event.button == 1:
            self.changing_circle.center = self.get_scaled_mouse_pos()


if __name__ == '__main__':
    CircleTest()
