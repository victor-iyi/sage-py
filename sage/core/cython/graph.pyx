"""Knowledge Graph.

   @author
     Victor I. Afolabi
     Artificial Intelligence & Software Engineer.
     Email: javafolabi@gmail.com | victor.afolabi@zephyrtel.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: graph.pyx.py
     Created on 28 January, 2019 @ 14:18.

   @license
     MIT License
     Copyright (c) 2019. Victor I. Afolabi. All rights reserved.
"""
# Built-in libraries.
import json
import uuid

from typing import AnyStr, Dict, List, Union


class Node:
    def __init__(self, key: str, value=None, **kwargs):
        self._key = key
        self._value = value
        self._is_scope = kwargs.get('is_scope', False)

    def __repr__(self):
        return 'Node({}, value={})'.format(self._key, self._value)

    def __str__(self):
        return '"{}" : "{}"'.format(self._key, self._value)

    def __format__(self, format_spec):
        if format_spec == "!r":
            return self.__repr__()
        else:
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
    def __init__(self, key: str, **kwargs):
        super(Scope, self).__init__(key, is_scope=True, **kwargs)

        self._value = kwargs.get('value', [])
        self._namespace = kwargs.get('namespace', uuid.NAMESPACE_OID)

        self._generator = uuid.uuid5(namespace=self._namespace,
                                     name=str(key))
        self._id = self._generator.hex

    def __repr__(self):
        return 'Scope({}, value={})'.format(self._key, self._value)

    def __str__(self):
        msg = self.__print(self)
        return msg

    def __iter__(self):
        for v in self._value:
            yield v

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


class Graph:
    def __init__(self, path, **kwargs):
        self._root = Scope("ns")
        with open(path) as f:
            data = json.loads(f.read())
        self.load(self._root, data)

    def __repr__(self):
        return 'Graph(root={:!r})'.format(self._root)

    def __str__(self):
        return self._root.__str__()

    def __format__(self, format_spec):
        if '!r' in format_spec:
            return self.__repr__()
        else:
            return self.__str__()

    def load(self, base: Scope, data: Union[Dict, List, AnyStr]):
        if isinstance(data, (dict, list)):
            data_it = data.items() if isinstance(data, dict) else enumerate(data)
            for key, value in data_it:
                # print(key, value)
                if isinstance(value, str):
                    base.add_node(Node(key, value))
                elif isinstance(value, (dict, list)):
                    scope = Scope(key)
                    self.load(scope, value)
                    base.add_scope(scope)
        # elif isinstance(value, str):
        #     base.add_node(Node(key, value))
        else:
            raise TypeError('Expected one of List, Dict, Str. Got {}'
                            .format(type(data)))

    @property
    def root(self):
        return self._root
