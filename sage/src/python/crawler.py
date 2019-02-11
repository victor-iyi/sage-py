"""Crawler utility for parsing https://schema.org.

   @author
     Victor I. Afolabi
     Artificial Intelligence & Software Engineer.
     Email: javafolabi@gmail.com | victor.afolabi@zephyrtel.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: crawler.py
     Created on 07 February, 2019 @ 12:56.

   @license
     Apache 2.0 License
     Copyright (c) 2019. Victor I. Afolabi. All rights reserved.
"""

from sage.core import Log, get_properties

if __name__ == '__main__':
    properties = get_properties('Book', with_base=True)
    Log.debug(properties)
