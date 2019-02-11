# Sage

Sage is an open-source Knowledge Graph which uses <https://schema.org> and [JSON-LD](https://json-ld.org) serialization inspired by [Google's Knowledge Graph](https://en.wikipedia.org/wiki/Knowledge_Graph).

[![Appveyor Build status](https://ci.appveyor.com/api/projects/status/sc059tu6cepei47f?svg=true)](https://ci.appveyor.com/project/victor-iyiola/sage)
[![Travis Build Status](https://travis-ci.org/victor-iyiola/sage.svg?branch=develop)](https://travis-ci.org/victor-iyiola/sage)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![GitHub Releases](https://img.shields.io/github/release/victor-iyiola/sage.svg)](https://github.com/victor-iyiola/sage/releases)
[![GitHub Issues](https://img.shields.io/github/issues/victor-iyiola/sage.svg)](http://github.com/victor-iyiola/sage/issues)

- [Sage](#sage)
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

The `sage.core` package is built with [Cython](https://cython.org) - meaning it has to be built before usage. To build it simply run the Cython build script in the project root:

```bash
sh ./scripts/cython.sh
```

## Usage

The [Sage API](./sage) has a relatively simple API. The code snippet below builds a simple Knowledge Graph.

```python
from config import FS
from sage.core import File, Log, Graph

# Path to a JSON-LD file.
path = File.join(FS.CACHE_DIR,
                 'graph/examples/avatar.jsonld')

# Create a Graph object from a JSON-LD file.
g = Graph(path=path)
Log.pretty('{:!r}'.format(g))
```

## Credits

- [Tomiiide](https://github.com/tomiiide)
- [NIOCRAFT](http://niocraft.com) - R&amp;D Agency Innovative Artificial Intelligence Solutions.

## Contribution

You are very welcome to modify and use them in your own projects.

Please keep a link to the [original repository](https://github.com/victor-iyiola/sage). If you have made a fork with substantial modifications that you feel may be useful, then please [open a new issue on GitHub](https://github.com/victor-iyiola/sage/issues) with a link and short description.

## License (Apache)

This project is opened under the [Apache License 2.0](./LICENSE) which allows very broad use for both private and commercial purposes.

A few of the images used for demonstration purposes may be under copyright. These images are included under the "fair usage" laws.
