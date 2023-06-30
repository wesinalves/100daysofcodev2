"""
# Journey Python - Chapter 40
# Writing csv files.
"""
import csv

headers = ['Nome','Marca','Valor','Validade']

rows = [
    ('açucar','união',4.5,'25/03/2024'),
    ('feijão','kidelicia',8.7,'25/03/2023'),
    ('arroz','tio joão',5.5,'13/09/2022'),
    ('café','nescafé',8.4,'15/08/2025')
]

with open('products.csv', 'w') as file:
    w = csv.writer(file)
    w.writerow(headers)
    w.writerows(rows)