current_version = input()
new_version = current_version.split(".")
next_version = "".join(new_version)
next_version = int(next_version) + 1
next_version = str(next_version)
next_version = ".".join(list(next_version))
print(next_version)

