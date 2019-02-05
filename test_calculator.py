import pytest


@pytest.mark.parametrize("a, b, expected", [(5, 3, 2), (5, -2, 7),
                                            (30, 20, 10), ])
def test_calculator(a, b, expected):
    from calculator import subtract_two_numbers
    answer = subtract_two_numbers(a, b)
    assert answer == expected
