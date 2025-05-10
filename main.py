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
c1 = Cell(cv)
c2 = Cell(cv)
c3 = Cell(cv)
c4 = Cell(cv)
c5 = Cell(cv)

c1.draw(5, 15, 35, 35)
c2.draw(5, 45, 35, 65)
c3.draw(5, 75, 35, 95)
c4.draw(5, 105, 35, 125)
c5.draw(5, 135, 35, 155)



c1.draw_move(c4)
win.wait_for_close()