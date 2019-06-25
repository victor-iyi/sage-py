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
from typing import Union, Tuple, List, Dict

# Third-party libraries.
from sqlalchemy import create_engine, Column, ForeignKey, Integer, String
from sqlalchemy.sql import operators
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.types import TypeDecorator, VARCHAR
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy.ext.declarative import declarative_base

# Custom libraries.
from config.consts import FS
from sage.core.utils import File, Log

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
    # default: https://schema.org/Thing
    schema = Column(String(250))
    # Serialized dictionary.
    payload = Column(JSON_Type)
    # List of connections to other Vertices.
    edges = relationship('Edge', secondary='connection')

    def __init__(self, str label = None, str schema = None, dict payload=None):
        self.label = label  # Key: name
        self.schema = schema  # Key: @type
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
    # Supported file formats.
    SUPPORTED_FORMATS = ('json', 'jsonld', 'json-ld',
                         'rdf', 'xml', 'nt')

    __tablename__ = 'graph'
    # Unique integer column.
    id = Column(Integer, primary_key=True)
    # Name of the graph.
    name = Column(String(250))
    # Foreign key to Vertex.
    vertex_id = Column(String(8), ForeignKey('vertex.id'))
    # Relational mapper to Vertex.
    vertex = relationship("Vertex")

    def __init__(self, str name, str base=None, data=None,
                 str data_file=None, bint verbose=1):
        # Graph's name.
        self.name = name
        # Base directory to save graph db.
        self.base = base or FS.DATABASE_DIR
        # Verbosity.
        self.verbose = verbose

        self._sess = self._initialize_session()

        if data_file is not None:
            data = Graph.read(data_file)

        # Load data if available.
        if data is not None:
            self.load(data)

    def _initialize_session(self):
        import os
        # Save current dir to switch back later.
        cdef str cur_dir = os.path.abspath(os.curdir)

        # Switch directory to base dir.
        os.chdir(self.base)

        # Create DB engine & session.
        engine = create_engine(f'sqlite:///{self.name}.db')
        BaseSchema.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        sess = Session()

        # Switch back to cur dir.
        os.chdir(cur_dir)

        return sess

    def __repr__(self):
        return f'<Graph({self.name})>'

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

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._sess.close()

    def load(self, data):
        cdef:
            str label, nbr_label

        # New Scope.
        if isinstance(data, dict):
            # Add vertex in current scope to graph.
            label = data.get('name', 'Unknown')
            schema = data.get('@type', 'Thing')
            schema = (', '.join(schema) if isinstance(schema, list)
                      else schema)
            vertex = self.add_vertex(label, schema)

            # Loop through the key-value pairs of current vertex.
            for k, v in data.items():
                # Key doesn't start with "@" & Value must be a primitive type.
                if not k.startswith('@') and isinstance(v, (int, float, str, bool)):
                    # Add necessary payloads.
                    vertex.payload[k] = v
                # A new list of scopes.
                elif isinstance(v, (list, tuple)):
                    for item in v:  # Loop through the list.
                        # Assert that we have another scope (neighboring scope).
                        if isinstance(item, dict):
                            nbr_label = item.get('name', 'Unknown')
                            nbr_schema = item.get('@type', 'Thing')
                            nbr_schema = (', '.join(nbr_schema)
                                          if isinstance(nbr_schema, list)
                                          else nbr_schema)
                            nbr = self.add_vertex(nbr_label, nbr_schema)
                            vertex.add_neighbor(nbr, predicate=k)
                        # Visit neighboring scope.
                        self.load(item)

                elif isinstance(v, dict):
                    # Direct neighboring scope.
                    nbr_label = v.get('name', 'Unknown')
                    nbr_schema = v.get('@type', 'Thing')
                    nbr_schema = (', '.join(nbr_schema)
                                  if isinstance(nbr_schema, list)
                                  else nbr_schema)
                    nbr = self.add_vertex(nbr_label, nbr_schema)
                    vertex.add_neighbor(nbr, predicate=k)
                    # Visit direct neighboring scope.
                    self.load(v)

        elif isinstance(data, (list, tuple)):
            # In case scope starts with a list.
            for item in data:
                self.load(item)

    @staticmethod
    def read(str path):
        # Check if file exists.
        if not File.is_file(path):
            raise FileNotFoundError(f'{path} was not found.')

        # Get the file extension.
        cdef str ext = File.ext(path)

        # Supported file formats.
        if ext not in Graph.SUPPORTED_FORMATS:
            raise AssertionError(f'Expected one of: {Graph.SUPPORTED_FORMATS}.'
                                 f' Got {ext}')

        if ext in ('json', 'jsonld', 'json-ld'):
            # Load JSON-LD file.
            with open(path, mode='r', encoding='utf-8') as f:
                return json.loads(f.read())
        else:
            # TODO(victor-iyiola): Support for RDF/XML & n-triples.
            Log.warn('RDF/XML & n-triple not yet supported.')
            return NotImplemented

    def add_vertex(self, str label, str schema = None) -> Vertex:
        # Check if label-schema combo already exist.
        vertex = self[label, schema]

        if vertex is None:
            # Create a new vertex.
            vertex = Vertex(label=label, schema=schema)
            # Add new vertex to DB.
            self._sess.add(vertex)
            self._sess.commit()

        # return created vertex
        return vertex

    def get_vertex(self, v: Union[str, Tuple[str, str], Vertex]) -> Union[Vertex, None]:
        return self[v]

    def add_edge(self, edge):
        pass

    def close(self):
        self._sess.close()

    @property
    def vertices(self) -> List[Vertex]:
        return self._sess.query(Vertex).all()
