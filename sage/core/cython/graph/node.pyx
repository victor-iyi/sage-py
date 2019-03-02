"""Node definition file.

   @author
     Victor I. Afolabi
     Artificial Intelligence Expert & Researcher.
     Email: javafolabi@gmail.com | victor.afolabi@zephyrtel.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: node.pyx
     Created on 20 February, 2019 @ 21:20.

   @license
     MIT License
     Copyright (c) 2019. Victor I. Afolabi. All rights reserved.
"""

import uuid
from typing import Any

cdef class Node:
    def __cinit__(self, str key, value=None, is_scope=False):
        self.key = key
        self.value = value
        self.is_scope = is_scope

    def __repr__(self):
        return 'Node({}, value={})'.format(self.key, self.value)

    def __str__(self):
        return '"{}" : "{}"'.format(self.key, self.value)

    def __format__(self, str format_spec):
        if format_spec == "!r":
            return self.__repr__()
        return self.__str__()

cdef class Scope(Node):
    def __cinit__(self, str key, value: Any = None, is_scope=True):
        super(Scope, self).__cinit__(key, is_scope=is_scope)
        self.value = value or []

        _generator = uuid.uuid5(namespace=uuid.NAMESPACE_OID,
                                name=str(key))
        self.id = _generator.hex

    def __repr__(self):
        return 'Scope({}, value={})'.format(self.key, self.value)

    def __str__(self):
        return self.__print(self)

    def __iter__(self):
        for v in self.value:
            yield v

    cdef str __print(self, base, str so_far=''):
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
        self.value.append(scope)

    cdef void add_node(self, Node node):
        self.value.append(node)

cpdef Node newNode(str key, value=None):
    return Node(key, value, is_scope=False)

cpdef Scope newScope(str key, value=None):
    return  Scope(key, value, is_scope=True)