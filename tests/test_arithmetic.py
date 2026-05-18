from toycalc import add


def test_adds_integers() -> None:
    assert add(2, 3) == 5


def test_adds_negative_numbers() -> None:
    assert add(-2, -3) == -5


def test_adds_float_values() -> None:
    assert add(1.25, 2.5) == 3.75
