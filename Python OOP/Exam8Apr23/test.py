def repeatedString(s, n):
    initial_sequence = s
    init_string_lenght = len(initial_sequence)
    total_string_lenght = n

    whole_repeats = total_string_lenght // init_string_lenght
    last_sequence = s[:(total_string_lenght % init_string_lenght)]

    initial_sequence_count = len([x for x in initial_sequence if x == "a"])
    last_sequence_count = len([x for x in last_sequence if x == "a"])

    total_occurences_of_a = initial_sequence_count * whole_repeats + last_sequence_count

    return total_occurences_of_a

print(repeatedString("aba", 2))