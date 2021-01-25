import invoke


@invoke.task()
def check(c):
    """Run formatting, linting and testing."""
    c.run("isort dddentity tests")
    c.run("black dddentity tests")
    c.run("flake8 dddentity tests")
    c.run("mypy dddentity tests")
    c.run("pytest tests")
