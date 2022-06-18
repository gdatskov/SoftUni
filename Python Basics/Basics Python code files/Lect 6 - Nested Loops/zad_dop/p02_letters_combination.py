start_interval = input()
end_interval = input()
miss_char = input()
valid_combinations = 0

for char_1 in range(ord(start_interval), ord(end_interval) + 1):
    if char_1 != ord(miss_char):
        for char_2 in range(ord(start_interval), ord(end_interval) + 1):
            if char_2 != ord(miss_char):
                for char_3 in range(ord(start_interval), ord(end_interval) + 1):
                    if char_3 != ord(miss_char):
                        valid_combinations += 1
                        print(f"{chr(char_1)}{chr(char_2)}{chr(char_3)}", end=" ")
print(valid_combinations)
