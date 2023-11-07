import pytest

from fraction import Fraction


def test_fraction_is_a_value_object():
    assert Fraction.of(1, 2) == Fraction.of(1, 2)


def test_fraction_with_positive_numerator_and_nul_denominator_is_infinity():
    assert Fraction.of(0, 1) == Fraction.infinity()


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