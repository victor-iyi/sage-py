"""File system configuration module.

   @author
     Victor I. Afolabi
     Artificial Intelligence & Software Engineer.
     Email: javafolabi@gmail.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: fs.py
     Created on 26 January, 2018 @ 01:11 PM.

   @license
     Apache License 2.0
     Copyright (c) 2018. Victor I. Afolabi. All rights reserved.
"""

# Built-in libraries.
import os.path
from abc import ABCMeta

# Custom libraries.
from config.config import Config

# Exported configurations.
__all__ = [
    'FS', 'LOGGER', 'SETUP',
]


################################################################################################
# +--------------------------------------------------------------------------------------------+
# | FS: File System.
# +--------------------------------------------------------------------------------------------+
################################################################################################
class FS(metaclass=ABCMeta):
    # Project name & absolute directory.
    PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))
    APP_NAME = os.path.basename(PROJECT_DIR)

    # Directory to save stuffs.
    CACHE_DIR = os.path.join(PROJECT_DIR, 'cache')
    CONFIG_DIR = os.path.join(PROJECT_DIR, 'config')

    # Libraries & Include folders.
    LIB_DIR = os.path.join(PROJECT_DIR, 'avatar')
    VENDOR_DIR = os.path.join(LIB_DIR, 'vendor')
    INCLUDE_DIR = os.path.join(PROJECT_DIR, 'include')


################################################################################################
# +--------------------------------------------------------------------------------------------+
# | Setup configuration constants.
# +--------------------------------------------------------------------------------------------+
################################################################################################
class SETUP(metaclass=ABCMeta):
    # Global setup configuration.
    __global = Config.from_cfg(os.path.join(FS.PROJECT_DIR,
                                            "config/setup/global.cfg"))
    # Build mode/type.
    MODE = __global['config']['MODE']


################################################################################################
# +--------------------------------------------------------------------------------------------+
# | Logger: Logging configuration paths.
# +--------------------------------------------------------------------------------------------+
################################################################################################
class LOGGER(metaclass=ABCMeta):
    # Root Logger:
    ROOT = os.path.join(FS.PROJECT_DIR, 'config/logger', f'{SETUP.MODE}.cfg')

    # Another logger goes here: (and updated in helpers/utils.py)
