"""Part of Speech Tagging (Word-Sense Disambiguation).

   @author
     Victor I. Afolabi
     Artificial Intelligence Expert & Researcher.
     Email: javafolabi@gmail.com | victor.afolabi@zephyrtel.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: pos.py
     Created on 21 February, 2019 @ 09:51 AM.

   @license
     MIT License
     Copyright (c) 2019. Victor I. Afolabi. All rights reserved.
"""

import nltk
from sage.core import Log

text = ("James Cameron was born in London on 16th August, 1954. He directed "
        "the movie Avatar, a Science Fiction movie and here's a link to the "
        "preview of the trailer: https://avatar.trailer.com.")

"""
James Cameron --born in--> London
James Cameron --birthday--> 16th August, 1954
James Cameron --directed--> Avatar

Avatar --genre--> Science Fiction
Avatar --trailer--> https://avatar.trailer.com
"""

tokens = nltk.word_tokenize(text)
tagged = nltk.pos_tag(tokens)
entities = nltk.ne_chunk(tagged, binary=False)
entities.draw()

if __name__ == '__main__':
    Log.debug(tagged)
    Log.debug(entities)
