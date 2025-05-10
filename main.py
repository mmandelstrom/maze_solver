from window import Window
from drawing import *
from cell import *


p1 = Point(15, 15)
p2 = Point(200, 200)
p3 = Point(300, 300)
p4 = Point(600, 300)
line = Line(p1, p2)
line2 = Line(p3, p4)
win = Window(800, 600)
cv = win.get_canvas()
cells = [
    Cell(10, 10, 50, 50, cv, True, False, True, False),
    Cell(10, 60, 50, 100, cv),
    Cell(10, 110, 50, 150, cv, False, True, False, True),
    Cell(10, 160, 50, 200, cv, False, False, False, True),
    Cell(10, 210, 50, 250, cv, True, False, False, True)
]

for c in cells:
    c.draw()


win.wait_for_close()