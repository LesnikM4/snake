#!/usr/bin/env python3

from keyboard import add_hotkey
from time import sleep
from os import system
from random import randint

def put_meat():
    a = randint(1,10)
    b = randint(1,10)
    if field[a][b] == ".":
        field[a][b] = "*"
    else:
        put_meat()

def pressed_key(key):
    global snake_direction
    global snake_direction_old
    if not (snake_direction_old == "right" and key == "left" 
    or snake_direction_old == "left" and key == "right"
    or snake_direction_old == "up" and key == "down"
    or snake_direction_old == "down" and key == "up"):
        snake_direction = key

add_hotkey("right", pressed_key, args=['right'])
add_hotkey("left", pressed_key, args=['left'])
add_hotkey("up", pressed_key, args=['up'])
add_hotkey("down", pressed_key, args=['down'])
add_hotkey("space", pressed_key, args=['down'])

play_on = "Process"

field = [list("############"),
         list("#..........#"),
         list("#.%%@......#"),
         list("#..........#"),
         list("#..........#"),
         list("#..........#"),
         list("#..........#"),
         list("#..........#"),
         list("#..........#"),
         list("#..........#"),
         list("#..........#"),
         list("############")]

snake_top = [4,2]
snake = [[2,2],[3,2],[4,2]]
snake_len = 2

put_meat()
snake_direction = "right"
snake_direction_old = "right"

system('cls||clear')
for i in field:
    for ii in i:
        print(ii, end='')
    print("")
print("Start     02")

while play_on == "Process":

    sleep(0.5)

    system('cls||clear')

    if snake_direction == "right":
        next_top = [snake_top[0]+1,snake_top[1]+0]
    elif snake_direction == "left":
        next_top = [snake_top[0]-1,snake_top[1]+0]
    elif snake_direction == "up":
        next_top = [snake_top[0]+0,snake_top[1]-1]
    elif snake_direction == "down":
        next_top = [snake_top[0]+0,snake_top[1]+1]
    snake_direction_old = snake_direction

    in_next_top = field[next_top[1]][next_top[0]]
    if snake_len >= 30:
        play_on = "Win    "
    elif in_next_top == "#":
        play_on = "Fail   "
    elif in_next_top == "." or in_next_top == "%":
        snake.append(next_top)
        remove_tail = snake.pop(0)

        field[remove_tail[1]][remove_tail[0]] = "."
        if field[next_top[1]][next_top[0]] == "%":
            play_on = "Fail   "

        if play_on == "Process":
            field[next_top[1]][next_top[0]] = "@"
            field[snake_top[1]][snake_top[0]] = "%"

            snake_top = [next_top[0]+0,next_top[1]+0]
    elif in_next_top == "*":
        snake.append(next_top)

        field[next_top[1]][next_top[0]] = "@"
        field[snake_top[1]][snake_top[0]] = "%"

        put_meat()
        snake_top = [next_top[0]+0,next_top[1]+0]
        snake_len += 1
    else:
        print("WTF?")

    for i in field:
        for ii in i:
            print(ii, end='')
        print()
    print(play_on, "   ", f'{snake_len:02}', sep="")

