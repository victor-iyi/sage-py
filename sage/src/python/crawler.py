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

import urllib3
from bs4 import BeautifulSoup

url = 'https://health-science/schema.org'

# Requesting web page source code.
http = urllib3.PoolManager()
response = http.request('GET', url)
source = response.data.decode('utf-8')

# Beautiful Soup parser.
soup = BeautifulSoup(source, 'lxml')
mainContent = soup.find('div', id='mainContent')
print(mainContent)
