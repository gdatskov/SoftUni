# text = input()
# list_of_text = list(text)
# convert = ""
# ascii_list = []
# for i in range(len(list_of_text)):
#     if ord(list_of_text[i]) < 97:
#         ascii_list.append(chr(ord(list_of_text[i])+(97-65)))
#     else:
#         ascii_list.append(chr(ord(list_of_text[i])))
# new_string = "".join(ascii_list)
# sand = list("sand")
#
# cut_string = new_string
# cut_list = ascii_list
# # while "sand" in cut_string:
#     for x in cut_list:
#         if x in sand:
#             cut_list.remove(x)
#             break
# print(cut_list)
# if "s" in ascii_list and "a" in ascii_list and "n" in ascii_list and "d" in ascii_list:
# #     print("YES")
# print(new_string.count("sand"))
text = input()
text = text.lower()

my_list = ["sand", "water", "fish", "sun"]
counter = 0

for item in my_list:
    if item in text:
        word_count_txt = text.count(item)
        counter += word_count_txt

print(counter)