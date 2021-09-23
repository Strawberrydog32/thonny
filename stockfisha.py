#!python3
from stockfish import Stockfish
import pygame as pg
import numpy as np
import sys

#initialize stockfish
stockfish = Stockfish("C:\\Users\\Acer\\Downloads\\stockfish_14_win_x64_avx2\\stockfish_14_win_x64_avx2\\stockfish_14_x64_avx2.exe", parameters={"Threads": 500})
stockfish.set_depth(40)


#initialize pygame
pg.init()

size = width, height = 1920, 1080
speed = [20, 20]
black = 0, 0, 0

screen = pg.display.set_mode(size)

ball = pg.image.load("img/intro_ball.gif")
ballrect = ball.get_rect()

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pg.display.flip()

window = "yes"

#Mainloop prototype
position = parse_fen(stockfish.get_fen_position())
window.set_position(position)
while True:
    while True:
        position = window.get_position()
        move = window.get_move()
        if stockfish.is_move_correct:
            window.set_move(move)
            break
        else:
            window.set_position(position)
    




"""
while True:
    print(stockfish.get_board_visual())
    while True:
        x = input("Input a move: ")
        if stockfish.is_move_correct(x):
            break
        else:
            print("Invalid move")
    stockfish.make_moves_from_current_position([x])
    stockfish.make_moves_from_current_position([stockfish.get_best_move()])

"""