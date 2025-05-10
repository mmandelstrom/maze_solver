#This file will hold maze class and associated methods
from cell import *
from window import *

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()

    def _create_cells(self):
        self._cells = [Cell() for col in range(self._num_cols)]
        print(f"self._cells: {self._cells}")
        
win = Window(800, 600)
maze = Maze(15, 23, 10, 10, 5, 5, win)