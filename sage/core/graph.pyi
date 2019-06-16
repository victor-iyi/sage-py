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

# Custom libraries.
from sage.core.base import Base
from sage.core.schema import Graph, Vertex, Query


class MultiKnowledgeGraph(Base):
    """MultiKnowledgeGraph stores multiple related graphs.

    Methods:

    Attributes:
        name (str)
        base (str)
        graphs (List[Graph])

    See Also:
        KnowledgeGraph - stores single entities & their relationship to other entities.
    """

    """Graph's identifier & the base name in file system."""
    name = ...  # type: str

    """Base file where"""
    base = ...  # type: str

    """List of related graphs."""
    graphs = ...  # type: List[Graph]

    def __init__(self, name: str, **kwargs): ...

    def __getitem__(self, item: Union[str,
                                      Tuple[str, str],
                                      Tuple[str, str, str],
                                      Tuple[str, Vertex]]) -> Union[Vertex, Graph, None]: ...

    def get(self, *item: Union[str,
                               Tuple[str, str],
                               Tuple[str, str, str],
                               Tuple[str, Vertex]]) -> Union[Query, Graph, None]: ...

    def add_graph(self, name: str, data_file: str = None) -> Graph: ...

    @classmethod
    def from_dir(cls: MultiKnowledgeGraph, path: str) -> MultiKnowledgeGraph: ...


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
            # Loads knowledge data to KnowledgeGraph.

    Attributes:
        label (str): Label given to Knowledge Graph for description.
        graph (Graph): Internal graph database managed by Knowledge Graph.

    See Also:
        MultiKnowledgeGraph - stores multiple related graphs.

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
    SUPPORTED_FORMATS = ...  # type: Tuple[str]

    """Label given to Knowledge Graph for description."""
    label = ...  # type: str

    """Internal graph database managed by Knowledge Graph."""
    graph = ...  # type: Graph

    """List of all Vertex objects in Graph."""
    vertices = ...  # type: List[Vertex]

    def __init__(self, name: str, data_file: str, **kwargs):
        """Knowledge Graph initialization.

        Args:
            name (str): Label given to Knowledge Graph for description.
            data_file (str): Path to Knowledge data.
        """

    def get(self, other: Union[str, Tuple[str, str], Vertex]) -> Query:
        """Returns a match object for `other` if Vertex is in Graph.

        Args:
            other (Union[str, Tuple[str, str], Vertex]):

        Returns:
            sqlalchemy.query.Query - SQLAlchemy's Query match object.
        """

    def __contains__(self, other: Union[str, Tuple[str, str], Vertex]) -> bool:
        """Checks if `other` is in Graph.

        Args:
            other (Union[str, Tuple[str, str], Vertex]):

        Returns:
            bool - True if it exists, False otherwise.
        """

    def __getitem__(self, other: Union[str, Tuple[str, str], Vertex]) -> Union[Vertex, None]:
        """Retrieve Vertex from Graph.

        Examples:
            ```python
            >>> g = Graph('sage')
            >>> victor = g.add_vertex('Victor', 'Person')
            >>> g[victor]
            <Vertex(label=Victor, schema=Person)>
            >>> g['Victor', 'Person']
            <Vertex(label=Victor, schema=Person)>
            >>> g[victor.id]
            <Vertex(label=Victor, schema=Person)>
            ```

        Args:
            other (Union[str, Tuple[str, str], Vertex]):

        Returns:
            Union[Vertex, None] - Returns Vertex object if `other` is found, None otherwise.
        """

    def __enter__(self) -> KnowledgeGraph: ...

    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...

    def add_triple(self, triples: Iterable[Tuple[str, str, str]]) -> None: ...

    @classmethod
    def fromfile(cls: KnowledgeGraph, path: str) -> KnowledgeGraph:
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

    def load(self, data: Union[List[Dict[str, Any]], Dict[str, Any]]) -> None:
        """Load knowledge data to Knowledge Graph.

        Args:
            data (Union[List[Dict[str, Any]], Dict[str, Any]]): Knowledge data to be loaded into Knowledge Graph.

        Returns:
            None
        """

    def depth_first(self, start: Vertex, visited: List[Vertex] = None, to_visit: List[Vertex] = None) -> Vertex:
        """Perform depth first search algorithm on Knowledge Graph.

        Args:
            start (Vertex): Start Vertex - Where to start search.
            visited (List[Vertex]): List of visited vertices.
            to_visit (List[Vertex]): List of vertices to be visited.

        Returns:
            Vertex - Vertex where goal is found.
        """

    def close(self) -> None:
        """Close database session & clean up resources.

        Returns:
            None
        """
