import pygame

from view import View
from board import Board
from controller import Controller


pygame.init()

view = View()
board = Board()

controller = Controller(board, view)


while True:
    controller.run()