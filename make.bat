@ECHO OFF
REM Makefile for project needs
REM Author: Ben Trachtenberg
REM Version: 2.0.0
REM

IF "%1" == "all" (
    uv run black pod_porter/
    uv run black tests/
    uv run pylint pod_porter\
    uv run pytest --cov --cov-report=html -vvv
    uv run bandit -c pyproject.toml -r .
    uv export --no-dev --no-emit-project --no-editable > requirements.txt
    uv export --no-emit-project --no-editable > requirements-dev.txt
    GOTO END
)

IF "%1" == "build" (
    uv build --wheel --sdist
    GOTO END
)

IF "%1" == "coverage" (
    uv run pytest --cov --cov-report=html -vvv
    GOTO END
)

IF "%1" == "pylint" (
    uv run pylint pod_porter\
    GOTO END
)

IF "%1" == "pytest" (
    uv run pytest --cov -vvv
    GOTO END
)

IF "%1" == "format" (
    uv run black pod_porter/
    uv run black tests/
    GOTO END
)

IF "%1" == "check-security" (
    uv run bandit -c pyproject.toml -r .
    GOTO END
)

IF "%1" == "pip-export" (
    uv export --no-dev --no-emit-project --no-editable > requirements.txt
    uv export --no-emit-project --no-editable > requirements-dev.txt
    GOTO END
)

IF "%1" == "gh-pages" (
    rmdir /s /q docs\source\code
    uv run sphinx-apidoc -o ./docs/source/code ./pod_porter
    uv run sphinx-build ./docs ./docs/gh-pages
    GOTO END
)

@ECHO make options
@ECHO     all             To run coverage, format, pylint, and check-vuln
@ECHO     build           To build a distribution
@ECHO     coverage        To run coverage and display ASCII and output to htmlcov
@ECHO     format          To format the code with black
@ECHO     pylint          To run pylint
@ECHO     pytest          To run pytest with verbose option


:END
