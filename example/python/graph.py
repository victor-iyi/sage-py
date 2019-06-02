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
    path = File.join(FS.CACHE_DIR, 'graph/examples/new-york.jsonld')
    kg = KnowledgeGraph.fromfile(path)
    Log.info('Knowledge Graph')
    Log.debug(kg.vertices)
    thing = kg['Unknown', 'Thing']
    Log.debug(f'thing = {thing}')
    Log.info("Payload:")
    Log.pretty(thing.payload)
    Log.info("Edges:")
    Log.debug(f'thing.edges = {thing.edges}')
    for edge in thing.edges:
        Log.debug(f'edge = {edge}')

    # Close connection.
    kg.close()
