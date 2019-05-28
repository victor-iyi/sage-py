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
import unittest

# Custom libraries.
from config.consts import FS
from sage.core.utils import File
from sage.core.schema import Graph


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph('test')
        self.graph_path = File.join(FS.DATABASE_DIR,
                                    'test.db')

    def tearDown(self):
        File.remove(File.join(FS.DATABASE_DIR,
                              f'{self.graph.name}.db'))
        self.graph.close()

    def test_graph_creation(self):
        self.assertEqual(self.graph.name, 'test')
        self.assertTrue(File.is_file(self.graph_path))

    def test_query(self):
        pass

    def test_add_neighbor(self):
        pass

    def test_add_vertex(self):
        pass

    def test_get_vertex(self):
        pass


if __name__ == '__main__':
    unittest.main()
