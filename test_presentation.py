import pytest

from fraction import Fraction


def test_fraction_is_a_value_object():
    assert Fraction.of(1, 2) == Fraction.of(1, 2)


def test_fraction_with_positive_numerator_and_nul_denominator_is_infinity():
    assert Fraction.of(1, 0) == Fraction.infinity()


def test_fraction_with_negative_numerator_and_nul_denominator_is_minus_infinity():
    assert Fraction.of(-1, 0) == Fraction.minus_infinity()


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
def test_fraction_presentation(numerator, denominator, representation):
    assert Fraction.of(numerator, denominator).representation() == representation


def test_presentation_of_inf():
    assert Fraction.infinity().representation() == "+inf"


def test_presentation_of_minus_inf():
    assert Fraction.minus_infinity().representation() == "-inf"


def test_presentation_of_zero():
    assert Fraction.of(0, 1).representation() == "0"


def test_addition_of_two_fractions_1():
    assert Fraction.of(1, 4) + Fraction.of(1, 4) == Fraction.of(1, 2)


def test_addition_of_two_fractions_2():
    assert Fraction.of(1, 3) + Fraction.of(1, 7) == Fraction.of(7 + 3, 21)


def test_fraction_plus_infinity_is_infinity():
    assert Fraction.infinity() + Fraction.of(7, 11) == Fraction.infinity()
    assert Fraction.of(7, 11) + Fraction.infinity() == Fraction.infinity()


def test_fraction_plus_minus_infinity_is_minus_infinity():
    assert Fraction.minus_infinity() + Fraction.of(7, 11) == Fraction.minus_infinity()
    assert Fraction.of(7, 11) + Fraction.minus_infinity() == Fraction.minus_infinity()


def test_infinity_plus_minus_infinity_is_zero():
    assert Fraction.infinity() + Fraction.minus_infinity() == Fraction.zero()
    assert Fraction.minus_infinity() + Fraction.infinity() == Fraction.zero()
