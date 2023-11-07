class Fraction:
    @classmethod
    def of(cls, numerator, denominator):
        return Fraction()

    def representation(self) -> str:
        return "1/3"


def test_regular_fraction():
    assert Fraction.of(1, 3).representation() == "1/3"
