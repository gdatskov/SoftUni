entry = input()
word_list = entry.split(" ")
even_words_list = [word for word in word_list if len(word) % 2 == 0]
for word in even_words_list:
    print(word)
