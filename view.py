import pygame


class View:
    TESTBOARD = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    def __init__(self):
        
        pygame.display.set_caption("Noughts and Crosses")

        
        self.win = pygame.display.set_mode((300, 300))

        self.unitSize = 20

        self.canvasLength = 3 * self.unitSize
        self.canvasHeight = 3 * self.unitSize

    def draw_grid(self, grid):
        for row in range(3):
            for col in range(3):
                pygame.draw.rect(self.win, (255, 255, 255), (col * 100, row * 100, 100, 100), 1)
                
                if grid[row, col] == 1:
                    pygame.draw.circle(self.win, (255, 255, 255), (col * 100 + 50, row * 100 + 50), 40, 1)
                elif grid[row, col] == 2:
                    pygame.draw.line(self.win, (255, 255, 255), (col * 100 + 10, row * 100 + 10), (col * 100 + 90, row * 100 + 90))
                    pygame.draw.line(self.win, (255, 255, 255), (col * 100 + 90, row * 100 + 10), (col * 100 + 10, row * 100 + 90))
                



    def render(self, grid):

        self.win.fill((0, 0, 0))

        self.draw_grid(grid)

        pygame.display.update()


