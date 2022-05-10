#!/usr/bin/env python3

from keyboard import add_hotkey
from time import sleep
from os import system
from random import randint

def pressed_key(key):
    global snake_direction
    if not (snake_direction_old == "right" and key == "left"
    or snake_direction_old == "left" and key == "right"
    or snake_direction_old == "up" and key == "down"
    or snake_direction_old == "down" and key == "up"):
        snake_direction = key

add_hotkey("right", pressed_key, args=['right'])
add_hotkey("left", pressed_key, args=['left'])
add_hotkey("up", pressed_key, args=['up'])
add_hotkey("down", pressed_key, args=['down'])

def put_meat(field):
    meat_a = randint(1,field_width)
    meat_b = randint(1,field_height)
    if field[meat_a][meat_b] == symbol_free:
        meat = [meat_a, meat_b]
    else:
        meat = put_meat(field)
    return meat

def get_next_top(snake_direction, snake_top):
    if snake_direction == "right":
        next_top = [snake_top[0]+1,snake_top[1]+0]
    elif snake_direction == "left":
        next_top = [snake_top[0]-1,snake_top[1]+0]
    elif snake_direction == "up":
        next_top = [snake_top[0]+0,snake_top[1]-1]
    elif snake_direction == "down":
        next_top = [snake_top[0]+0,snake_top[1]+1]
    return next_top

def check_play_on(next_top):
    in_next_top = field[next_top[1]][next_top[0]]
    if snake_len >= 30:
        play_on = "Win    "
    elif in_next_top == symbol_fence:
        play_on = "Fail   "
    elif in_next_top == symbol_body:
        remove_tail = snake[0]
        if next_top != remove_tail:
            play_on = "Fail   "
        else:
            play_on = "Process"
    else:
        play_on = "Process"
    return play_on


def print_field():
    global field
    field = []
    for line_number in range(field_height + 2):
        if line_number == 0 or line_number == field_height + 1 :
            line = symbol_fence * (field_width + 2)
        else:
            line = symbol_fence + field_width*symbol_free + symbol_fence
        field.append(list(line))
    for snake_path in snake:
        snake_path_x, snake_path_y = snake_path
        field[snake_path_y][snake_path_x] = symbol_body
    snake_top_x, snake_top_y = snake_path
    field[snake_top_y][snake_top_x] = symbol_top

    if meat != 0:
        meat_x, meat_y = meat
        field[meat_y][meat_x] = symbol_meat


    system('cls||clear')
    for i in field:
        for ii in i:
            print(ii, end='')
        print()
    print(play_on, "   ", f'{snake_len:02}', sep="")

# SETTINGS
symbol_free = " "
symbol_fence = "#"
symbol_body = "0"
symbol_top = "@"
symbol_meat = "*"

field_width = 10
field_height = 10

speed = 0.5

# INIT
play_on = "Process"
snake = [[2,2],[3,2],[4,2]]
snake_top = [4,2]
snake_len = 2
snake_direction = "right"
snake_direction_old = "right"
meat = 0
field = []

print_field()
meat = put_meat(field)

# GAME
print_field()
while play_on == "Process":
    sleep(speed)
    next_top = get_next_top(snake_direction, snake_top)
    snake_direction_old = snake_direction
    play_on = check_play_on(next_top)
    in_next_top = field[next_top[1]][next_top[0]]

    if play_on == "Process" and in_next_top == symbol_free or in_next_top == symbol_body:
        snake.append(next_top)
        remove_tail = snake.pop(0)
        snake_top = [next_top[0]+0,next_top[1]+0]
    elif play_on == "Process" and in_next_top == symbol_meat:
        snake.append(next_top)
        meat = put_meat(field)
        snake_top = [next_top[0]+0,next_top[1]+0]
        snake_len += 1
    print_field()

input("Press to close window")
