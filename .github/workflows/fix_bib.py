# -*- coding: utf-8 -*-

import os, re

PATH = os.path.dirname(os.getcwd())
BIB_FILE = os.path.join(PATH,'publications-list/publications.bib')

# Normalize author name
author_regex = re.compile(r'L(?:uiz)?\.?\s*F?(?:ernando)?\.?\s*O?(?:liveira)?\.?\s*Chamon(\*?)')
with open(BIB_FILE, 'r') as input_file, open(os.path.join(PATH, 'temp.bib'), 'w') as output_file:
    for line in input_file:
        str = re.sub(author_regex, r'L. F. O. Chamon\1', line)
        output_file.write(str)

os.rename(os.path.join(PATH, "temp.bib"), BIB_FILE)
