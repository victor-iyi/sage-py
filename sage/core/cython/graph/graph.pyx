"""Implementation of Graph database.

   @author
     Victor I. Afolabi
     Artificial Intelligence & Software Engineer.
     Email: javafolabi@gmail.com | victor.afolabi@zephyrtel.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: graph.py
     Created on 12 May, 2019 @ 11:20 PM.

   @license
     Apache 2.0 License
     Copyright (c) 2019. Victor I. Afolabi. All rights reserved.
"""

from config.consts import FS

from sage.core.base import Base
from sage.core.schema import Graph
from sage.core.utils import File, Log

__all__ = [
    'KnowledgeGraph',
    'MultiKnowledgeGraph',
]


class MultiKnowledgeGraph(Base):
    def __init__(self, str name, **kwargs):
        super(MultiKnowledgeGraph, self).__init__(**kwargs)
        self.label = name

        # Base directory where graph is stored.
        self.base = File.join(FS.DATABASE_DIR, name)
        File.make_dirs(self.base)

        # List of graphs contained in Multi-KG.
        self._graphs = dict()

    def __getitem__(self, item):
        result = None
        if isinstance(item, str):
            if item in self._graphs:
                result = self._graphs[item]
            else:
                raise KeyError(f'{item} not found in graph.')
        elif isinstance(item, tuple):
            graph, item = self.__get_validate(item)
            result = graph[item]
        else:
            raise TypeError(f'Expected one of str & tuple got {type(item)}')
        return result

    def get(self, item):
        result = None
        if isinstance(item, str):
            if item in self._graphs:
                result = self._graphs[item]
            else:
                raise KeyError(f'{item} not found in graph.')
        elif isinstance(item, tuple):
            graph, item = self.__get_validate(item)
            result = graph.get(item)
        else:
            raise TypeError(f'Expected one of str & tuple got {type(item)}')

        return result

    @classmethod
    def from_dir(cls, str path):
        # `path` must be a directory.
        if not File.is_dir(path):
            raise FileNotFoundError(f"{path} does not exist"
                                    " or isn\'t a directory.")

        # Create a new multi-knowledge graph.
        cdef str name = File.filename(path)
        inst = cls(name.replace(' ', '_').replace('-', '_'))

        cdef str file_path
        # Get all files in directory.
        for file_path in File.get_files(path, optimize=False):
            if File.ext(file_path) in Graph.SUPPORTED_FORMATS:
                name = File.filename(file_path)
                inst.add_graph(name.replace(' ', '_').replace('-', '_'),
                               data_file=file_path)
            else:
                Log.warn(f'{file_path} not supported.')

        return inst

    def add_graph(self, str name, str data_file=None):
        if name in self._graphs:
            raise KeyError(f'{name} already exists.')

        g = Graph(name, base=self.base,
                  data_file=data_file)
        self._graphs[name] = g

        return g

    def __get_validate(self, item):
        if not isinstance(item, tuple) or len(item) < 2:
            raise AssertionError('Expected one of Tuple[str, str], '
                                 'Tuple[str, str, str] or Tuple[str, Vertex]')

        # Get the graph to be queried.
        name = item[0]

        if name not in self._graphs:
            raise KeyError(f'Graph `{name}` does not exist.')

        # Grab remaining item(s).
        item = item[1] if len(item[1:]) == 1 else item[1:]

        return self._graphs[name], item

    @property
    def graphs(self):
        return list(self._graphs.values())


class KnowledgeGraph(Base):
    # Supported file formats.
    SUPPORTED_FORMATS = ('json', 'jsonld', 'json-ld',
                         'rdf', 'xml', 'nt')

    def __init__(self, str name, str data_file=None, **kwargs):
        super(KnowledgeGraph, self).__init__(**kwargs)
        self.label = name
        # Base path where graph data is stored.
        self.base = FS.DATABASE_DIR
        File.make_dirs(self.base)

        self._graph = Graph(name, base=self.base,
                            data_file=data_file)

    def __getitem__(self, other):
        return self._graph[other]

    def __contains__(self, other):
        return self._graph.__contains__(other)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._graph.close()

    def get(self, other):
        return self._graph.get(other)

    def add_triple(self, triples):
        for triple in triples:
            # Subject vertex.
            subj = self._graph.add_vertex(triple[0])
            # Object vertex.
            obj = self._graph.add_vertex(triple[2])
            # Connect subject vertex to object vertex.
            subj.add_neighbor(obj, predicate=triple[1])

    @classmethod
    def fromfile(cls, str path):
        # Create a new KnowledgeGraph instance.
        inst = cls(name=File.filename(path),
                   data_file=path)

        # Return KnowledgeGraph object.
        return inst

    def load(self, data):
        self._graph.load(data)

    def reached_goal(self, vertex):
        return vertex

    def depth_first(self, start, list visited=None, list to_visit=None):
        # Iterative approach to depth-first search.
        visited = visited or [start]
        to_visit = to_visit or [start]

        # While there's still a node to visit.
        while to_visit:
            vertex = visited.pop()
            # Goal check.
            if self.reached_goal(vertex):
                return vertex

            # Visit vertex edges.
            for edge in vertex.edges:
                child = self._graph[edge.vertex_id]
                # Extend child node if not already visited.
                if child not in visited:
                    visited.append(child)
                    to_visit.append(child)

        return start

    def close(self):
        self._graph.close()

    @property
    def graph(self):
        return self._graph

    @property
    def vertices(self):
        return self._graph.vertices
