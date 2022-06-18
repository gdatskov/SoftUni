
text = input()
list1 = text.split(" ")
negative_list = []
for i in range(len(list1)):
    negative_list.append(-int(list1[i]))

print(negative_list)

