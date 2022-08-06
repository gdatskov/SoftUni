entry = list(input())
# \*{2}[A-Z][a-z_]{2,}\*{2}|\:{2}[A-Z][a-z_]{2,}\:{2}
# print(entry)
buffer = ""
candidates = []
numbers = []
start = None
end = None

while entry:
    symbol = entry.pop()
    if symbol.isnumeric():
        numbers.append(symbol)
    buffer += symbol
    if buffer[len(buffer)-2:] in ["**", "::"] and len(buffer) == 2:
        start = buffer[len(buffer)-2:]
    if not start and len(buffer) > 1:
        buffer = buffer[len(buffer)-1:]
    if start and not end:
        end = start
    if len(buffer) >= 2+3+2 and buffer[len(buffer)-2:] == end:
        if buffer[2:-2].isalpha() and buffer[-3].isupper() and buffer[2:-3].islower():
            candidates.append("".join(reversed(buffer)))
        buffer = ""
        end = None
        start = None

total_candidates = len(candidates)

mul = 1
for x in numbers:
    mul *= int(x)

ascii_sum = 0
for smiley in candidates:
    ascii_sum = 1
    for y in smiley[2:-2]:
        ascii_sum += ord(y)
    if ascii_sum < mul:
        candidates.remove(smiley)

print(f"Cool threshold: {mul}")
print(f"{total_candidates} emojis found in the text. The cool ones are:")
for smiley in reversed(candidates):
    print(smiley)
