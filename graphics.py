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

    def draw_line(self, line, fill_color = "black"):
        line.draw(self.__canvas, fill_color)



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y



class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill = fill_color, width=2)


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
