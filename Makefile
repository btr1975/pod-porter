# Makefile for project needs
# Author: Ben Trachtenberg
# Version: 1.0.8
#

.PHONY: all info build build-container coverage format pylint pytest start-container stop-container remove-container \
        gh-pages check-vuln

info:
	@echo "make options"
	@echo "    all                 To run coverage, format, pylint, and check-vuln"
	@echo "    build               To build a distribution"
	@echo "    build-container     To build a container image"
	@echo "    check-vuln          To check for vulnerabilities in the dependencies"
	@echo "    coverage            To run coverage and display ASCII and output to htmlcov"
	@echo "    format              To format the code with black"
	@echo "    pylint              To run pylint"
	@echo "    pytest              To run pytest with verbose option"
	@echo "    start-container     To start the container"
	@echo "    stop-container      To stop the container"
	@echo "    remove-container    To remove the container"


all: coverage format pylint check-vuln

build:
	@python -m build


build-container:
	@cd containers && podman build --ssh=default --build-arg=build_branch=main -t pod-porter:latest -f Containerfile




coverage:
	@pytest --cov --cov-report=html -vvv

format:
	@black pod_porter/
	@black tests/

pylint:
	@pylint pod_porter/

pytest:
	@pytest --cov -vvv




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

check-vuln:
	@pip-audit -r requirements.txt
