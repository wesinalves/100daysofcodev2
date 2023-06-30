"""
# Journey Python - Chapter 40
# dumps and loads json data.
"""
import json

data = {
    'Nome': 'açucar',
    'Marca': 'união',
    'Valor': 4.5,
    'Validade': '25/03/2024'
}

json_str = json.dumps(data)

data = json.loads(json_str)

for key, item in data.items():
    print(type(item))