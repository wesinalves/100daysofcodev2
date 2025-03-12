"""
# Journey Python - Chapter 40
# Reading csv files.
"""
import csv
from collections import namedtuple

with open('products.csv', 'r') as file:
    data = csv.reader(file)
    headers = next(data)

    # for row in data:
    #     print(f'{headers[0]}: {row[0]}, {headers[2]}: {row[2]}')

    Row = namedtuple('Row', headers)
    for r in data:
        row = Row(*r)
        print(f'{headers[0]}: {row.Nome}, {headers[2]}: {row.Valor}')
