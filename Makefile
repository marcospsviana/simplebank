setup:
	python setup_database.py

formater:
	black .

check:
	flake8 .