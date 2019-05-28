"""Test for creating Vertices.

   @author
     Victor I. Afolabi
     Artificial Intelligence Expert & Researcher.
     Email: javafolabi@gmail.com | victor.afolabi@zephyrtel.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: test_vertex.py
     Created on 28 May, 2019 @ 11:58 AM.

   @license
     Apache 2.0 License
     Copyright (c) 2019. Victor I. Afolabi. All rights reserved.
"""

# Built-in libraries.
import json
import unittest

# custom libraries.
from config.consts import FS
from sage.core.utils import File
from sage.core.schema import Vertex, Edge


class TestVertex(unittest.TestCase):
    def setUp(self):
        self.vertex = Vertex('Avatar', 'Movie')
        self.avatar_path = File.join(FS.CACHE_DIR,
                                     'graph/examples/avatar.jsonld')
        self.avatar_data = json.load(open(self.avatar_path))

    def test_label_and_schema(self):
        self.assertEqual(self.vertex.label, 'Avatar')
        self.assertEqual(self.vertex.schema, 'Movie')
        self.assertNotEqual(self.vertex.label, 'Something Else')
        self.assertIsNotNone(self.vertex.schema)

    def test_edges(self):
        # Create new neighbor.
        nbr = Vertex('James Cameron', 'Person')
        # Add created neighbor.
        self.vertex.add_neighbor(nbr, predicate='director')
        # Check it's length.
        self.assertEqual(len(self.vertex.edges), 1)

        # Get added edge.
        director = self.vertex.edges[0]
        self.assertIsInstance(director, Edge)
        self.assertEqual(director.vertex_id, nbr.id)
        self.assertEqual(director.predicate, 'director')

        # Because director is not part of a graph (no session).
        self.assertIsNone(director.id)
        self.assertIsNone(director.vertex)

    def test_payload(self):
        self.assertDictEqual(self.vertex.payload, {})
        self.assertEqual(len(self.vertex.payload), 0)

        payload = {
            "genre": "Science Fiction",
            "trailer": "https://avatar.com/trailer.mp4"
        }
        # Add payload.
        self.vertex.add_payload(payload)
        self.assertDictEqual(self.vertex.payload, payload)
        self.assertEqual(len(self.vertex.payload), 2)
        self.assertEqual(self.vertex.payload['genre'],
                         'Science Fiction')
        self.assertEqual(self.vertex.payload['trailer'],
                         'https://avatar.com/trailer.mp4')

        # Add more payload
        self.vertex.payload['rating'] = '*****'
        self.assertEqual(len(self.vertex.payload), 3)
        self.assertEqual(self.vertex.payload['rating'], '*****')

        # Add payload that already exists.
        self.vertex.add_payload(payload)
        self.assertEqual(len(self.vertex.payload), 3)


if __name__ == '__main__':
    unittest.main()
