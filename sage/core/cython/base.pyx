"""Base class for Sage.

   @author
     Victor I. Afolabi
     Artificial Intelligence & Software Engineer.
     Email: javafolabi@gmail.com | victor.afolabi@zephyrtel.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: base.pyx
     Created on 28 January, 2018 @ 12:38 PM.

   @license
     Apache License 2.0
     Copyright (c) 2018. Victor I. Afolabi. All rights reserved.
"""

# Built-in libraries.
from abc import ABCMeta
from typing import Any

# Classes in this file.
__all__ = [
    'Base', 'Mode', 'Attr',
]


################################################################################################
# +--------------------------------------------------------------------------------------------+
# | Run mode: Tran, test, validation.
# +--------------------------------------------------------------------------------------------+
################################################################################################
class Mode(metaclass=ABCMeta):
    TEST = 'test'
    TRAIN = 'train'
    PREDICT = 'predict'
    VALIDATE = 'validation'
    INFERENCE = 'inference'


################################################################################################
# +--------------------------------------------------------------------------------------------+
# | Base: Base class for all classes.
# +--------------------------------------------------------------------------------------------+
################################################################################################
# noinspection PyUnusedLocal
cdef class Base:
    cdef:
        readonly str _name
        readonly int _verbose
    def __init__(self, verbose=1, name=None):
        # Verbosity level: 0 or 1.
        self._verbose = verbose
        self._name = name or self.__class__.__name__

    def __repr__(self):
        """Object representation of Sub-classes."""
        # cdef list args = self._get_args()
        cdef list kwargs = self._get_kwargs()

        # Format arguments.
        # fmt = ", ".join(map(repr, args))
        cdef str k, fmt = ""

        # Format keyword arguments.
        for k, v in kwargs:
            if k in ('filename', 'ids'):  # Don't include these in print-out.
                continue
            fmt += ", {}={!r}".format(k, v)

        # Object representation of Class.
        return '{}({})'.format(self.__class__.__name__, fmt.lstrip(', '))

    def __str__(self):
        """String representation of Sub-classes."""
        return "{}()".format(self.__class__.__name__,
                             ", ".join(map(str, self._get_args())))

    def __format__(self, str format_spec):
        if format_spec == "!r":
            return self.__repr__()
        return self.__str__()

    def _log(self, *args: Any, str level='log', **kwargs: Any):
        """Logging method helper based on verbosity."""
        # No logging if verbose is not 'on'.
        if not kwargs.pop('verbose', self._verbose):
            return

        # Validate log levels.
        cdef tuple _levels = ('log', 'debug', 'info', 'warn',
                              'error', 'critical', 'exception')
        if level.lower() not in _levels:
            raise ValueError("`level` must be one of {}".format(_levels))

        # Call the appropriate log level, eg: Log.info(*args, **kwargs)
        eval(f'Log.{level.lower()}(*args, **kwargs)')

    cpdef list _get_args(self):
        # names = ('data_dir', 'sub_dirs', 'results_dir')
        # return [getattr(self, f'_{name}') for name in names]
        return []

    cpdef list _get_kwargs(self):
        # names = ('verbose', 'version')
        # return [(name, getattr(self, f'_{name}')) for name in names]
        cdef str k
        return sorted([(k.lstrip('_'), getattr(self, f'{k}'))
                       for k in self.__dict__.keys()])

    property name:
        def __get__(self):
            return self._name
    property verbose:
        def __get__(self):
            return self._verbose


class Attr(dict):
    """Get attributes.

    Examples:
        ```python
        >>> d = Attr({'foo':3})
        >>> d['foo']
        3
        >>> d.foo
        3
        >>> d.bar
        Traceback (most recent call last):
        ...
        AttributeError: 'Attr' object has no attribute 'bar'

        Works recursively

        >>> d = Attr({'foo':3, 'bar':{'x':1, 'y':2}})
        >>> isinstance(d.bar, dict)
        True
        >>> d.bar.x
        1

        Bullet-proof

        >>> Attr({})
        {}
        >>> Attr(d={})
        {}
        >>> Attr(None)
        {}
        >>> d = {'a': 1}
        >>> Attr(**d)
        {'a': 1}

        Set attributes

        >>> d = Attr()
        >>> d.foo = 3
        >>> d.foo
        3
        >>> d.bar = {'prop': 'value'}
        >>> d.bar.prop
        'value'
        >>> d
        {'foo': 3, 'bar': {'prop': 'value'}}
        >>> d.bar.prop = 'newer'
        >>> d.bar.prop
        'newer'


        Values extraction

        >>> d = Attr({'foo':0, 'bar':[{'x':1, 'y':2}, {'x':3, 'y':4}]})
        >>> isinstance(d.bar, list)
        True
        >>> from operator import attrgetter
        >>> map(attrgetter('x'), d.bar)
        [1, 3]
        >>> map(attrgetter('y'), d.bar)
        [2, 4]
        >>> d = Attr()
        >>> d.keys()
        []
        >>> d = Attr(foo=3, bar=dict(x=1, y=2))
        >>> d.foo
        3
        >>> d.bar.x
        1

        Still like a dict though

        >>> o = Attr({'clean':True})
        >>> o.items()
        [('clean', True)]

        And like a class

        >>> class Flower(Attr):
        ...     power = 1
        ...
        >>> f = Flower()
        >>> f.power
        1
        >>> f = Flower({'height': 12})
        >>> f.height
        12
        >>> f['power']
        1
        >>> sorted(f.keys())
        ['height', 'power']
        ```
    """

    def __init__(self, d=None, **kwargs):
        if d is None:
            d = {}
        if kwargs:
            d.update(**kwargs)
        for k, v in d.items():
            setattr(self, k, v)
        # Class attributes
        for k in self.__class__.__dict__.keys():
            if not (k.startswith('__') and k.endswith('__')):
                setattr(self, k, getattr(self, k))

    def __setattr__(self, name, value):
        if isinstance(value, (list, tuple)):
            value = [self.__class__(x)
                     if isinstance(x, dict) else x for x in value]
        elif isinstance(value, dict) and not isinstance(value, self.__class__):
            value = self.__class__(value)
        super(Attr, self).__setattr__(name, value)
        super(Attr, self).__setitem__(name, value)

    __setitem__ = __setattr__