numbers_dictionary = {}

line = input('Please enter your string number: ')

while line != "Search":
    try:
        number_as_string = line
        number = int(input('Please enter your integer number: '))
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print('The variable number must be an integer')
    line = input('Please enter your string number: ')

line = input('Please enter your search string number: ')
while line != "Remove":
    try:
        searched = line
        print(numbers_dictionary[searched])
    except KeyError:
        print('Number does not exist in dictionary')
    line = input('Please enter you search string number: ')

line = input('Please enter your delete string number: ')

while line != "End":
    try:
        searched = line
        del numbers_dictionary[searched]
    except KeyError:
        print('Number does not exist in dictionary')
    line = input('Please enter your delete string number: ')

print(numbers_dictionary)