# Built-in libraries.
import secrets
from collections import defaultdict
from typing import Any, Union

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
# TODO: Write to a file or DB.
store = defaultdict(list)


def is_new_entry(label, schema):
    if label in store:
        return schema not in store[label]
    return True


class Vertex:
    def __init__(self, label, schema=None, data=None, tmp=False):
        if not tmp:
            assert is_new_entry(label, schema), "Vertex already exist!"

        self.label = label
        self.schema = schema
        # Can't be chaned once instantiated.
        self.__id = secrets.token_hex(8)
        self.payload = data      # Data contained by vertex.
        self.type = None
        self.connected_to = {}   # Connection to other vertex.
        store[label].append(schema)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.__id}, {self.label})'

    def __str__(self):
        return f'Vertex({self.id}): {str([x.id for x in self.connected_to])}'

    def __eq__(self, other):
        return isinstance(self, type(other)) and (self.__key() == other.__key())

    def __key(self):
        return (self.label, self.schema)

    def __hash__(self):
        return hash(self.__key())

    @classmethod
    def fromlabel(cls, label, schema):
        inst = cls(label, schema, tmp=True)
        return inst

    def add_neighbor(self, nbr, predicate=None):
        self.connected_to[nbr] = predicate

    def get_predicates(self, nbr):
        return self.connected_to[nbr]

    @property
    def id(self):
        return self.__id

    @property
    def data(self):
        return self.payload

    @property
    def connections(self):
        return self.connected_to.keys()

    @property
    def predicates(self):
        return self.connected_to.values()


class Predicate:
    def __init__(self, pred: Any):
        self.pred = pred

    def __new__(self, pred: Any):
        # TODO: Maybe validate schema.
        self.pred = pred

    def __repr__(self):
        return f'{self.__class__.__name__}({self.pred})'


class Object(Vertex):
    def __init__(self, key: str, data=None):
        super(Object, self).__init__(key, data=data)


class Subject(Vertex):
    def __init__(self, key: str, data=None):
        super(Subject, self).__init__(key, data=data)


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

class Graph:
    # label: [schema]
    # TODO: Create a Graph Store DB.
    store = defaultdict(list)

    def __init__(self):
        self.graph = {}
        self.__n_vertices = 0

    def __repr__(self):
        return f'{self.__class__.__name__}({self.graph})'

    def __len__(self):
        return self.__n_vertices

    def __getitem__(self, id):
        return self.graph[id]

    def get_vertex(self, label, *, schema=None):
        tmp = Vertex.fromlabel(label, schema)
        for _, v in self.graph.items():
            if (tmp.label, tmp.schema) == (v.label, v.schema):
                return v
        return None

    @staticmethod
    def is_new_entry(label, schema):
        if label in Graph.store:
            return schema not in Graph.store[label]
        return True

    def add_vertex(self, label, schema=None, data=None):
        # TODO: Handle default schema.
        try:
            vertex = Vertex(label, schema, data)
            self.graph[vertex.id] = vertex
            self.__n_vertices += 1
            return vertex
        except AssertionError:
            print("Vertex already exist")
            return None


if __name__ == '__main__':
    data = [
        ('Victor', 'age', 23),
        ('Victor', 'month', 'October'),
        ('Victor', 'bestFriends', 'Dara'),
        ('Dara', 'school', 'China'),
        ('Ope', 'school', 'USA'),
        ('Ope', 'field', 'Medical'),
        ('Victor', 'field', 'Science'),
        ('Dara', 'field', 'Engineering'),
    ]

    graph = Graph()
    for (subject, predicate, obj) in data:
        try:
            vertex = graph.add_vertex(subject)
            if vertex is not None:
                try:
                    v = Vertex(obj)
                    vertex.add_neighbor(v, predicate)
                except AssertionError:
                    print(f'{obj} already exist!')
        except AssertionError:
            print(f'{subject} already exist!')

    print(graph)

    # Get the "Victor" with "None" schema.
    victor = graph.get_vertex('Victor', schema=None)
    print(victor.connections)
    print(victor.predicates)
