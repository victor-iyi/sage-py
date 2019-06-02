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

import json

from sage.core.schema import Graph
from sage.core.base import Base
from sage.core.utils import Log, File

__all__ = ['KnowledgeGraph']


class KnowledgeGraph(Base):
    # Supported file formats.
    SUPPORTED_FORMATS = ('json', 'jsonld', 'json-ld',
                         'rdf', 'xml', 'nt')

    def __init__(self, str name):
        self.label = name
        self._graph = Graph(name)

    def __getitem__(self, other):
        return self._graph[other]

    def __contains__(self, other):
        return self._graph.__contains__(other)

    def __enter__(self):
        self._graph = Graph(self.label)
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
        # noinspection PyUnusedLocal
        data = KnowledgeGraph.read(path)

        # Create a new KnowledgeGraph instance.
        inst = cls(name=File.filename(path))
        inst.load(data)

        # TODO: Add data to inst.
        #   Construct Knowledge Graph with data.

        # Return KnowledgeGraph object.
        return inst

    @staticmethod
    def read(str path):
        # Check if file exists.
        if not File.is_file(path):
            raise FileNotFoundError(f'{path} was not found.')

        # Get the file extension.
        cdef str ext = File.ext(path)

        # Supported file formats.
        if ext not in KnowledgeGraph.SUPPORTED_FORMATS:
            raise AssertionError(f'Expected one of: {KnowledgeGraph.SUPPORTED_FORMATS}.'
                                 f' Got {ext}')

        if ext in ('json', 'jsonld', 'json-ld'):
            # Load JSON-LD file.
            with open(path, mode='r', encoding='utf-8') as f:
                return json.loads(f.read())
        else:
            # TODO(victor-iyiola): Support for RDF/XML & n-triples.
            Log.warn('RDF/XML & n-triple not yet supported.')
            return NotImplemented

    def load(self, data):
        cdef:
            str label, nbr_label

        # New Scope.
        if isinstance(data, dict):
            # Add vertex in current scope to graph.
            label = data.get('name', 'Unknown')
            schema = data.get('@type', 'Thing')
            schema = (', '.join(schema) if isinstance(schema, list)
                      else schema)
            vertex = self._graph.add_vertex(label, schema)

            # Loop through the key-value pairs of current vertex.
            for k, v in data.items():
                # Key doesn't start with "@" & Value must be a primitive type.
                if not k.startswith('@') and isinstance(v, (int, float, str, bool)):
                    # Add necessary payloads.
                    vertex.payload[k] = v
                # A new list of scopes.
                elif isinstance(v, (list, tuple)):
                    for item in v:  # Loop through the list.
                        # Assert that we have another scope (neighboring scope).
                        if isinstance(item, dict):
                            nbr_label = item.get('name', 'Unknown')
                            nbr_schema = item.get('@type', 'Thing')
                            nbr_schema = (', '.join(nbr_schema)
                                          if isinstance(nbr_schema, list)
                                          else nbr_schema)
                            nbr = self._graph.add_vertex(nbr_label, nbr_schema)
                            vertex.add_neighbor(nbr, predicate=k)
                        # Visit neighboring scope.
                        self.load(item)
                elif isinstance(v, dict):
                    # Direct neighboring scope.
                    nbr_label = v.get('name', 'Unknown')
                    nbr_schema = v.get('@type', 'Thing')
                    nbr_schema = (', '.join(nbr_schema)
                                  if isinstance(nbr_schema, list)
                                  else nbr_schema)
                    nbr = self._graph.add_vertex(nbr_label, nbr_schema)
                    vertex.add_neighbor(nbr, predicate=k)
                    # Visit direct neighboring scope.
                    self.load(v)
        elif isinstance(data, (list, tuple)):
            # In case scope starts with a list.
            for item in data:
                self.load(item)

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
