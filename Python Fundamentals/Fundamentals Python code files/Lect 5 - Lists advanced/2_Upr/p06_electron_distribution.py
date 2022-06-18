electrons = int(input())
list_of_shells = []
shell = 0
while electrons > 0:
    shell += 1
    shell_electrons = 2 * shell ** 2
    if shell_electrons <= electrons:
        free_electrons = shell_electrons
    else:
        free_electrons = electrons
    list_of_shells.append(free_electrons)
    electrons -= free_electrons
print(list_of_shells)

