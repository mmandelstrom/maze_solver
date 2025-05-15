from window import Window
from drawing import *
from cell import *
from maze import *

win = Window(800, 600)
maze = Maze(150, 100, 10, 10, 30, 30, win)


maze.solve()

win.wait_for_close()