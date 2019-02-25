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
     File: dtype.pyx
     Created on 25 February, 2019 @ 09:53 PM.

   @license
     MIT License
     Copyright (c) 2019. Victor I. Afolabi. All rights reserved.
"""
import re

# __all__ = ['DataType', 'Boolean', 'Number', 'Text', 'URL', 'Time', 'Date', 'DateTime']

cdef class DataType(object):
    def __init__(self, o: object = ...) -> None:
        self.__o = o

    def __repr__(self):
        return '{}()'.format(self.__class__.__name__)

    def __format__(self, format_specs):
        if format_specs == '!r':
            return self.__repr__()
        return self.__str__()

cdef class Boolean(int):
    def __init__(self, b: bool = None):
        self.__b = b

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, self.__b)

    def __str__(self):
        return self.__b

    def __neg__(self) -> int: ...

    def __pos__(self) -> int: ...

    def __eq__(self, x) -> bool:
        return self.__b == x

    def __ne__(self, x) -> bool:
        return self.__b != x

    def __lt__(self, x) -> bool:
        return self.__b < x

    def __le__(self, x) -> bool:
        return self.__b <= x

    def __gt__(self, x) -> bool:
        return self.__b > x

    def __ge__(self, x) -> bool:
        return self.__b >= x

cdef class Number:
    """Integral adds a conversion to int and the bit-string operations."""

    __slots__ = ('__n',)

    def __init__(self, n):
        self.__n = n

    def __add__(self, x):
        return self.__n + x

    def __sub__(self, x):
        return self.__n - x

    def __mul__(self, x):
        return self.__n * x

    def __floordiv__(self, x):
        return self.__n.__floordiv__(x)

    def __truediv__(self, x):
        return self.__n.__truediv__(x)

    def __mod__(self, x) -> int:
        return self.__n % x

    def __divmod__(self, x):
        return self.__n.__divmod__(x)

    def __radd__(self, x) -> int:
        return self.__n.__radd__(x)

    def __rsub__(self, x) -> int:
        return self.__rsub__(x)

    def __rmul__(self, x) -> int:
        return self.__n.__rmul__(x)

    def __rfloordiv__(self, x) -> int:
        return self.__n.__rfloordiv__(x)

    def __rtruediv__(self, x) -> float:
        return self.__n.__rtruediv__(x)

    def __rmod__(self, x) -> int:
        return self.__n.__rmod__(x)

    def __rdivmod__(self, x):
        return self.__n.__rdivmod__(x)

    def __int__(self):
        """int(self)"""
        return int(self.__n)

    # Concrete implementations of Rational and Real abstract methods.
    def __float__(self):
        """float(self) == float(int(self))"""
        return float(self.__n)

    def __bool__(self):
        """bool(self)"""
        return bool(self.__n)

    def __str__(self):
        return str(self.__n)

    def __index__(self):
        """Called whenever an index is needed, such as in slicing"""
        return int(self.__n)

    def __pow__(self, exponent, modulus):
        """self ** exponent % modulus, but maybe faster.

        Accept the modulus argument if you want to support the
        3-argument version of pow(). Raise a TypeError if exponent < 0
        or any argument isn't Integral. Otherwise, just implement the
        2-argument version described in Complex.
        """
        return self.__n ** exponent % modulus

    def __lshift__(self, other):
        """self << other"""
        return self.__n << other

    def __rlshift__(self, other):
        """other << self"""
        return other << self.__n

    def __rshift__(self, other):
        """self >> other"""
        return self.__n >> other

    def __rrshift__(self, other):
        """other >> self"""
        return other >> self.__n

    def __and__(self, other):
        """self & other"""
        return self.__n & other

    def __rand__(self, other):
        """other & self"""
        return other & self.__n

    def __xor__(self, other):
        """self ^ other"""
        return self.__n ^ other

    def __rxor__(self, other):
        """other ^ self"""
        return other ^ self.__n

    def __or__(self, other):
        """self | other"""
        return self.__n | other

    def __ror__(self, other):
        """other | self"""
        return other | self.__n

    def __invert__(self):
        """~self"""
        return ~self.__n

    @property
    def numerator(self):
        """Integers are their own numerators."""
        return +self.__n

    @property
    def denominator(self):
        """Integers have a denominator of 1."""
        return 1

cdef class Text(str):
    def __init__(self, text=None):
        self.__text = text

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__,
                               self.__text)

    def __str__(self):
        return self.__text

cdef class URL(Text):
    def __init__(self, url: str = None):
        # URL match pattern.
        __pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
        match = re.match(__pattern, url)

        if not match:
            raise ValueError('Invalid URL {}'.format(url))

        self.__url = match.group()

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__,
                               self.__url)

    def __str__(self):
        return self.__url
