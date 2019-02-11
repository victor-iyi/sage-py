"""Crawler utility for parsing https://schema.org.

   @author
     Victor I. Afolabi
     Artificial Intelligence & Software Engineer.
     Email: javafolabi@gmail.com | victor.afolabi@zephyrtel.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: crawler.py
     Created on 07 February, 2019 @ 12:56.

   @license
     MIT License
     Copyright (c) 2019. Victor I. Afolabi. All rights reserved.
"""

import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
from sage.core import Log


def get(url, **kwargs):
    response, data = None, None
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3)'
                      ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                      '50.0.2661.102 Safari/537.36'
    }
    try:
        if kwargs:
            data = urllib.parse.urlencode(kwargs)
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


def parse_property(body: BeautifulSoup):
    properties = []

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


def get_properties(schema_type, baseURL='https://schema.org/', with_base=False):
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
        >>> properties = get_properties('Book')
        >>> Log.debug(properties)
        DEBUG    | {
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
    """
    url = urllib.parse.urljoin(baseURL, schema_type)
    source = get(url)

    if not source:
        Log.fatal('Could not retrieve source. Please check the URL & try again.')

    soup = BeautifulSoup(source, 'lxml')
    table = soup.find('table', class_='definition-table')
    super_types = table.find_all('tbody', class_='supertype')

    if with_base:
        ...

    properties = parse_property(super_types[0])
    result = {
        '@id': 'schema:{}'.format(schema_type),
        'name': schema_type,
        'properties': properties
    }

    return result


if __name__ == '__main__':
    properties = get_properties('Book')
    Log.debug(properties)
