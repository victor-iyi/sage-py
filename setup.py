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
import platform
from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension

# Custom libraries.
from config import FS

# Compiler & Linker flags.
compile_extra_args = []
link_extra_args = []

# Platform specific flags.
if platform.system() == "Windows":
    compile_extra_args = ["/std:c++latest", "/EHsc"]
elif platform.system() == "Darwin":
    compile_extra_args = ['-std=c++17', "-mmacosx-version-min=10.9"]
    link_extra_args = ["-stdlib=libc++", "-mmacosx-version-min=10.9"]

# Cython extension modules.
ext_modules = [
    # Cython.
    Extension(name="*",
              language="c++",
              sources=[
                  'sage/core/cython/**/*.pyx',
              ],
              include_dirs=[FS.INCLUDE_DIR, ],
              extra_compile_args=compile_extra_args,
              extra_link_args=link_extra_args),
]

# Compiler directives
compiler_directives = {
    'language_level': 3,
    'always_allow_keywords': True,
}

setup(
    name='sage',
    version='1.0.0',
    # packages=[],
    requires=['Cython'],
    package_data={
        'sage/core': ['sage/core/cython/**/*.pxd',
                      'sage/core/cython/**/*.pyx'],
        'sage/core/data': ['sage/core/cython/data/*.pxd',
                           'sage/core/cython/data/*.pyx'],
        'sage/core/crawler': ['sage/core/cython/crawler/*.pxd',
                              'sage/core/cython/crawler/*.pyx'],
        'sage/core/graph': ['sage/core/cython/graph/*.pxd',
                            'sage/core/cython/graph/*.pyx'],
    },
    ext_modules=cythonize(ext_modules,
                          compiler_directives=compiler_directives),
    url='https://github.com/victor-iyiola/sage',
    license='Apache',
    author='Victor I. Afolabi',
    author_email='javafolabi@gmail.com',
    description=("Sage is an open-source Knowledge Graph which uses <https://schema.org> "
                 "and [JSON-LD](https://json-ld.org) serialization inspired by [Google's "
                 "Knowledge Graph](https://en.wikipedia.org/wiki/Knowledge_Graph)."),
    long_description=open('README.md', mode='r', encoding='utf-8').read()
)
