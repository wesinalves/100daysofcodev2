"""
# Journey Python - Chapter 40
# Writing xml files.
"""
from xml.etree import ElementTree as ET
tree = ET.parse('produtos.xml')
root = tree.getroot()

product = {
    'Nome': 'leite',
    'Marca': 'itambé',
    'Valor': 15.9,
    'Validade': '29/05/2025'
}
child = ET.Element('produto')
child.set("id", "5")

for key, value in product.items():
    node = ET.Element(key)
    node.text = str(value)
    child.append(node)

root.append(child)
tree.write('produtos2.xml')