from lifegame.cell import Cell


class TestCell:
    cell: Cell

    def setup_method(self) -> None:
        self.cell = Cell()

    def test_creation(self) -> None:
        assert self.cell.is_alive is False

    def test_kill(self) -> None:
        self.cell.kill()
        assert self.cell.is_alive is False

    def test_resurrect(self) -> None:
        self.cell.resurrect()
        assert self.cell.is_alive is True

    def test_get_neighbours(self) -> None:
        assert self.cell.get_neighbours() == []

    def test_add_neighbour(self) -> None:
        neighbour = Cell()
        self.cell.add_neighbour(neighbour)
        assert self.cell.get_neighbours() == [neighbour]
        assert neighbour.get_neighbours() == [self.cell]

    def test_get_alive_neighbours(self) -> None:
        neighbour = Cell()
        neighbour.resurrect()
        self.cell.add_neighbour(neighbour)
        assert self.cell.get_alive_neighbours() == [neighbour]
        assert neighbour.get_alive_neighbours() == []

    def test_neighbours_are_unique(self) -> None:
        neighbour = Cell()
        self.cell.add_neighbour(neighbour)
        self.cell.add_neighbour(neighbour)
        assert self.cell.get_neighbours() == [neighbour]
        assert neighbour.get_neighbours() == [self.cell]

    def test_add_neighbours(self) -> None:
        neighbour1 = Cell()
        neighbour2 = Cell()
        self.cell.add_neighbours([neighbour1, neighbour2])
        assert self.cell.get_neighbours() == [neighbour1, neighbour2]
        assert neighbour1.get_neighbours() == [self.cell]
        assert neighbour2.get_neighbours() == [self.cell]

    def test_update_state_no_neighbours_should_die(self) -> None:
        self.cell.resurrect()
        self.cell.update_state()
        assert self.cell.is_alive is False

    def test_update_state_two_alive_neighbours_should_remain_alive(self) -> None:
        self.cell.resurrect()
        self._add_x_alive_neighbours(2)
        self.cell.update_state()
        assert self.cell.is_alive is True

    def test_update_state_two_alive_neighbours_should_remain_dead(self) -> None:
        self._add_x_alive_neighbours(2)
        self.cell.update_state()
        assert self.cell.is_alive is False

    def test_update_state_three_alive_neighbours_should_remain_alive(self) -> None:
        self.cell.resurrect()
        self._add_x_alive_neighbours(3)
        self.cell.update_state()
        assert self.cell.is_alive is True

    def test_update_state_three_alive_neighbours_should_become_alive(self) -> None:
        self._add_x_alive_neighbours(3)
        self.cell.update_state()
        assert self.cell.is_alive is True

    def test_update_state_four_alive_neighbours_remain_dead(self) -> None:
        self._add_x_alive_neighbours(4)
        self.cell.update_state()
        assert self.cell.is_alive is False

    def test_update_state_four_alive_neighbours_should_die(self) -> None:
        self.cell.resurrect()
        self._add_x_alive_neighbours(4)
        self.cell.update_state()
        assert self.cell.is_alive is False

    def _add_x_alive_neighbours(self, x: int) -> None:
        for i in range(x):
            neighbour = Cell()
            neighbour.resurrect()
            self.cell.add_neighbour(neighbour)
