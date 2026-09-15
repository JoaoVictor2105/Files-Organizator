from pathlib import Path
import shutil

search_paste = input('Select a paste: ')

while not Path(search_paste).exists() or not Path(search_paste).is_dir() == True:
    search_paste = input('Select a paste: ')

print('Caminho válido:', search_paste)