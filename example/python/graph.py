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
    path = File.join(FS.CACHE_DIR, 'graph/examples/avatar.jsonld')
    kg = KnowledgeGraph.fromfile(path)
    Log.info('Knowledge Graph')
    Log.debug(kg.vertices)

    # Working with Vertices.
    Log.info("Avatar:")
    avatar = kg['Avatar', 'Movie']
    Log.debug(f'avatar = {avatar}')
    Log.debug(f'avatar.id = {avatar.id}')
    Log.debug(f'avatar.payload = {avatar.payload}')
    Log.debug(f'avatar.edges = {avatar.edges}')

    # Working with Edges...
    Log.info("Director:")
    director = avatar.edges[0]
    Log.debug(f'director.id = {director.id}')
    Log.debug(f'director.vertex = {director.vertex}')
    Log.debug(f'director.vertex_id = {director.vertex_id}')
    Log.debug(f'kg[director.vertex_id] = {kg[director.vertex_id]}')
    Log.debug(f'director.predicate = {director.predicate}')
    Log.debug(f'avatar.payload = {avatar.payload}')

    # Testing Graph.
    # example = {
    #     "@type": 'Person',
    #     "name": 'Victor',
    #     "age": 22,
    #     "month": 'October',
    #     'bestFriends': [
    #         {
    #             "@type": 'Person',
    #             "name": 'Dara',
    #             "school": {
    #                 "@type": 'Place',
    #                 'name': 'China',
    #                 'population': 21341341234
    #             },
    #             "field": 'Engineering'
    #         },
    #         {
    #             "@type": 'Person',
    #             "name": 'Ope',
    #             "school": 'USA',
    #             "field": 'Medicine'
    #         }
    #     ],
    #     "field": "Science"
    # }
    # kg = KnowledgeGraph('example')
    # kg.load(data=example)
    # Log.debug(kg.vertices)
