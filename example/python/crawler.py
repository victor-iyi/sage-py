"""Crawler utility for parsing https://schema.org.

   @author
     Victor I. Afolabi
     Artificial Intelligence & Software Engineer.
     Email: javafolabi@gmail.com | victor.afolabi@zephyrtel.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: crawler.py
     Created on 07 February, 2019 @ 12:56 PM.

   @license
     Apache 2.0 License
     Copyright (c) 2019. Victor I. Afolabi. All rights reserved.
"""

from sage.core.utils import Log
from sage.core.data import Dataset


if __name__ == '__main__':
    d = Dataset("path/to/file")
    Log.debug(d.get(4))
    # properties = get_properties('Person', compact=True)
    # Log.pretty(properties)
