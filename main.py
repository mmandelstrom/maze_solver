from window import Window
from drawing import *


p1 = Point(15, 15)
p2 = Point(200, 200)
p3 = Point(300, 300)
p4 = Point(600, 300)
line = Line(p1, p2)
line2 = Line(p3, p4)
win = Window(800, 600)
win.draw_line(line, "white")
win.draw_line(line2, "red")

win.wait_for_close()