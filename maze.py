#This file will hold maze class and associated methods
from cell import *
from window import *
import time #Imported to use sleep to visualize animation
import random 
from drawing import *

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None, seed = None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed is not None:
            random.seed(seed)
        self._create_cells()
        self.seed = seed
        


    def _create_cells(self):
        self._cells = []
        
        for i in range(self._num_rows):#For each row create a new row
            row = []
            for j in range(self._num_cols):#For each column create a cell and call draw method
                row.append(Cell(self._win))
            self._cells.append(row)#Add row to list before moving on to the next row

        for i in range(self._num_rows): #Loop through each row
            for j in range(self._num_cols): #And each column
                self._draw_cell(i, j) #Draw each cell using i and j
        
        self._break_walls_r(0, 0) #Create path in the maze
        self._break_entrance_and_exit() #Open entrance and exit
        self._reset_cells_visited() #Reset visited status to be reused



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

        self._cells[last_row][last_col].has_bottom_wall = False #Break bottom wall for last cell
        self._draw_cell(last_row, last_col) #Redraw cell to graphically show wall is broken


    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True #Visit current cell

        while True:
            to_visit = []
            if i - 1 >= 0:
                if not self._cells[i - 1][j].visited:
                    to_visit.append((i - 1, j))
            if j - 1 >= 0:
                if not self._cells[i][j - 1].visited:
                    to_visit.append((i, j - 1))
            if i + 1 < self._num_rows:
                if not self._cells[i + 1][j].visited:
                    to_visit.append((i + 1, j))
            if j + 1 < self._num_cols:
                if not self._cells[i][j + 1].visited:
                    to_visit.append((i, j + 1))
    
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return  
            old_i = i
            old_j = j

            i, j = random.choice(to_visit)

            if i < old_i: #Moving up
                if old_i > 0:
                    self._cells[old_i][old_j].has_top_wall = False
                    self._draw_cell(old_i, old_j)
                if i < self._num_rows - 1:
                    self._cells[i][j].has_bottom_wall = False
                    self._draw_cell(i, j)

            if j < old_j: #Moving left
                if old_j > 0:
                    self._cells[old_i][old_j].has_left_wall = False
                    self._draw_cell(old_i, old_j)
                if j < self._num_cols - 1:
                    self._cells[i][j].has_right_wall = False
                    self._draw_cell(i, j)

            if i > old_i: #Moving down
                if old_i < self._num_rows - 1:
                    self._cells[old_i][old_j].has_bottom_wall = False
                    self._draw_cell(old_i, old_j)
                if i > 0:
                    self._cells[i][j].has_top_wall = False
                    self._draw_cell(i, j)

            if j > old_j: #Moving right
                if old_j < self._num_cols - 1:
                    self._cells[old_i][old_j].has_right_wall = False
                    self._draw_cell(old_i, old_j)
                if j > 0:
                    self._cells[i][j].has_left_wall = False
                    self._draw_cell(i, j)

            self._break_walls_r(i, j)


    def _reset_cells_visited(self):
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._cells[i][j].visited = False


    def solve(self):
        if self._solve_r(0, 0) == True:
            print("Maze solved successfully")
        else:
            print("Maze not solved :(")
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self._num_rows - 1 and j == self._num_cols - 1: #If you are in the final cell
            return True
        
        directions = [
            (-1, 0, "has_top_wall", "has_bottom_wall"),   # Up
            (1, 0, "has_bottom_wall", "has_top_wall"),    # Down
            (0, -1, "has_left_wall", "has_right_wall"),   # Left
            (0, 1, "has_right_wall", "has_left_wall"),    # Right
        ]

        for delta_i, delta_j, wall_here, wall_there in directions:
            new_i = i + delta_i
            new_j = j + delta_j
            if new_i >= 0 and new_i < self._num_rows and new_j >= 0 and new_j < self._num_cols: #Make sure new values are withing the maze
                wall_here_val = getattr(self._cells[i][j], wall_here)
                wall_there_val = getattr(self._cells[new_i][new_j], wall_there)

                if not self._cells[new_i][new_j].visited and not wall_here_val and not wall_there_val: #If there are no walls move to new cell
                    self._cells[i][j].draw_move(self._cells[new_i][new_j])
                    if self._solve_r(new_i, new_j) == True: #IF maze was solved return true
                        return True
                    else: #Else redo and try antother direction
                        self._cells[i][j].draw_move(self._cells[new_i][new_j], undo=True)

        return False
        


