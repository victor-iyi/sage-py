"""Test for loading https://schema.org file format.

   @author
     Victor I. Afolabi
     Artificial Intelligence Expert & Researcher.
     Email: javafolabi@gmail.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: test_schema_org.py
     Created on 07 June, 2019 @ 07:09 PM.

   @license
     Apache 2.0 License
     Copyright (c) 2019. Victor I. Afolabi. All rights reserved.
"""

# Built-in libraries.
import unittest

# Custom libraries.
from config.consts import FS
from sage.core import KnowledgeGraph, File


class TestSchemaOrg(unittest.TestCase):
    def setUp(self):
        path = File.join(FS.GRAPH_DIR, 'schema-org/{}.jsonld')
        # Utility function for creating Knowledge graph.
        self.create = lambda name: KnowledgeGraph.fromfile(path.format(name))

    def test_action(self):
        kg = self.create('action')

        self.assertEqual(kg.label, 'action')
        self.assertEqual(len(kg.vertices), 6)

        node = kg['Unknown', 'ListenAction']
        self.assertEqual(len(node.edges), 5)

    def test_creative_work(self):
        kg = self.create('creative-work')
        self.assertEqual(kg.label, 'creative-work')
        self.assertEqual(len(kg.vertices), 3)
        node = kg['Holt Physical Science', 'Book']
        self.assertEqual(len(node.edges), 2)

    def test_event(self):
        kg = self.create('event')
        self.assertEqual(kg.label, 'event')
        self.assertEqual(len(kg.vertices), 4)
        node = kg['Typhoon with Radiation City', 'Event']
        self.assertEqual(len(node.edges), 2)

    def test_medical_condition(self):
        kg = self.create('medical-condition')
        self.assertEqual(kg.label, 'medical-condition')
        self.assertEqual(len(kg.vertices), 25)

        node = kg['Stable angina', 'MedicalCondition']
        self.assertEqual(len(node.edges), 20)

    def test_movie(self):
        kg = self.create('movie')
        self.assertEqual(kg.label, 'movie')
        self.assertEqual(len(kg.vertices), 8)
        node = kg['Pirates of the Carribean: On Stranger Tides (2011)', 'Movie']
        self.assertEqual(len(node.edges), 7)

    def test_property_value(self):
        kg = self.create('property-value')
        self.assertEqual(kg.label, 'property-value')
        self.assertEqual(len(kg.vertices), 6)
        node = kg['Beach in Mexico', 'ImageObject']
        self.assertEqual(len(node.edges), 5)


if __name__ == '__main__':
    unittest.main()
