pre-commit:
	@echo "Running FLAKE8 Linter on project..." && flake8
	@git update-index --again

setup:
	@echo "make pre-commit" > ./.git/hooks/pre-commit && chmod +x ./.git/hooks/pre-commit