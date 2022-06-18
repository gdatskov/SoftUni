word = input()

# for i in range(1, len(word)+1):
#     print(word[-i], end="")

for i in (range(len(word)-1, -1, -1)):
    print(word[i], end="")
