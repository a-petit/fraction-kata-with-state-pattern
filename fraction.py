from abc import ABC, abstractmethod
from dataclasses import dataclass
from math import gcd


@dataclass(frozen=True)
class Fraction(ABC):

    @classmethod
    def of(cls, numerator, denominator):
        if numerator == 0:
            return _Zero()
        if denominator == 0:
            return _Infinity() if numerator >= 0 else _MinusInfinity()

        if denominator < 0:
            numerator *= -1
            denominator *= -1

        d = gcd(numerator, denominator)
        numerator //= d
        denominator //= d
        return RegularFraction(numerator, denominator)

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def representation(self) -> str:
        pass

    @classmethod
    def infinity(cls):
        return _Infinity()

    @classmethod
    def minus_infinity(cls):
        return _MinusInfinity()

    @classmethod
    def zero(cls) -> 'Fraction':
        return _Zero()


@dataclass(frozen=True)
class RegularFraction(Fraction):
    def __add__(self, other):
        if isinstance(other, RegularFraction):
            return Fraction.of(
                self._numerator * other._denominator + other._numerator * self._denominator,
                self._denominator * other._denominator)
        if isinstance(other, Fraction):
            return other + self

        raise Exception

    def representation(self) -> str:
        return f"{self._numerator}/{self._denominator}"

    _numerator: int
    _denominator: int


@dataclass(frozen=True)
class _Zero(Fraction):

    def __add__(self, other):
        return other

    def representation(self) -> str:
        return "0"


@dataclass(frozen=True)
class _Infinity(Fraction):
    def __add__(self, other):
        if isinstance(other, _MinusInfinity):
            return Fraction.zero()
        if isinstance(other, Fraction):
            return self

        raise Exception

    def representation(self) -> str:
        return "+inf"


@dataclass(frozen=True)
class _MinusInfinity(Fraction):
    def __add__(self, other):
        if isinstance(other, _Infinity):
            return Fraction.zero()
        if isinstance(other, Fraction):
            return self

        raise Exception

    def representation(self) -> str:
        return "-inf"
