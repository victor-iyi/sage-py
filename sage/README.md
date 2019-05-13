# Sage API

The `sage` API consist several packages & modules to work with  logging, file, cache, downloader, data transformation, and many more. The `sage.core` package is built with [Cython](https://cython.org) - meaning it has to be built before usage. To build it simply run the Cython build script in the project root:

```sh
sh ./scripts/build/cython.sh
```

## `sage` API packages

- `sage.core` - Core functionalities including utilities & base classes.

  - `sage.core.base` - Consist of base classes for `Mode` and `Base` class for other objects.

  - `sage.core.utils` - Consist of utility classes e.g `File`, `Log`, `Downloader`, and `Cache`.

  - `sage.core.graph` - Core Knowledge Graph module. Main class for creation is `KnowledgeGraph` & supporting classes
   includes `Vertex`, `Edge` and `Graph`.

  - `sage.core.crawler` - Implements several utility functions for parsing web pages like `get_source`, `get_properties`, etc.