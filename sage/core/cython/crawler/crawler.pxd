"""
   @author
     Victor I. Afolabi
     Artificial Intelligence Expert & Researcher.
     Email: javafolabi@gmail.com | victor.afolabi@zephyrtel.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: crawler.pxd
     Created on 20 February, 2019 @ 12:06.

   @license
     MIT License
     Copyright (c) 2019. Victor I. Afolabi. All rights reserved.
"""

# Retrieve the source code of a given URL.
#
# Args:
#     url (str): Target URL.
#     query_dict (Dict[str, str]): Key value pair to be constructed
#         for query string.
#
# Returns:
#     str: Decoded source code of the give URL.
cpdef str get_source(str url, dict query_dict= *)

# Get properties for a schema Type.
#
# Args:
#     schema_type (str): A valid schema:Type.
#     baseURL (str, optional): Defaults to "https://schema.org/". Base URL to schema.
#
# Notes:
#     # rangeIncludes is similar to ExpectedTypes.
#     # domainIncludes is similar to other places where this property can be found.
#
# Examples:
#     ```python
#     >>> from sage.core.utils import Log
#     >>> properties = get_properties('Book')
#     >>> Log.pretty(properties)
#     {'@id': 'schema:Book',
#      'name': 'Book',
#      'properties': [{'domainIncludes': ['http://schema.org/Book'],
#                      'rangeIncludes': ['http://schema.org/Boolean'],
#                      'rdfs:Property': 'http://schema.org/abridged',
#                      'rdfs:comment': 'Indicates whether the book is an abridged '
#                                      'edition.',
#                      'rdfs:label': 'abridged'},
#                     ...,
#                     {'domainIncludes': ['http://schema.org/Book'],
#                      'rangeIncludes': ['http://schema.org/Integer'],
#                      'rdfs:Property': 'http://schema.org/numberOfPages',
#                      'rdfs:comment': 'The number of pages in the book.',
#                      'rdfs:label': 'numberOfPages'}]}
#     ```
#
# Returns:
#     Union[Dict[str, Any], List[Dict[str, Any]]] - Returns a dict if with_base=False,
#         otherwise it returns a list of dicts.
cpdef dict get_properties(str schema_type, str baseURL= *, bint compact= *)

################################################################################################
# +--------------------------------------------------------------------------------------------+
# | Private functions.
# +--------------------------------------------------------------------------------------------+
################################################################################################
cdef list _parse_property(body, bint compact= *)
