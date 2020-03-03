import pygame
from player_control import Control
from Snake import snake_move
from Level import level_
from FOOD import Food

pygame.init()
screen = pygame.display.set_mode((441, 441))
screen1 = pygame.display.set_mode((441, 441))
control = Control()
snake = snake_move()
level = level_()
level.create_LVL()

food = Food()
level.init_field2()
level.init_field()
food.create_food_position2(level)
food.create_food_position(level)
speed = 0
score = 0
f1_small = pygame.font.Font(None, 18)
f2_medium = pygame.font.Font(None, 36)
f3_big = pygame.font.Font(None, 65)

while control.game_Play == True:

    score_counter = f2_medium.render('Score:%s' % (level.score), 3, (255, 255, 0))
    game_name = f3_big.render('Змейка', 1, (255, 255, 0))

    game_contol = f1_small.render('Управление: Стрелочки + "Space" для паузы', 1, (255, 255, 0))
    help_txt = f1_small.render('Игра состоит из двух уровней, ', 1,
                               (255, 255, 0))
    help_txt2 = f1_small.render('надо набрать 10 очков чтобы перейти на второй,', 1,
                                (255, 255, 0))
    help_txt3 = f1_small.render('после чего очки обнулятся,', 1,
                                (255, 255, 0))
    help_txt4 = f1_small.render('на втором уровне надо собрать 20 очков, ', 1,
                                (255, 255, 0))
    help_txt5 = f1_small.render(' после чего игра считается пройденной!', 1,
                                (255, 255, 0))
    start_text = f2_medium.render('Что бы начать нажмите "SPACE"', 1, (255, 255, 0))

    win_txt = f3_big.render('Вы победили!', 1, (255, 255, 0))
    win_help = f1_small.render('Нажмите "Esc" что бы выйти', 1, (255, 255, 0))

    pygame.display.update()
    control.snake_control()
    screen.fill(pygame.Color("Black"))
    level.draw_ground(screen)
    snake.draw_snake(screen)
    snake.end_of_level()

    screen.blit(score_counter, (300, 10))

    if level.score < 10 and level.level1 is True:
        level.draw_LVL1(screen)
        food.create_food(screen)
        pygame.display.update()

    elif level.score == 10:
        level.level1 = False
        level.level2 = True
        level.newLVL = True
        level.score = 0

    elif level.level1 is False:
        level.draw_LVL2(screen)
        food.create_food2(screen)
        pygame.display.update()
    if level.score == 20 and level.level1 is False:
        pygame.draw.rect(screen, pygame.Color('Grey'), pygame.Rect(0, 0, 441, 441))
        screen.blit(win_txt, (100, 30))
        screen.blit(win_help, (140, 170))
        pygame.display.update()

    if control.pause is True and control.game_start_counter is True:
        pygame.draw.rect(screen, pygame.Color('Grey'), pygame.Rect(0, 0, 441, 441))
        screen.blit(game_name, (130, 30))
        screen.blit(game_contol, (80, 100))
        screen.blit(help_txt, (80, 130))
        screen.blit(help_txt2, (80, 150))
        screen.blit(help_txt3, (80, 170))
        screen.blit(help_txt4, (80, 190))
        screen.blit(help_txt5, (80, 210))
        screen.blit(start_text, (30, 300))
        pygame.display.update()
    if speed % 1000 == 0 and control.pause is False:
        snake.move(control)
        snake.cheack_wall(level)
        snake.eat(food, level)
        snake.end_of_level()
        snake.animation()
    speed += 50
    pygame.display.flip()
