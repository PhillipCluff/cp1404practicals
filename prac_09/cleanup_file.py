"""

"""
import shutil
import os

def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    things = []
    new_name_2 = ""
    for i, char in enumerate(new_name):
        if char.isupper() and i > 0:
            things.append("_")
            things.append(char)
        else:
            things.append(char)
    for thing in things:
        new_name_2 += thing
    print(new_name_2)

    return new_name


def run_demo_walk():

    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            new_name = get_fixed_filename(filename)
            print("Old name: {}, New name: {}".format(filename, new_name))



run_demo_walk()
