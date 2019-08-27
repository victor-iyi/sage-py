"""Usage of KnowledgeGraph and MultiKnowledgeGraph.

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
import sys

from config.consts import FS

from sage.core.utils import Log, File
from sage.core.graph import KnowledgeGraph, MultiKnowledgeGraph


# def single(name: str = 'medical-condition',
#            node_name: str = 'Stable angina',
#            node_schema: str = 'MedicalCondition'):
#     # Create Single Knowledge Graph.
#     Log.warn(f'Loading for {name}')
#     path = File.join(FS.GRAPH_DIR,
#                      f'schema-org/{name}.jsonld')
#     kg = KnowledgeGraph(name, data_file=path)
#
#     # Display all vertices.
#     Log.info(f'Medical vertices: ({len(kg.vertices)})')
#     Log.debug(kg.vertices)
#
#     # Query graph for a named node with schema.
#     node = kg[node_name, node_schema]
#     Log.info(f'Medical Edges: ({len(node.edges)})')
#     for edge in node.edges:
#         vertex = kg[edge.vertex_id]
#         Log.debug(f'{edge.vertex} --{edge.predicate}--> {vertex}')
#
#     Log.info(f'Medical Payload: ({len(node.payload)})')
#     for key, value in node.payload.items():
#         Log.debug(f'{key}: {value}')
#
#     Log.debug('\n')


def single(name: str = 'medical-condition',
           node_name: str = 'Stable angina',
           node_schema: str = 'MedicalCondition'):
    # Create Single Knowledge Graph.
    Log.warn(f'Loading for {name}')
    path = File.join(FS.GRAPH_DIR,
                     f'schema-org/{name}.jsonld')
    kg = KnowledgeGraph.fromfile(path, description=None)

    # Display all vertices.
    Log.info(f'Graph vertices: ({len(kg.vertices)})')
    Log.debug(kg.vertices)

    # Query graph for a named node with schema.
    node = kg[node_name, node_schema]
    Log.debug(f'Node: {node} -- {node.id}')
    Log.info(f'Graph Edges: ({len(node.edges)})')
    for edge in node.edges:
        vertex = kg[edge.vertex_id]
        Log.debug(f'{edge.vertex} --{edge.predicate}--> {vertex}')

    Log.info(f'Graph Payload: ({len(node.payload)})')
    for key, value in node.payload.items():
        Log.debug(f'{key}: {value}')
    Log.debug('\n')

    kg.close()


def multiple(graph_name: str = 'medical_condition',
             graph_entity: str = 'Stable angina',
             entity_schema: str = 'MedicalCondition'):
    path = File.join(FS.GRAPH_DIR, 'schema-org')
    Log.warn(f'Loading graphs in `{path}`')

    # Load multiple graphs from a base directory.
    mkg = MultiKnowledgeGraph.from_dir(path)
    Log.debug(mkg)

    # Display all graphs associated with mkg.
    Log.info(f'Display all graphs ({len(mkg.graphs)}).')
    Log.debug(mkg.graphs)

    # Getting a single entity from a named graph.
    Log.info(f'Getting `{graph_name}` graph.')
    node = mkg[graph_name, graph_entity, entity_schema]
    Log.debug(node)


if __name__ == '__main__':
    # Process single knowledge graph.
    single(name='medical-condition',
           node_name='Stable angina',
           node_schema='MedicalCondition')
    single(name='avatar',
           node_name='Avatar',
           node_schema='Movie')

    # Process multiple related knowledge graph.
    # multiple(graph_name='movie',
    #          graph_entity='Pirates of the Carribean: On Stranger Tides (2011)',
    #          entity_schema='Movie')
