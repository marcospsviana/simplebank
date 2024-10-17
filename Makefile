setup:
	python models.py

formater:
	black .
	isort .

check:
	flake8 .

test:
	python -m pytest tests -vss 