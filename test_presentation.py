from dataclasses import dataclass

import pytest


@dataclass(frozen=True)
class Fraction:
    _numerator: int
    _denominator: int

    @classmethod
    def of(cls, numerator, denominator):
        return Fraction(numerator, denominator)

    def representation(self) -> str:
        return f"{self._numerator}/{self._denominator}"


@pytest.mark.parametrize("numerator, denominator, representation", [
    (1, 3, "1/3"),
    (3, 7, "3/7"),
])
def test_regular_fraction(numerator, denominator, representation):
    assert Fraction.of(numerator, denominator).representation() == representation
