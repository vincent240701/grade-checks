import pytest

from src.grade_average import calculate_average


# Valid inputs: whole numbers from 0 to 100 -> returns the average (ordinary division)
@pytest.mark.parametrize(
    "mark_one, mark_two, expected",
    [
        (60, 80, 70),  # typical marks, even sum
        (50, 51, 50.5),  # example from spec, keeps fractional part
        (0, 0, 0),  # both at lower boundary
        (100, 100, 100),  # both at upper boundary
        (0, 100, 50),  # lower and upper boundary together
        (0, 1, 0.5),  # just above lower boundary, odd sum
        (99, 100, 99.5),  # just below upper boundary, odd sum
    ],
)
def test_valid_marks_returns_average(mark_one, mark_two, expected):
    # Act
    result = calculate_average(mark_one, mark_two)

    # Assert
    assert result == expected


def test_odd_sum_keeps_fractional_part_not_rounded_down():
    # Arrange
    mark_one = 50
    mark_two = 51

    # Act
    result = calculate_average(mark_one, mark_two)

    # Assert
    assert result != 50  # must not round down
    assert result == 50.5


# Correct type (int) but outside 0 to 100 -> ValueError
@pytest.mark.parametrize(
    "mark_one, mark_two",
    [
        (-1, 50),  # mark_one just below lower boundary
        (101, 50),  # mark_one just above upper boundary
        (50, -1),  # mark_two just below lower boundary
        (50, 101),  # mark_two just above upper boundary
    ],
)
def test_mark_outside_range_raises_value_error(mark_one, mark_two):
    with pytest.raises(ValueError):
        calculate_average(mark_one, mark_two)


# Wrong data type -> TypeError (bool is NOT a valid int)
@pytest.mark.parametrize(
    "mark_one, mark_two",
    [
        (50.5, 60),  # mark_one is a float
        (50, 60.0),  # mark_two is a float
        ("50", 60),  # mark_one is a string
        (50, "60"),  # mark_two is a string
        (None, 60),  # mark_one is missing (None)
        (50, None),  # mark_two is missing (None)
        (True, 60),  # mark_one is a bool
        (50, False),  # mark_two is a bool
    ],
)
def test_mark_with_invalid_type_raises_type_error(mark_one, mark_two):
    with pytest.raises(TypeError):
        calculate_average(mark_one, mark_two)
