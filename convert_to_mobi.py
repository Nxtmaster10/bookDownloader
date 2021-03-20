import os
from os import listdir, rename
from os.path import isfile, join
import subprocess


# return name of file to be kept after conversion.
# we are just changing the extension. azw3 here.
def get_final_filename(f):
    f = f.split(".")
    filename = ".".join(f[0:-1])
    processed_file_name = filename + ".mobi"
    return processed_file_name


# return file extension. pdf or epub or mobi
def get_file_extension(f):
    return f.split(".")[-1]


# list of extensions that needs to be ignored.
ignored_extensions = ["pdf"]

# here all the downloaded files are kept
mypath = os.path.abspath("drm_removed")

# path where converted files are stored
mypath_converted = os.path.abspath("output")

# path where processed files will be moved to, clearing the downloaded folder
mypath_processed = os.path.abspath("bin")

converted_files = [f for f in listdir(mypath_converted) if isfile(os.path.join(mypath_converted, f))]


def convert(file):
    final_file_name = get_final_filename(file)
    print("Final Filename: {} \nConverted Path: {}".format(final_file_name, mypath_converted))
    out_file = os.path.join(mypath_converted, final_file_name)
    print("Output: " + out_file)

    extension = get_file_extension(file)
    if final_file_name not in converted_files and extension not in ignored_extensions:
        print("Converting : " + file)

        try:
            myfile = os.path.join(mypath, file)
            subprocess.call(
                ["ebook-convert", myfile, out_file])

        except Exception as e:
            print(e)
    else:
        print("Already exists : " + final_file_name)
