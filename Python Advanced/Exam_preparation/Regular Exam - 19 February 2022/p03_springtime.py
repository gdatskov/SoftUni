def start_spring(**kwargs):
    result = []
    type_dict = dict()
    for key, value in kwargs.items():
        if value not in type_dict.keys():
            type_dict[value] = [key]
        else:
            type_dict[value].append(key)
    for key, value in sorted(type_dict.items(), key=lambda x: (-len(x[1]), x[0])):
        result.append(f"{key}:")
        for item in sorted(value):
            result.append(f"-{item}")

    return "\n".join(result)

example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}

print(start_spring(**example_objects))
print()

example_objects2 = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects2))
print()
example_objects3 = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects3))

