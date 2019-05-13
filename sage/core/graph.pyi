"""Knowledge Graph schema.

   @author
     Victor I. Afolabi
     Artificial Intelligence Expert & Researcher.
     Email: javafolabi@gmail.com | victor.afolabi@zephyrtel.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: graph.pyi
     Created on 09 May, 2019 @ 08:57 PM.

   @license
     Apache 2.0 License
     Copyright (c) 2019. Victor I. Afolabi. All rights reserved.
"""

# Built-in libraries.
from typing import Union, Tuple, List, Dict, Any, Iterable
from sage.core.base import Base
from sage.core.schema import Graph


class KnowledgeGraph(Base):
    """KnowledgeGraph stores entities & relationship to other entities.

    Methods:
        def __init__(self, name: str): ...

        def add_triple(self, triples: Iterable[Tuple[str, str, str]]) -> None:
            #

        @classmethod
        def fromfile(cls, path: str) -> KnowledgeGraph:
            # Create KnowledgeGraph instance from file.

        @staticmethod
        def read(path: str) -> Union[List, Dict[str, Any]]:
            # Read data from a given file.

        def load(self, data: Union[List[Dict[str, Any]], Dict[str, Any]]) -> None: ...

    Attributes:
        label (str): Label given to Knowledge Graph for description.
        graph (Graph): Internal graph database managed by Knowledge Graph.

    Examples:
        ```python
        >>> from config.consts import FS
        >>> from sage.core.utils import File, Log
        >>>
        >>> # Loading Graph data from File.
        >>> path = File.join(FS.CACHE_DIR, 'graph/examples/avatar.jsonld')
        >>>
        >>> kg = KnowledgeGraph.fromfile(path)
        INFO     | New Vertex: label: Avatar, schema=Movie
        INFO     | New Vertex: label: James Cameron, schema=Person
        >>> Log.debug(kg.graph.vertices)
        DEBUG    | [<Vertex(label='Avatar', schema='Movie')>, <Vertex(label='James Cameron', schema='Person')>]
        >>>
        >>> avatar = kg.graph['Avatar', 'Movie']
        >>> Log.debug(f'avatar = {avatar}')
        DEBUG    | avatar = <Vertex(label='Avatar', schema='Movie')>
        >>> Log.debug(f'avatar.payload = {avatar.payload}')
        DEBUG    | avatar.payload = {'name': 'Avatar', 'genre': 'Science Fiction', 'trailer': 'https://example.com/trailer.mp4'}
        >>> Log.debug(f'avatar.edges = {avatar.edges}')
        DEBUG    | avatar.edges = [<Edge(e147c670075ef62b, director)>]
        ```
    """

    """Supported file formats."""
    SUPPORTED_FORMATS = ...  # type: tuple

    """Label given to Knowledge Graph for description."""
    label = ...  # type: str

    """Internal graph database managed by Knowledge Graph."""
    graph = ...  # type: Graph

    def __init__(self, name: str):
        """Knowledge Graph initialization.

        Args:
            name (str): Label given to Knowledge Graph for description.
        """

    def add_triple(self, triples: Iterable[Tuple[str, str, str]]) -> None: ...

    @classmethod
    def fromfile(cls, path: str) -> KnowledgeGraph:
        """Create KnowledgeGraph instance from file.

        Args:
            path (str): Path to a file. File must be supported file formats.
                See `KnowledgeGraph.SUPPORTED_FORMATS`.

        Returns:
            KnowledgeGraph - An instance of knowledge graph, loaded with data
                from file in the given path.
        """

    @staticmethod
    def read(path: str) -> Union[List, Dict[str, Any]]:
        """Read data from a given file.

        Args:
            path (str): Path to file containing Linked data. File must be supported
                file formats. See `KnowledgeGraph.SUPPORTED_FORMATS`.

        Returns:
            Union[List, Dict[str, Any]] - Linked data in a list or dict data structure.
        """

    def load(self, data: Union[List[Dict[str, Any]], Dict[str, Any]]) -> None: ...
