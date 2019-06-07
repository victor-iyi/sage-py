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

from sage.core.graph import KnowledgeGraph
from sage.core.utils import Log, File
from config.consts import FS


def create_kg(name: str):
    Log.warn(f'Loading for {name}')
    path = File.join(FS.GRAPH_DIR, f'schema-org/{name}.jsonld')
    return KnowledgeGraph.fromfile(path)


def action():
    kg = create_kg('action')

    Log.info(f'Action vertices: ({len(kg.vertices)})')
    Log.debug(kg.vertices)

    node = kg['Unknown', 'ListenAction']
    Log.info(f'Action Edges: ({len(node.edges)})')
    for edge in node.edges:
        vertex = kg[edge.vertex_id]
        Log.debug(f'{edge.vertex} --{edge.predicate}--> {vertex}')

    Log.debug('')


def creative_work():
    kg = create_kg('creative-work')

    Log.info(f'Creative Work vertices: ({len(kg.vertices)})')
    Log.debug(kg.vertices)

    node = kg['Holt Physical Science', 'Book']
    Log.info(f'Creative Work Edges: ({len(node.edges)})')
    for edge in node.edges:
        vertex = kg[edge.vertex_id]
        Log.debug(f'{edge.vertex} --{edge.predicate}--> {vertex}')

    Log.debug('')


def event():
    kg = create_kg('event')

    Log.info(f'Event vertices: ({len(kg.vertices)})')
    Log.debug(kg.vertices)

    node = kg['Typhoon with Radiation City', 'Event']
    Log.info(f'Event Edges: ({len(node.edges)})')
    for edge in node.edges:
        vertex = kg[edge.vertex_id]
        Log.debug(f'{edge.vertex} --{edge.predicate}--> {vertex}')

    Log.debug('')


def medical_condition():
    kg = create_kg('medical-condition')

    Log.info(f'Medical vertices: ({len(kg.vertices)})')
    Log.debug(kg.vertices)

    node = kg['Stable angina', 'MedicalCondition']
    Log.info(f'Medical Edges: ({len(node.edges)})')
    for edge in node.edges:
        vertex = kg[edge.vertex_id]
        Log.debug(f'{edge.vertex} --{edge.predicate}--> {vertex}')

    Log.debug('')


def movie():
    kg = create_kg('movie')

    Log.info(f'Movie vertices: ({len(kg.vertices)})')
    Log.debug(kg.vertices)

    node = kg['Pirates of the Carribean: On Stranger Tides (2011)', 'Movie']
    Log.info(f'Movie Edges: ({len(node.edges)})')
    for edge in node.edges:
        vertex = kg[edge.vertex_id]
        Log.debug(f'{edge.vertex} --{edge.predicate}--> {vertex}')

    Log.debug('')


def property_value():
    kg = create_kg('property-value')

    Log.info(f'Property vertices: ({len(kg.vertices)})')
    Log.debug(kg.vertices)

    node = kg['Beach in Mexico', 'ImageObject']
    Log.info(f'Property Edges: ({len(node.edges)})')
    for edge in node.edges:
        vertex = kg[edge.vertex_id]
        Log.debug(f'{edge.vertex} --{edge.predicate}--> {vertex}')

    Log.debug('')


if __name__ == '__main__':
    action()
    creative_work()
    event()
    medical_condition()
    movie()
    property_value()
