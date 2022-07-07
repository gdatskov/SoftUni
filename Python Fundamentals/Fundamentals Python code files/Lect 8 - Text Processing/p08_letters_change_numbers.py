entry = input().strip().split()

total_sum = 0

for st in entry:
    st = st.strip()
    first_letter = st[0]
    last_letter = st[-1]
    number = int(st[1:-1])

    if first_letter.isupper():
        first_ord = ord(first_letter) - ord("A") + 1
        number /= first_ord
    else:
        first_ord = ord(first_letter) - ord("a") + 1
        number *= first_ord

    if last_letter.isupper():
        last_ord = ord(last_letter) - ord("A") + 1
        number -= last_ord
    else:
        last_ord = ord(last_letter) - ord("a") + 1
        number += last_ord

    total_sum += number

print(f"{total_sum:.2f}")
