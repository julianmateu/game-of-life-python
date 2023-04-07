import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

from lifegame.grid import Grid, initialize_grid_to_shape
from tests.lifegame.shapes import JULIANS_PULSAR


def main():
    width = 35
    height = 50
    frames = 100
    shape = JULIANS_PULSAR
    shape_name = "julians_pulsar"
    animate = True

    grid = initialize_grid_to_shape(width, height, shape)
    if animate:
        animate_grid(grid, width, height, frames, shape_name)
    else:
        plot_initial_state(grid)


def animate_grid(
    grid: Grid, width: int, height: int, frames: int, shape_name: str
) -> None:
    fig, ax = plt.subplots()
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)

    scat = ax.scatter(0, 0)

    def animate(i):
        alive_cells = grid.get_alive_cells()
        pos = []
        for cell in alive_cells:
            pos.append(grid.get_position(cell))
        scat.set_offsets(pos)
        grid.update_state()

    ani = animation.FuncAnimation(fig, animate, frames=frames, interval=100)
    writer = animation.FFMpegWriter(fps=15, metadata=dict(artist="Me"), bitrate=1800)
    ani.save(f"game_of_life_{shape_name}.mp4", writer=writer)


def plot_initial_state(grid: Grid) -> None:
    fig = plt.figure()
    alive_cells = grid.get_alive_cells()
    x, y = [], []
    for cell in alive_cells:
        cell_x, cell_y = grid.get_position(cell)
        x.append(cell_x)
        y.append(cell_y)
    plt.scatter(x, y)
    plt.show()


if __name__ == "__main__":  # pragma: no cover
    main()
