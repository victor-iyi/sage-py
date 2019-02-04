"""Creation of Knowledge Graph.

   @author
     Victor I. Afolabi
     Artificial Intelligence & Software Engineer.
     Email: javafolabi@gmail.com | victor.afolabi@zephyrtel.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: graph.pyi
     Created on 28 January, 2019 @ 12:53 PM.

   @license
     Apache License 2.0
     Copyright (c) 2019. Victor I. Afolabi. All rights reserved.
"""
from typing import AnyStr, Dict, List, Union, Any, Optional


class Node:
    key = ...  # type: str
    value = ...  # type: Any
    is_scope = ...  # type: bool

    def __init__(self, key: str, value: Optional[Any] = None, **kwargs) -> None: ...

    def __repr__(self) -> str: ...

    def __str__(self) -> str: ...

    def __format__(self, format_spec) -> str: ...


class Scope(Node):
    id = ...  # type: str
    key = ...  # type: str
    value = ...  # type: List[Node]
    is_scope = ...  # type: bool
    namespace = ...  # type: str

    def __init__(self, key: str, value: Optional[List[Union[Scope, Node, Any]]] = ..., **kwargs: Any) -> None: ...

    def __repr__(self) -> str: ...

    def __str__(self) -> str: ...

    def __iter__(self) -> Node: ...

    def __print(self, base: Union[Node, Scope], so_far: str = "") -> str: ...

    def add_scope(self, scope: Scope) -> None: ...

    def add_node(self, node: Node) -> None: ...


class Graph:
    root = ...  # type: Scope

    def __init__(self, path: str, **kwargs): ...

    def __repr__(self) -> str: ...

    def __str__(self) -> str: ...

    def __format__(self, format_spec: str) -> str: ...

    def load(self, base: Union[Node, Scope], data: Union[Dict, List, AnyStr]) -> None: ...
