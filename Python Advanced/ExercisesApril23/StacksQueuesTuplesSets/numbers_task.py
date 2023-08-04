from collections import deque

first_seq = set(map(int, input().split()))
second_seq = set(map(int, input().split()))

commands_count = int(input())


def get_command_and_seq(entry: str):
    command_list = deque(entry.split())
    command = f"{command_list.popleft()} {command_list.popleft()}"
    return command, set(map(int, command_list))


for _ in range(commands_count):
    entry = input()
    command, set_seq = get_command_and_seq(entry)
    if command == "Add First":
        first_seq = first_seq.union(set_seq)
    elif command == "Add Second":
        second_seq= second_seq.union(set_seq)
    elif command == "Remove First":
        first_seq = first_seq.difference(set_seq)
    elif command == "Remove Second":
        second_seq = second_seq.difference(set_seq)
    elif command == "Check Subset":
        print(first_seq.issubset(second_seq) or second_seq.issubset(first_seq))

print(first_seq)
print(second_seq)

