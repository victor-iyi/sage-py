"""File system configuration module.

   @author
     Victor I. Afolabi
     Artificial Intelligence & Software Engineer.
     Email: javafolabi@gmail.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: fs.py
     Created on 26 January, 2018 @ 01:11 PM.

   @license
     Apache License 2.0
     Copyright (c) 2018. Victor I. Afolabi. All rights reserved.
"""

# Built-in libraries.
import os.path
from abc import ABCMeta
from collections import namedtuple

# Custom libraries.
from config.config import Config

# Exported configurations.
__all__ = [
    'FS', 'LOGGER', 'SETUP',
]


################################################################################################
# +--------------------------------------------------------------------------------------------+
# | FS: File System.
# +--------------------------------------------------------------------------------------------+
################################################################################################
class FS(metaclass=ABCMeta):
    # Project name & absolute directory.
    PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))
    APP_NAME = os.path.basename(PROJECT_DIR)

    # Directory to save stuffs.
    CONFIG_DIR = os.path.join(PROJECT_DIR, 'config')

    # Libraries & Include folders.
    LIB_DIR = os.path.join(PROJECT_DIR, 'sage')
    VENDOR_DIR = os.path.join(LIB_DIR, 'vendor')
    INCLUDE_DIR = os.path.join(LIB_DIR, 'include')

    # Resources & data directories.
    RESOURCE_DIR = os.path.join(PROJECT_DIR, 'resources')
    CACHE_DIR = os.path.join(RESOURCE_DIR, 'cache')
    DATASET_DIR = os.path.join(RESOURCE_DIR, 'dataset')
    DATABASE_DIR = os.path.join(RESOURCE_DIR, 'database')

    # WebQSP & QALD-7 Wikidata.
    __DatasetDir = namedtuple('DatasetDir',
                              ['base', 'zip', 'url',
                               'train', 'test', 'valid'])

    # Dataset base location.
    __Qald_Base = os.path.join(DATASET_DIR, 'QALD')
    __WebQSP_Base = os.path.join(DATASET_DIR, 'WebQSP')

    # Question & Answering over Linked Data (QALD) Dataset info.
    QALD_DIR = __DatasetDir(base=__Qald_Base,
                            zip=__Qald_Base.rstrip('/') + '.zip',
                            url='https://github.com/ag-sc/QALD/archive/master.zip',
                            train=os.path.join(__Qald_Base,
                                               '7/data/qald-7-train-en-wikidata.json'),
                            test=os.path.join(__Qald_Base,
                                              '7/data/qald-7-test-en-wikidata.json'),
                            valid=None)

    # Web Question for Semantic Parsing (WebQSP) info.
    # noinspection SpellCheckingInspection
    WebQSP_DIR = __DatasetDir(base=__WebQSP_Base,
                              zip=__WebQSP_Base.rstrip('/') + '.zip',
                              url=('https://download.microsoft.com/download/F/5/0/'
                                   'F5012144-A4FB-4084-897F-CFDA99C60BDF/WebQSP.zip'),
                              train=os.path.join(__WebQSP_Base,
                                                 'data/WebQSP.train.json'),
                              test=os.path.join(__WebQSP_Base,
                                                'data/WebQSP.test.json'),
                              valid=None)


################################################################################################
# +--------------------------------------------------------------------------------------------+
# | Setup configuration constants.
# +--------------------------------------------------------------------------------------------+
################################################################################################


class SETUP(metaclass=ABCMeta):
    # Global setup configuration.
    __global = Config.from_cfg(os.path.join(FS.CONFIG_DIR,
                                            "setup/global.cfg"))
    # Build mode/type.
    MODE = __global['config']['MODE']


################################################################################################
# +--------------------------------------------------------------------------------------------+
# | Logger: Logging configuration paths.
# +--------------------------------------------------------------------------------------------+
################################################################################################
class LOGGER(metaclass=ABCMeta):
    # Root Logger:
    ROOT = os.path.join(FS.CONFIG_DIR, f'logger/{SETUP.MODE}.cfg')

    # Another logger goes here: (and updated in helpers/utils.py)
