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
    def representation(self) -> str:
        pass

    @classmethod
    def infinity(cls):
        return _Infinity()

    @classmethod
    def minus_infinity(cls):
        return _MinusInfinity()


@dataclass(frozen=True)
class RegularFraction(Fraction):
    def representation(self) -> str:
        return f"{self._numerator}/{self._denominator}"

    _numerator: int
    _denominator: int


@dataclass(frozen=True)
class _Zero(Fraction):

    def representation(self) -> str:
        return "0"


@dataclass(frozen=True)
class _Infinity(Fraction):
    def representation(self) -> str:
        return "+inf"


@dataclass(frozen=True)
class _MinusInfinity(Fraction):
    def representation(self) -> str:
        return "-inf"
