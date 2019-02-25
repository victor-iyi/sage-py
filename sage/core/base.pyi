"""Base module for Python objects.

   @author
     Victor I. Afolabi
     Artificial Intelligence & Software Engineer.
     Email: javafolabi@gmail.com | victor.afolabi@zephyrtel.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: base.pyi
     Created on 28 January, 2019 @ 12:42.

   @license
     Apache License 2.0
     Copyright (c) 2019. Victor I. Afolabi. All rights reserved.
"""

# Built-in libraries.
from abc import ABCMeta
from typing import Union, List, Iterable, Dict, Optional, Any, Tuple


class Mode(metaclass=ABCMeta):
    __class__ = ...  # type: type
    __module__ = ...  # type: str
    __doc__ = ...  # type: Optional[str]
    __dict__ = ...  # type: Dict[str, Any]
    __slots__ = ...  # type: Union[str, Iterable[str]]

    VAL = ...  # type: str
    TEST = ...  # type: str
    TRAIN = ...  # type: str
    PREDICT = ...  # type: str
    VALIDATE = ...  # type: str


class Base(object, metaclass=ABCMeta):
    """Base class for objects.

    Methods:
        def __init__(self, *args: Any, **kwargs: Any) -> None:
            # Object initialization.

        def __repr__(self) -> str:
            # Object representation of class.

        def __str__(self) -> str:
            # String representation of class.

        def __format__(self, format_spec: Optional[str]) -> str:
            # For string formatting.

        def _log(self, *args: Any, level: Optional[str] = 'debug', **kwargs: Any) -> None:
            # Handy logger method for logging & debugging.

        def _get_args(self) -> List[Any]:
            # Get class arguments.

        def _get_kwargs(self) -> Dict[str, Any]:
            # Get class keyword arguments.

    Attributes:
        verbose (int, optional): Defaults to 1.
        name (str, optional): Class alias (for saving & collecting metadata).
    """
    __class__ = ...  # type: type
    __module__ = ...  # type: str
    __doc__ = ...  # type: Optional[str]
    __dict__ = ...  # type: Dict[str, Any]
    __slots__ = ...  # type: Union[str, Tuple[str]]

    # Properties.
    verbose = ...  # type: int
    name = ...  # type: str

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

    def __repr__(self) -> str: ...

    def __str__(self) -> str: ...

    def __format__(self, format_spec: Optional[str]) -> str: ...

    def _log(self, *args: Any,
             level: Optional[str] = 'debug', **kwargs: Any) -> None: ...

    def _get_args(self) -> List[Any]: ...

    def _get_kwargs(self) -> Dict[str, Any]: ...


##################################################################################################
# +----------------------------------------------------------------------------------------------+
# | Attributes getter.
# +----------------------------------------------------------------------------------------------+
##################################################################################################
# noinspection PyUnresolvedReferences
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

    def __init__(self, d: dict = None, **kwargs: Any) -> None: ...

    def __setattr__(self, name: str, value: Any) -> None: ...

    __setitem__ = __setattr__
