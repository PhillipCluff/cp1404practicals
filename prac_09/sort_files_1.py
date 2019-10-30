import os
import shutil

os.chdir('FilesToSort')

# file_types = ["xlsx", "xls", "txt", "png", "jpg", "gif", "docx", "doc"]
#
# for this_type in file_types:
#     try:
#         os.mkdir(this_type)
#     except FileExistsError:
#         pass

for filename in os.listdir('.'):
    extension = filename.split('.')[-1]
    # print(filename,  extension)
    try:
        os.mkdir(extension)
    except FileExistsError:
        pass
    shutil.move(filename, extension + "/" + filename)

    # if filename.endswith("txt"):
    #     print("{} has moved to txt".format(filename))
