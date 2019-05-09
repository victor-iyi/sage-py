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
from typing import Union, Tuple, List, TypeVar

Session = TypeVar('Session')
Query = TypeVar('Query')
Base = TypeVar('Base')


class Vertex(Base):
    """Vertex

    """

    """Table name"""
    __tablename__ = ...  # type: str

    """Unique 8-bit token assigned to each Vertex."""
    id = ...  # type: str

    """Vertex label."""
    label = ...  # type: str

    """Vertex schema."""
    schema = ...  # type: str

    def __init__(self, label: str = None, schema: str = None):
        """Vertex.__init__

        Args:
            label (str): Defaults to None.
            schema (str): Defaults to None.
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

    def hash(self) -> int:
        """Vertex's hashing function.

        Returns:
            int - Hash based on Vertex.__key()
        """

    def add_neighbor(self, nbr, predicate=None):
        """

        Args:
            nbr ():
            predicate ():

        Returns:

        """

    def get_predicate(self, nbr):
        """

        Args:
            nbr ():

        Returns:

        """


class Graph(Base):
    """Graph

    """

    """DB table name."""
    __tablename__ = 'graph'

    """Unique integer primary key."""
    id = ...  # type: int

    """Graph name - DB Storage name."""
    name = ...  # type: str

    """Vertex Id foreign key."""
    vertex_id = ...  # type: int

    """Vertex relational mapper."""
    vertex = ...  # type: List[Vertex]

    """List of Vertex objects in Graph."""
    vertices = ...  # type: List[Vertex]

    def __init__(self, name: str, verbose: int = 1):
        """Graph.__init__

        Args:
            name (str): A descriptive name used to save Graph DB in memory.
            verbose (int): Defaults to 1.
        """

    def _initialize_session(self) -> Session:
        """Initializes SQLAlchemy Engine & initializes db session.

        Returns:
            Session - DB Session to save & query DB.
        """

    def __repr__(self) -> str:
        """Pretty object representation of class."""

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
            >>> g['Victor', 'Person']
            >>> g[victor.id]
            ```

        Args:
            other (Union[str, Tuple[str, str], Vertex]):

        Returns:
            Union[Vertex, None] - Returns Vertex object if `other` is found, None otherwise.
        """

    def add_vertex(self, label: str, schema: str = None) -> Vertex:
        """Add a new Vertex/Node to the Graph if it doesn't already exist.

        Args:
            label (str):
            schema (str): Defaults to None.

        Returns:
            Vertex - Added vertex.
        """

    def get_vertex(self, v: Union[str, Tuple[str, str], Vertex]) -> Union[Vertex, None]:
        """Retrieve a named vertex from the graph.

        Args:
            v (Union[str, Tuple[str, str], Vertex]): Vertex ID,
                (label, schema) combo or Vertex object.

        Returns:
            Union[Vertex, None] - Returns vertex if vertex exists in Graph otherwise, None.
        """

    def add_edge(self, sub, obj, pred):
        """

        Args:
            sub ():
            obj ():
            pred ():

        Returns:

        """
