import pygame

"""The snake class which has many functions"""


class Snake(pygame.sprite.Sprite):
    body = [(10, 20)]

    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.dirnx = 0
        self.dirny = 1
        self.width = 15
        self.height = 15
        self.head_color = (0, 255, 0)
        self.direction = 'none'
        self.speed = 4

    # draw the entire body of the snake by looping through the body list
    def draw_snake(self):
        for i, j in self.body:
            pygame.draw.rect(self.screen, self.head_color, (i, j, self.width, self.height))

    # Move the snake in the direction pressed by making a new head postion
    # and putting it in the front and take out the last part in the boody list
    def move_snake(self, display_height, display_width):
        if self.direction == 'none':
            self.draw_snake()
        elif self.direction == 'down' and self.body[0][1] < display_height - self.height:
            new_x = self.body[0][0]
            new_y = self.body[0][1] + self.speed
            new_head = (new_x, new_y)
            self.body.insert(0, new_head)
            self.remove_tail()
            self.draw_snake()
        elif self.direction == 'up' and self.body[0][1] > 0:
            new_x = self.body[0][0]
            new_y = self.body[0][1] - self.speed
            new_head = (new_x, new_y)
            self.body.insert(0, new_head)
            self.remove_tail()
            self.draw_snake()
        elif self.direction == 'right' and self.body[0][0] < display_width - self.width:
            new_x = self.body[0][0] + self.speed
            new_y = self.body[0][1]
            new_head = (new_x, new_y)
            self.body.insert(0, new_head)
            self.remove_tail()
            self.draw_snake()
        elif self.direction == 'left' and self.body[0][0] > 0:
            new_x = self.body[0][0] - self.speed
            new_y = self.body[0][1]
            new_head = (new_x, new_y)
            self.body.insert(0, new_head)
            self.remove_tail()
            self.draw_snake()

    # Remove the last item in the body list
    def remove_tail(self):
        self.body.pop()

    # add a body part to the snake
    def add_body(self):
        if self.direction == 'up':
            new_x = self.body[len(self.body) - 1][0]
            new_y = self.body[len(self.body) - 1][1] + self.height
            new_body_part = (new_x, new_y)
            self.body.append(new_body_part)
        if self.direction == 'down':
            new_x = self.body[len(self.body) - 1][0]
            new_y = self.body[len(self.body) - 1][1] - self.height
            new_body_part = (new_x, new_y)
            self.body.append(new_body_part)
        if self.direction == 'left':
            new_x = self.body[len(self.body) - 1][0] + self.width
            new_y = self.body[len(self.body) - 1][1]
            new_body_part = (new_x, new_y)
            self.body.append(new_body_part)
        if self.direction == 'right':
            new_x = self.body[len(self.body) - 1][0] - self.width
            new_y = self.body[len(self.body) - 1][1]
            new_body_part = (new_x, new_y)
            self.body.append(new_body_part)

    def reset(self):
        self.body = [(10, 20)]
        self.direction = 'none'

    # check for collision with itself by making a dict and seeing if any of the (x,y) repeat
    def check_collision(self):
        body_dict = {}
        for i in self.body:
            body_dict[i] = body_dict.get(i, 0) + 1
        for key in body_dict:
            if body_dict[key] > 1:
                return True
            else:
                return False

    # check if snake head hits any borders
    def check_borders(self):
        if self.body[0][0] == 586 or self.body[0][0] == -2:
            return True
        elif self.body[0][1] == 0 or self.body[0][1] == 488:
            return True
        else:
            return False

    # a helper function to perform reset
    def check_game_over(self):
        if self.check_collision():
            self.reset()
        elif self.check_borders():
            self.reset()
