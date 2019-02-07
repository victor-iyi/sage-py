"""Handy utility classes.

   @author
     Victor I. Afolabi
     Artificial Intelligence & Software Engineer.
     Email: javafolabi@gmail.com | victor.afolabi@zephyrtel.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: utils.pyx
     Created on 28 January, 2019 @ 12:49 PM.

   @license
     Apache License 2.0
     Copyright (c) 2019. Victor I. Afolabi. All rights reserved.
"""

import logging
# Built-in libraries.
import os
import pickle
import sys
import tarfile
import urllib.request
import zipfile
from abc import ABCMeta
from logging.config import fileConfig
from typing import Callable, Iterable

# Third-party library.
import numpy as np

# Custom libraries.
from config import consts

# from nltk import word_tokenize

# Exported classes and functions.
__all__ = [
    'Downloader', 'Cache', 'File', 'Log',
]


################################################################################################
# +--------------------------------------------------------------------------------------------+
# | Downloader: For fetching resources from the internet & extracting compressed files.
# +--------------------------------------------------------------------------------------------+
################################################################################################
class Downloader(metaclass=ABCMeta):
    @staticmethod
    def maybe_download(str url, str download_dir=None, extract: bool = False, overwrite: bool = False):
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

        # Filename for saving the file downloaded from the internet.
        # Use the filename from the URL and add it to the download_dir.
        download_dir = download_dir or "downloads/"
        filename = os.path.join(download_dir, os.path.basename(url))

        # Check if the file already exists.
        # If it exists then we assume it has also been extracted,
        # otherwise we need to download and extract it now.
        if not os.path.exists(filename) or overwrite:
            # Check if the download directory exists, otherwise create it.
            if not os.path.exists(download_dir):
                os.makedirs(download_dir)

            # Download the file from the internet.
            filename, _ = urllib.request.urlretrieve(
                url=url, filename=filename,
                reporthook=Log.report_hook
            )

            Log.info("\nDownload finished.")

            return (Downloader.maybe_extract(file=filename,
                                             extract_dir=download_dir,
                                             overwrite=overwrite) if extract
                    else filename)

        Log.info("Data has apparently already been downloaded and unpacked.")
        return filename

    @staticmethod
    def maybe_extract(str file, str extract_dir=None, overwrite: bool = False):
        # Ensure the file exists.
        if not os.path.isfile(file):
            raise FileNotFoundError('"{}" not found!'.format(file))

        # Retrieve extracted directory.
        extract_dir = extract_dir or os.path.dirname(file)
        extract_dir = os.path.join(extract_dir, os.path.basename(file))

        # Don't extract if it's already been extracted.
        if os.path.isdir(extract_dir) and not overwrite:
            Log.warn('Already extracted to "{}"'.format(extract_dir))
            return extract_dir

        # Create extract directory if it doesn't exist.
        if not os.path.isdir(extract_dir):
            os.makedirs(extract_dir)

        # Read mode.
        cdef str mode = "r"

        if zipfile.is_zipfile(file):
            Extractor = zipfile.ZipFile
        elif tarfile.is_tarfile(file):
            # Change to tarball extractor.
            Extractor = tarfile.open

            # Update mode for a gzipped file.
            if file.endswith('gz'):
                mode = "r:gz"
        else:
            # Unrecognized compressed file.
            raise ValueError('{} must a zipped or tarball file'.format(file))

        with Extractor(file, mode=mode) as ex:
            ex.extractall(extract_dir)

        # Display & return extracted directory.
        Log.info('Successfully extracted to {}'.format(extract_dir))
        return extract_dir


################################################################################################
# +--------------------------------------------------------------------------------------------+
# | File: File utility class for working with directories & files.
# +--------------------------------------------------------------------------------------------+
################################################################################################
class File(metaclass=ABCMeta):
    @staticmethod
    def make_dirs(str path, int verbose=0):
        """Create Directory if it doesn't exist.

        Args:
            path (str): Directory/directories to be created.
            verbose (bool, optional): Defaults to 0. 0 turns of logging,
                while 1 gives feedback on creation of director(y|ies).

        Example:
            ```python
            >>> path = os.path.join("path/to", "be/created/")
            >>> File.make_dirs(path, verbose=1)
            INFO  |  "path/to/be/created/" has been created.
            ```
        """

        # if director(y|ies) doesn't already exist.
        if not os.path.isdir(path):
            # Create director(y|ies).
            os.makedirs(path)

            if verbose:
                # Feedback based on verbosity.
                Log.info('"{}" has been created.'.format(path))

    @staticmethod
    def get_dirs(str path, exclude: Iterable[str] = None, optimize: bool = False):
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
        # Return only list of directories.
        return File.listdir(path, exclude=exclude, dirs_only=True, optimize=optimize)

    @staticmethod
    def get_files(path: str, exclude: Iterable[str] = None, optimize: bool = False):
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
        # Return only list of directories.
        return File.listdir(path, exclude=exclude, files_only=True, optimize=optimize)

    @staticmethod
    def listdir(path: str, exclude: Iterable[str] = None,
                dirs_only: bool = False, files_only: bool = False,
                optimize: bool = False):
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
        if not os.path.isdir(path):
            raise FileNotFoundError('"{}" was not found!'.format(path))

        # Get all files in `path`.
        if files_only:
            paths = (os.path.join(path, p) for p in os.listdir(path)
                     if os.path.isfile(os.path.join(path, p)))
        else:
            # Get all directories in `path`.
            if dirs_only:
                paths = (os.path.join(path, p) for p in os.listdir(path)
                         if os.path.isdir(os.path.join(path, p)))
            else:
                # Get both files and directories.
                paths = (os.path.join(path, p) for p in os.listdir(path))

        # Exclude paths from results.
        if exclude is not None:
            # Remove excluded paths.
            paths = filter(lambda p: os.path.basename(p) not in exclude, paths)

        # Convert generator expression to list.
        if not optimize:
            paths = list(paths)

        return paths


