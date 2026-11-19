# C339 CA1 - Project 05: Grade Checking System

Unit tests for `calculate_average()` (src/grade_average.py) and `has_passed()` (src/grade_pass.py).

## Run the tests locally

```
python -m pip install -r requirements.txt
python -m pytest -v
python -m pytest --cov=src --cov-report=term-missing
```

Tests also run automatically on GitHub Actions (see `.github/workflows/tests.yml`).

## Known failures (expected)

The test run currently shows **5 failed, 30 passed**. The failures are defects in the
supplied source code, found by the tests. They are not errors in the tests or the workflow.

| Failing test | Spec requirement | Actual behaviour | Cause |
|---|---|---|---|
| `test_valid_marks_returns_average[50-51-50.5]`, `[0-1-0.5]`, `[99-100-99.5]`, `test_odd_sum_keeps_fractional_part_not_rounded_down` | 3.1: use ordinary division and keep the fractional part (50 and 51 average to 50.5) | Returns 50, 0 and 99 | `grade_average.py` uses floor division `//` instead of `/` |
| `test_score_50_or_more_returns_true[50]` | 3.2: a score of 50 or more is a pass | `has_passed(50)` returns `False` | `grade_pass.py` uses `score > 50` instead of `score >= 50` |

## Reading the GitHub Actions result

A red X on a run can mean two different things. Check which step failed:

- **"Run the unit tests with coverage" step failed** and the log lists `FAILED` lines:
  the tests ran, but the code does not meet the specification. This is a *test failure*,
  which is what is happening here (see the table above).
- **"Set up Python" or "Install pytest and pytest-cov" step failed**: the runner could
  not prepare the environment, for example because of a wrong Python version or package
  name. This is an *environment setup error*. No tests ran at all.

## Workflow triggers (CA1 enhancement)

- Push to `main` that changes `src/`, `tests/`, `requirements.txt` or the workflow file
- Pull request into `main` (draft pull requests are skipped until marked "Ready for review")
- Manual "Run workflow" button in the Actions tab (`workflow_dispatch`)
- A newer push cancels an older run that is still in progress (`concurrency`)

A push that only changes documentation such as this README does not run the tests.
