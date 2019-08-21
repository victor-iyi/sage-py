# sage-py

> Python bindings for [Sage](https://github.com/victor-iyiola/sage-py).

Sage is an open-source Knowledge Graph which uses <https://schema.org> and [JSON-LD](https://json-ld.org) serialization inspired by [Google's Knowledge Graph](https://en.wikipedia.org/wiki/Knowledge_Graph).

[![Build status](https://ci.appveyor.com/api/projects/status/w8coyh60l36s0fbk?svg=true)](https://ci.appveyor.com/project/victor-iyiola/sage-py)
[![Build Status](https://travis-ci.org/victor-iyiola/sage-py.svg?branch=master)](https://travis-ci.org/victor-iyiola/sage-py)
[![GitHub issues](https://img.shields.io/github/issues/victor-iyiola/sage-py)](https://github.com/victor-iyiola/sage-py/issues)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](./LICENSE)

- [sage-py](#sage-py)
  - [Functionalities](#functionalities)
  - [Setup](#setup)
  - [Usage](#usage)
  - [Credits](#credits)
  - [Contribution](#contribution)
  - [License (Apache)](#license-apache)

## Functionalities

Sage basically reads your `.jsonld` file & builds a Knowledge Graph using <https://schema.org> standards. It can also
 load in Knowledge triples from [WikiData](https://www.wikidata.org/wiki/Special:EntityPage/Q6108942), or any [FOAF
 ontology](<https://en.wikipedia.org/wiki/FOAF_(ontology)>).

## Setup

The `sage.core` package is written in [Cython](https://cython.org) - meaning it has to be built before usage. To
build it simply run the Cython build script in the project root:

```bash
sh ./scripts/cython.sh
```

## Usage

The [Sage API](./sage) has a relatively simple API. The code snippet below builds a simple Knowledge Graph.

```python
from config.consts import FS
from sage.core.utils import Log, File
from sage.core.graph import KnowledgeGraph

# !- Loading Graph data from File.
path = File.join(FS.CACHE_DIR, 'graph/examples/avatar.jsonld')

# !- Loading KnowledgeGraph from file.
kg = KnowledgeGraph.fromfile(path)
# INFO     | New Vertex: label: Avatar, schema=Movie
# INFO     | New Vertex: label: James Cameron, schema=Person

Log.debug(kg.graph.vertices)
# DEBUG    | [<Vertex(label='Avatar', schema='Movie')>, <Vertex(label='James Cameron', schema='Person')>]

# !- Retrieve Vertices in the Graph.
avatar = kg.graph['Avatar', 'Movie']
Log.debug(f'avatar = {avatar}')
# DEBUG    | avatar = <Vertex(label='Avatar', schema='Movie')>
Log.debug(f'avatar.payload = {avatar.payload}')
# DEBUG    | avatar.payload = {'name': 'Avatar', 'genre': 'Science Fiction', 'trailer': 'https://example.com/trailer
Log.debug(f'avatar.edges = {avatar.edges}')
# DEBUG    | avatar.edges = [<Edge(e147c670075ef62b, director)>]

# !- Close Knowledge Graph connection.
kg.close()
```

## Credits

- [Tomiiide](https://github.com/tomiiide)
- [NIOCRAFT](http://niocraft.com) - R&amp;D Agency Innovative Artificial Intelligence Solutions.

## Contribution

You are very welcome to modify and use them in your own projects.

Please keep a link to the [original repository](https://github.com/victor-iyiola/sage-py). If you have made a fork with substantial modifications that you feel may be useful, then please [open a new issue on GitHub](https://github.com/victor-iyiola/sage-py/issues) with a link and short description.

## License (Apache)

This project is opened under the [Apache License 2.0](./LICENSE) which allows very broad use for both private and commercial purposes.

A few of the images used for demonstration purposes may be under copyright. These images are included under the "fair usage" laws.
