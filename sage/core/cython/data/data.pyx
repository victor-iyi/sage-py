"""Data processing pipeline.

   @author
     Victor I. Afolabi
     Artificial Intelligence Expert & Researcher.
     Email: javafolabi@gmail.com | victor.afolabi@zephyrtel.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: data.pyx
     Created on 02 March, 2019 @ 03:52 PM.

   @license
     Apache 2.0 License
     Copyright (c) 2019. Victor I. Afolabi. All rights reserved.
"""

from sage.core.cython.base import Base

cdef class Dataset(Base):
    def __cinit__(self, str path):
        self.path = path

    def get(self, int index):
        return index
