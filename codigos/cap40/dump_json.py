"""
# Journey Python - Chapter 40
# dumps and loads json file.
"""
import json

data = {
    'Nome': 'açucar',
    'Marca': 'união',
    'Valor': 4.5,
    'Validade': {'dia': 3, 'mes': 4, 'ano': 2022}
}

with open('data.json', 'w') as file:
    json.dump(data, file)

with open('data.json', 'r') as file:
    data = json.load(file)

for key, item in data.items():
    if key == 'Validade':
        print(f"Data: {item['dia']}/{item['mes']}/{item['ano']}")
    else:
        print(key, item)