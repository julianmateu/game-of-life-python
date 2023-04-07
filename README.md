# Conway's Game of Life in Python

A simple application in python that generates an animation of [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life). See an example in [`game_of_life.mp4`](./game_of_life.mp4)

Based on the [`hello-python` repo](https://github.com/julianmateu/hello-python), which creates a basic python application using [GNU Make](https://www.gnu.org/software/make/), it can be configured to use
[pipenv](https://pypi.org/project/pipenv/) or [venv](https://docs.python.org/3/library/venv.html). It also uses
[black](https://pypi.org/project/black/), [pytest](https://pypi.org/project/pytest/),
[pytest-cov](https://pypi.org/project/pytest-cov/), [mypy](https://pypi.org/project/mypy/),
and [isort](https://pypi.org/project/isort/), all running in a
[VSCode devcontainer](https://code.visualstudio.com/docs/devcontainers/containers).

## Getting started
Define if you'll use pipenv or virtualenv. Copy the `.env.example` file to the `.env` file and customize:
```bash
cp .env.example .env
```

Depending on which environment you're going to use, run:
```bash
make init-repo-pipenv
```
or
```bash
make init-repo-virtualenv 
source .venv/bin/activate
```

Run the application:
```bash
make run
```

Run the tests, lint, type check and coverage:
```bash
make check
```

The coverage report will be present in the [`htmlcov`](./htmlcov/) folder.
