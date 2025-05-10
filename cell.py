#This file will holde cell class and methods
from drawing import *

class Cell:
    def __init__(self, canvas):
        self.has_left_wall = True
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = canvas

    def draw(self, x1, y1, x2, y2):
        canvas = self._win
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        if self.has_left_wall: #Check for each wall and draw them
            line = Line(Point(x1, y1), Point(x1, y2)) #Draw by creating a line object using 2 points x1/y1 x2/y2
            line.draw(canvas, "white")
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            line.draw(canvas, "white")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            line.draw(canvas, "white")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            line.draw(canvas, "white")

    def draw_move(self, to_cell, undo=False): #Method to draw movement from center of a cell to another
        half_length = abs(self._x2 - self._x1) // 2 #Fixed calculation for center of cells
        from_x = half_length + self._x1
        from_y = half_length + self._y1

        half_length2 = abs(to_cell._x2 - to_cell._x1) // 2
        to_x = half_length2 + to_cell._x1
        to_y = half_length2 + to_cell._y1

        canvas = self._win
        if undo:
            fill_color = "gray"
        else:
            fill_color = "red"


        line = Line(Point(from_x, from_y), Point(to_x, to_y))
        line.draw(canvas, fill_color)
