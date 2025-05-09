#This file will hold the window class

from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height): #In the initializer we set height, width and create a root for tk and create an pack canvas to ready it to be displayed
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title = "title"
        canvas = Canvas(self.__root)
        canvas.pack()
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
        


    

