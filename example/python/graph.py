"""
    # from sage.core.utils import Log

    # class Node:
    #     ID_LEN = 8   # Max length of id tokens.
    #     NODES = []   # Keep track of all nodes created.

    #     def __init__(self, data: Any = None):
    #         self._id = secrets.token_hex(Node.ID_LEN)
    #         self.data = data

    #     @classmethod
    #     def from_data(cls, id: str, data):
    #         assert(len(id) == Node.ID_LEN)
    #         node = cls(data)
    #         node._id = id
    #         return node

    #     def __repr__(self):
    #         return f'{self.__class__.__name__}({self._id})'

    #     def __key(self):
    #         return self._id

    #     def __eq__(self, other):
    #         return (isinstance(self, type(other)) and
    #                 self.__key() == self.__key())

    #     def __hash__(self):
    #         return hash(self.__key())

    #     @property
    #     def id(self):
    #         return self._id


    # class Edge(Node):
    #     def __init__(self, data: Node, next: Node):
    #         super(Node).__init__(data)


    # class Graph:
    #     def __init__(self):
    #         self.graph = defaultdict(list)
    #         self.vertices = []
    #         self.edges = []

    #     def __repr__(self):
    #         return f'{self.__class__.__name__}({self.graph})'

    #     def __getitem__(self, node_id: str):
    #         return self.graph[node_id]

    #     def add_edge(self, src: Node, dest: Node):
    #         self.graph[src.data].append(dest.data)

    #     def get_edges(self):
    #         edges = []

    #         # for each node in graph
    #         for node in self.graph:
    #             # for each neighbor node of a single node
    #             for neighbor in self.graph[node]:
    #                 # if edge exists then append
    #                 edges.append((node, neighbor))

    #         return edges

    #     # def add_node(self, node: Node):
    #     #     self.graph[node.id] = node


    # class Predicate(Edge):
    #     def __init__(self, src: Node, dest: Node):
    #         super(Predicate, self).__init__(src, dest)
    #         self.src = src
    #         self.dest = dest


    # class Object(Edge):
    #     def __init__(self, data: Any = None):
    #         super(Object, self).__init__(data)


    # class Subject(Node):
    #     def __init__(self, data: Any = None):
    #         super(Subject, self).__init__(data)


    # if __name__ == '__main__':
    #     g = Graph()

    #     g.add_edge(Node('a'), Node('c'))
    #     g.add_edge(Node('b'), Node('c'))
    #     g.add_edge(Node('b'), Node('e'))
    #     g.add_edge(Node('c'), Node('d'))
    #     g.add_edge(Node('c'), Node('e'))
    #     g.add_edge(Node('c'), Node('a'))
    #     g.add_edge(Node('c'), Node('b'))
    #     g.add_edge(Node('e'), Node('b'))
    #     g.add_edge(Node('d'), Node('c'))
    #     g.add_edge(Node('e'), Node('c'))

    #     print(f'graph = {g}')
    #     node = Node('Victor')
    #     print(f'node = {node}')


    # class Object:
    #     def __new__(self, label, schema=None):
    #         # Check if label-schema combo exists.
    #         # Create a new Vertex if it doesn't exist.
    #         # If it exists, query label-schema combo from Graph
    #         # Return Vertex
    #         pass


    # class Subject:
    #     def __new__(self, label, schema=None):
    #         # Check if label-schema combo exists.
    #         # Create a new Vertex if it doesn't exist.
    #         # If it exists, query label-schema combo from Graph
    #         # Return Vertex
    #         pass


    # class Predicate:
    #     def __new__(self, label):
    #         return label


    # class Graph:

    #     Labels = []

    #     def __init__(self):
    #         self.graph = {}
    #         self.__n_vertices = 0

    #     def __repr__(self):
    #         return f'{self.__class__.__name__}({self.graph})'

    #     def __len__(self):
    #         return self.numVertices

    #     def __iter__(self):
    #         return iter(self.graph.values())

    #     def __contains__(self, node):
    #         return node in self.graph

    #     def add_vertex(self, key: Union[str, int], *, data: Any = None):
    #         self.__n_vertices += 1  # Increment number of vertices.
    #         newVertex = Vertex(key, data=data)
    #         self.graph[key] = newVertex
    #         return newVertex

    #     def get_vertex(self, node):
    #         if node in self.graph:
    #             return self.graph[node]
    #         return None

    #     def add_edge(self, f: Vertex, t: Vertex, predicate=0):
    #         # f - from (src)   t - to (dest)
    #         if f not in self.graph:
    #             _ = self.add_vertex(f)
    #         if t not in self.graph:
    #             _ = self.add_vertex(t)
    #         self.graph[f].add_neighbor(self.graph[t], Predicate(predicate))

    #     @property
    #     def vertices(self):
    #         return self.graph.keys()
"""
# # TODO: Write to a file or DB.
# store = defaultdict(list)


