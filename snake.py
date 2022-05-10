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
    a = randint(1,10)
    b = randint(1,10)
    if field[a][b] == " ":
        field[a][b] = "*"
    else:
        put_meat(field)

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


def print_field(field, play_on, snake_len):
    system('cls||clear')
    for i in field:
        for ii in i:
            print(ii, end='')
        print()
    print(play_on, "   ", f'{snake_len:02}', sep="")

# SETTINGS
symbol_free = " "
symbol_fence = "#"
symbol_body = "%"
symbol_top = "@"
symbol_meat = "*"

field_width = 10
field_height= 10

# INIT
field = [list("############"),
         list("#          #"),
         list("# %%@      #"),
         list("#          #"),
         list("#          #"),
         list("#          #"),
         list("#          #"),
         list("#          #"),
         list("#          #"),
         list("#          #"),
         list("#          #"),
         list("############")]
put_meat(field)
play_on = "Process"
snake_top = [4,2]
snake = [[2,2],[3,2],[4,2]]
snake_len = 2
snake_direction = "right"
snake_direction_old = "right"

# GAME
print_field(field, play_on, snake_len)
while play_on == "Process":
    sleep(0.5)
    next_top = get_next_top(snake_direction, snake_top)
    snake_direction_old = snake_direction
    play_on = check_play_on(next_top)
    in_next_top = field[next_top[1]][next_top[0]]
    
    if play_on == "Process" and in_next_top == symbol_free or in_next_top == symbol_body:
        snake.append(next_top)
        remove_tail = snake.pop(0)

        field[remove_tail[1]][remove_tail[0]] = symbol_free
        field[next_top[1]][next_top[0]] = symbol_top
        field[snake_top[1]][snake_top[0]] = symbol_body

        snake_top = [next_top[0]+0,next_top[1]+0]
    elif play_on == "Process" and in_next_top == symbol_meat:
        snake.append(next_top)

        field[next_top[1]][next_top[0]] = symbol_top
        field[snake_top[1]][snake_top[0]] = symbol_body

        put_meat(field)
        snake_top = [next_top[0]+0,next_top[1]+0]
        snake_len += 1
    print_field(field, play_on, snake_len)

input("Press to close window")
