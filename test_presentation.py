from dataclasses import dataclass
from math import gcd

import pytest


@dataclass(frozen=True)
class Fraction:
    _numerator: int
    _denominator: int

    @classmethod
    def of(cls, numerator, denominator):
        if denominator < 0:
            numerator *= -1
            denominator *= -1
        d = gcd(numerator, denominator)
        numerator //= d
        denominator //= d
        return Fraction(numerator, denominator)

    def representation(self) -> str:
        return f"{self._numerator}/{self._denominator}"


@pytest.mark.parametrize("numerator, denominator, representation", [
    # Fractions basiques
    (1, 3, "1/3"),
    (3, 7, "3/7"),
    # Fractions négatives
    (-1, 4, "-1/4"),
    (1, -4, "-1/4"),
    (-1, -4, "1/4"),
    # Fractions simplifiées
    (2, 4, "1/2"),
])
def test_regular_fraction(numerator, denominator, representation):
    assert Fraction.of(numerator, denominator).representation() == representation
