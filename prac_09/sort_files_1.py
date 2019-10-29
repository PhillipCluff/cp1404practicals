import os
import shutil

os.chdir('FilesToSort')

file_types = ["xlsx", "xls", "txt", "png", "jpg", "gif", "docx", "doc"]

for this_type in file_types:
    try:
        os.mkdir(this_type)
    except FileExistsError:
        pass

for filename in os.listdir('.'):
    if filename.endswith("txt"):
        print("{} has moved to txt".format(filename))

        shutil.move(filename, "txt")
    elif filename.endswith("doc"):
        print("{} has moved to doc".format(filename))

        shutil.move(filename, "doc")
    elif filename.endswith("xlsx"):
        print("{} has moved to xlsx".format(filename))

        shutil.move(filename, "xlsx")
    elif filename.endswith("xls"):
        print("{} has moved to xls".format(filename))

        shutil.move(filename, "xls")
    elif filename.endswith("png"):
        print("{} has moved to png".format(filename))

        shutil.move(filename, "png")
    elif filename.endswith("jpg"):
        print("{} has moved to jpg".format(filename))

        shutil.move(filename, "jpg")
    elif filename.endswith("gif"):
        print("{} has moved to gif".format(filename))

        shutil.move(filename, "gif")
    elif filename.endswith("docx"):
        print("{} has moved to docx".format(filename))

        shutil.move(filename, "docx")
    else:
        pass
