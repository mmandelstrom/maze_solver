from window import Window
from drawing import *
from cell import *
from maze import *

win = Window(800, 600)
maze = Maze(150, 100, 4, 4, 30, 30, win, seed=1)

win.wait_for_close()