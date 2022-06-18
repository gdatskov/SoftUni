entry1 = input()
entry2 = input()

list1 = entry1.split(", ")
list2 = entry2.split(", ")
list3 = []
list4 = []
# for word1 in list1:
#     # list3.extend(set(word1 for word2 in list2 if word1 in word2))
#     # това също работи като подцикъл
#
#
#     for word2 in list2:
#         if word1 in word2 and word1 not in list3:
#             list3.append(word1)
#     # това работи като подцикъл

# list4 = [list(word2 for word2 in list2 if word1 in word2) for word1 in list1]
# не съвсем... станаха листи в листа


# list5 = [word1 for word1 in list1 for word2 in list2 if word1 in word2]
# не съвсем, има дуплицирани верни резултати


list6 = [word1 for word1 in list1 if word1 in entry2]
# мдяяя... лесното решение, ако не забравиш да не сплитваш


# print(list3)
# print(list(list3))
# print(list4)
# print(list5)
print(list6)
