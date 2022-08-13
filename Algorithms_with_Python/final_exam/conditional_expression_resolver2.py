from collections import deque

entry = input()
entry_list = deque(entry.split())

def extract_bool(queue, bool_list):
    iterations = 0
    while True:
        if queue[1] == "?":
            bool_list.append(entry_list.popleft())
            entry_list.popleft()
            iterations += 1
        else:
            return queue, bool_list, iterations

bool_list = []
extract_bool(entry_list, bool_list)
true_results = []
false_results = []
while entry_list:
    iterations = 1
    true_results.append(entry_list.popleft())
    entry_list.popleft()
    if entry_list[1] == "?":
        entry_list, bool_list, iterations = extract_bool(entry_list, bool_list)
    for _ in range(iterations):
        true_results.append(entry_list.popleft())
    for _ in range(iterations):
        false_results.append(entry_list.popleft())
        entry_list.popleft()
    for _ in range(iterations):
        condition = bool_list.pop()
        if condition == "t":
            exit()



# print(entry_list)


# # print("true", true_result)
# # print("fal", false_result)
# # print("con", condition)
#
# middle_idx = len(entry_list) // 2
# result = entry_list[middle_idx]
#
# while len(entry_list) >= 5:
#     middle_idx = len(entry_list) // 2
#     true_result = result
#     false_result = entry_list[middle_idx + 2]
#     condition = entry_list[middle_idx - 2]
#
#     if condition == "t":
#         result = true_result
#     else:
#         result = false_result
#
#     entry_list[middle_idx+2] = result
#     entry_list = entry_list[:middle_idx-2] + entry_list[middle_idx+2:]
#     # print(entry_list)
#
# # print(entry_list[len(entry_list) // 2])
# print(result)
