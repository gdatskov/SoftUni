N1 = int(input())
N2 = int(input())
operator = input()

even_odd = ""

if operator == "+":
    if (N1 + N2) % 2 == 0:
        even_odd = "even"
    else: even_odd = "odd"
    print(f"{N1} {operator} {N2} = {N1+N2} - {even_odd}")
if operator == "-":
    if (N1 - N2) % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
    print(f"{N1} {operator} {N2} = {N1 - N2} - {even_odd}")
if operator == "*":
    if (N1 * N2) % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
    print(f"{N1} {operator} {N2} = {N1 * N2} - {even_odd}")
if operator == "/":
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    else:
        print(f"{N1} {operator} {N2} = {N1 / N2:.2f}")
if operator == "%":
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    else:
        print(f"{N1} {operator} {N2} = {N1 % N2}")