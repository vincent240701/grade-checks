# C339 CA1 - Project 05: Grade Checking System

Unit tests for `calculate_average()` (src/grade_average.py) and `has_passed()` (src/grade_pass.py).

## Run the tests locally

```
python -m pip install -r requirements.txt
python -m pytest -v
python -m pytest --cov=src --cov-report=term-missing
```

Tests also run automatically on GitHub Actions (see `.github/workflows/tests.yml`).
