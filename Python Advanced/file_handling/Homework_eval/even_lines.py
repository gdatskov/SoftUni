replaceable = {"-", ",", ".", "!", "?"}

with open("even_lines.txt", "r") as file:
    for i, line in enumerate(file):
        if i % 2 == 0:
            result = " ".join(line.strip().split()[::-1])
            for s in replaceable:
                result = result.replace(s, "@")
            print(result)



