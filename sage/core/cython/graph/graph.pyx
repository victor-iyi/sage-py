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

cimport node
import node

cdef class Graph:
    def __cinit__(self, str path):
        self.root = node.newScope("ns")
        with open(path) as f:
            data = json.loads(f.read())
        self.load(self.root, data)

    def __repr__(self):
        return 'Graph(root={:!r})'.format(self.root)

    def __str__(self):
        return self.root.__str__()

    def __format__(self, str format_spec):
        if '!r' in format_spec:
            return self.__repr__()
        return self.__str__()

    cpdef void load(self, node.Scope base, data: Union[Dict, List, AnyStr]):
        cdef:
            str key
            cdef node.Scope scope
        if isinstance(data, (dict, list)):
            data_it = data.items() if isinstance(data, dict) else enumerate(data)
            for key, value in data_it:
                if isinstance(value, str):
                    base.add_node(node.newNode(str(key), value))
                elif isinstance(value, (dict, list)):
                    scope = node.newScope(key)
                    self.load(scope, value)
                    base.add_scope(scope)
        else:
            raise TypeError('Expected one of List, Dict, Str. Got {}'
                            .format(type(data)))

cpdef Graph newGraph(str path):
    return Graph(path)
