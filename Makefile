ifdef OS
   export PYTHON_COMMAND=python
   export UV_INSTALL_CMD=pip install uv==0.2.15
   export VENV_BIN=.venv/Scripts
else
   export PYTHON_COMMAND=python3.12
   export UV_INSTALL_CMD=pip install uv==0.2.15
   export VENV_BIN=.venv/bin
endif

lock:
	. $(VENV_BIN)/activate && uv lock

sync:
	. $(VENV_BIN)/activate && uv sync

sync-dev:
	. $(VENV_BIN)/activate && uv sync --all-extras

lint:
	. $(VENV_BIN)/activate && ruff format
	. $(VENV_BIN)/activate && ruff check --fix
	. $(VENV_BIN)/activate && mypy --ignore-missing-imports --install-types --non-interactive --package intesa_vincente_llm