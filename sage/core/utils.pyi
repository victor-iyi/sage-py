"""sage.core.utils - Consist of utility class for the `sage` API.

   @author
     Victor I. Afolabi
     Artificial Intelligence & Software Engineer.
     Email: javafolabi@gmail.com | victor.afolabi@zephyrtel.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: utils.pyi
     Created on 28 January, 2019 @ 12:43 PM.

   @license
     Apache License 2.0
     Copyright (c) 2019. Victor I. Afolabi. All rights reserved.
"""

# Built-in libraries.
from abc import ABCMeta
from typing import (List, Iterable, Callable, Union, SupportsBytes,
                    SupportsInt, Optional, Generator, Any)

# Third-party libraries.
import numpy as np
from logging import Logger


################################################################################################
# +--------------------------------------------------------------------------------------------+
# | Downloader: For fetching resources from the internet & extracting compressed files.
# +--------------------------------------------------------------------------------------------+
################################################################################################
class Downloader(metaclass=ABCMeta):
    @staticmethod
    def maybe_download(url: str, download_dir: Optional[str] = None,
                       extract: Optional[bool] = False,
                       overwrite: Optional[bool] = False) -> str:
        ...

    @staticmethod
    def maybe_extract(file: str, extract_dir: Optional[str] = None,
                      overwrite: Optional[bool] = False) -> str: ...


################################################################################################
# +--------------------------------------------------------------------------------------------+
# | File: File utility class for working with directories & files.
# +--------------------------------------------------------------------------------------------+
################################################################################################
class File(metaclass=ABCMeta):
    @staticmethod
    def make_dirs(path: str, verbose: Optional[int] = 0) -> None:
        ...

    @staticmethod
    def get_dirs(path: str, exclude: Optional[Iterable[str]] = None,
                 optimize: Optional[bool] = False) -> Union[Generator[str], List[str]]: ...

    @staticmethod
    def get_files(path: str, exclude: Optional[Iterable[str]] = None,
                  optimize: Optional[bool] = False) -> Union[Generator[str], List[str]]: ...

    @staticmethod
    def listdir(path: str, exclude: Optional[Iterable[str]] = None,
                dirs_only: Optional[bool] = False, files_only: Optional[bool] = False,
                optimize: Optional[bool] = False) -> Union[Generator[str], List[str]]: ...


################################################################################################
# +--------------------------------------------------------------------------------------------+
# | Log: For logging and printing download progress, etc...
# +--------------------------------------------------------------------------------------------+
################################################################################################
class Log(metaclass=ABCMeta):
    # File logger configuration.
    _logger = ...  # type: Logger

    # Log Level.
    level = ...  # type: int

    @staticmethod
    def setLevel(level: int) -> None: ...

    @staticmethod
    def debug(*args: Any, sep: Optional[str] = " ", **kwargs: Any) -> None: ...

    @staticmethod
    def info(*args: Any, sep: Optional[str] = " ", **kwargs: Any) -> None: ...

    @staticmethod
    def warn(*args: Any, sep: Optional[str] = " ", **kwargs: Any) -> None: ...

    @staticmethod
    def error(*args: Any, sep: Optional[str] = " ", **kwargs: Any) -> None: ...

    @staticmethod
    def critical(*args: Any, sep: Optional[str] = " ", **kwargs: Any) -> None: ...

    @staticmethod
    def fatal(*args: Any, sep: Optional[str] = " ", code: Optional[int] = 1, **kwargs: Any) -> None: ...

    @staticmethod
    def log(*args: Any, verbose: Optional[int] = 1, sep: Optional[str] = " ", **kwargs: Any) -> None: ...

    @staticmethod
    def progress(count: int, max_count: int) -> None: ...

    @staticmethod
    def report_hook(block_no: int,
                    read_size: Union[SupportsBytes, SupportsInt],
                    file_size: Union[SupportsBytes, SupportsBytes]) -> None: ...


################################################################################################
# +--------------------------------------------------------------------------------------------+
# | Cache: For saving objects and converting numpy objects to pickle.
# +--------------------------------------------------------------------------------------------+
################################################################################################
class Cache(metaclass=ABCMeta):
    @staticmethod
    def cache(cache_path: str, fn: Callable,
              use_numpy: Optional[bool] = False, verbose: Optional[int] = 1,
              *args: Any, **kwargs: Any) -> Any: ...

    @staticmethod
    def cache_numpy(cache_path: str, fn: Callable, *args: Any, **kwargs: Any) -> Any: ...

    @staticmethod
    def convert_numpy2pickle(in_path: str, out_path: str) -> None: ...
