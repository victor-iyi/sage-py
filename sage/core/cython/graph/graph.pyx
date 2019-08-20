"""Implementation of Graph database.

   @author
     Victor I. Afolabi
     Artificial Intelligence & Software Engineer.
     Email: javafolabi@gmail.com | victor.afolabi@zephyrtel.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: graph.py
     Created on 12 May, 2019 @ 11:20 PM.

   @license
     Apache 2.0 License
     Copyright (c) 2019. Victor I. Afolabi. All rights reserved.
"""
import json
from abc import abstractmethod

# from queue import Queue
# from threading import Thread
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config.consts import FS

from sage.core.base import Base
from sage.core.schema import Graph, Vertex, BaseSchema
from sage.core.utils import File, Log

__all__ = [
    'KnowledgeGraph',
    'MultiKnowledgeGraph',
]


# class Worker(Thread):
#     def __init__(self, inst, queue):
#         super(Worker, self).__init__()
#         self.inst = inst
#         self.queue = queue
#
#     def run(self):
#         while True:
#             name, data_file = self.queue.get()
#             try:
#                 self.inst.add_graph(name, data_file)
#             finally:
#                 self.queue.task_done()


class BaseKG(Base):
    # Supported file formats.
    SUPPORTED_FORMATS = ('json', 'jsonld', 'json-ld',
                         'rdf', 'xml', 'nt')

    def __init__(self, str name, str description=None,
                 str base_dir=None, data=None, str data_file=None,
                 **kwargs):
        self.label = name
        self.description = description
        # Base path where graph data is stored.
        self.base_dir = FS.DATABASE_DIR
        File.make_dirs(self.base_dir)

        overwrite = kwargs.get('overwrite', False)
        self._sess = self._initialize_session(overwrite=overwrite)

    def __repr__(self):
        return f'{self.name}({self.label})'

    def __getitem__(self, item):
        return self.get(item)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._sess.close()

    def __contains__(self, item):
        v = self.get(item)
        return v is not None

    @abstractmethod
    def get(self, item):
        return NotImplemented

    @staticmethod
    def read(str path):
        # Check if file exists.
        if not File.is_file(path):
            raise FileNotFoundError(f'{path} was not found.')

        # Get the file extension.
        cdef str ext = File.ext(path)

        # Supported file formats.
        if ext not in BaseKG.SUPPORTED_FORMATS:
            raise AssertionError(f'Expected one of: {BaseKG.SUPPORTED_FORMATS}.'
                                 f' Got {ext}')

        if ext in ('json', 'jsonld', 'json-ld'):
            # Load JSON-LD file.
            with open(path, mode='r', encoding='utf-8') as f:
                return json.loads(f.read())
        else:
            # TODO(victor-iyiola): Support for RDF/XML & n-triples.
            Log.warn('RDF/XML & n-triple not yet supported.')
            return NotImplemented

    def add_vertex(self, str label, str schema, str graph_id):
        vertex = self.get_vertex(label=label, schema=schema, graph_id=graph_id)
        if vertex is not None:
            return vertex

        # Create a new vertex.
        vertex = Vertex(label=label, schema=schema, graph_id=graph_id)
        self._sess.add(vertex)
        self._sess.commit()
        return vertex

    def close(self):
        self._sess.close()

    def get_graph_by_name(self, str graph_name):
        """Retrieve graph object by graph's name.

        Args:
            graph_name (str): Name of graph to lookup.

        Returns:
            Union[Graph, None] - Graph instance if graph name
                is found in the db.
        """
        return self._sess.query(Graph).filter_by(name=graph_name).first()

    def get_vertex(self, str vertex_id=None, str label=None,
                   str schema=None, str graph_id=None):
        result = None

        if vertex_id is not None:
            result = self._sess.query(Vertex).filter_by(id=vertex_id).first()
        elif label is not None and schema is not None:
            if graph_id is not None:
                # Get vertex from a specific graph.
                result = self._sess.query(Vertex) \
                    .filter_by(label=label, schema=schema,
                               graph_id=graph_id) \
                    .first()
            else:
                # Get vertex from default graph.
                result = self._sess.query(Vertex) \
                    .filter_by(label=label, schema=schema,
                               graph_id=self._default_graph.id) \
                    .first()
        else:
            raise ValueError('Expected one of `id` or `label` & `schema`.')

        return result

    def get_vertex_by_label(self, str label):
        return self._sess.query(Vertex).filter_by(label=label).all()

    def load(self, data, str graph_id):
        # Declare schemas & labels.
        cdef str schema, label, nbr_schema, nbr_label

        # First verify that `graph_id` exists.
        if isinstance(data, dict):
            # FIXME: Pass a *pointer* to `data` and not the `data` itself.
            schema = self._get_schema(data, marker='@type', default='Thing')
            label = self._get_label(data, schema=schema, marker='name')
            # Add Vertex to graph.
            vertex = self.add_vertex(label, schema, graph_id)

            # Loop through key-value pairs of current vertex.
            for k, v in data.items():
                # Key doesn't start with "@" & Value must be a primitive type.
                if not k.startswith('@') and isinstance(v, (int, float, str, bool)):
                    # Add necessary payloads.
                    vertex.payload[k] = v
                # A new list of scopes.
                elif isinstance(v, (list, tuple)):
                    for item in v:  # Loop through the list.
                        self.load(item, graph_id)

                elif isinstance(v, dict):
                    # Direct neighboring scope.
                    nbr_schema = self._get_schema(v, marker='@type', default='Thing')
                    nbr_label = self._get_label(v, schema=nbr_schema, marker='name')
                    nbr = self.add_vertex(nbr_label, nbr_schema, graph_id)
                    vertex.add_neighbor(nbr, predicate=k)
                    # Visit direct neighboring scope.
                    self.load(v, graph_id)

        elif isinstance(data, (list, tuple)):
            for item in data:
                self.load(item, graph_id)

        # Commit all changes.
        self._sess.commit()

    def _get_label(self, dict data, schema='Thing', marker='name'):
        # TODO: Search for best marker for given schema (with fallback strategy).
        # maker = get_best_marker(schema, data.keys())
        return data.get(marker, 'Unknown')

    def _get_schema(self, dict data, marker='@type', default='Thing'):
        # If a list or tuple is returned. Pick the best schema.
        result = data.get(marker, default)
        if isinstance(result, (list, tuple)):
            # TODO: Pick the best (most specific schema) `result`.
            return result[0]
        return result

    def _initialize_session(self, bint overwrite=False):
        import os
        # Save current dir to switch back later.
        cdef str cur_dir = os.path.abspath(os.curdir)

        # Switch directory to base dir.
        os.chdir(self.base_dir)
        cdef str filename = f'{self.label}.db'

        if File.is_file(filename) and overwrite:
            File.remove(filename)

        # Create DB engine & session.
        engine = create_engine(f'sqlite:///{filename}')
        if not File.is_file(filename):
            BaseSchema.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        sess = Session()

        # Switch back to cur dir.
        os.chdir(cur_dir)

        return sess


