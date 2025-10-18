.PHONY: install
install:
	@poetry install

.PHONY: lint
lint:
	@poetry run flake8 algoritms LeetCode