"""Graph database.

   @author
     Victor I. Afolabi
     Artificial Intelligence & Software Engineer.
     Email: javafolabi@gmail.com | victor.afolabi@zephyrtel.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: graph.py
     Created on 10 February, 2019 @ 17:03.

   @license
     Apache 2.0 License
     Copyright (c) 2019. Victor I. Afolabi. All rights reserved.
"""

from config import FS
from sage.core import File, Log, Graph

if __name__ == '__main__':
    path = File.join(FS.CACHE_DIR, 'graph/examples/avatar.jsonld')
    g = Graph(path=path)
    Log.debug('\n{:!s}'.format(g))
