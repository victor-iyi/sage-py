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
from typing import Union, Tuple, List, Dict, Optional
from sqlalchemy.ext.declarative import declarative_base

# TypeVars.
BaseSchema = declarative_base()


class Edge(BaseSchema):
    """Edge which is describes the connection between one Vertex & it's neighbors.

    Methods:
        def __init__(self, vertex_id: str, predicate: str): ...

        def __repr__(self) -> str: ...

        def __eq__(self, other: str) -> bool: ...

    Attributes:
        __tablename__ (str): Table name.
        id (int): Table's primary key.
        vertex_id (str): Vertex which the edge is connected to.
        predicate (str): Describing the connection `vertex` has with `vertex_id`.
        vertex (Vertex): Source Vertex (`vertex`) is connected to `vertex_id`.

    """

    """Table name."""
    __tablename__ = ...  # type: str

    """Table's primary key."""
    id = ...  # type: int

    """Vertex which the edge is connected to."""
    vertex_id = ...  # type: str

    """Describing the connection `vertex` has with `vertex_id`."""
    predicate = ...  # type: str

    """Source Vertex (`vertex`) is connected to `vertex_id`."""
    vertex = ...  # type: Vertex

    def __init__(self, vertex_id: str, predicate: Optional[str]): ...

    def __repr__(self) -> str: ...

    def __eq__(self, other: str) -> bool: ...


class Graph(BaseSchema):
    """Graph database Schema.

    Methods:
        def __init__(self, name: str, base: Optional[str] = ...,
                    verbose: Optional[int] = 1):
            # Graph.__init__

        def __repr__(self) -> str:...

    Attributes:
        __tablename__ (str): DB table name.
        id (int): Unique integer primary key.
        name (str): Graph name - DB Storage name.
        description (str): Graph description.
    """

    """DB table name."""
    __tablename__ = 'graph'

    """Unique integer primary key."""
    id = ...  # type: str

    """Graph name - DB Storage name."""
    name = ...  # type: str

    """Graph description."""
    description = ...  # type: Optional[str]

    def __init__(self, name: str, description: Optional[str] = ...):
        """Create a new instance of Graph.

        Args:
            name (str): A descriptive name used to save Graph DB in memory.
            description (Optional[str]): Defaults to `None`. Graph's description.
        """

    def __repr__(self) -> str:
        """Pretty object representation of class."""


class Vertex(BaseSchema):
    """Vertex (or Node) - representing each Entity in Graph.

    Methods:
        def __init__(self, label: str = None, schema: str = None):
            # Vertex initialization.

        def __repr__(self) -> str:
            # Object representation of Vertex.

        def __key(self) -> Tuple[str, str, str]:
            # Vertex's hashing key.

        def __eq__(self, other: Union[str, Tuple[str, str], Vertex]) -> bool:
            # Equality comparision operator overload.

        def __hash__(self) -> int:
            # Vertex's hashing function.

        def add_neighbor(self, nbr, predicate=None):...

        def get_predicate(self, nbr):...

    Attributes:
        __tablename__ (str): Table name.
        id (str): Unique 8-bit token assigned to each Vertex.
        label (str): Vertex label.
        schema (str): Vertex schema.
    """

    """Table name"""
    __tablename__ = ...  # type: str

    """Unique 8-bit token assigned to each Vertex."""
    id = ...  # type: str

    """Vertex label."""
    label = ...  # type: Optional[str]

    """Vertex schema."""
    schema = ...  # type: Optional[str]

    """Graph ID - A foreign key that references the Graph this vertex belongs to."""
    graph_id = ...  # type: str

    """Payload which current vertex carries. Contains information about Vertex."""
    payload = ...  # type: Optional[Dict[str, str]]

    """Connection of Vertex to other Vertex in the Graph."""
    edges = ...  # type: List[Edge]

    def __init__(self, label: str, schema: str, graph_id: str, payload: Dict[str, str] = ...):
        """Create a new instance of a Vertex.

        Args:
            label (str): Defaults to None. Vertex label.
            schema (str): Defaults to None. Vertex schema.
            graph_id (str): Defaults to None. Graph ID that references the
                Graph this vertex belongs to.
            payload (Dict[str, str]): Defaults to empty dictionary. Other
                information to be stored in vertex.
        """

    def __repr__(self) -> str:
        """Object representation of Vertex"""

    def __key(self) -> Tuple[str, str, str]:
        """Vertex's hashing key.

        Returns:
            Tuple[str, str, str] - Id, Label, Schema.
        """

    def __eq__(self, other: Union[str, Tuple[str, str], Vertex]) -> bool:
        """Equality comparision operator overload.

        Args:
            other (Union[str, Tuple[str, str], Vertex]): Unique vertex token,
                tuple of (label, schema) combo or Vertex object.

        Returns:
            bool - True if other matches current Vertex.
        """

    def __hash__(self) -> int:
        """Vertex's hashing function.

        Returns:
            int - Hash based on Vertex.__key()
        """

    def add_neighbor(self, nbr: Vertex, predicate: Optional[str] = None) -> Edge:
        """Add new connection to the current Vertex object.

        Args:
            nbr (Vertex): Destination vertex, which current vertex
                is connected to.
            predicate (str): Description of their connection.

        Returns:
            Edge - Edge object containing connection details.
        """

    def add_payload(self, payload: Dict[str, str]) -> None:
        """Add payload to current Vertex. Appends if not already exits.

        Args:
            payload (Dict[str, str]): Contains information conveyed by current Vertex.

        Returns:
            None
        """

    def get_connection(self, nbr: Vertex) -> Union[Edge, None]:
        """Retrieve immediate connection to target vertex.

        Args:
            nbr (Vertex): Vertex to get connected edges from.

        Returns:
            Union[Edge, None] - Returns edge or None if it doesn't exits.
        """

    def get_predicate(self, nbr: Vertex) -> str:
        """Get connection of current Vertex with a neighboring Vertex.

        Args:
            nbr (Vertex): Get connection of current Vertex with this
                neighboring Vertex.

        Returns:
            str - Connection predicate (description).
        """
