"""Implementation of Graph database.

   @author
     Victor I. Afolabi
     Artificial Intelligence Expert & Researcher.
     Email: javafolabi@gmail.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: graph.pyi
     Created on 09 May, 2019 @ 08:57 PM.

   @license
     Apache 2.0 License
     Copyright (c) 2019. Victor I. Afolabi. All rights reserved.
"""

# Built-in libraries.
from typing import Union, Tuple, List, Dict, Any, Iterable, Optional

# Custom libraries.
from sage.core.base import Base
from sage.core.schema import Graph, Vertex


class BaseKG(Base):
    """Supported file formats."""
    SUPPORTED_FORMATS = ...  # type: Tuple[str]

    """Label given to Knowledge Graph for reference."""
    label = ...  # type: str

    """Description of the Knowledge Graph."""
    description = ...  # type: str

    def __init__(self, name: str, description: Optional[str] = None, base_dir: Optional[str] = None,
                 data: Optional[Union[Dict[str, Any], Iterable[Dict[str, Any]]]] = None,
                 data_file: Optional[str] = None,
                 **kwargs):
        """Base Knowledge Graph initialization.

        Args:
            name (str): Label given to Knowledge Graph for description.
            description (str): Defaults to None. Knowledge graph's description.
            base_dir (str): Defaults to `FS.DATABASE_DIR`. Base directory to
                store graph database file.
            data (Union[Dict[str, Any], Iterable[Dict[str, Any]]]): Defaults to None.
                Knowledge data to be loaded into the Knowledge Graph.
            data_file (str): Defaults to None. Path to Knowledge data.

        Keyword Args:
            overwrite (bool): Defaults to False. Overwrite existing
                Knowledge graph with same name.

        Raises:
            FileNotFoundError: When `data_file` doesn't exist.
            AssertionError: Raised when `data_file` isn't of the
                supported format.
            NotImplementedError: Raised when unimplemented supported
                file format is encountered.
        """

    def __repr__(self) -> str: ...

    def __contains__(self, other: Union[str, Tuple[str, str]]) -> bool:
        """Checks if `other` is in Graph.

        Args:
            other (Union[str, Tuple[str, str]]):

        Returns:
            bool - True if it exists, False otherwise.
        """

    def __enter__(self) -> KnowledgeGraph: ...

    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...

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

    @staticmethod
    def read(path: str) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
        """Read data from a given file.

        Args:
            path (str): Path to file containing Linked data. File must be supported
                file formats. See `KnowledgeGraph.SUPPORTED_FORMATS`.

        Returns:
            Union[List, Dict[str, Any]] - Linked data in a list or dict data structure.
        """

    def add_edge(self, sub, obj, pred):
        """Add new edge to graph.

        Args:
            sub ():
            obj ():
            pred ():

        Returns:

        """

    def add_triple(self, triples: Iterable[Tuple[str, str, str]]) -> None: ...

    def add_vertex(self, label: str, schema: Optional[str] = None, graph_id: Optional[str] = None) -> Vertex:
        """Add a new Vertex/Node to the Graph if it doesn't already exist.

        Args:
            label (str):
            schema (str): Defaults to None.
            graph_id (str): Defaults to None.

        Returns:
            Vertex - Added vertex.
        """

    def close(self) -> None:
        """Close database session & clean up resources.

        Returns:
            None
        """

    def get_graph_by_name(self, graph_name: str) -> Union[Graph, None]:
        """Retrieve graph object by graph's name.

        Args:
            graph_name (str): Name of graph to lookup.

        Returns:
            Union[Graph, None] - Graph instance if graph name
                is found in the db.
        """

    def get_vertex_by_label(self, label: str) -> Union[List[Vertex], None]:
        """Retrieve all vertex objects by label.

        Args:
            label (str): Vertex label.

        Returns:
            Union[Graph, None] - Graph instance if graph name
                is found in the db.
        """

    def get_vertex(self, vertex_id: Optional[str] = None,
                   label: Optional[str] = None,
                   schema: Optional[str] = None,
                   graph_id: Optional[str] = None) -> Union[Vertex, None]:
        """Retrieve a named vertex from the graph.

        Args:
            vertex_id (str): Defaults to None. Vertex ID,
            label (str): Defaults to None.
            schema: (str): Defaults to None.
            graph_id (str): Defaults to None.

        Returns:
            Union[Vertex, None] - Returns vertex if vertex exists in Graph otherwise, None.
        """

    def load(self, data: Union[List[Dict[str, Any]], Dict[str, Any]], graph_id: str) -> None:
        """Load knowledge data to Knowledge Graph.

        Args:
            data (Union[List[Dict[str, Any]], Dict[str, Any]]): Knowledge data to
                be loaded into Knowledge Graph.
            graph_id (str): Graph id to load vertices to. Defaults to the default graph.

        Returns:
            None
        """


