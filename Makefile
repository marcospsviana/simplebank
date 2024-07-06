setup:
	python models.models.py

formater:
	black .

check:
	flake8 .