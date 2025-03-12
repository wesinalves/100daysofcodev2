"""
# Journey Python - Chapter 40
# organizing files with shutil module.
"""
from shutil import copy
import os

# set source and destination paths
source_dir = os.path.expanduser('~/Downloads/test')
images_folder = os.path.expanduser('~/Picures')
videos_folder = os.path.expanduser('~/Videos')
documents_folder = os.path.expanduser('~/Documents')
musics_folder = os.path.expanduser('~/Music')

for file in os.listdir(source_dir):
    ext = os.path.splitext(file)[1]
    path = os.path.join(source_dir, file)
    match ext:
        case '.mp4' | '.mpeg':
            copy(path, videos_folder)
            os.unlink(path)
        case '.png' | '.jpg' | '.jpeg' | '.webp':
            copy(path, images_folder)
            os.unlink(path)
        case '.mp3' | '.wav':
            copy(path, musics_folder)
            os.unlink(path)
        case '.doc' | '.docx':
            copy(path, documents_folder)
            os.unlink(path)
        case _:
            print(ext, 'Formato de arquivo não suportado')