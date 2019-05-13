"""Knowledge Graph high level classes.

   @author
     Victor I. Afolabi
     Artificial Intelligence Expert & Researcher.
     Email: javafolabi@gmail.com | victor.afolabi@zephyrtel.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: graph.pxd
     Created on 13 May, 2019 @ 08:27 PM.

   @license
     Apache 2.0 License
     Copyright (c) 2019. Victor I. Afolabi. All rights reserved.
"""
from sage.core.cython.base cimport Base

cdef class KnowledgeGraph(Base):
    cdef:
        public str label

    cpdef void add_triple(self, triples)
    cpdef void load(self, data)
