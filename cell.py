from tkinter import Tk, BOTH, Canvas

class Cell:
    def __init__(self, x1, y1, x2, y2, left_wall = True, right_wall = True, top_wall = True, bottom_wall = True):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self.has_left_wall = left_wall
        self.has_right_wall = right_wall
        self.has_top_wall = top_wall
        self.has_bottom_wall = bottom_wall

    def draw(self, canvas, fill_color):
        if self.has_left_wall:
            canvas.create_line(self._x1, self._y1, self._x1, self._y2, fill = fill_color)
        if self.has_right_wall:
            canvas.create_line(self._x2, self._y1, self._x2, self._y2, fill = fill_color)
        if self.has_top_wall:
            canvas.create_line(self._x1, self._y1, self._x2, self._y1, fill = fill_color)
        if self.has_bottom_wall:
            canvas.create_line(self._x1, self._y2, self._x2, self._y2, fill = fill_color)
