#This file will hold maze class and associated methods
from cell import *
from window import *
import time #Imported to use sleep to visualize animation

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        
        for i in range(self._num_cols):#For each row create a new row
            col = []
            for j in range(self._num_rows):#For each column create a cell and call draw method
                col.append(Cell(self._win))
            self._cells.append(col)#Add row to list before moving on to the next row

        for i in range(self._num_cols): #Loop through each row
            for j in range(self._num_rows): #And each column
                self._draw_cell(i, j) #Draw each cell using i and j
        
        self._break_entrance_and_exit()



    def _draw_cell(self, i, j):
        #Calculate the values for x1/x2/y1/y2 using i and j
        x1 = self._x1 + j * self._cell_size_x
        y1 = self._y1 + i * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y

        self._cells[i][j].draw(x1, y1, x2, y2) #Draw each cell
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.02)
        

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False #Break top wall for first cell
        self._draw_cell(0, 0) #Redraw cell to graphically show wall is broken

        last_col = self._num_cols - 1
        last_row = self._num_rows - 1

        self._cells[last_col][last_row].has_bottom_wall = False #Break bottom wall for last cell
        self._draw_cell(last_col, last_row) #Redraw cell to graphically show wall is broken

            