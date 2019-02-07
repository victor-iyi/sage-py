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
        """Download and extract the data if it doesn't already exist.

        Notes:
            Assumes the url is a zip or tar-ball file.

        Arguments:
            url {str} -- Internet URL for the tar-file to download.
                e.g: "http://nlp.stanford.edu/data/glove.6B.zip"

            download_dir {str} -- Directory to download files.
                e.g: "datasets/GloVe/" (default {'downloads'})

            extract {bool} -- If set to `True` compressed files are extracted automatically.
                (default {False})

            overwrite {bool} -- Force download even if the file already exists.
                (default {False})

        Returns:
            str: Filename if `extract==False`, otherwise `extract_dir` is returned.
        """

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
        """Create Directory if it doesn't exist.

        Args:
            path (str): Directory/directories to be created.
            verbose (bool, optional): Defaults to 0. 0 turns of logging,
                while 1 gives feedback on creation of director(y|ies).

        Example:
            ```python
            >>> import os.path
            >>> path = os.path.join("path/to", "be/created/")
            >>> File.make_dirs(path, verbose=1)
            INFO  |  "path/to/be/created/" has been created.
            ```
        """

    @staticmethod
    def get_dirs(path: str, exclude: Optional[Iterable[str]] = None,
                 optimize: Optional[bool] = False) -> Union[Generator[str], List[str]]:
        """Retrieve all directories in a given path.

        Args:
            path (str): Base directory of directories to retrieve.
            exclude (Iterable[str], optional): Defaults to None. List of paths to
                remove from results.
            optimize (bool, optional): Defaults to False. Return an generator object,
                to prevent loading all directories in memory, otherwise: return results
                as a normal list.

        Raises:
            FileNotFoundError: `path` was not found.

        Returns:
            Union[Generator[str], List[str]]: Generator expression if optimization is turned on,
                otherwise list of directories in given path.
        """

    @staticmethod
    def get_files(path: str, exclude: Optional[Iterable[str]] = None,
                  optimize: Optional[bool] = False) -> Union[Generator[str], List[str]]:
        """Retrieve all files in a given path.

        Args:
            path (str): Base directory of files to retrieve.
            exclude (Iterable[str], optional): Defaults to None. List of paths to
                remove from results.
            optimize (bool, optional): Defaults to False. Return an generator object,
                to prevent loading all directories in memory, otherwise: return results
                as a normal list.

        Raises:
            FileNotFoundError: `path` was not found.

        Returns:
            Union[Generator[str], List[str]]: Generator expression if optimization is turned on,
                otherwise list of files in given path.
        """

    @staticmethod
    def listdir(path: str, exclude: Optional[Iterable[str]] = None,
                dirs_only: Optional[bool] = False, files_only: Optional[bool] = False,
                optimize: Optional[bool] = False) -> Union[Generator[str], List[str]]:
        """Retrieve files/directories in a given path.

        Args:
            path (str): Base directory of path to retrieve.
            exclude (Iterable[str], optional): Defaults to None. List of paths to
                remove from results.
            dirs_only (bool, optional): Defaults to False. Return only directories in `path`.
            files_only (bool, optional): Defaults to False. Return only files in `path`.
            optimize (bool, optional): Defaults to False. Return an generator object,
                to prevent loading all directories in memory, otherwise: return results
                as a normal list.

        Raises:
            FileNotFoundError: `path` was not found.

        Returns:
            Union[Generator[str], List[str]]: Generator expression if optimization is turned on,
                otherwise list of directories in given path.
        """


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
    def getLogger() -> Logger: ...

    @staticmethod
    def debug(*args: Any, **kwargs: Any) -> None: ...

    @staticmethod
    def info(*args: Any, **kwargs: Any) -> None: ...

    @staticmethod
    def warn(*args: Any, **kwargs: Any) -> None: ...

    @staticmethod
    def error(*args: Any, **kwargs: Any) -> None: ...

    @staticmethod
    def critical(*args: Any, **kwargs: Any) -> None: ...

    @staticmethod
    def exception(*args: Any, **kwargs: Any) -> None: ...

    @staticmethod
    def fatal(*args: Any, code: Optional[int] = 1, **kwargs: Any) -> None: ...

    @staticmethod
    def log(*args: Any, verbose: Optional[int] = 1, **kwargs: Any) -> None:
        """Logging method avatar based on verbosity.

        Args:
            *args (Any): Arguments to be printed.
            verbose (int, optional): Defaults to 1. Verbosity level.

        Keyword Args:
            level (int, optional): Defaults to ``Log.level``.
            sep (char, optional): Defaults to " ".

        Returns:
            None
        """

    @staticmethod
    def progress(count: int, max_count: int) -> None:
        """Prints task progress *(in %)*.

        Args:
            count {int}: Current progress so far.
            max_count {int}: Total progress length.
        """

    @staticmethod
    def report_hook(block_no: int,
                    read_size: Union[SupportsBytes, SupportsInt],
                    file_size: Union[SupportsBytes, SupportsBytes]) -> None:
        """Calculates download progress of downloaded files.

        Args:
            block_no {int}: Current download state.
            read_size {bytes}: Current downloaded size.
            file_size {bytes}: Total file size.

        Returns:
            None.
        """


################################################################################################
# +--------------------------------------------------------------------------------------------+
# | Cache: For saving objects and converting numpy objects to pickle.
# +--------------------------------------------------------------------------------------------+
################################################################################################
class Cache(metaclass=ABCMeta):
    @staticmethod
    def cache(cache_path: str, fn: Callable,
              use_numpy: Optional[bool] = False, verbose: Optional[int] = 1,
              *args: Any, **kwargs: Any) -> Any:
        """Cache-wrapper for a function or class.

        Notes:
            If the cache-file exists then the data is reloaded and
            returned, otherwise the function is called and the result
            is saved to cache. The fn-argument can also be a class
            instead, in which case an object-instance is created and
            saved to the cache-file.

        Args:
            cache_path (str): File-path for the cache-file.
            fn (Callable): Function or class to be called.
            use_numpy (bool, optional): Defaults to False. Save object as
                a numpy object.
            verbose (int, optional): Defaults to 1. Verbosity level.
            args (Any): Arguments to the function or class-init.
            kwargs(Dict[str, Any]): Keyword arguments to the function
                    or class-init.

        Raises:
            TypeError: Expected a NumPy object, got `type(obj)`.

        See Also:
            `Cache.cache_numpy(...)`

        Returns:
            Any: The result of calling the function or creating the object-instance.
        """

    @staticmethod
    def cache_numpy(cache_path: str, fn: Callable, *args: Any, **kwargs: Any) -> Any: ...

    @staticmethod
    def convert_numpy2pickle(in_path: str, out_path: str) -> None:
        """Convert a numpy-file to pickle-file.

        Notes:
            The first version of the cache-function used numpy for
            saving the data. Instead of re-calculating all the data,
            you can just convert the cache-file using this function.

        Args:
            in_path (str): Input file in numpy-format written using numpy.save().
            out_path (str): Output file written as a pickle-file.

        Returns:
            Nothing.
        """
