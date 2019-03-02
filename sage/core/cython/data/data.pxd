"""
   @author
     Victor I. Afolabi
     Artificial Intelligence Expert & Researcher.
     Email: javafolabi@gmail.com | victor.afolabi@zephyrtel.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: data.py
     Created on 02 March, 2019 @ 16:08.

   @license
     MIT License
     Copyright (c) 2019. Victor I. Afolabi. All rights reserved.
"""

cdef class Node:
    cdef:
        public value
        readonly str key
        readonly bint is_scope
