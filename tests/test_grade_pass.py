import pytest

from src.grade_pass import has_passed


# Score of 50 or more -> pass (returns True)
@pytest.mark.parametrize(
    "score",
    [
        50,  # exactly the pass mark (boundary)
        51,  # just above the pass mark
        75,  # typical passing score
        100,  # upper boundary
    ],
)
def test_score_50_or_more_returns_true(score):
    # Act
    result = has_passed(score)

    # Assert
    assert result is True


# Score below 50 -> not a pass (returns False)
@pytest.mark.parametrize(
    "score",
    [
        49,  # just below the pass mark (boundary)
        25,  # typical failing score
        1,  # just above lower boundary
        0,  # lower boundary
    ],
)
def test_score_below_50_returns_false(score):
    # Act
    result = has_passed(score)

    # Assert
    assert result is False


# Correct type (int) but outside 0 to 100 -> ValueError
@pytest.mark.parametrize(
    "score",
    [
        -1,  # just below lower boundary
        101,  # just above upper boundary
    ],
)
def test_score_outside_range_raises_value_error(score):
    with pytest.raises(ValueError):
        has_passed(score)


# Wrong data type -> TypeError (None and bool are invalid)
@pytest.mark.parametrize(
    "score",
    [
        None,  # missing score
        50.0,  # float
        "50",  # string
        True,  # bool is not a valid int
        False,  # bool is not a valid int
    ],
)
def test_score_with_invalid_type_raises_type_error(score):
    with pytest.raises(TypeError):
        has_passed(score)