# def is_new_entry(label, schema):
#     if label in store:
#         return schema not in store[label]
#     return True


# class Vertex:
#     def __init__(self, label, schema=None, data=None, tmp=False):
#         if not tmp:
#             assert is_new_entry(label, schema), "Vertex already exist!"

#         self.label = label
#         self.schema = schema
#         # Can't be chaned once instantiated.
#         self.__id = secrets.token_hex(8)
#         self.payload = data      # Data contained by vertex.
#         self.type = None
#         self.connected_to = {}   # Connection to other vertex.
#         store[label].append(schema)

#     def __repr__(self):
#         return f'{self.__class__.__name__}({self.__id}, {self.label})'

#     def __str__(self):
#         return f'Vertex({self.id}): {str([x.id for x in self.connected_to])}'

#     def __eq__(self, other):
#         return isinstance(self, type(other)) and (self.__key() == other.__key())

#     def __key(self):
#         return (self.label, self.schema)

#     def __hash__(self):
#         return hash(self.__key())

#     @classmethod
#     def fromlabel(cls, label, schema):
#         inst = cls(label, schema, tmp=True)
#         return inst

#     def add_neighbor(self, nbr, predicate=None):
#         self.connected_to[nbr] = predicate

#     def get_predicates(self, nbr):
#         return self.connected_to[nbr]

#     @property
#     def id(self):
#         return self.__id

#     @property
#     def data(self):
#         return self.payload

#     @property
#     def connections(self):
#         return self.connected_to.keys()

#     @property
#     def predicates(self):
#         return self.connected_to.values()


# class Graph:
#     # label: [schema]
#     # TODO: Create a Graph Store DB.
#     store = defaultdict(list)

#     def __init__(self):
#         self.graph = {}
#         self.__n_vertices = 0

#     def __repr__(self):
#         return f'{self.__class__.__name__}({self.graph})'

#     def __len__(self):
#         return self.__n_vertices

#     def __getitem__(self, id):
#         return self.graph[id]

#     def get_vertex(self, label, *, schema=None):
#         tmp = Vertex.fromlabel(label, schema)
#         for _, v in self.graph.items():
#             if (tmp.label, tmp.schema) == (v.label, v.schema):
#                 return v
#         return None

#     @staticmethod
#     def is_new_entry(label, schema):
#         if label in Graph.store:
#             return schema not in Graph.store[label]
#         return True

#     def add_vertex(self, label, schema=None, data=None):
#         # TODO: Handle default schema.
#         try:
#             vertex = Vertex(label, schema, data)
#             self.graph[vertex.id] = vertex
#             self.__n_vertices += 1
#             return vertex
#         except AssertionError:
#             print("Vertex already exist")
#             return None
# Built-in libraries.
import secrets
from typing import Union, Tuple, List

# Third-party libraries.
from sqlalchemy import Column, ForeignKey, Integer, String, Text
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
    # schema = Column(String(250), default='http://schema.org/Thing')
    description = Column(Text, nullable=True)
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
    vertex = relationship("Vertex")

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


if __name__ == '__main__':
    triples = [
        ('Victor', 'age', 23),
        ('Victor', 'month', 'October'),
        ('Victor', 'bestFriends', 'Dara'),
        ('Dara', 'school', 'China'),
        ('Ope', 'school', 'USA'),
        ('Ope', 'field', 'Medical'),
        ('Victor', 'field', 'Science'),
        ('Dara', 'field', 'Engineering'),
    ]

    graph = Graph('sage')

    for triple in triples:
        vertex = graph.add_vertex(triple[0])
        Log.debug(vertex)
        # TODO: Add vertex connections (neighbors).

    Log.warn(graph.vertices)
