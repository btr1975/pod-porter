# Makefile for project needs
# Author: Ben Trachtenberg
# Version: 2.0.0
#

.PHONY: all info build build-container coverage format pylint pytest start-container stop-container remove-container \
        gh-pages check-security pip-export

info:
	@echo "make options"
	@echo "    all                 To run coverage, format, pylint, and check-vuln"
	@echo "    build               To build a distribution"
	@echo "    build-container     To build a container image"
	@echo "    coverage            To run coverage and display ASCII and output to htmlcov"
	@echo "    format              To format the code with black"
	@echo "    pylint              To run pylint"
	@echo "    pytest              To run pytest with verbose option"
	@echo "    start-container     To start the container"
	@echo "    stop-container      To stop the container"
	@echo "    remove-container    To remove the container"


all: format pylint coverage check-security pip-export

build:
	@uv build --wheel --sdist

coverage:
	@uv run pytest --cov --cov-report=html -vvv

format:
	@uv run black pod_porter/
	@uv run black tests/

pylint:
	@uv run pylint pod_porter/

pytest:
	@uv run pytest --cov -vvv

check-security:
	@uv run bandit -c pyproject.toml -r .

pip-export:
	@uv export --no-dev --no-emit-project --no-editable > requirements.txt
	@uv export --no-emit-project --no-editable > requirements-dev.txt

build-container:
	@cd containers && podman build --ssh=default --build-arg=build_branch=main -t pod-porter:latest -f Containerfile

start-container:
	@podman run -itd --name pod-porter -p 8080:8080 localhost/pod-porter:latest

stop-container:
	@podman stop pod-porter

remove-container:
	@podman rm pod-porter

gh-pages:
	@rm -rf ./docs/source/code
	@sphinx-apidoc -o ./docs/source/code ./pod_porter
	@sphinx-build ./docs ./docs/gh-pages
