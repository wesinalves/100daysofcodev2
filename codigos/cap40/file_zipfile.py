"""
# Journey Python - Chapter 40
# zip files.
"""
import zipfile
zip = zipfile.ZipFile('files.zip', 'w')
zip.mkdir('basededados')

files = [
    'relatoriogeral.xml',
    'basededados/equipamentos.csv',
    'basededados/funcionarios.csv',
    'basededados/produtos.csv'
]

for file in files:
    zip.write(file, compress_type=zipfile.ZIP_BZIP2)

zip.close()
print('Arquivos compactados com sucesso!')