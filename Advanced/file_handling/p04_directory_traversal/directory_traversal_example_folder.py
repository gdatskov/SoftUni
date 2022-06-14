# Problem definition:
"""
Write a program that traverses a given directory for all files.
Search through the first level of the directory only and write information about each found file in report.txt.
The files should be grouped by their extension. Extensions should be ordered by name alphabetically.
The files with extensions should also be sorted by name. report.txt should be saved in the chosen directory.
"""

# Example directory:
"""
"./example_files"
"""

# Expected output (in "report.txt" file):
"""
.html
- - - index_inception1.html
.js
- - - index_inception1.js
.pptx
- - - demo_inception1.pptx
.py
- - - program.py
- - - python.py
.txt
- - - log.txt
- - - notes.txt

"""

from os import listdir
from os.path import isfile

files = dict()
current_directory = listdir("./example_files/")

# Reading the directory for files:
for element in current_directory:
    if isfile(f"./example_files/{element}"):
        extension = element.split(".")[-1]
        if extension in files:
            files[extension].append(element)
        else:
            files[extension] = [element]

# Writing the report for files in folder:
with open("./report.txt", "w") as report:
    for extension in files.keys():
        report.write(f".{extension}" + '\n')
        for file in files[extension]:
            report.write(f"- - - {file}" + '\n')


