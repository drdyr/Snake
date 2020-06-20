import pygame
import sys
import random


class Segment:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(25 * self.x, 25 * self.y, 25, 25)

    def draw(self):
        self.rect = pygame.Rect(25 * self.x, 25 * self.y, 25, 25)
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 0)


class Snake:
    def __init__(self, head):
        self.segments = [head]
        self.head = head
        self.tail = head

    def add_segment(self):
        new_segment = Segment(self.tail.x, self.tail.y)
        self.segments.append(new_segment)
        self.tail = new_segment

    def move(self, direction):
        global current_food

        if self.head.x == current_food.x and self.head.y == current_food.y:
            self.add_segment()
            current_food = create_food()

        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].x = self.segments[i - 1].x
            self.segments[i].y = self.segments[i - 1].y

        if direction == "up":
            if self.head.y == 0:
                self.head.y = 14
            else:
                self.head.y -= 1
        elif direction == "down":
            if self.head.y == 14:
                self.head.y = 0
            else:
                self.head.y += 1
        elif direction == "left":
            if self.head.x == 0:
                self.head.x = 14
            else:
                self.head.x -= 1
        elif direction == "right":
            if self.head.x == 14:
                self.head.x = 0
            else:
                self.head.x += 1

    def is_collision(self):
        segment_coordinates = []
        for segment in snake.segments[1:]:
            segment_coordinate = [segment.x, segment.y]
            segment_coordinates.append(segment_coordinate)

        return [self.head.x, self.head.y] in segment_coordinates

    def draw(self):
        for segment in self.segments:
            segment.draw()


class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(25 * self.x, 25 * self.y, 25, 25)

    def draw(self):
        self.rect = pygame.Rect(25 * self.x, 25 * self.y, 25, 25)
        pygame.draw.rect(screen, (0, 255, 0), self.rect, 0)


pygame.init()
clock = pygame.time.Clock()
grid_width = 15
grid_height = 15
screen_width, screen_height = 25 * grid_width, 25 * grid_height
screen = pygame.display.set_mode((screen_width, screen_height))

head = Segment(7, 7)
snake = Snake(head)


def create_food():

    segment_coordinates = []
    for segment in snake.segments:
        segment_coordinate = [segment.x, segment.y]
        segment_coordinates.append(segment_coordinate)

    food_coordinate = [15, 15]
    while food_coordinate in segment_coordinates or food_coordinate == [15, 15]:
        food_coordinate = [random.randint(0, 14), random.randint(0, 14)]
    return Food(food_coordinate[0], food_coordinate[1])


current_food = create_food()


direction = "up"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and direction != "down":
                direction = "up"
            if event.key == pygame.K_s and direction != "up":
                direction = "down"
            if event.key == pygame.K_a and direction != "right":
                direction = "left"
            if event.key == pygame.K_d and direction != "left":
                direction = "right"

    screen.fill((0, 0, 0))
    current_food.draw()
    snake.draw()
    if snake.is_collision():
        pygame.quit()
        sys.exit()

    snake.move(direction)

    pygame.display.flip()

    clock.tick(8)