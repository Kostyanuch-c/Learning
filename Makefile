.PHONY: install
install:
	@poetry install --no-root

.PHONY: lint
lint:
	@poetry run flake8 algoritms LeetCode