"""
   @author
     Victor I. Afolabi
     Artificial Intelligence & Software Engineer.
     Email: javafolabi@gmail.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: __init__.py
     Package: config
     Created on 28 January, 2018 @ 01:03 PM.

   @license
     MIT License
     Copyright (c) 2018. Victor I. Afolabi. All rights reserved.
"""

# File system.
from config.consts import FS, LOGGER, SETUP

# Configuration utils.
from config.config import Config

__all__ = [
    # Configuration utils.
    'Config',

    # File system configurations.
    'FS', 'SETUP', 'LOGGER',
]
