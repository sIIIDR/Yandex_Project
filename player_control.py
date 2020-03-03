import pygame
from pygame.locals import *


class Control:
    def __init__(self):
        self.game_Play = True
        self.direction_controller = 'RIGHT'
        self.game_start = False
        self.pause = True
        self.game_start_counter = True

    #Простой контролер персонажа, в зависимости от нажатой кнопки двигается
    def snake_control(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.game_Play = False

            elif event.type == KEYDOWN:
                if event.key == K_RIGHT and self.direction_controller != 'LEFT':
                    self.direction_controller = 'RIGHT'
                elif event.key == K_LEFT and self.direction_controller != 'RIGHT':
                    self.direction_controller = 'LEFT'
                elif event.key == K_UP and self.direction_controller != 'DOWN':
                    self.direction_controller = 'UP'
                elif event.key == K_DOWN and self.direction_controller != 'UP':
                    self.direction_controller = 'DOWN'
                elif event.key == K_ESCAPE:
                    self.game_Play = False
                elif event.key == K_SPACE:
                    if self.pause == True:
                        self.pause = False
                        self.game_start_counter = False
                    else:
                        self.pause = True
