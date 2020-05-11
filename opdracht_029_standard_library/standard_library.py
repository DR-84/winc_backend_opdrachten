import secret
import os
import shutil

# https://docs.python.org/2/library/argparse.html (maybe check this later)
# opdracht 1:

folder = r"C:\Users\ddder\OneDrive\Bureaublad\Picapica"


def files_in_dir(path):
    for i in os.listdir(path):
        print(i)


# files_in_dir(folder)

# opdracht 2:


def file_is_juf(files):
    for i in os.listdir(files):
        just_number = os.path.splitext(i)[0]
        if int(just_number) % 7 == 0 or "7" in just_number:
            shutil.move(files + r"\\" + i, secret.juf)
        else:
            shutil.move(files + r"\\" + i, secret.rest)


file_is_juf(secret.files)
