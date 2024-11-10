@ECHO OFF
REM Makefile for project needs
REM Author: Ben Trachtenberg
REM Version: 1.0.7
REM

IF "%1" == "all" (
    pytest --cov --cov-report=html -vvv
    black pod_porter/
    black tests/
    pylint pod_porter\
    pip-audit -r requirements.txt
    GOTO END
)

IF "%1" == "build" (
    python -m build
    GOTO END
)

IF "%1" == "coverage" (
    pytest --cov --cov-report=html -vvv
    GOTO END
)

IF "%1" == "pylint" (
    pylint pod_porter\
    GOTO END
)

IF "%1" == "pytest" (
    pytest --cov -vvv
    GOTO END
)

IF "%1" == "format" (
    black pod_porter/
    black tests/
    GOTO END
)

IF "%1" == "check-vuln" (
    pip-audit -r requirements.txt
    GOTO END
)

IF "%1" == "gh-pages" (
    rmdir /s /q docs\source\code
    sphinx-apidoc -o ./docs/source/code ./pod_porter
    sphinx-build ./docs ./docs/gh-pages
    GOTO END
)

@ECHO make options
@ECHO     all             To run coverage, format, pylint, and check-vuln
@ECHO     build           To build a distribution
@ECHO     coverage        To run coverage and display ASCII and output to htmlcov
@ECHO     check-vuln      To check for vulnerabilities in the dependencies
@ECHO     format          To format the code with black
@ECHO     pylint          To run pylint
@ECHO     pytest          To run pytest with verbose option


:END
