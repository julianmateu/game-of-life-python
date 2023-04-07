ifneq (,$(wildcard ./.env))
    include .env
    export
endif
SRC_DIR=lifegame
TEST_DIR=tests
RUN_PIPENV=pipenv run
ifeq (${USE_PIPENV}, true)
RUN=${RUN_PIPENV}
endif

.PHONY: test
test:
	$(RUN) pytest

.PHONY: coverage
coverage:
	$(RUN) pytest -vv \
	-o log_cli=true --log-cli-level=DEBUG \
	--cov-report=html \
	--cov-fail-under=90 \
	--cov=$(SRC_DIR) \
	--cov=main.py

.PHONY: lint
lint:
	$(RUN) black $(SRC_DIR) $(TEST_DIR) main.py
	$(RUN) isort $(SRC_DIR) $(TEST_DIR) main.py

.PHONY: type-check
type-check:
	$(RUN) mypy $(SRC_DIR) $(TEST_DIR) main.py

.PHONY: check
check: lint type-check coverage

.PHONY: run
run:
	$(RUN) python main.py

.PHONY: init-repo-pipenv
init-repo-pipenv:
	pipenv --python $$(cat .python-version)
	pipenv install -r requirements.txt
	pipenv install --dev -r requirements-dev.txt

.PHONY: init-repo-virtualenv
init-repo-virtualenv:
	python -m venv .venv
	. .venv/bin/activate; pip install -r requirements.txt; pip install -r requirements-dev.txt
