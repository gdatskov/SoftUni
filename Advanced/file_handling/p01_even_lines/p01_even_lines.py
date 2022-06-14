"""
Problem definition:
Write a program that reads a text file and prints on the console its even lines. Line numbers start from 0.
Before you print the result, replace {"-", ",", ".", "!", "?"} with "@" and reverse the order of the words.

Expected output:
fault@ his wasn't it but him@ judge to quick was @I
safer@ is It here@ hide @Quick@

"""

# Imports
from collections import deque
# import os
# char = file.read(1)
# if char == os.linesep: ("\n" == "\r\n: False)
# Somehow it reads "\n" instead of "\r\n" from file, so i'll replace it with linesep = "\n"
linesep = "\n"

# Parameter and constants definition
print_line = deque()
edit = list()
count = 0
symbols_to_replace = ["-", ",", ".", "!", "?"]
EOF = ""        # End of file
EOL = linesep   # End of line
EOW = " "       # End of word

# Execution code
with open("./text_input_file.txt", "r") as file:

    while True:
        char = file.read(1)

        if char in symbols_to_replace:          # If current symbol has to be replaced with "@"
            edit.append("@")

        elif char in [EOW, EOF, linesep]:       # If its either end of word or line or file:
            edit = ["".join(edit)]              # Join current collection of symbols and append left as a word
            print_line.appendleft(edit.pop())

            if char in [EOF, linesep]:          # If EOL or EOF, print and clear all words (reversed)
                print(" ".join(print_line))     # and count the line
                print_line.clear()
                count += 1

                if count % 2 == 1:              # If next line is odd, skip it
                    file.readline()

        else:
            edit.append(char)                   # If regular text symbol(nothing above), add it to word

        if char == EOF:                         # End loop at EOF
            break                               # (keep it at the end, since we still have some operations at EOF==EOL)
