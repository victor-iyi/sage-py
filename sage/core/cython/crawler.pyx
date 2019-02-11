"""Crawler Utility for parsing https://schema.org/

   @author
     Victor I. Afolabi
     Artificial Intelligence & Software Engineer.
     Email: javafolabi@gmail.com | victor.afolabi@zephyrtel.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: crawler.pyx
     Created on 11 February, 2019 @ 06:50 PM.

   @license
     Apache 2.0 License
     Copyright (c) 2019. Victor I. Afolabi. All rights reserved.
"""

import urllib.parse
import urllib.error
import urllib.request

from bs4 import BeautifulSoup

from sage.core.utils import Log

################################################################################################
# +--------------------------------------------------------------------------------------------+
# | Exported functions.
# +--------------------------------------------------------------------------------------------+
################################################################################################
cpdef str get_source(str url, dict query_dict=None):
    """Retrieve the source code of a given URL.

    Args:
        url (str): Target URL.
        query_dict (Dict[str, str]): Key value pair to be constructed
            for query string.

    Returns:
        str: Decoded source code of the give URL.
    """
    cdef str response = None, data = None
    cdef dict headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3)'
                      ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                      '50.0.2661.102 Safari/537.36'
    }
    try:
        if query_dict is not None:
            data = urllib.parse.urlencode(query_dict)
            data = data.encode('utf-8')

        # Request webpage with query-strings & headers.
        req = urllib.request.Request(url, data=data, headers=headers)
        request = urllib.request.urlopen(req)
        response = request.read().decode()

    except urllib.error.HTTPError as http_err:
        Log.exception(f'HTTPError: {http_err}')
    except urllib.error.URLError as url_err:
        Log.exception(f'URLError: {url_err}')

    return response

cpdef dict get_properties(str schema_type, str baseURL='https://schema.org/'):
    """Get properties for a schema Type.

    Args:
        schema_type (str): A valid schema:Type.
        baseURL (str, optional): Defaults to "https://schema.org/". Base URL to schema.

    Notes:
        # rangeIncludes is similar to ExpectedTypes.
        # domainIncludes is similar to other places where this property can be found.

    Examples:
        ```python
        >>> from sage.core.utils import Log
        >>> properties = get_properties('Book')
        >>> Log.pretty(properties)
        {'@id': 'schema:Book',
         'name': 'Book',
         'properties': [{'domainIncludes': ['http://schema.org/Book'],
                         'rangeIncludes': ['http://schema.org/Boolean'],
                         'rdfs:Property': 'http://schema.org/abridged',
                         'rdfs:comment': 'Indicates whether the book is an abridged '
                                         'edition.',
                         'rdfs:label': 'abridged'},
                        ...,
                        {'domainIncludes': ['http://schema.org/Book'],
                         'rangeIncludes': ['http://schema.org/Integer'],
                         'rdfs:Property': 'http://schema.org/numberOfPages',
                         'rdfs:comment': 'The number of pages in the book.',
                         'rdfs:label': 'numberOfPages'}]}
        ```

    Returns:
        Union[Dict[str, Any], List[Dict[str, Any]]] - Returns a dict if with_base=False,
            otherwise it returns a list of dicts.
    """
    cdef str url = urllib.parse.urljoin(baseURL, schema_type)
    cdef str source = get_source(url)

    if not source:
        Log.fatal('Could not retrieve source. Please check the URL & try again.')

    soup = BeautifulSoup(source, 'lxml')
    table = soup.find('table', class_='definition-table')
    super_types = table.find_all('tbody', class_='supertype')

    cdef list properties = _parse_property(super_types[0])
    cdef dict result = {
        '@id': 'schema:{}'.format(schema_type),
        'name': schema_type,
        'properties': properties
    }

    return result

################################################################################################
# +--------------------------------------------------------------------------------------------+
# | Private functions.
# +--------------------------------------------------------------------------------------------+
################################################################################################
cdef list _parse_property(body):
    cdef:
        list properties = []
        dict template

    trs = body.find_all('tr', typeof='rdfs:Property')
    for tr in trs:
        template = {
            'rdfs:label': '',  # Name of property.
            'rdfs:Property': '',  # Full schema of property.
            'rdfs:comment': '',  # Property description.
            'rangeIncludes': [],  # Expected types.
            'domainIncludes': [],  # Possible domains found.
        }
        code = tr.select('code > a')[0]
        rangeIncludes = tr.find_all('link', property='rangeIncludes')
        domainIncludes = tr.find_all('link', property='domainIncludes')

        template['rdfs:label'] = code.get_text()
        template['rdfs:Property'] = tr['resource']
        template['rdfs:comment'] = tr.find('td', property='rdfs:comment').get_text()
        template['rangeIncludes'] = list(map(lambda tag: tag['href'], rangeIncludes))
        template['domainIncludes'] = list(map(lambda tag: tag['href'], domainIncludes))

        properties.append(template)

    return properties
