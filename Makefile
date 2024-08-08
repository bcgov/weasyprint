.PHONY: install, dev, format, weasyprint

install:
	pip install -r requirements-dev.txt
	pip install -r requirements.txt

dev:
	fastapi dev

format:
	black .

weasyprint:
	docker run -p 8080:8080 --pull always ghcr.io/bcgov/weasyprint:latest
