"""Sage data types.

   @summary
     Type Hierarchy:
       - DataType
         - Boolean
            False
            True
         - Date
         - DateTime
         - Number
           Float
           Integer
         - Text
           URL
         - Time

   @author
     Victor I. Afolabi
     Artificial Intelligence Expert & Researcher.
     Email: javafolabi@gmail.com | victor.afolabi@zephyrtel.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: dtype.pyi
     Created on 26 February, 2019 @ 12:21 AM.

   @license
     MIT License
     Copyright (c) 2019. Victor I. Afolabi. All rights reserved.
"""
from typing import Tuple, Union


class DataType(object):
    def __init__(self, o: object = ...) -> None: ...

    def __repr__(self) -> str: ...

    def __format__(self, format_specs: str) -> str: ...


class Boolean(int):
    def __init__(self, b: bool = None) -> None: ...

    def __repr__(self) -> str: ...

    def __str__(self) -> str: ...

    def __neg__(self) -> int: ...

    def __pos__(self) -> int: ...

    def __eq__(self, x) -> bool: ...

    def __ne__(self, x) -> bool: ...

    def __lt__(self, x) -> bool: ...

    def __le__(self, x) -> bool: ...

    def __gt__(self, x) -> bool: ...

    def __ge__(self, x) -> bool: ...


class Number:
    """Integral adds a conversion to int and the bit-string operations."""
    # Integers are their own numerators.
    numerator = ...  #type: int

    # Integers have a denominator of 1.
    denominator = ...  #type: int

    __slots__ = ...  # type: Tuple[str]

    def __init__(self, n: Union[float, int]) -> Number: ...

    def __add__(self, x: Union[Number, float, int]) -> Union[Number, float, int]: ...

    def __sub__(self, x): ...

    def __mul__(self, x): ...

    def __floordiv__(self, x): ...

    def __truediv__(self, x): ...

    def __mod__(self, x) -> int: ...

    def __divmod__(self, x): ...

    def __radd__(self, x) -> int: ...

    def __rsub__(self, x) -> int: ...

    def __rmul__(self, x) -> int: ...

    def __rfloordiv__(self, x) -> int: ...

    def __rtruediv__(self, x) -> float: ...

    def __rmod__(self, x) -> int: ...

    def __rdivmod__(self, x): ...

    def __int__(self):
        """int(self)"""

    # Concrete implementations of Rational and Real abstract methods.
    def __float__(self) -> float:
        """float(self) == float(int(self))"""

    def __bool__(self) -> bool:
        """bool(self)"""

    def __str__(self) -> str: ...

    def __index__(self) -> int:
        """Called whenever an index is needed, such as in slicing"""

    def __pow__(self, exponent, modulus):
        """self ** exponent % modulus, but maybe faster.

        Accept the modulus argument if you want to support the
        3-argument version of pow(). Raise a TypeError if exponent < 0
        or any argument isn't Integral. Otherwise, just implement the
        2-argument version described in Complex.
        """

    def __lshift__(self, other):
        """self << other"""

    def __rlshift__(self, other):
        """other << self"""

    def __rshift__(self, other):
        """self >> other"""

    def __rrshift__(self, other):
        """other >> self"""

    def __and__(self, other):
        """self & other"""

    def __rand__(self, other):
        """other & self"""

    def __xor__(self, other):
        """self ^ other"""

    def __rxor__(self, other):
        """other ^ self"""

    def __or__(self, other):
        """self | other"""

    def __ror__(self, other):
        """other | self"""

    def __invert__(self):
        """~self"""


class Text(str):
    def __init__(self, text: str = ...) -> None: ...

    def __repr__(self) -> str: ...

    def __str__(self) -> str: ...


class URL(Text):
    def __init__(self, url: str = ...) -> None: ...

    def __repr__(self) -> str: ...

    def __str__(self) -> str: ...