################################################################################################
# +--------------------------------------------------------------------------------------------+
# | Log: For logging and printing download progress, etc...
# +--------------------------------------------------------------------------------------------+
################################################################################################
class Log(metaclass=ABCMeta):
    # File logger configuration.
    fileConfig(consts.LOGGER.ROOT)
    _logger = logging.getLogger()

    # Log Level.
    level = _logger.level

    @staticmethod
    def setLevel(level: int):
        Log._logger.setLevel(level=level)

    @staticmethod
    def getLogger():
        return Log._logger

    @staticmethod
    def debug(*args, **kwargs):
        Log._logger.debug(*args, **kwargs)

    @staticmethod
    def info(*args, **kwargs):
        Log._logger.info(*args, **kwargs)

    @staticmethod
    def warn(*args, **kwargs):
        Log._logger.warning(*args, **kwargs)

    @staticmethod
    def error(*args, **kwargs):
        Log._logger.error(*args, **kwargs)

    @staticmethod
    def critical(*args, **kwargs):
        Log._logger.critical(*args, **kwargs)

    @staticmethod
    def exception(*args, **kwargs):
        Log._logger.exception(*args, **kwargs)

    @staticmethod
    def fatal(*args, **kwargs):
        cdef int code = kwargs.pop('code', 1)
        Log._logger.fatal(*args, **kwargs)
        exit(code)

    @staticmethod
    def log(*args, **kwargs):
        """Logging method avatar based on verbosity.

        Args:
            *args

        Keyword Args:
            verbose (int, optional): Defaults to 1.
            level (int, optional): Defaults to ``Log.level``.
            sep (char, optional): Defaults to " ".

        Returns:
            None
        """

        # No logging if verbose is not 'on'.
        if not kwargs.pop('verbose', 1):
            return

        Log._logger.log(Log.level, *args, **kwargs)

    @staticmethod
    def progress(int count, int max_count):
        """Prints task progress *(in %)*.

        Args:
            count {int}: Current progress so far.
            max_count {int}: Total progress length.
        """

        # Percentage completion.
        cdef float pct_complete = count / max_count

        # Status-message. Note the \r which means the line should
        # overwrite itself.
        cdef str msg = "\r- Progress: {0:.02%}".format(pct_complete)

        # Print it.
        sys.stdout.write(msg)
        sys.stdout.flush()

    @staticmethod
    def report_hook(block_no: int, read_size: bytes, file_size: bytes):
        """Calculates download progress of downloaded files.

        Args:
            block_no {int}: Current download state.
            read_size {bytes}: Current downloaded size.
            file_size {bytes}: Total file size.

        Returns:
            None.
        """
        # Calculates download progress given the block number, a read size,
        #  and the total file size of the URL target.
        pct_complete = float(block_no * read_size) / float(file_size)

        msg = "\r\t -Download progress {:.02%}".format(pct_complete)
        # Log.log(msg)
        sys.stdout.stdwrite(msg)
        sys.stdout.flush()


################################################################################################
# +--------------------------------------------------------------------------------------------+
# | Cache: For saving objects and converting numpy objects to pickle.
# +--------------------------------------------------------------------------------------------+
################################################################################################
class Cache(metaclass=ABCMeta):
    @staticmethod
    def cache(cache_path: str, fn: Callable, use_numpy: bool = False, *args, **kwargs):
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
        # Extract keyword arguments.
        verbose = kwargs.pop('verbose', 1)

        # If the cache-file exists.
        if os.path.exists(cache_path):
            if use_numpy:
                obj = np.load(cache_path)
            else:
                # Load the cached data from the file.
                with open(cache_path, mode='rb') as file:
                    obj = pickle.load(file)

            if verbose:
                Log.info(f"- Data loaded from cache-file: {os.path.relpath(cache_path)}")
        else:
            # The cache-file does not exist.

            # Call the function / class-init with the supplied arguments.
            obj = fn(*args, **kwargs)

            # Create cache-directory if it doesn't exist.
            if not os.path.isdir(os.path.dirname(cache_path)):
                os.makedirs(os.path.dirname(cache_path))

            # Save the data to a cache-file.
            if use_numpy:
                if isinstance(obj, np.ndarray):
                    np.save(cache_path, obj)
                else:
                    raise TypeError(f"Expected a NumPy object, got {type(obj)}")
            else:
                with open(cache_path, mode='wb') as file:
                    pickle.dump(obj, file)

            if verbose:
                Log.info(f"- Data saved to cache-file: {os.path.relpath(cache_path)}")

        return obj

    @staticmethod
    def cache_numpy(cache_path: str, fn: Callable, *args, **kwargs):
        return Cache.cache_numpy(cache_path=cache_path,
                                 fn=fn, use_numpy=True,
                                 *args, **kwargs)

    @staticmethod
    def convert_numpy2pickle(in_path: str, out_path: str):
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

        # Load the data using numpy.
        data = np.load(in_path)

        # Save the data using pickle.
        with open(out_path, mode='wb') as file:
            pickle.dump(data, file)
