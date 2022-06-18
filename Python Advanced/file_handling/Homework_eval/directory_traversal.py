from os import walk

result = dict()

for _, _, files in walk("./"):
    for file in files:
        extension = file.split(".")[-1]
        if extension not in result:
            result[extension] = []
        result[extension].append(file)

for key, value in sorted(result.items()):
    print("." + key)
    for file in sorted(value):
        print(f"--- {file}")