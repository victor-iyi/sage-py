"""Crawler Utility for parsing https://schema.org/

   @author
     Victor I. Afolabi
     Artificial Intelligence & Software Engineer.
     Email: javafolabi@gmail.com | victor.afolabi@zephyrtel.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: crawler.py
     Package: sage.core
     Created on 11 February, 2019 @ 06:58 PM.

   @license
     Apache 2.0 License
     Copyright (c) 2019. Victor I. Afolabi. All rights reserved.
"""
from typing import Dict, Any, Optional


def get_source(url: str, query_dict: Dict[str, str] = None) -> str:
    """Retrieve the source code of a given URL.

    Args:
        url (str): Target URL.
        query_dict (Dict[str, str]): Key value pair to be constructed
            for query string.

    Returns:
        str: Decoded source code of the give URL.
    """


def get_properties(schema_type: str, baseURL: Optional[str] = 'https://schema.org/',
                   with_base: Optional[bool] = False) -> Dict[str, Any]:
    """Get properties for a schema Type.

    Args:
        schema_type (str): A valid schema:Type.
        baseURL (str, optional): Defaults to "https://schema.org/". Base URL to schema.
        with_base (bool, optional): Defaults to False. Whether or not to include
            super-class properties.

    Notes:
        # rangeIncludes is similar to ExpectedTypes.
        # domainIncludes is similar to other places where this property can be found.

    Examples:
        ```python
        >>> from pprint import pprint
        >>> properties = get_properties('Book')
        >>> pprint(properties)
        {
            '@id': 'schema:Book',
            'name': 'Book',
            'properties': [
                {
                    'rdfs:label': 'abridged',
                    'rdfs:Property': 'http://schema.org/abridged',
                    'rdfs:comment': 'Indicates whether the book is an abridged edition.',
                    'rangeIncludes': ['http://schema.org/Boolean'],
                    'domainIncludes': ['http://schema.org/Book']
                },
                ...,
                {
                    'rdfs:label': 'numberOfPages',
                    'rdfs:Property': 'http://schema.org/numberOfPages',
                    'rdfs:comment': 'The number of pages in the book.',
                    'rangeIncludes': ['http://schema.org/Integer'],
                    'domainIncludes': ['http://schema.org/Book']
                }
            ]
        }
        ```

    Returns:
        Union[Dict[str, Any], List[Dict[str, Any]]] - Returns a dict if with_base=False,
            otherwise it returns a list of dicts.
    """
