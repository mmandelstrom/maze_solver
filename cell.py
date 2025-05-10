#This file will holde cell class and methods
from drawing import *

class Cell:
    def __init__(self, x1, y1, x2, y2, canvas, left_wall = True, top_wall = True,  right_wall = True, bottom_wall = True):
        self.has_left_wall = left_wall
        self.has_top_wall = top_wall
        self.has_right_wall = right_wall
        self.has_bottom_wall = bottom_wall
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = canvas

    def draw(self):
        canvas = self._win
        x1 = self._x1
        x2 = self._x2
        y1 = self._y1
        y2 = self._y2

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
        canvas = self._win
        if undo:
            fill_color = "red"
        else:
            fill_color = "gray"

        from_x = (self._x1 + self._x2) / 2
        from_y = (self._y1 + self._y2) / 2
        to_x = (to_cell._x1 + to_cell._x2) / 2
        to_y = (to_cell._y1 + to_cell._y2) / 2

        line = Line(Point(from_x, from_y), Point(to_x, to_y))
        line.draw(canvas, fill_color)

