# Use this script to clean up logs when they are littered by useless lines that make analysis unnecessarily hard
# It takes the filename and string to get rid of as arguments
#NCA 170925

import os
import errno
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-filename")
parser.add_argument("-string")
args = parser.parse_args()

file_to_clean = args.filename
string_to_remove = args.string

name_of_file = str(os.path.splitext(os.path.basename(file_to_clean))[0])

newfile = (name_of_file + "_new.txt")

with open(file_to_clean, "r") as input:
    with open(newfile, "wb") as out:
        for line in input:
            if string_to_remove not in line:
                out.write(line + os.linesep)
