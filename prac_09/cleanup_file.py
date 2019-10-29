"""

"""
import shutil
import os

def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    things = []
    for i, char in enumerate(new_name):
        if char.isupper() and i > 0:
            print("{} : {}".format(i, char))
            things.append(i)
    for thing in things:
        split_words = new_name.split(thing)
        for word in split_words:
            new_name = "".join(word, "_")

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
