"""
# Journey Python - Chapter 40
# Reading xml files.
"""
from xml.etree import ElementTree as ET

tree = ET.parse('produtos.xml')
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib['id'], child[0].text, child[1].text)