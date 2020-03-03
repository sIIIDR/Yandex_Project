import pygame
import random

class Food:
    def __init__(self):
        self.food_transform1 = []
        self.food_transform2 = []

    def create_food_position(self, level):
        self.food_transform1 = random.choice(level.field)

    def create_food_position2(self, level):
        self.food_transform2 = random.choice(level.field2)

    def create_food(self, screen):
        pygame.draw.rect(screen, pygame.Color("Blue"),
                         pygame.Rect(self.food_transform1[0], self.food_transform1[1], 10, 10))

    def create_food2(self, screen):
        pygame.draw.rect(screen, pygame.Color("Blue"),
                         pygame.Rect(self.food_transform2[0], self.food_transform2[1], 10, 10))
