import re

validation_pattern = r"(.*)>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([^><]{3})<(.*)"

inputs_number = int(input())
for _ in range(inputs_number):
    groups = {}
    password = input()
    valid_password = re.search(validation_pattern, password)
    even_more_valid_password = False
    if valid_password:
        for num in range(6):
            groups[num] = valid_password.groups()[num]
        even_more_valid_password = True if groups[0] == groups[5] else False
    if even_more_valid_password:
        print(f"Password: {''.join(val for key, val in groups.items() if key not in [0,5])}")
    else:
        print("Try another password!")