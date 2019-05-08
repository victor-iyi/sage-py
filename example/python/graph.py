# Built-in libraries.
import secrets
from collections import defaultdict
from typing import Any, Union

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

class Vertex:
    def __init__(self, key: Union[str, int], data: Any = None):
        self.id = key
        self.payload = data
        self.connectedTo = {}

    def __repr__(self):
        return f'{self.__class__.__name__}({self.id})'

    def addNeighbor(self, nbr, predicate=None):
        self.connectedTo[nbr] = predicate

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getPredicates(self, nbr):
        return self.connectedTo[nbr]


class Predicate:
    def __init__(self, pred: Any):
        self.pred = pred

    def __repr__(self):
        return f'{self.__class__.__name__}({self.pred})'

    def __new__(self, pred: Any):
        # TODO: Maybe validate schema.
        self.pred = pred


class Object(Vertex):
    def __init__(self, key: str, data=None):
        super(Object, self).__init__(key, data=data)


class Subject(Vertex):
    def __init__(self, key: str, data=None):
        super(Subject, self).__init__(key, data=data)


class Graph:
    def __init__(self):
        self.graph = {}
        self.numVertices = 0

    def __repr__(self):
        return f'{self.__class__.__name__}({self.graph})'

    def addVertex(self, key):
        self.numVertices += 1  # Increment number of vertices.
        newVertex = Vertex(key)
        self.graph[key] = newVertex
        return newVertex

    def getVertex(self, node):
        if node in self.graph:
            return self.graph[node]
        return None

    def __contains__(self, node):
        return node in self.graph

    def addEdge(self, f, t, predicate=0):
        # f - from (src)   t - to (dest)
        if f not in self.graph:
            _ = self.addVertex(f)
        if t not in self.graph:
            _ = self.addVertex(t)
        self.graph[f].addNeighbor(self.graph[t], Predicate(predicate))

    def getVertices(self):
        return self.graph.keys()

    def __iter__(self):
        return iter(self.graph.values())


if __name__ == '__main__':
    graph = Graph()
    tokens = [secrets.token_hex(8) for _ in range(6)]
    for key in tokens:
        graph.addVertex(key)

    print(graph)
    graph.addEdge(tokens[0], tokens[1], 5)
    graph.addEdge(tokens[0], tokens[5], 2)
    graph.addEdge(tokens[1], tokens[2], 4)
    graph.addEdge(tokens[2], tokens[3], 9)
    graph.addEdge(tokens[3], tokens[4], 7)
    graph.addEdge(tokens[3], tokens[5], 3)
    graph.addEdge(tokens[4], tokens[0], 1)
    graph.addEdge(tokens[5], tokens[4], 8)
    graph.addEdge(tokens[5], tokens[2], 1)

    for v in graph:
        for w in v.getConnections():
            print("( %s , %s )" % (v.getId(), w.getId()))
    print(graph)
