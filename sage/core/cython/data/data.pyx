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
    """Dataset - Base class for dataset objects.

    Methods:
        def maybe_download_and_extract(self): ...
        def get(self, index): ...
        def to_tfData(self): ... [May be a decorator]
        def load(): ... [Returns a tf.Data or NumPy array based on parameters]

    Attributes:
        path (str): Path where dataset is saved.
        cache (bool):
        cache_dir (str):
    """
    def __init__(self, str path, **kwargs):
        self.path = path
        self.cache = kwargs.get('cache', False)
        self.cache_dir = kwargs.get('cache_dir', None)

    cpdef int get(self, int index):
        return index

    cpdef void maybe_download_and_extract(self):
        pass
