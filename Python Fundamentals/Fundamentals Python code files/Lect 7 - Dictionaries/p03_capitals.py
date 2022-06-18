some_dic = dict()
entry1 = input().split(", ")
entry2 = input().split(", ")

# Това работи
# for country in range(len(entry1)):
#     some_dic[entry1[country]] = entry2[country]

# И това работи
# for country in entry1:
#     some_dic[country] = entry2[entry1.index(country)]

# малко е тъпо... ама нали искат comprehension
# some_dic = {country: entry2[entry1.index(country)] for country in entry1}

# със зиП:
zipped_data = list(zip(entry1, entry2))
some_dic = {country: capital for country, capital in zipped_data}

for elem in some_dic:
    print(f"{elem} -> {some_dic[elem]}")
