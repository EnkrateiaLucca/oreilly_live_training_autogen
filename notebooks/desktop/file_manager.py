# filename: file_manager.py

import os
import shutil

downloads_dir = '/Users/greatmaster/Downloads'

for filename in os.listdir(downloads_dir):
    print(f'File: {filename}')
    action = input('Enter "k" to keep, "d" to delete, or "m" to move: ')
    
    if action.lower() == 'd':
        os.remove(os.path.join(downloads_dir, filename))
        print(f'{filename} has been deleted.')
    elif action.lower() == 'm':
        destination = input('Enter the destination directory: ')
        shutil.move(os.path.join(downloads_dir, filename), destination)
        print(f'{filename} has been moved to {destination}.')
    else:
        print(f'{filename} has been kept.')