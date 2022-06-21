text = list(input())
unique = set(text)
output = dict()

for z in unique:
    output[z] = (text.count(z))

print("\n".join([f"{k}: {v} time/s" for k, v in sorted(output.items())]))

