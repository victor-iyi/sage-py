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
from typing import Union, List, Iterable, Dict, Optional, Any


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
    __slots__ = ...  # type: Union[str, Iterable[str]]

    # Properties.
    verbose = ...  # type: int
    name = ...  # type: str

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

    def __repr__(self) -> str: ...

    def __str__(self) -> str: ...

    def __format__(self, format_spec: Optional[str]) -> str: ...

    def _log(self, *args: Any, level: Optional[str] = 'debug', **kwargs: Any) -> None: ...

    def _get_args(self) -> List[Any]: ...

    def _get_kwargs(self) -> Dict[str, Any]: ...
