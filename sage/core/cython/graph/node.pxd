"""Node declaration file.

   @author
     Victor I. Afolabi
     Artificial Intelligence Expert & Researcher.
     Email: javafolabi@gmail.com | victor.afolabi@zephyrtel.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: node.pxd
     Created on 20 February, 2019 @ 09:19 PM.

   @license
     MIT License
     Copyright (c) 2019. Victor I. Afolabi. All rights reserved.
"""

cdef class Node:
    cdef:
        public _value
        readonly str _key
        readonly bint _is_scope

cdef class Scope(Node):
    cdef:
        readonly _namespace, _generator
        readonly str _id, _type

    cdef str __print(self, Node base, str so_far= *)
    cdef void add_scope(self, Scope scope)
    cdef void add_node(self, Node node)

# cdef Node newNode(str key, value= *, *)
# cdef Scope newScope(str key, value = *, *)
