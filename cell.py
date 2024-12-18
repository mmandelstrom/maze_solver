from tkinter import Tk, BOTH, Canvas
from graphics import Line, Point, Window

#Initialized class with all walls and no x/y coordinates as defaults, sets self._win as input win
class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.visited = False


#Sets x / y values, if walls are present they are drawn
    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self._win is None:
            return
        
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "white")

        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "white")

        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "white")

        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "white")

        
        

#Gets center x / y from x1,x2,y1,y2 of both cells then calls draw_line between them
    def draw_move(self, to_cell, undo=False):
        from_half_length = abs(self._x2 - self._x1) // 2
        from_center_x = from_half_length + self._x1
        from_center_y = from_half_length + self._y1

        to_half_length = abs(to_cell._x2 - to_cell._x1) // 2
        to_center_x = to_half_length + to_cell._x1
        to_center_y = to_half_length + to_cell._y1

        fill_color = "red"
        if undo:
            fill_color = "gray"

        line = Line(Point(from_center_x, from_center_y), Point(to_center_x, to_center_y))
        self._win.draw_line(line, fill_color)
        
