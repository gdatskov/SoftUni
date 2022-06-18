def palindrome_check(entry_list):
    entry_list = entry.split(", ")
    for element in entry_list:
        reverse_element = list(element)
        list.reverse(reverse_element)
        list_of_element = list(element)
        if list_of_element == reverse_element:
            print(True)
        else:
            print(False)


entry = input()
palindrome_check(entry)     #True or False for each element


