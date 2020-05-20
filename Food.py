import pygame
import random

"""This is the food class which has two functions: draw and check for collision with snake"""


class Food(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.width = 15
        self.height = 15
        self.color = (0, 0, 255)
        self.radius = 5
        self.x = random.randint(3, 480)
        self.y = random.randint(3, 380)

    # draw the food circle onto the screen
    def draw_food(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    # check if food circle collides with head of snake
    def check_collision(self, snake):
        if snake.body[0][1] <= self.y <= (snake.body[0][1] + snake.height):
            if self.x <= snake.body[0][0] < (self.x + self.radius) or snake.body[0][0] <= self.x < (
                    snake.body[0][0] + snake.width):
                return True
