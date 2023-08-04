# 3.	Record Unique Names
# Write a program, which will take a list of names and print only the unique names in the list.
# The order in which we print the result does not matter.
from collections import deque

number_of_names = int(input())

names = deque()

for x in range(number_of_names):
    names.append(input())

for x in set(names):
    print(x)


