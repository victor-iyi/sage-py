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
    'Base', 'Mode'
]


################################################################################################
# +--------------------------------------------------------------------------------------------+
# | Run mode: Tran, test, validation.
# +--------------------------------------------------------------------------------------------+
################################################################################################
class Mode:
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
class Base(object, metaclass=ABCMeta):
    def __init__(self, *args, **kwargs):
        # Verbosity level: 0 or 1.
        self._verbose = kwargs.setdefault('verbose', 1)
        self._name = kwargs.setdefault('name', self.__class__.__name__)

    def __repr__(self):
        """Object representation of Sub-classes."""
        # cdef list args = self._get_args()
        cdef dict kwargs = self._get_kwargs()

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

    def __format__(self, format_spec):
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

    def _get_args(self):
        # names = ('data_dir', 'sub_dirs', 'results_dir')
        # return [getattr(self, f'_{name}') for name in names]
        return []

    def _get_kwargs(self):
        # names = ('verbose', 'version')
        # return [(name, getattr(self, f'_{name}')) for name in names]
        cdef str k
        return sorted([(k.lstrip('_'), getattr(self, f'{k}'))
                       for k in self.__dict__.keys()])

    @property
    def name(self):
        return self._name

    @property
    def verbose(self):
        return self._verbose
