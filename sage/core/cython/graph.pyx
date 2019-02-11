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
import uuid

from typing import Union, List, Dict, AnyStr, Any

# Combined type def for a Node & Scope.
ctypedef fused Vertex_t:
    str
    Node
    Scope

cdef class Node(object):
    cdef:
        # Vertex_t _value
        readonly str _key
        readonly bint _is_scope

    def __init__(self, key: str, value=None, **kwargs):
        self._key = key
        self._value = value
        self._is_scope = kwargs.get('is_scope', False)

    def __repr__(self):
        return 'Node({}, value={})'.format(self._key, self._value)

    def __str__(self):
        return '"{}" : "{}"'.format(self._key, self._value)

    def __format__(self, str format_spec):
        if format_spec == "!r":
            return self.__repr__()
        return self.__str__()

    property key:
        def __get__(self):
            return self._key
    property is_scope:
        def __get__(self):
            return self._is_scope

    property value:
        def __get__(self):
            return self._value
        def __set__(self, value):
            self._value = value

cdef class Scope(Node):
    cdef:
        readonly str _id

    def __init__(self, key: str, value: Any = None, **kwargs):
        super(Scope, self).__init__(key, value=value, is_scope=True, **kwargs)
        self._value = value or []

        self._namespace = kwargs.get('namespace', uuid.NAMESPACE_OID)
        self._generator = uuid.uuid5(namespace=self._namespace,
                                     name=str(key))
        self._id = self._generator.hex

    def __repr__(self):
        return 'Scope({}, value={})'.format(self._key, self._value)

    def __str__(self):
        return self.__print(self)

    def __iter__(self):
        for v in self._value:
            yield v

    cdef str __print(self, Vertex_t base, str so_far=''):
        if isinstance(base, Scope):
            so_far = "{}<{}>: {{\n".format(base.key, base.id)
            for child in base:
                so_far += self.__print(child, so_far)
            so_far += '}'
        elif isinstance(base, Node):
            so_far = "\t{:!s},".format(base)
        else:
            raise ValueError('Expected one of Scope, Node. got {}'
                             .format(type(base)))
        so_far += '\n'
        return so_far

    cdef void add_scope(self, Scope scope):
        self._value.append(scope)

    cdef void add_node(self, Node node):
        self._value.append(node)

    property id:
        def __get__(self):
            return self._id
    property value:
        def __get__(self):
            return self._value

cdef class Graph:
    cdef readonly Scope _root

    def __init__(self, str path, **kwargs):
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
            Scope scope
        if isinstance(data, (dict, list)):
            data_it = data.items() if isinstance(data, dict) else enumerate(data)
            for key, value in data_it:
                # print(key, value)
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
