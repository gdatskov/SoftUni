entry = input()
rage_query = []
rage_power = []
total_rage = []
last_symbol = ""

for i in range(len(entry)):

    sym = entry[i]

    if i < len(entry)-1:
        next_sym = entry[i+1]
    else:
        next_sym = ""

    if not sym.isdigit():
        rage_query.append(sym)
    else:
        rage_power.append(sym)

    if sym.isdigit() and not next_sym.isdigit():
        total_rage.extend(x.upper() for x in rage_query * int("".join(rage_power)))
        rage_query.clear()
        rage_power.clear()

print(f"Unique symbols used: {len(set(total_rage))}")
print("".join(total_rage))
