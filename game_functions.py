import pygame
import sys


# Check the food list to see if it's empty and fill it is
def check_foods_list(foods, Food, display_surface):
    if len(foods) < 1:
        new_food = Food(display_surface)
        foods.append(new_food)


# Check userinput
def check_events(snake):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake.direction != 'right':
                snake.direction = 'left'
            elif event.key == pygame.K_RIGHT and snake.direction != 'left':
                snake.direction = 'right'
            elif event.key == pygame.K_UP and snake.direction != 'down':
                snake.direction = 'up'
            elif event.key == pygame.K_DOWN and snake.direction != 'up':
                snake.direction = 'down'


# check if food and snake (x,y) are close, if so, increase size
def check_collide(foods, snake):
    if foods[0].check_collision(snake):
        snake.add_body()
        foods.pop()
