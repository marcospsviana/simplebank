setup:
	python models.models.py

formater:
	black .
	isort .

check:
	flake8 .