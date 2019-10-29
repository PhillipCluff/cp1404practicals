import os
import shutil

os.chdir('FilesToSort')

extensions_to_category = {}

for filename in os.listdir('.'):
    if filename.split('.')[-1] not in extensions_to_category:
        extensions_to_category[filename.split('.')[-1]] = filename.split('.')[-1]
    else:
        pass

print(extensions_to_category)
