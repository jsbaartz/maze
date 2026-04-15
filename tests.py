import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )

    def test_maze_small_grid(self):
        num_cols = 2
        num_rows = 3
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._Maze__cells), num_cols)
        self.assertEqual(len(m1._Maze__cells[0]), num_rows)

    def test_maze_single_cell(self):
        num_cols = 1
        num_rows = 1
        m1 = Maze(0, 0, num_rows, num_cols, 20, 20)
        self.assertEqual(len(m1._Maze__cells), num_cols)
        self.assertEqual(len(m1._Maze__cells[0]), num_rows)

    def test_maze_rectangular_grid(self):
        num_cols = 5
        num_rows = 8
        m1 = Maze(0, 0, num_rows, num_cols, 15, 12)
        self.assertEqual(len(m1._Maze__cells), num_cols)
        self.assertEqual(len(m1._Maze__cells[0]), num_rows)

    def test_maze_wide_grid(self):
        num_cols = 20
        num_rows = 4
        m1 = Maze(0, 0, num_rows, num_cols, 5, 5)
        self.assertEqual(len(m1._Maze__cells), num_cols)
        self.assertEqual(len(m1._Maze__cells[0]), num_rows)

    def test_maze_break_entrance_and_exit(self):
        num_cols = 4
        num_rows = 3
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        self.assertEqual(
            m1._Maze__cells[0][0].has_top_wall,
            False,
        )

        self.assertEqual(
            m1._Maze__cells[num_cols - 1][num_rows - 1].has_bottom_wall,
            False,
        )
    def test_reset_cells_visited(self):
        m1 = Maze(0, 0, 3, 3, 10, 10, seed=0)

        # After maze generation, all cells should have been visited
        for i in range(3):
            for j in range(3):
                self.assertEqual(m1._Maze__cells[i][j].visited, False)


if __name__ == "__main__":
    unittest.main()