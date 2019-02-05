"""

   @author
     Victor I. Afolabi
     Artificial Intelligence & Software Engineer.
     Email: javafolabi@gmail.com | victor.afolabi@zephyrtel.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: node.pyx
     Created on 28 January, 2019 @ 12:52 PM.

   @license
     Apache License 2.0
     Copyright (c) 2019. Victor I. Afolabi. All rights reserved.
"""

import uuid
from typing import List

from sage.core.base import Base


class Node(Base):
    def __init__(self, key: str, value=None, **kwargs):
        super(Node, self).__init__(**kwargs)
        self._key = key
        self._value = value
        self._is_scope = kwargs.get('is_scope', False)

    def __repr__(self):
        return 'Node({}, value={})'.format(self._key, self._value)

    def __str__(self):
        return '"{}" : "{}"'.format(self._key, self._value)

    def __format__(self, format_spec: str):
        if format_spec == "!r":
            return self.__repr__()
        return self.__str__()

    @property
    def key(self):
        return self._key

    @property
    def value(self):
        return self._value

    @property
    def is_scope(self):
        return self._is_scope


class Scope(Node):
    def __init__(self, key: str, value: List[Node] = None, **kwargs):
        super(Scope, self).__init__(key, is_scope=True, **kwargs)

        self._value = value or []
        self._namespace = kwargs.get('namespace', uuid.NAMESPACE_OID)

        self._generator = uuid.uuid5(namespace=self._namespace,
                                     name=str(key))
        self._id = self._generator.hex
        self.__i = 0  # iterator counter.

    def __repr__(self):
        return 'Scope({}, value={})'.format(self._key, self._value)

    def __str__(self):
        return self.__print(self)

    def __iter__(self):
        return self

    def __len__(self):
        return len(self._value)

    def __next__(self):
        if self.__i >= len(self._value):
            raise StopIteration()

        ret = self._value[self.__i]
        self.__i += 1

        return ret

    def __print(self, base, so_far=""):
        if isinstance(base, Scope):
            so_far = "{}<{}>: {{\n".format(base.key, base.id)
            for child in base:
                so_far += self.__print(child, so_far)
            so_far += "}"
        elif isinstance(base, Node):
            so_far = "\t{:!s},".format(base)
        else:
            raise ValueError('Expected one of Scope, Node. got {}'
                             .format(type(base)))
        so_far += '\n'
        return so_far

    def add_scope(self, scope):
        self._value.append(scope)

    def add_node(self, node):
        self._value.append(node)

    @property
    def id(self):
        return self._id
