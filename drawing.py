#This file will hold point and draw classes
from tkinter import Tk, BOTH, Canvas

class Point: #Represents a point in the window, used to draw
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line: #Class used to draw lines, takes 2 Points(Class) as input
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2 

    def draw(self, canvas, fill_color):
        x1 = self.point_1.x
        x2 = self.point_2.x
        y1 = self.point_1.y
        y2 = self.point_2.y
        canvas.create_line(x1, y1, x2, y2, fill=fill_color, width=2)
