#This file will hold the window class

from tkinter import Tk, BOTH, Canvas
from drawing import *

class Window:
    def __init__(self, width, height): #In the initializer we set height, width and create a root for tk and create an pack canvas to ready it to be displayed
        self.__width = width
        self.__height = height
        self.__root = Tk()
        self.__root.title = "title"
        self.__canvas = Canvas(self.__root, height=self.__height, width=self.__width)
        self.__canvas.pack(fill="both", expand=1)
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self): #Trigger a redrawing of window when this method is called
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self): #Continiously call redraw while running is True
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, Line, fill_color):
        Line.draw(self.__canvas, fill_color)



    

