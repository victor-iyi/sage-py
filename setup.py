"""Distribution setup file to install & build libraries.

   @author
     Victor I. Afolabi
     Artificial Intelligence & Software Engineer.
     Email: javafolabi@gmail.com | victor.afolabi@zephyrtel.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: setup.py
     Created on 28 January, 2019 @ 01:27 PM.

   @license
     Apache License 2.0
     Copyright (c) 2019. Victor I. Afolabi. All rights reserved.
"""

# Built-in libraries.
from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension

# Custom libraries.
from config import FS

# Cython extension modules.
ext_modules = [
    # Cython.
    Extension(name="*",
              language="c++",
              sources=['sage/core/cython/*.pyx',
                       # 'sage/core/cython/*.pxd'
                       ],
              # libraries=[],
              # library_dirs=[FS.VENDOR_DIR, ],
              include_dirs=[FS.INCLUDE_DIR, ]),
    # Cython.
    Extension(name="graph",
              language="c++",
              sources=['sage/core/cython/graph/*.pyx',
                       'sage/core/cython/graph/*.pxd'],
              # libraries=[],
              # library_dirs=[FS.VENDOR_DIR, ],
              include_dirs=[FS.INCLUDE_DIR, ]),
    # Cython.
    Extension(name="crawler",
              language="c++",
              sources=['sage/core/cython/crawler/*.pyx',
                       'sage/core/cython/crawler/*.pyd'],
              # libraries=[],
              # library_dirs=[FS.VENDOR_DIR, ],
              include_dirs=[FS.INCLUDE_DIR, ]),

]

# Compiler directives
compiler_directives = {
    'language_level': 3,
}

setup(
    name='sage',
    version='1.0.0',
    # packages=[],
    requires=['Cython'],
    ext_modules=cythonize(ext_modules,
                          compiler_directives=compiler_directives),
    url='https://github.com/victor-iyiola/sage',
    license='MIT',
    author='Victor I. Afolabi',
    author_email='javafolabi@gmail.com',
    description=("Sage is an open-source Knowledge Graph which uses <https://schema.org> "
                 "and [JSON-LD](https://json-ld.org) serialization inspired by [Google's "
                 "Knowledge Graph](https://en.wikipedia.org/wiki/Knowledge_Graph)."),
    long_description=open('README.md', mode='r', encoding='utf-8').read()
)
