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
     MIT License
     Copyright (c) 2019. Victor I. Afolabi. All rights reserved.
"""

# Built-in libraries.
from abc import ABCMeta, abstractmethod
from typing import (
    Union, Tuple, List, Iterable,
    Dict, Optional, Any, TypeVar
)

# Third-party libraries.
import numpy as np

# Type alias.
_Tensor = TypeVar('_Tensor')


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


class ModelBase(Base, metaclass=ABCMeta):
    name = ...  # type: str
    mode = ...  # type: str
    cache = ...  # type: bool
    cache_dir = ...  # type: str

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...

    @abstractmethod
    def call(self, *args: Any, **kwargs: Any) -> Any: ...

    @staticmethod
    def int_shape(x: _Tensor) -> Tuple[int]: ...
