import pygame
from pygame.locals import *

MOVE_DOWN = 'down'
MOVE_UP = 'up'
MOVE_RIGHT = 'right'
MOVE_LEFT = 'left'
SNAKE_SIZE_WIDTH = 20
SNAKE_SIZE_HEIGHT = 20

class Snake:
    x = 0
    y = 0
    last_action = MOVE_DOWN
    screen = None

    def __init__(self, screen):
        self.screen = screen

    def move_up(self):
        self.y -= SNAKE_SIZE_HEIGHT
        self.last_action = MOVE_UP

    def move_down(self):
        self.y += SNAKE_SIZE_HEIGHT
        self.last_action = MOVE_DOWN

    def move_right(self):
        self.x += SNAKE_SIZE_WIDTH
        self.last_action = MOVE_RIGHT

    def move_left(self):
        self.x -= SNAKE_SIZE_WIDTH
        self.last_action = MOVE_LEFT

    def set_last_action(self, move):
        self.last_action = move

    def move(self):
        if self.last_action == MOVE_UP:
            self.move_up()
        if self.last_action == MOVE_DOWN:
            self.move_down()
        if self.last_action == MOVE_RIGHT:
            self.move_right()
        if self.last_action == MOVE_LEFT:
            self.move_left()

    def draw(self):
        pygame.draw.rect(self.screen, (0, 0, 0), (self.x, self.y, SNAKE_SIZE_WIDTH, SNAKE_SIZE_HEIGHT))


pygame.display.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Snake")
screen = pygame.display.set_mode([800, 600])

snake = Snake(screen)

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                snake.set_last_action(MOVE_DOWN)
            if event.key == pygame.K_w:
                snake.set_last_action(MOVE_UP)
            if event.key == pygame.K_a:
                snake.set_last_action(MOVE_LEFT)
            if event.key == pygame.K_d:
                snake.set_last_action(MOVE_RIGHT)

    screen.fill([255, 255, 255])

    snake.move()
    snake.draw()

    pygame.display.flip()
    pygame.display.update()
    clock.tick(5)


