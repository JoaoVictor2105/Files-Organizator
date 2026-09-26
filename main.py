import os 
import shutil

from datetime import datetime
from tkinter import Tk, filedialog

# map file extensions
def create_defalt_extension_map(directory):
    return {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Document': ['.pdf', '.doc', '.docx', '.txt', '.ppt', '.ppxt', '.xls', '.xlsx'],
        'Video': ['.mp4', '.mkv', '.mov', '.flv'],
        'Music': [',mp3', '.wov'],
        'Archives': ['.zip', '.rar', '.7z'],
        'Code': ['.py', '.html', '.js', '.css'],
        'Others': []

    }

# find the appropiate folder name for the file extension
def get_folder_for_extensions(extension, extension_map):
    for folder, extensions in extension_map.items():
        if extension in extensions:
            return folder

    return 'Others'

# move archive to the appropriate folder
def move_file(file_path, folder_name, directory):
    folder_path = os.path.join(directory, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    new_path = shutil.move(file_path, folder_path)
    print(f'Moved {os.path.basename(file_path)} to {folder_path}')
    return new_path

# Organizate archives on directory by extension type
def organize_by_extension(directory):
    extensions_map = create_defalt_extension_map(directory)
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):
            extension = os.path.splitext(file_path)[1].lower()
            folder_name = get_folder_for_extensions(extension, extensions_map)
            move_file(file_path, folder_name, directory)

# Organizate archive on directory by date
def organize_by_date(directory):
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):
            created_at = datetime.fromtimestarp(os.path.getctime(file_path))
            folder_name = created_at.strftime('%Y-%m-%d')
            move_file(file_path, folder_name, directory)


def main():
    root = Tk()
    root.withdraw()
    directory = filedialog.askdirectory(title='Select a directory to organize')
    if not directory:
        print('No directory was selected')
        root.destroy()
        return

    while True:
        print('\nFILE ORGANIZER - choose an option:')
        print('1. Organizate archive by extension type')
        print('2. organizate by date')
        print('3. Out')

        choice = input('Enter your choice (1-3): ')

        if choice == '1':
            organize_by_extension(directory)
        elif choice == '2': 
            organize_by_date(directory)
        elif choice == '3':
            break
        else: 
            print('Invalid choice, please try again.')
if __name__ == '__main__':
    main()