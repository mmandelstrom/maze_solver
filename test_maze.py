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
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )
    
    def test_maze_create_cells_2(self):
        win = Window(800, 600)
        maze = Maze(100, 100, 20, 30, 5, 5, win)
        self.assertEqual(len(maze._cells), 20)
        self.assertEqual(len(maze._cells[0]), 30)

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

    def test_break_walls_r_seed(self):
        win = Window(800, 600)
        m1 = Maze(100, 200, 10, 10, 10, 10, win, seed=1)
        m2 = Maze(100, 200, 10, 10, 10, 10, win, seed=1)

        for i in range(m1._num_rows):
            for j in range(m1._num_cols):
                self.assertEqual(m1._cells[i][j].has_top_wall, m2._cells[i][j].has_top_wall)
                self.assertEqual(m1._cells[i][j].has_right_wall, m2._cells[i][j].has_right_wall)
                self.assertEqual(m1._cells[i][j].has_bottom_wall, m2._cells[i][j].has_bottom_wall)
                self.assertEqual(m1._cells[i][j].has_left_wall, m2._cells[i][j].has_left_wall)

    def test_break_walls_r_seed_more_rows(self):
        win = Window(800, 600)
        m1 = Maze(100, 200, 15, 10, 10, 10, win, seed=1)
        m2 = Maze(100, 200, 15, 10, 10, 10, win, seed=1)

        for i in range(m1._num_rows):
            for j in range(m1._num_cols):
                self.assertEqual(m1._cells[i][j].has_top_wall, m2._cells[i][j].has_top_wall)
                self.assertEqual(m1._cells[i][j].has_right_wall, m2._cells[i][j].has_right_wall)
                self.assertEqual(m1._cells[i][j].has_bottom_wall, m2._cells[i][j].has_bottom_wall)
                self.assertEqual(m1._cells[i][j].has_left_wall, m2._cells[i][j].has_left_wall)


    def test_break_walls_r_seed_more_cols(self):
        win = Window(800, 600)
        m1 = Maze(100, 200, 12, 20, 10, 10, win, seed=1)
        m2 = Maze(100, 200, 12, 20, 10, 10, win, seed=1)

        for i in range(m1._num_rows):
            for j in range(m1._num_cols):
                self.assertEqual(m1._cells[i][j].has_top_wall, m2._cells[i][j].has_top_wall)
                self.assertEqual(m1._cells[i][j].has_right_wall, m2._cells[i][j].has_right_wall)
                self.assertEqual(m1._cells[i][j].has_bottom_wall, m2._cells[i][j].has_bottom_wall)
                self.assertEqual(m1._cells[i][j].has_left_wall, m2._cells[i][j].has_left_wall)


    def test_break_walls_r_seed_2(self):
        win = Window(800, 600)
        m1 = Maze(100, 200, 12, 20, 10, 10, win, seed=2)
        m2 = Maze(100, 200, 12, 20, 10, 10, win, seed=2)

        for i in range(m1._num_rows):
            for j in range(m1._num_cols):
                self.assertEqual(m1._cells[i][j].has_top_wall, m2._cells[i][j].has_top_wall)
                self.assertEqual(m1._cells[i][j].has_right_wall, m2._cells[i][j].has_right_wall)
                self.assertEqual(m1._cells[i][j].has_bottom_wall, m2._cells[i][j].has_bottom_wall)
                self.assertEqual(m1._cells[i][j].has_left_wall, m2._cells[i][j].has_left_wall)


if __name__ == "__main__":
    unittest.main()