class KnowledgeGraph(BaseKG):

    def __init__(self, str name, str description=None,
                 str base_dir=None, data=None, str data_file=None,
                 **kwargs):
        super(KnowledgeGraph, self).__init__(name, description,
                                             base_dir=base_dir, data=data,
                                             data_file=data_file, **kwargs)

        # Add the default graph to the db.
        self._default_graph = self.get_graph_by_name(name)
        if self._default_graph is None:
            self._default_graph = Graph(name=name, description=description)
            self._sess.add(self._default_graph)
            self._sess.commit()

        # Read knowledge data from file.
        if data_file is not None:
            # assert data is None, 'Provide `data` or `data_file` but not both.'
            data = KnowledgeGraph.read(data_file)

        # Load Knowledge Graph with knowledge data.
        if data is not None:
            self.load(data, self._default_graph.id)

    @classmethod
    def fromfile(cls, str path, str description=None, **kwargs):
        # Create a new KnowledgeGraph instance.
        inst = cls(name=File.filename(path),
                   description=description,
                   data_file=path, **kwargs)

        # Return KnowledgeGraph object.
        return inst

    def get(self, item):
        result = None
        if isinstance(item, str):
            result = self.get_vertex(vertex_id=item)
        elif isinstance(item, tuple):
            assert len(item) == 2, 'Only label & schema expected.'
            result = self.get_vertex(label=item[0], schema=item[1])
        else:
            raise TypeError(f'Expected one of str or Tuple[str, str],'
                            f'got {type(item)}')

        return result

    @property
    def vertices(self):
        return self._sess.query(Vertex) \
            .filter_by(graph_id=self._default_graph.id) \
            .all()


class MultiKnowledgeGraph(Base):
    def __init__(self, str name):
        super(MultiKnowledgeGraph, self).__init__()
        self.label = name

        # Base directory where graph is stored.
        self.base_dir = File.join(FS.DATABASE_DIR, name)
        File.make_dirs(self.base_dir)

        # List of graphs contained in Multi-KG.
        self._graphs = dict()

    def __getitem__(self, item):
        result = None
        if isinstance(item, str):
            if item in self._graphs:
                result = self._graphs[item]
            else:
                raise KeyError(f'{item} not found in graph.')
        elif isinstance(item, tuple):
            graph, item = self.__get_validate(item)
            result = graph[item]
        else:
            raise TypeError(f'Expected one of str & tuple got {type(item)}')
        return result

    def get(self, item):
        result = None
        if isinstance(item, str):
            if item in self._graphs:
                result = self._graphs[item]
            else:
                raise KeyError(f'{item} not found in graph.')
        elif isinstance(item, tuple):
            graph, item = self.__get_validate(item)
            result = graph.get(item)
        else:
            raise TypeError(f'Expected one of str & tuple got {type(item)}')

        return result

    @classmethod
    def from_dir(cls, str path):
        # `path` must be a directory.
        if not File.is_dir(path):
            raise FileNotFoundError(f"{path} does not exist"
                                    " or isn\'t a directory.")

        # Create a new multi-knowledge graph.
        cdef str name = File.filename(path)
        inst = cls(name.replace(' ', '_').replace('-', '_'))

        # Get all files in directory.
        cdef str file_path
        for file_path in File.get_files(path, optimize=False):
            if File.ext(file_path) in KnowledgeGraph.SUPPORTED_FORMATS:
                name = File.filename(file_path)
                inst.add_graph(name.replace(' ', '_').replace('-', '_'),
                               data_file=file_path)
            else:
                Log.warn(f'{file_path} not supported.')

        return inst

    def add_graph(self, str name, str data_file=None):
        if name in self._graphs:
            raise KeyError(f'{name} already exists.')

        g = Graph(name, base=self.base_dir,
                  data_file=data_file)
        self._graphs[name] = g

        return g

    def __get_validate(self, item):
        if not isinstance(item, tuple) or len(item) < 2:
            raise AssertionError('Expected one of Tuple[str, str], '
                                 'Tuple[str, str, str] or Tuple[str, Vertex]')

        # Get the graph to be queried.
        name = item[0]

        if name not in self._graphs:
            raise KeyError(f'Graph `{name}` does not exist.')

        # Grab remaining item(s).
        item = item[1] if len(item[1:]) == 1 else item[1:]

        return self._graphs[name], item

    @property
    def graphs(self):
        return list(self._graphs.values())
