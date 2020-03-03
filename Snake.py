import pygame
from player_control import Control
from Level import level_

level = level_()
control = Control()


class snake_move:
    # Движение игрока
    def __init__(self):
        self.head = [45, 45]
        self.body = [[45, 45], [34, 45], [23, 45]]

    def move(self, control):
        if control.direction_controller == 'RIGHT':
            self.head[0] += 11
        elif control.direction_controller == 'LEFT':
            self.head[0] -= 11
        elif control.direction_controller == 'UP':
            self.head[1] -= 11
        elif control.direction_controller == 'DOWN':
            self.head[1] += 11

    def animation(self):
        self.body.insert(0, list(self.head))
        self.body.pop()

    # Отрисовка персонажа
    def draw_snake(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, pygame.Color('Green'), pygame.Rect(segment[0], segment[1], 10, 10))

    # Границы уровня
    def end_of_level(self):
        if self.head[0] == 419:
            self.head[0] = 23
        elif self.head[0] == 23:
            self.head[0] = 419
        elif self.head[1] == 34:
            self.head[1] = 419
        elif self.head[1] == 419:
            self.head[1] = 34

    # Сбор очков
    def eat(self, FOOD, level):
        if self.head == FOOD.food_transform1:
            level.score += 1
            self.body.append(FOOD.food_transform1)
            FOOD.create_food_position(level)

        if self.head == FOOD.food_transform2:
            level.score += 1
            self.body.append(FOOD.food_transform2)
            FOOD.create_food_position2(level)

    # Проверка на то что игрок куда то врезался(после этого игра рестартится)
    def cheack_wall(self, level):
        if level.level1 == True:
            if self.head in level.wall:
                self.head = [45, 45]
                while len(self.body) > 3:
                    self.body.pop()
                self.body = [[45, 45], [34, 45], [23, 45]]
                level.score = 0
        if level.level2 == True:
            if self.head in level.wall2:
                self.head = [45, 45]
                while len(self.body) > 3:
                    self.body.pop()
                self.body = [[45, 45], [34, 45], [23, 45]]
                level.score = 0
        if self.head in self.body[1:]:
            self.head = [45, 45]
            while len(self.body) > 3:
                self.body.pop()
            self.body = [[45, 45], [34, 45], [23, 45]]
            level.score = 0

        if level.newLVL == True:
            self.head = [45, 45]
            while len(self.body) > 3:
                self.body.pop()
            self.body = [[45, 45], [34, 45], [23, 45]]
            level.score = 0
            level.newLVL = False