from graphics import Window, Point, Line
from cell import Cell

win = Window(800, 600)


c1 = Cell(win)
c1.has_left_wall = False
c1.draw(50, 50, 100, 100)

c2 = Cell(win)
c2.has_right_wall = False
c2.draw(125, 125, 200, 200)

c1.draw_move(c2, True)




win.wait_for_close()