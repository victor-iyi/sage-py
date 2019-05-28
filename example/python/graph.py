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

if __name__ == '__main__':
    # Loading Graph data from File.
    # path = File.join(FS.CACHE_DIR, 'graph/examples/avatar.jsonld')
    # kg = KnowledgeGraph.fromfile(path)
    # Log.info('Knowledge Graph')
    # Log.debug(kg.vertices)
    #
    # # Working with Vertices.
    # Log.info("Avatar:")
    # avatar = kg['Avatar', 'Movie']
    # Log.debug(f'avatar = {avatar}')
    # Log.debug(f'avatar.id = {avatar.id}')
    # Log.debug(f'avatar.payload = {avatar.payload}')
    # Log.debug(f'avatar.edges = {avatar.edges}')
    #
    # # Working with Edges...
    # Log.info("Director:")
    # director = avatar.edges[0]
    # Log.debug(f'director.id = {director.id}')
    # Log.debug(f'director.vertex = {director.vertex}')
    # Log.debug(f'director.vertex_id = {director.vertex_id}')
    # Log.debug(f'kg[director.vertex_id] = {kg[director.vertex_id]}')
    # Log.debug(f'director.predicate = {director.predicate}')
    # Log.debug(f'avatar.payload = {avatar.payload}')

    # Testing Graph.
    example = {
        "@type": 'Person',
        "name": 'Victor',
        "age": 22,
        "month": 'October',
        'bestFriends': [
            {
                "@type": 'Person',
                "name": 'Dara',
                "school": {
                    "@type": 'Place',
                    'name': 'China',
                    'population': 21341341234
                },
                "field": 'Engineering'
            },
            {
                "@type": 'Person',
                "name": 'Ope',
                "school": 'USA',
                "field": 'Medicine'
            }
        ],
        "field": "Science"
    }

    with KnowledgeGraph('example') as kg:
        kg.load(data=example)
        Log.debug(kg.vertices)

        victor = kg['Victor', 'Person']
        Log.debug(f'victor = {victor}')
        Log.debug(f'victor.id = {victor.id}')
        Log.debug(f'victor.edges = {victor.edges}')
        Log.debug(f'victor.payload = {victor.payload}')

        for edge in victor.edges:
            vertex = kg[edge.vertex_id]
            Log.info(f'{edge.vertex} ={edge.predicate}=> {vertex}')
            Log.debug(f'vertex.payload = {vertex.payload}')
            Log.debug(f'kg[edge.vertex_id] = {kg[edge.vertex_id]}')
            Log.debug(f'edge.vertex_id = {edge.vertex_id}')
            Log.debug(f'edge.vertex = {edge.vertex}')

    # kg = KnowledgeGraph('example')
    # kg.load(data=example)
    # Log.debug(kg.vertices)
    #
    # victor = kg['Victor', 'Person']
    # Log.debug(f'victor = {victor}')
    # Log.debug(f'victor.id = {victor.id}')
    # Log.debug(f'victor.edges = {victor.edges}')
    # Log.debug(f'victor.payload = {victor.payload}')
