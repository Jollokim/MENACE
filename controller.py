import pygame

from view import View
from board import Board


class Controller:
    def __init__(self, board: Board, view: View):
        self.board = board
        self.view = view

    def run(self):
        pygame.time.delay(10)

        self.view.render(self.board.grid)
        
        self.event_handler()


    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                xpos, ypos = pygame.mouse.get_pos()
                self.play_move(xpos, ypos)


    def play_move(self, xpos, ypos):
        col = int(xpos / 100)
        row = int(ypos / 100)

        if not self.board.grid[row, col]:
            if self.board.playerTurn:
                self.board.grid[row, col] = 2
                self.board.playerTurn = 0
            else:
                self.board.grid[row, col] = 1
                self.board.playerTurn = 1

        # return if someone won here?
            
            

        