"""
# Journey Python - Chapter 40
# Reading csv files.
"""
import csv

with open('products.csv', 'r') as file:
    data = csv.reader(file)
    headers = next(data)

    for row in data:
        print(f'{headers[0]}: {row[0]}, {headers[2]}: {row[2]}')