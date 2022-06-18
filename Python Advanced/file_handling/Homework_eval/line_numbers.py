import string


def count(line):
        marks = 0
        letters = 0
        for s in line:
            if s in string.punctuation:
                marks += 1
            elif s in string.ascii_letters:
                letters += 1
        return letters, marks


with open("./even_lines.txt", "r") as input_file, open("./output.txt", "w") as output_file:
    for i, line in enumerate(input_file):
        letters, puncs = count(line)
        output_file.write(f"Line {i + 1}: {line.strip()} ({letters})({puncs})\n")





