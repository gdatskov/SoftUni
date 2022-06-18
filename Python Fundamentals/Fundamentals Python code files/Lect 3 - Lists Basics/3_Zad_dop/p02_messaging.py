number_entry = input()
string_entry = input()
new_list = []
number_list = number_entry.split(" ")
number_list = "".join(number_list)
number_list = list(number_list)
for i in range(len(number_list)):
    number_list[i] = int(number_list[i])
index_sum = sum(number_list)
if index_sum > len(string_entry):

# for item in number_list:
#     new_list.append(int(number_list))
# print(new_list)
# text = input()
# li = list(text)
# print(li)