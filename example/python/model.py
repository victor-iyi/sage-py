"""Model construction.

   @author
     Victor I. Afolabi
     Artificial Intelligence Expert & Researcher.
     Email: javafolabi@gmail.com | victor.afolabi@zephyrtel.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: model.py
     Created on 11 March, 2019 @ 06:31 AM.

   @license
     Apache 2.0 License
     Copyright (c) 2019. Victor I. Afolabi. All rights reserved.
"""

from sage.core import KnowledgeGraph, Log, File
from config.consts import FS

if __name__ == '__main__':
    kg = KnowledgeGraph('graph')
    path = File.join(FS.CACHE_DIR, 'graph/examples/creative-work.jsonld')
    data = KnowledgeGraph.read(path)
    kg.load(data)
    Log.debug(kg.graph.vertices)
    kg.close()
