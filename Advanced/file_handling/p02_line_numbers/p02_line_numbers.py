"""
Problem definition:
Write a program that reads a text file, inserts line numbers in front of each line,
and counts all the letters and punctuation marks.
The result should be written to another text file.


Input text file example:
-I was quick to judge him, but it wasn't his fault.
-Is this some kind of joke?! Is it?
-Quick, hide here. It is safer.


Expected output (as new text file):
Line 1: -I was quick to judge him, but it wasn't his fault. (37)(4)
Line 2: -Is this some kind of joke?! Is it? (24)(4)
Line 3: -Quick, hide here. It is safer. (22)(4)

"""

# Imports
import string

# Parameter definition
alpha_count = 0
punctuation_count = 0
number_of_lines = 0

# Execution code
with open("./text_input_file.txt", "r") as input_file:
    output_file = open("./text_output_file.txt", "w")
    while True:
        line = input_file.readline()

        if line == "":
            break
        else:
            number_of_lines += 1

        for char in line:
            if char == "\n":
                line = line.replace("\n", "")
            if char.isalpha():
                alpha_count += 1
            if char in string.punctuation:
                punctuation_count += 1

        output_file.write(
            f"Line: {number_of_lines} {line} ({alpha_count}) ({punctuation_count}) \n"
        )

        alpha_count = 0
        punctuation_count = 0

        if line == "":
            break

    output_file.close()
input_file.close()