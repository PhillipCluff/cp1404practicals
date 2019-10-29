import os

os.chdir('FilesToSort')

for filename in os.listdir('.'):
    if filename.endswith("txt"):
        print("I am a TXT:{}".format(filename))
    elif filename.endswith("doc"):
        print("I am a DOC:{}".format(filename))
    else:
        pass
