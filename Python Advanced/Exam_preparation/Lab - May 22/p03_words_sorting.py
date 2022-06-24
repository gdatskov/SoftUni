def words_sorting(*args):
    dic = dict()

    for word in args:
        ascii_sum = 0
        for char in word:
            ascii_sum += ord(char)
        dic[word] = ascii_sum

    odd = True if sum(dic.values()) % 2 == 1 else False

    if odd:
        text = [f"{key} - {value}" for key, value in sorted(dic.items(), key=lambda x: -x[1])]
    else:
        text = [f"{key} - {value}" for key, value in sorted(dic.items(), key=lambda x: x[0])]

    return "\n".join(text)

print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))
print()
print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))
print()
print(
    words_sorting(
        'cacophony',
        'accolade'
  ))
