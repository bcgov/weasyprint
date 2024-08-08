.PHONY: install, dev, format

install:
	pip install -r requirements-dev.txt
	pip install -r requirements.txt

dev:
	fastapi dev

format:
	black .
