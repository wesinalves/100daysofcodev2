"""
# Journey Python - Chapter 40
# Reading gzip files.
"""

import gzip
content = b'Lorem ipsum dolor sit amet, consectetur adipiscing elit\n.'

with gzip.open('compress_data.gz', 'wb') as file:
    for _ in range(5):
        file.write(content)

with open('compress_data.gz', 'rb') as file:
    print(file.read())

with gzip.open('compress_data.gz', 'rb') as file:
    print(file.read())
