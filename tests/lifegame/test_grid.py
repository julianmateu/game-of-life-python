from lifegame.cell import Cell
from lifegame.grid import Grid, initialize_grid_to_shape


class TestGrid:
    def setup_method(self) -> None:
        self.grid = Grid(3, 3)

    def test_creation(self) -> None:
        assert self.grid.get_width() == 3
        assert self.grid.get_height() == 3

    def test_get_cell(self) -> None:
        assert self.grid.get_cell(0, 0).is_alive == False
        assert self.grid.get_cell(1, 1).is_alive == False
        assert self.grid.get_cell(2, 2).is_alive == False

        assert self.grid.get_cell(0, 0).get_neighbours() == [
            self.grid.get_cell(0, 1),
            self.grid.get_cell(1, 0),
            self.grid.get_cell(1, 1),
        ]

    def test_get_neighbours(self) -> None:
        assert self.grid.get_neighbours(0, 0) == [
            self.grid.get_cell(0, 1),
            self.grid.get_cell(1, 0),
            self.grid.get_cell(1, 1),
        ]
        assert self.grid.get_neighbours(1, 1) == [
            self.grid.get_cell(0, 0),
            self.grid.get_cell(0, 1),
            self.grid.get_cell(0, 2),
            self.grid.get_cell(1, 0),
            self.grid.get_cell(1, 2),
            self.grid.get_cell(2, 0),
            self.grid.get_cell(2, 1),
            self.grid.get_cell(2, 2),
        ]
        assert self.grid.get_neighbours(2, 2) == [
            self.grid.get_cell(1, 1),
            self.grid.get_cell(1, 2),
            self.grid.get_cell(2, 1),
        ]

    def test_get_alive_cells(self) -> None:
        self._add_x_alive_neighbours(1, 0, 0)
        assert self.grid.get_alive_cells() == [self.grid.get_cell(0, 1)]

    def test_update_state(self) -> None:
        self._add_x_alive_neighbours(1, 0, 0)
        self.grid.update_state()
        assert self.grid.get_alive_cells() == []

    def _add_x_alive_neighbours(self, x: int, x_pos: int, y_pos: int) -> None:
        neighbours = self.grid.get_neighbours(x_pos, y_pos)
        for i in range(x):
            neighbours[i].resurrect()

    def test_glider(self):
        # ..X.
        # X.X.
        # .XX.

        # .X..
        # ..XX
        # .XX.
        glider = [
            (0, 2),
            (1, 0),
            (1, 2),
            (2, 1),
            (2, 2),
        ]

        self.grid = initialize_grid_to_shape(5, 5, glider, offset=0)

        self.grid.update_state()
        assert set(self.grid.get_alive_cells()) == {
            self.grid.get_cell(0, 1),
            self.grid.get_cell(1, 2),
            self.grid.get_cell(1, 3),
            self.grid.get_cell(2, 1),
            self.grid.get_cell(2, 2),
        }
