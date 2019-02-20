"""Knowledge Graph.

   @author
     Victor I. Afolabi
     Artificial Intelligence & Software Engineer.
     Email: javafolabi@gmail.com | victor.afolabi@zephyrtel.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: graph.pyx.py
     Created on 28 January, 2019 @ 02:18 PM.

   @license
     Apache 2.0 License
     Copyright (c) 2019. Victor I. Afolabi. All rights reserved.
"""

import json
from typing import Union, List, Dict, AnyStr

from node cimport Scope
from node import Node, Scope

cdef class Graph:
    cdef readonly Scope _root

    def __cinit__(self, str path, **kwargs):
        self._root = Scope("ns")
        with open(path) as f:
            data = json.loads(f.read())
        self.load(self._root, data)

    def __repr__(self):
        return 'Graph(root={:!r})'.format(self._root)

    def __str__(self):
        return self._root.__str__()

    def __format__(self, str format_spec):
        if '!r' in format_spec:
            return self.__repr__()
        return self.__str__()

    cpdef void load(self, Scope base, data: Union[Dict, List, AnyStr]):
        cdef:
            str key
            cdef Scope scope
        if isinstance(data, (dict, list)):
            data_it = data.items() if isinstance(data, dict) else enumerate(data)
            for key, value in data_it:
                if isinstance(value, str):
                    base.add_node(Node(str(key), value))
                elif isinstance(value, (dict, list)):
                    scope = Scope(str(key))
                    self.load(scope, value)
                    base.add_scope(scope)
        else:
            raise TypeError('Expected one of List, Dict, Str. Got {}'
                            .format(type(data)))

    property root:
        def __get__(self):
            return self._root
