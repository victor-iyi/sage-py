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
from typing import List

from example.python import Graph
from sage.core.base import Base
from sage.core.utils import Log, File


class KnowledgeGraph(Base):
    # Supported file formats.
    SUPPORTED_FORMATS = ('json', 'jsonld', 'json-ld',
                         'rdf', 'xml', 'nt')

    def __init__(self, name):
        self.name = name
        self._graph = Graph(name)

    def add_triple(self, triples: List[tuple]):
        for triple in triples:
            # Subject vertex.
            subj = self._graph.add_vertex(triple[0])
            # Object vertex.
            obj = self._graph.add_vertex(triple[2])
            # Connect subject vertex to object vertex.
            subj.add_neighbor(obj, predicate=triple[1])

    @classmethod
    def fromfile(cls, path):
        # noinspection PyUnusedLocal
        data = KnowledgeGraph.read(path)

        # Create a new KnowledgeGraph instance.
        inst = cls(name=File.basename(path))

        # TODO: Add data to inst.
        #   Construct Knowledge Graph with data.

        # Return KnowledgeGraph object.
        return inst

    @staticmethod
    def read(path: str):
        # Check if file exists.
        if not File.is_file(path):
            raise FileNotFoundError(f'{path} was not found.')

        # Supported file formats.
        if not path.endswith(KnowledgeGraph.SUPPORTED_FORMATS):
            raise AssertionError(f'Expected one of: {KnowledgeGraph.SUPPORTED_FORMATS}')

        # Get the file extension.
        ext = File.ext(path)
        if ext in ('json', 'jsonld', 'json-ld'):
            # Load JSON-LD file.
            with open(path) as f:
                return json.loads(f.read())
        else:
            # TODO(victor-iyiola): Support for RDF/XML & n-triples.
            Log.warn('RDF/XML & n-triple not yet supported.')
            return NotImplemented

    # def load(self, base, data):
    #     if isinstance(data, (str, dict, list)):
    #         data_it = data.items() if isinstance(data, dict) else enumerate(data)
    #         for key, value in data_it:
    #             Log.debug(f'{key} {value}')
    #             if isinstance(value, str):
    #                 pass
    #             elif isinstance(value, (dict, list)):
    #                 pass
    #     else:
    #         raise TypeError(f'Expected one of list, dict, str. Got {type(data)}')

    # def load(self, base, data):
    #     if isinstance(data, (dict, list)):
    #         data_it = data.items() if isinstance(data, dict) else enumerate(data)
    #         for key, value in data_it:
    #             # print(key, value)
    #             if isinstance(value, str):
    #                 base.add_node(Node(str(key), value))
    #             elif isinstance(value, (dict, list)):
    #                 scope = Scope(str(key))
    #                 self.load(scope, value)
    #                 base.add_scope(scope)
    #     else:
    #         raise TypeError('Expected one of List, Dict, Str. Got {}'
    #                         .format(type(data)))


if __name__ == '__main__':
    # Testing Graph.
    triples = [
        ('Victor', 'age', '23'),
        ('Victor', 'month', 'October'),
        ('Victor', 'bestFriends', 'Dara'),
        ('Dara', 'school', 'China'),
        ('Ope', 'school', 'USA'),
        ('Ope', 'field', 'Medical'),
        ('Victor', 'field', 'Science'),
        ('Dara', 'field', 'Engineering'),
    ]

    graph = Graph('sage', verbose=1)

    for triple in triples:
        subj = graph.add_vertex(triple[0])
        obj = graph.add_vertex(triple[2])
        # TODO: Add vertex connections (neighbors).
        subj.add_neighbor(obj, predicate=triple[1])

    Log.warn(graph.vertices)
    victor = graph['Victor', None]
    dara = graph['Dara', None]
    Log.debug(f'victor = {victor}')
    Log.debug(f'victor.id = {victor.id}')
    Log.debug(f'dara.id = {dara.id}')
    Log.debug(f'victor.payload = {victor.payload}')
    Log.debug(f'victor.edges = {victor.edges}')
