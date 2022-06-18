import os


def travers_dict(dir_path, res):
    for x in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, x)):
            ext = x.split('.')[-1]
            if ext not in res:
                res[ext] = []
            res[ext].append(x)
        elif os.path.isdir(os.path.join(dir_path, x)):
            travers_dict(os.path.join(dir_path, x), res)


result = {}
travers_dict(os.getcwd(), result)

for key, value in result.items():
    print(f".{key}")
    for el in value:
        print(f"- - -{el}")
