"""
   @author
     Victor I. Afolabi
     Artificial Intelligence Expert & Researcher.
     Email: javafolabi@gmail.com | victor.afolabi@zephyrtel.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: graph.pyd
     Created on 20 February, 2019 @ 11:56.

   @license
     MIT License
     Copyright (c) 2019. Victor I. Afolabi. All rights reserved.
"""

from node cimport Scope

cdef class Graph:
    cdef readonly Scope _root

    cpdef void load(self, Scope base, data)
