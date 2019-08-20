"""Stubs for Cython modules.

   @author
     Victor I. Afolabi
     Artificial Intelligence & Software Engineer.
     Email: javafolabi@gmail.com | victor.afolabi@zephyrtel.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: __init__.py
     Package: sage.core
     Created on 28 January, 2019 @ 12:43.

   @license
     Apache License 2.0
     Copyright (c) 2019. Victor I. Afolabi. All rights reserved.
"""
from .base import Base, Mode, Attr
from .graph import KnowledgeGraph, MultiKnowledgeGraph
from .schema import Vertex, Graph, Edge
from .crawler import get_properties, get_source
from .utils import Log, File, Cache, Downloader
from .data import Dataset

__all__ = [
    # Base class.
    'Base', 'Mode', 'Attr',

    # Utils class.
    'Downloader', 'Cache', 'File', 'Log',

    # Knowledge Graph.
    'Vertex', 'Edge', 'Graph',
    'KnowledgeGraph', 'MultiKnowledgeGraph',

    # Crawler.
    'get_properties', 'get_source',

    # Dataset
    'Dataset',
]
