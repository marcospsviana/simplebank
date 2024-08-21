set-environment:
    python -m venv .venv
    source .venv/bin/activate
    python -m pip install poetry
    poetry install

setup:
	python models.models.py

formater:
	black .
	isort .

check:
	flake8 .

test:
	python -m pytest tests -vss --postgresql-host=localhost --postgresql-password=postgres --postgresql-user=postgres --cov=simplebank tests/