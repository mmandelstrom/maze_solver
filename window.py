from tkinter import Tk, BOTH, Canvas

class Window:

    #Constructor sets width, height and running Parameters. Creates a root widget and a canvas
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = "Maze solver"
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack()
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)


#Calls update methods on root
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

#Calls redraw method while running
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("Window was closed...")
        
#Sets running to false so redraw stops
    def close(self):
        self.__running = False


