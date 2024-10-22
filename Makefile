ifdef OS
   export VENV_BIN=.venv/Scripts
else
   export VENV_BIN=.venv/bin
endif

lock:
	. $(VENV_BIN)/activate && uv lock

compile:
	. $(VENV_BIN)/activate && uv pip compile pyproject.toml -o requirements.txt

sync:
	. $(VENV_BIN)/activate && uv sync

sync-dev:
	. $(VENV_BIN)/activate && uv sync --all-extras

format:
	. $(VENV_BIN)/activate && ruff format

lint:
	. $(VENV_BIN)/activate && ruff check --fix
	. $(VENV_BIN)/activate && mypy --ignore-missing-imports --install-types --non-interactive --package intesa_vincente_llm

create-env:
	uv venv

upgrade-deps:
	. $(VENV_BIN)/activate && uv lock --upgrade
