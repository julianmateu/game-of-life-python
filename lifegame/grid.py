from lifegame.cell import Cell


class Grid:
    def __init__(self, width: int, height: int) -> None:
        self._width = width
        self._height = height
        self._cellToPosition = {}
        self._cells: list[list[Cell]] = []
        for x in range(width):
            self._cells.append([])
            for y in range(height):
                self._cells[x].append(Cell())
                self._cellToPosition[self._cells[x][y].id] = (x, y)
        self._add_neighbours()

    def _add_neighbours(self) -> None:
        for x in range(self._width):
            for y in range(self._height):
                self._add_neighbours_to_cell(x, y)

    def _add_neighbours_to_cell(self, x: int, y: int) -> None:
        neighbours = self.get_neighbours(x, y)
        self.get_cell(x, y).add_neighbours(neighbours)

    def get_neighbours(self, x: int, y: int) -> list[Cell]:
        neighbours = []
        for x_pos in range(x - 1, x + 2):
            for y_pos in range(y - 1, y + 2):
                if self._is_valid_position(x_pos, y_pos) and not (
                    x_pos == x and y_pos == y
                ):
                    neighbours.append(self.get_cell(x_pos, y_pos))
        return neighbours

    def _is_valid_position(self, x: int, y: int) -> bool:
        return 0 <= x < self._width and 0 <= y < self._height

    def get_position(self, cell: Cell) -> tuple[int, int]:
        return self._cellToPosition[cell.id]

    def get_cell(self, x: int, y: int) -> Cell:
        return self._cells[x][y]

    def get_width(self) -> int:
        return self._width

    def get_height(self) -> int:
        return self._height

    def update_state(self) -> None:
        for row in self._cells:
            for cell in row:
                cell.compute_next_state()
        for row in self._cells:
            for cell in row:
                cell.advance_to_next_state()

    def get_alive_cells(self) -> list[Cell]:
        alive_cells = []
        for x in range(self._width):
            for y in range(self._height):
                if self.get_cell(x, y).is_alive:
                    alive_cells.append(self.get_cell(x, y))
        return alive_cells

    def __repr__(self) -> str:
        return f"Grid(width={self._width}, height={self._height})"


def initialize_grid_to_shape(
    width: int, height: int, shape: list[tuple[int, int]], offset: int = 10
) -> Grid:
    grid = Grid(width, height)
    for x, y in shape:
        grid.get_cell(offset + x, offset + y).resurrect()
    return grid
