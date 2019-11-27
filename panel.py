# Gluttonous Snake

import pygame
import random
# import sys
# from pygame.locals import *


class App:

    # constructor
    def __init__(self):
        pygame.init()
        self._running = True
        self.screen = None
        self.length = 3
        self.screen_color = (225, 225, 225)
        self.screen = pygame.display.set_mode((640, 400), 0, 32)
        self.screen.fill(self.screen_color)
        pygame.display.flip()

        self.clock = pygame.time.Clock()
        self.snake_direction = 'R'
        self.food = [{'x': 1, 'y': 1}]

        self.snake_size = 20  # the size of each snake block
        self.snake_color = (225, 80, 0)
        startx = self.screen.get_width()//2
        starty = self.screen.get_height()//2
        self.snake_position = [{'x': startx, 'y': starty},
                               {'x': startx-self.snake_size, 'y': starty},
                               {'x': startx-self.snake_size*2, 'y': starty}]

    def main(self):
        '''main program. It will call every other program, just like a control panel'''
        pygame.init()

        pygame.display.set_caption('Gluttonous Snake')
        self.draw_food()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameover()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and not self.snake_direction == 'D':
                        self.snake_direction = 'U'
                    elif event.key == pygame.K_DOWN and not self.snake_direction == 'U':
                        self.snake_direction = 'D'
                    elif event.key == pygame.K_LEFT and not self.snake_direction == 'R':
                        self.snake_direction = 'L'
                    elif event.key == pygame.K_RIGHT and not self.snake_direction == 'L':
                        self.snake_direction = 'R'
                    elif event.key == pygame.K_ESCAPE:
                        self.gameover()

            self.default_move()
            self.eat_food()
            self.snake_is_alive()
            self.draw_snake()
            self.clock.tick(10)
            pygame.display.update()

    def draw_snake(self):
        '''draw the snake, initial length is 3'''
        for one_block in self.snake_position:
            x = one_block['x']
            y = one_block['y']
            block = pygame.Rect(x, y, self.snake_size, self.snake_size)
            pygame.draw.rect(self.screen, self.snake_color, block)

    def snake_is_alive(self):
        '''determine whether the game is over'''
        if self.snake_position[0]['x'] + self.snake_size >= self.screen.get_width()+1 or \
                self.snake_position[0]['x'] <= -1 or \
                self.snake_position[0]['y'] >= self.screen.get_height() or \
                self.snake_position[0]['y'] + self.snake_size <= 0 or \
                self.snake_position[0] in self.snake_position[2:]:
            self.gameover()

    def default_move(self):
        '''get direction, and draw head and erase tail'''
        if self.snake_direction == 'R':
            new_head = {'x': self.snake_position[0]['x']+self.snake_size,
                        'y': self.snake_position[0]['y']}
        if self.snake_direction == 'L':
            new_head = {'x': self.snake_position[0]['x']-self.snake_size,
                        'y': self.snake_position[0]['y']}
        if self.snake_direction == 'U':
            new_head = {'x': self.snake_position[0]['x'],
                        'y': self.snake_position[0]['y']-self.snake_size}
        if self.snake_direction == 'D':
            new_head = {'x': self.snake_position[0]['x'],
                        'y': self.snake_position[0]['y']+self.snake_size}
        self.snake_position.insert(0, new_head)  # insert new_head at index 0
        block = pygame.Rect(
            self.snake_position[-1]['x'], self.snake_position[-1]['y'], self.snake_size, self.snake_size)
        pygame.draw.rect(self.screen, self.screen_color, block)
        self.snake_position = self.snake_position[:-1]

    def draw_food(self):
        '''draw the food'''
        food_x = random.randrange(
            self.snake_size, self.screen.get_width() - self.snake_size, self.snake_size)
        food_y = random.randrange(
            self.snake_size, self.screen.get_height() - self.snake_size, self.snake_size)
        self.food = [{'x': food_x, 'y': food_y}]
        x = self.food[0]['x']
        y = self.food[0]['y']
        apple_Rect = pygame.Rect(x, y, self.snake_size, self.snake_size)
        pygame.draw.rect(self.screen, (80, 200, 100), apple_Rect)

    def eat_food(self):
        if self.food[0] in self.snake_position:
            if self.snake_direction == 'R':
                new_head = {'x': self.snake_position[0]['x']+self.snake_size,
                            'y': self.snake_position[0]['y']}
            if self.snake_direction == 'L':
                new_head = {'x': self.snake_position[0]['x']-self.snake_size,
                            'y': self.snake_position[0]['y']}
            if self.snake_direction == 'U':
                new_head = {'x': self.snake_position[0]['x'],
                            'y': self.snake_position[0]['y']-self.snake_size}
            if self.snake_direction == 'D':
                new_head = {'x': self.snake_position[0]['x'],
                            'y': self.snake_position[0]['y']+self.snake_size}
            # insert new_head at index 0
            self.snake_position.insert(0, new_head)
            self.draw_food()

    def gameover(self):
        print('gameover')
        pygame.quit()


if __name__ == "__main__":
    theApp = App()
    theApp.main()
