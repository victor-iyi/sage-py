"""Tests for Knowledge Graph.

   @author
     Victor I. Afolabi
     Artificial Intelligence Expert & Researcher.
     Email: javafolabi@gmail.com | victor.afolabi@zephyrtel.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: test_knowledge_graph.py
     Created on 28 May, 2019 @ 12:00 PM.

   @license
     Apache 2.0 License
     Copyright (c) 2019. Victor I. Afolabi. All rights reserved.
"""
# Built-in libraries.
import unittest

# Custom libraries.
from config.consts import FS
from sage.core.utils import File
from sage.core.graph import KnowledgeGraph


class TestKnowledgeGraph(unittest.TestCase):
    def setUp(self):
        path = File.join(FS.CACHE_DIR,
                         'graph/examples/avatar.jsonld')
        self.kg = KnowledgeGraph.fromfile(path)

    def tearDown(self):
        File.remove(File.join(FS.DATABASE_DIR,
                              f'{self.graph.name}.db'))
        self.kg.close()

    # def test_from_file(self):
    #     path = File.join(FS.CACHE_DIR,
    #                      'graph/examples/avatar.jsonld')
    #     kg = KnowledgeGraph.fromfile(path)
    #     self.assertIsInstance(kg, KnowledgeGraph)
    #     self.assertEqual(kg.name, 'avatar')
    #
    #     # Raise file not found if file doesn't exist.
    #     # self.assertRaises(FileNotFoundError,
    #     #                   KnowledgeGraph.fromfile,
    #     #                   'some/path.jsonld')
    #
    #     # Raise assertion error for unsupported format
    #     # path = File.join(FS.CACHE_DIR,
    #     #                  'graph/examples/avatar.ext')
    #     # # Temporarily create file.
    #     # with open(path, mode='w') as _:
    #     #     ...
    #     #
    #     # self.assertRaises(AssertionError,
    #     #                   KnowledgeGraph.fromfile,
    #     #                   path)
    #     # File.remove(path)


if __name__ == '__main__':
    unittest.main()
