"""Graph database schema.

   @author
     Victor I. Afolabi
     Artificial Intelligence Expert & Researcher.
     Email: javafolabi@gmail.com | victor.afolabi@zephyrtel.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: schema.py
     Created on 12 May, 2019 @ 23:21.

   @license
     MIT License
     Copyright (c) 2019. Victor I. Afolabi. All rights reserved.
"""
# Built-in libraries.
import json
import secrets
from typing import Union, Tuple, List, Dict, Any

# Third-party libraries.
from sqlalchemy import create_engine, Column, ForeignKey, Integer, String
from sqlalchemy.sql import operators
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.types import TypeDecorator, VARCHAR
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy.ext.declarative import declarative_base

# Custom libraries.
from sage.core.utils import Log

__all__ = [
    'Edge', 'Vertex', 'Graph'
]

BaseSchema = declarative_base()


class JSONEncodedDict(TypeDecorator):
    impl = VARCHAR

    def coerce_compared_value(self, op, value):
        if op in (operators.like_op, operators.notlike_op):
            return String()
        else:
            return self

    def process_bind_param(self, value, dialect):
        if value is not None:
            value = json.dumps(value)
        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            value = json.loads(value)
        return value

    def process_literal_param(self, value, dialect):
        return super(JSONEncodedDict, self).process_literal_param(value, dialect)

    @property
    def python_type(self):
        return super(JSONEncodedDict, self).python_type


JSON_Type = MutableDict.as_mutable(JSONEncodedDict)


class Connection(BaseSchema):
    __tablename__ = 'connection'
    edge_id = Column(Integer, ForeignKey('edge.id'), primary_key=True)
    vertex_id = Column(String(8), ForeignKey('vertex.id'), primary_key=True)


class Edge(BaseSchema):
    __tablename__ = 'edge'
    id = Column(Integer, primary_key=True)
    vertex_id = Column(String(8), ForeignKey('vertex.id'))
    predicate = Column(String(256))
    vertices = relationship('Vertex', secondary='connection')

    def __init__(self, vertex_id, predicate):
        self.vertex_id = vertex_id
        self.predicate = predicate

    def __repr__(self):
        return f'<Edge({self.vertex_id}, {self.predicate})>'

    def __eq__(self, other):
        return self.vertex_id == other


class Vertex(BaseSchema):
    __tablename__ = 'vertex'

    # Unique ID.
    id = Column(String(8), primary_key=True, unique=True,
                default=lambda: secrets.token_hex(8),
                nullable=False)
    label = Column(String(250), nullable=False)
    # default: https://schema.org/Thing
    schema = Column(String(250))
    # Serialized dictionary.
    payload = Column(JSON_Type)
    # List of connections to other Vertices.
    edges = relationship('Edge', secondary='connection')

    def __init__(self, label: str = None, schema: str = None, payload=None):
        self.label = label  # Key: name
        self.schema = schema  # Key: @type
        self.payload = payload or dict()

    def __repr__(self):
        return f"<Vertex(label='{self.label}', schema='{self.schema}')>"

    def __key(self):
        return self.id, self.label, self.schema

    def __eq__(self, other) -> bool:
        if isinstance(other, type(self)):
            # other is a Vertex
            res = self.__key() == other.__key()
        elif isinstance(other, tuple):
            assert len(other) == 2, f'Expected 2 got {len(other)}'
            res = (self.label, self.schema) == other
        elif isinstance(other, str):
            res = self.id == other
        else:
            raise TypeError('Inappropriate argument type.')

        return res

    def __hash__(self) -> int:
        return hash(self.__key())

    def add_neighbor(self, nbr, predicate=None):
        """Add new connection to the current Vertex object.

        Args:
            nbr (Vertex): Destination vertex, which current vertex
                is connected to.
            predicate (str): Description of their connection.

        Returns:
            Edge - Edge object containing connection details.
        """
        for edge in self.edges:
            if edge.vertex_id == nbr.id:
                return edge
        # Edge not found. Create new edge.
        edge = Edge(nbr.id, predicate=predicate)
        self.edges.append(edge)
        return edge

    def add_payload(self, payload: Dict[str, str]):
        for k, v in payload.items():
            # Key doesn't start with "@" & Value must be a primitive type.
            if not k.startswith('@') and isinstance(v, (int, float, str, bool)):
                self.payload[k] = v

    def get_connection(self, nbr):
        """Retrieve immediate connection to target vertex.

        Args:
            nbr (Vertex):

        Returns:
            Union[Edge, None] - Containing details about their connection.
        """
        for edge in self.edges:
            if edge.vertex_id == nbr.id:
                return edge

        # No connection.
        return None


class Graph(BaseSchema):
    __tablename__ = 'graph'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    vertex_id = Column(String(8), ForeignKey('vertex.id'))
    vertex = relationship("Vertex")

    def __init__(self, name: str, verbose: int = 1):
        self.name = name
        self.verbose = verbose
        self._sess = self._initialize_session()

    def _initialize_session(self):
        engine = create_engine(f'sqlite:///{self.name}.db')
        BaseSchema.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        sess = Session()
        return sess

    def __repr__(self):
        return f'Graph({self.name})'

    def get(self, other: Union[str, Tuple[str, str], Vertex]):
        # other is either (label, schema) or id or Vertex
        # Get vertex for (label, schema) or id
        # Return match object or Raise exception for bad input.
        if isinstance(other, str):
            # Treat as id.
            match = self._sess.query(Vertex). \
                filter(Vertex.id == other)
        elif isinstance(other, tuple):
            # Treat as (label, schema) combo.
            assert len(other) == 2, f'Expected 2 got {len(other)}'

            match = self._sess.query(Vertex). \
                filter(Vertex.label == other[0]). \
                filter(Vertex.schema == other[1])
        elif isinstance(other, Vertex):
            # Treat as Vertex object.
            match = self._sess.query(Vertex). \
                filter(Vertex.id == other.id). \
                filter(Vertex.label == other.label). \
                filter(Vertex.schema == other.schema)
        else:
            raise TypeError('Inappropriate argument type.')

        return match

    def __contains__(self, other: Union[str, Tuple[str, str], Vertex]) -> bool:
        match = self.get(other)
        return len(match.all()) > 0

    def __getitem__(self, other: Union[str, Tuple[str, str],
                                       Tuple[str, None], Vertex]) -> Union[Vertex, None]:
        # self[id], self[label, schema], self[label], self[Vertex]
        # Returns Vertex or None
        return self.get(other).one_or_none()

    def add_vertex(self, label: str, schema: str = None) -> Vertex:
        # Check if label-schema combo already exist.
        vertex = self[label, schema]

        if vertex is None:
            if self.verbose:
                Log.info(f'New Vertex: label: {label}, schema={schema}')
            # Create a new vertex.
            vertex = Vertex(label=label, schema=schema)
            # Add new vertex to DB.
            self._sess.add(vertex)
            self._sess.commit()

        # return created vertex
        return vertex

    def get_vertex(self, v: Union[str, Tuple[str, str], Vertex]) -> Union[Vertex, None]:
        return self[v]

    def add_edge(self, sub, obj, pred):
        # sub: Vertex - Subject
        # obj: Vertex - Object
        # pred: str - Predicate
        pass

    @property
    def vertices(self) -> List[Vertex]:
        return self._sess.query(Vertex).all()
