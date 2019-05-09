# Built-in libraries.
import secrets
from typing import Union, Tuple, List

# Third-party libraries.
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

# Custom libraries.
from sage.core.utils import Log

Base = declarative_base()


class Vertex(Base):
    __tablename__ = 'vertex'

    id = Column(String(8), primary_key=True, unique=True,
                default=lambda: secrets.token_hex(8),
                nullable=False)
    label = Column(String(250), nullable=False)
    schema = Column(String(250))

    # neighbors [{vertex: predicate}]

    def __init__(self, label: str = None, schema: str = None):
        self.label = label
        self.schema = schema
        self.edges = {}  # {id: Vertex}

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

    def hash(self) -> int:
        return hash(self.__key())

    def add_neighbor(self, nbr, predicate=None):
        pass

    def get_predicate(self, nbr):
        pass


class Graph(Base):
    __tablename__ = 'graph'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    vertex_id = Column(String(8), ForeignKey('vertex.id'))
    vertex = relationship(Vertex)

    def __init__(self, name: str, verbose: int = 1):
        self.name = name
        self.verbose = verbose
        self._sess = self._initialize_session()

    def _initialize_session(self):
        engine = create_engine(f'sqlite:///{self.name}.db')
        Base.metadata.create_all(engine)
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

    def __getitem__(self, other: Union[str, Tuple[str, str], Vertex]) -> Union[Vertex, None]:
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

