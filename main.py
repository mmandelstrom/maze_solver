from graphics import Window, Point, Line

win = Window(800, 600)

l = Line(Point(50, 50), Point(0, 800))
win.draw_line(l, "red")



win.wait_for_close()