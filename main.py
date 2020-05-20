import pygame
from Snake import Snake
from Food import Food
import game_functions as gf

pygame.init()
display_width = 500
display_height = 400
display_surface = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Snake Game")
display_surface_color = (0, 0, 0)
clock = pygame.time.Clock()

# Objects
snake = Snake(display_surface)
foods = [Food(display_surface)]

while True:
    clock.tick(30)
    # draw surface
    display_surface.fill(display_surface_color)
    # check events
    gf.check_events(snake)
    gf.check_collide(foods, snake)
    gf.check_foods_list(foods, Food, display_surface)
    # Food Updates
    food = foods[0]
    food.draw_food()
    # snake updates
    snake.move_snake(display_height, display_width)
    snake.check_game_over()

    pygame.display.update()
