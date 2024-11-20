from graphics import Window, Point, Line, Cell

win = Window(800, 600)

l = Line(Point(50, 50), Point(0, 800))
c = Cell(50, 60, 100, 120, True, True, True, True)
c1 = Cell(0, 20, 40, 60, True, True, True, True)
c2 = Cell(600, 700, 650, 750, True, True, False, True)
c3 = Cell(300, 350, 400, 550, True, False, True, True)
c4 = Cell(140, 260, 170, 300, True, True, True, True)

win.draw_line(c, "red")
win.draw_line(c1, "blue")
win.draw_line(c2, "white")
win.draw_line(c3, "blue")
win.draw_line(c4, "black")




win.wait_for_close()