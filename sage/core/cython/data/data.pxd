"""Data processing pipeline.

   @author
     Victor I. Afolabi
     Artificial Intelligence Expert & Researcher.
     Email: javafolabi@gmail.com | victor.afolabi@zephyrtel.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: data.pxd
     Created on 02 March, 2019 @ 04:08 PM.

   @license
     Apache 2.0 License
     Copyright (c) 2019. Victor I. Afolabi. All rights reserved.
"""

from sage.core.cython.base cimport Base

cdef class Dataset(Base):
    cdef:
        public str path, cache_dir
        public bint cache


    cpdef int get(self, int index)
