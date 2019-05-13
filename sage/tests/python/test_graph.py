"""Test for Vertices & Graphs..

   @author
     Victor I. Afolabi
     Artificial Intelligence Expert & Researcher.
     Email: javafolabi@gmail.com | victor.afolabi@zephyrtel.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: test_graph.py
     Created on 13 May, 2019 @ 12:15.

   @license
     Apache 2.0 License
     Copyright (c) 2019. Victor I. Afolabi. All rights reserved.
"""
# Built-in libraries.
import json
import unittest

from config.consts import FS
from sage.core.utils import File
from example.python.schema import Vertex, Graph


class TestVertex(unittest.TestCase):
    def setUp(self):
        self.vertex = Vertex('Avatar', 'Movie')
        self.avatar_path = File.join(FS.CACHE_DIR,
                                     'graph/examples/avatar.jsonld')
        self.avatar_data = json.load(open(self.avatar_path))

    def test_label_and_schema(self):
        assert self.vertex.label == 'Avatar'
        assert self.vertex.schema == 'Movie'
        assert self.vertex.label != 'Something Else'
        assert self.vertex.schema is not None

    def test_edges(self):
        # Create new neighbor.
        nbr = Vertex('James Cameron', 'Person')
        # Add created neighbor.
        self.vertex.add_neighbor(nbr, predicate='director')
        # Check it's length.
        assert len(self.vertex.edges) == 1

        # Get added edge.
        director = self.vertex.edges[0]
        assert director.vertex_id == nbr.id
        assert director.predicate == 'director'

        # Because director is not part of a graph (no session).
        assert director.id is None
        assert director.vertex is None

    def test_payload(self):
        payload = {
            "genre": "Science Fiction",
            "trailer": "https://avatar.com/trailer.mp4"
        }
        assert self.vertex.payload == {}
        assert len(self.vertex.payload) == 0

        # Add payload.
        self.vertex.add_payload(payload)
        assert self.vertex.payload == payload
        assert len(self.vertex.payload) == 2
        assert self.vertex.payload['genre'] == 'Science Fiction'
        assert self.vertex.payload['trailer'] == 'https://avatar.com/trailer.mp4'

        # Add more payload
        self.vertex.payload['rating'] = '*****'
        assert len(self.vertex.payload) == 3
        assert self.vertex.payload['rating'] == '*****'

        # Add payload that already exists.
        self.vertex.add_payload(payload)
        assert len(self.vertex.payload) == 3


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph('test')
        self.graph_path = File.join(FS.DATABASE_DIR,
                                    'test.db')

    def test_graph_creation(self):
        assert self.graph.name == 'test'
        assert File.is_file(self.graph_path)


if __name__ == '__main__':
    unittest.main()
