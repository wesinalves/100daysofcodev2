"""
# Journey Python - Chapter 40
# dumps and loads json file.
"""
import json

data = {
    'Nome': 'açucar',
    'Marca': 'união',
    'Valor': 4.5,
    'Validade': '25/03/2024'
}

with open('data.json', 'w') as file:
    json.dump(data, file)

with open('data.json', 'r') as file:
    data = json.load(file)

for key, item in data.items():
    print(type(item))
