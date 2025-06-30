"""
# Journey Python - Chapter 40
# zip files.
"""
import zipfile
zip = zipfile.ZipFile('files.zip', 'w')
zip.mkdir('basededados')

files = [
    'data.json',
    'myfile.bin',
    'compress_data.txt',
    'produtos.xml',
    'produtos2.xml'
]

for file in files:
    zip.write(file, f'basededados/{file}', compress_type=zipfile.ZIP_BZIP2, )

print('Arquivos compactados com sucesso!')

zip.extractall('arquivos')

zip.close()