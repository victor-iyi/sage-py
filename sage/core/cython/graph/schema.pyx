"""Graph Database schema.

   @author
     Victor I. Afolabi
     Artificial Intelligence Expert & Researcher.
     Email: javafolabi@gmail.com | victor.afolabi@zephyrtel.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: schema.pyx
     Created on 13 May, 2019 @ 08:22 PM.

   @license
     MIT License
     Copyright (c) 2019. Victor I. Afolabi. All rights reserved.
"""
# Built-in libraries.
import json
import secrets

# Third-party libraries.
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.sql import operators
from sqlalchemy.orm import relationship
from sqlalchemy.types import TypeDecorator, VARCHAR
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy.ext.declarative import declarative_base

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
    # Vertex which the edge is connected to.
    vertex_id = Column(String(8), ForeignKey('vertex.id'))
    predicate = Column(String(256))
    # Source Vertex (`vertex`) is connected to `vertex_id`.
    vertex = relationship('Vertex', uselist=False, secondary='connection')

    def __init__(self, str vertex_id, str predicate):
        self.vertex_id = vertex_id
        self.predicate = predicate

    def __repr__(self):
        return f'<Edge({self.vertex_id}, {self.predicate})>'

    def __eq__(self, str other):
        return self.vertex_id == other


class Vertex(BaseSchema):
    __tablename__ = 'vertex'

    # Unique ID.
    id = Column(String(8), primary_key=True, unique=True,
                default=lambda: secrets.token_hex(8),
                nullable=False)
    label = Column(String(250), nullable=False)
    # FIXME: `default=https://schema.org/Thing`.
    schema = Column(String(250), nullable=False, default='Thing')
    # Serialized dictionary.
    payload = Column(JSON_Type)
    # List of connections to other Vertices.
    edges = relationship('Edge', secondary='connection')
    # Graph which vertex belongs to.
    graph_id = Column(String(8), ForeignKey('graph.id'))

    def __init__(self, str label = None, str schema = None, str graph_id=None, dict payload=None):
        self.label = label  # Key: name
        self.schema = schema  # Key: @type
        self.graph_id = graph_id  # Graph which vertex belongs to.
        self.payload = payload or dict()

    def __repr__(self):
        return f"<Vertex(label='{self.label}', schema='{self.schema}')>"

    def __key(self):
        return self.id, self.label, self.schema

    def __eq__(self, other) -> bool:
        cdef bint res
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

    def add_payload(self, payload):
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

    # Unique integer column.
    id = Column(String(8), primary_key=True, unique=True,
                default=lambda: secrets.token_hex(8),
                nullable=False)
    # Name of the graph.
    name = Column(String(250), unique=True)
    # Graph's description.
    description = Column(Text, nullable=True)

    def __init__(self, str name, str description=None):
        self.name = name
        self.description = description

    def __repr__(self):
        return f'<Graph({self.name})>'