class MultiKnowledgeGraph(Base):
    """MultiKnowledgeGraph stores multiple related graphs.

    Methods:
        def __init__(self, name: str, **kwargs):
            # Initialize an empty multiple knowledge graph.

        def __getitem__(self, item: Union[str,
                                      Tuple[str, str],
                                      Tuple[str, str, str],
                                      Tuple[str, Vertex]]) -> Union[Vertex, Graph, None]:
            # Getting specific graph or vertex of a graph from the Knowledge Graph.


    Attributes:
        name (str): Graph's identifier & the base name in file system.
        base (str): Base file where graph db is stored.
        graphs (List[Graph]): List of related graphs.

    Raises:
        FileNotFoundError - Occurs when a file is not found.
        AssertionError - Occurs when incorrect inputs are encountered.
        KeyError - Occurs during graph lookup.
        TypeError - Occurs when getting vertex or graph from Knowledge Graph.

    Examples:
          ```python
          >>> from config.consts import FS
          >>> from sage.core.utils import Log, File

          >>> path = File.join(FS.GRAPH_DIR, 'schema-org')
          >>> Log.warn(f'Loading graphs in `{path}`')

          >>> # Load multiple graphs from a base directory.
          >>> mkg = MultiKnowledgeGraph.from_dir(path)
          >>> Log.debug(mkg)

          >>> # Display all graphs associated with mkg.
          >>> Log.info(f'Display all graphs ({len(mkg.graphs)}).')
          >>> Log.debug(mkg.graphs)

          >>> # Getting a single entity from a named graph.
          >>> Log.info(f'Getting `medical_condition` graph.')
          >>> node = mkg['medical_condition', 'Stable angina', 'MedicalCondition']
          >>> Log.debug(node)
          ```
    See Also:
        KnowledgeGraph - stores single entities & their relationship to other entities.
    """

    """Graph's identifier & the base name in file system."""
    label = ...  # type: str

    """Base file where graph db is stored."""
    base = ...  # type: str

    """List of related graphs."""
    graphs = ...  # type: List[Graph]

    def __init__(self, name: str, **kwargs):
        """Initialize an empty multiple knowledge graph.

        Args:
            name (str): Identifier for the graph.

        Keyword Args:
            See `sage.core.Base` for more options.
        """

    def __getitem__(self, item: Union[str,
                                      Tuple[str, str],
                                      Tuple[str, str, str],
                                      Tuple[str, Vertex]]) -> Union[Vertex, Graph, None]:
        """Getting specific graph or vertex of a graph from the Knowledge Graph.

        Args:
            item (Union[str, Tuple[str, str], Tuple[str, str, str], Tuple[str, Vertex]]): Query
                the Knowledge Graph with the graph name and one of Vertex ID, Vertex name
                & schema or Vertex object.

        Returns:
            Union[Vertex, Graph, None] - Instance of a Graph if a single string is provided.
                Returns instance of a Vertex or None for other combination of arguments.
        """

    def get(self, *item: Union[str,
                               Tuple[str, str],
                               Tuple[str, str, str],
                               Tuple[str, Vertex]]) -> Union[Vertex, Graph, None]:
        """Getting specific graph or vertex of a graph from the Knowledge Graph.

        Args:
            item (Union[str, Tuple[str, str], Tuple[str, str, str], Tuple[str, Vertex]]): Query
                the Knowledge Graph with the graph name and one of Vertex ID, Vertex name &
                schema or Vertex object.

        Returns:
            Union[Query, Graph, None] - Instance of a Graph if a single string is provided.
                Returns instance of SQL-Alchemy Query or None for other combination of
                arguments.
        """

    def add_graph(self, name: str, data_file: str = None) -> Graph:
        """Adds a new graph into the Knowledge Graph with optional data loaded.

        Args:
            name (str): Graph name identifier.
            data_file (str): Defaults to None. Path to a loadable data into
                the graph. File must be of supported format.
                See `Graph.SUPPORTED_FORMAT`.

        Returns:
            Graph - Returns created graph.
        """

    @classmethod
    def from_dir(cls: MultiKnowledgeGraph, path: str) -> MultiKnowledgeGraph:
        """Creates a multiple graphs from data inferred from files in directory.

        Args:
            path (str): Path to a directory containing files to be loaded.

        Returns:
            MultiKnowledgeGraph - An instance of multiple knowledge graph
                with graph data.
        """


class KnowledgeGraph(BaseKG):
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

    """List of all Vertex objects in default Graph."""
    vertices = ...  # type: List[Vertex]

    def __init__(self, name: str, description: Optional[str] = None, base_dir: Optional[str] = None,
                 data: Optional[Union[Dict[str, Any], Iterable[Dict[str, Any]]]] = None,
                 data_file: Optional[str] = None,
                 **kwargs):
        """Knowledge Graph initialization.

        Args:
            name (str): Label given to Knowledge Graph for description.
            description (str): Defaults to None. Knowledge graph's description.
            base_dir (str): Defaults to `FS.DATABASE_DIR`. Base directory to
                store graph database file.
            data (Union[Dict[str, Any], Iterable[Dict[str, Any]]]): Defaults to None.
                Knowledge data to be loaded into the Knowledge Graph.
            data_file (str): Defaults to None. Path to Knowledge data.

        Keyword Args:
            overwrite (bool): Defaults to False. Overwrite existing
                Knowledge graph with same name.

        Raises:
            FileNotFoundError: When `data_file` doesn't exist.
            AssertionError: Raised when `data_file` isn't of the
                supported format.
            NotImplementedError: Raised when unimplemented supported
                file format is encountered.
        """

    @classmethod
    def fromfile(cls: KnowledgeGraph, path: str, description: str = None, **kwargs) -> KnowledgeGraph:
        """Create KnowledgeGraph instance from file.

        Args:
            path (str): Path to a file. File must be supported file formats.
                See `KnowledgeGraph.SUPPORTED_FORMATS`.
            description (str): Defaults to None. Knowledge Graph's description.

        Keyword Args:
            overwrite (bool): Defaults to False. Overwrite existing database file.

        Returns:
            KnowledgeGraph - An instance of knowledge graph, loaded with data
                from file in the given path.
        """

    def get(self, other: Union[str, Tuple[str, str], Vertex]) -> Union[Vertex, None]:
        """Returns a vertex object if Vertex is in Graph.

        Args:
            other (Union[str, Tuple[str, str], Vertex]):

        Returns:
            Union[Vertex, None] - Returns a vertex object, or None otherwise.
        """
