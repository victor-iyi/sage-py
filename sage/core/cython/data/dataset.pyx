"""
   @author
     Victor I. Afolabi
     Artificial Intelligence Expert & Researcher.
     Email: javafolabi@gmail.com | victor.afolabi@zephyrtel.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: dataset.pyx
     Created on 02 March, 2019 @ 04:08 PM.

   @license
     MIT License
     Copyright (c) 2019. Victor I. Afolabi. All rights reserved.
"""
cimport data

cpdef use_node(data.Node node):
    print(node.key, node.value, node.is_scope)