class Cell:
    def __init__(self) -> None:
        self.id = id(self)
        self.is_alive = False
        self.neighbours: list["Cell"] = []
        self.next_state = False

    def kill(self) -> None:
        self.is_alive = False

    def resurrect(self) -> None:
        self.is_alive = True

    def kill_next(self) -> None:
        self.next_state = False

    def resurrect_next(self) -> None:
        self.next_state = True

    def get_neighbours(self) -> list["Cell"]:
        return self.neighbours

    def add_neighbour(self, neighbour: "Cell") -> None:
        self._append_neighbour_if_not_present(neighbour)
        neighbour._append_neighbour_if_not_present(self)

    def _append_neighbour_if_not_present(self, neighbour: "Cell") -> None:
        if neighbour not in self.neighbours:
            self.neighbours.append(neighbour)

    def add_neighbours(self, neighbours: list["Cell"]) -> None:
        for neighbour in neighbours:
            self.add_neighbour(neighbour)

    def get_alive_neighbours(self) -> list["Cell"]:
        return [neighbour for neighbour in self.neighbours if neighbour.is_alive]

    def update_state(self) -> None:
        self.compute_next_state()
        self.advance_to_next_state()

    def advance_to_next_state(self) -> None:
        self.is_alive = self.next_state

    def compute_next_state(self) -> None:
        alive_neighbours = self.get_alive_neighbours()
        self.next_state = self.is_alive
        if self.is_alive:
            if len(alive_neighbours) < 2:
                self.kill_next()
            elif len(alive_neighbours) > 3:
                self.kill_next()
        else:
            if len(alive_neighbours) == 3:
                self.resurrect_next()

    def __repr__(self) -> str:
        return f"Cell(id={self.id}, is_alive={self.is_alive})"
