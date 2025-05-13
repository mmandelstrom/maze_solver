#This file will hold unittests for the maze class and related methods
from maze import Maze
from window import Window
import unittest

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        win = Window(800, 600)
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_maze_create_cells_2(self):
        win = Window(800, 600)
        maze = Maze(100, 100, 20, 30, 5, 5, win)
        self.assertEqual(len(maze._cells), 30)
        self.assertEqual(len(maze._cells[0]), 20)

    def test_break_entrance_and_exit(self):
        win = Window(800, 600)
        m = Maze(100, 200, 5, 5, 10, 10, win)
        self.assertEqual(m._cells[0][0].has_top_wall, False)
        self.assertEqual(m._cells[-1][-1].has_bottom_wall, False)

    def test_break_entrance_and_exit_more_cols(self):
        win = Window(800, 600)
        m = Maze(100, 200, 15, 5, 10, 10, win)
        self.assertEqual(m._cells[0][0].has_top_wall, False)
        self.assertEqual(m._cells[-1][-1].has_bottom_wall, False)

    def test_break_entrance_and_exit_more_rows(self):
        win = Window(800, 600)
        m = Maze(100, 200, 5, 15, 10, 10, win)
        self.assertEqual(m._cells[0][0].has_top_wall, False)
        self.assertEqual(m._cells[-1][-1].has_bottom_wall, False)
   

if __name__ == "__main__":
    unittest.main()