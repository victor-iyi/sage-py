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
    cdef:
        public _value
        readonly str _key
        readonly bint _is_scope

    def __cinit__(self, key: str, value=None, **kwargs):
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
        readonly _namespace, _generator
        readonly str _id, _type

    def __cinit__(self, key: str, value: Any = None, **kwargs):
        super(Scope, self).__cinit__(key, is_scope=True, **kwargs)
        self._value = value or []

        _generator = uuid.uuid5(namespace=uuid.NAMESPACE_OID,
                                name=str(key))
        self._id = _generator.hex

    def __repr__(self):
        return 'Scope({}, value={})'.format(self._key, self._value)

    def __str__(self):
        return self.__print(self)

    def __iter__(self):
        for v in self._value:
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
        self._value.append(scope)

    cdef void add_node(self, Node node):
        self._value.append(node)

    property id:
        def __get__(self):
            return self._id
    property type:
        def __get__(self):
            return self._type
