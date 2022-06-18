from collections import deque

matrix_rows, matrix_cols = [int(x) for x in input().split()]
entry_string = deque(input())

# snake_matrix = [] #ver 1
snake_que = deque()
# row_count = 0   # ver 2

# while len(snake_matrix) < matrix_rows:    #ver 1
# while row_count < matrix_rows:  # ver 2
for row in range(matrix_rows):  # ver 3 => without while cycle
    current_row = deque()
    # row_count += 1  # ver 2

    for col in range(matrix_cols):
        if len(snake_que) == 0:
            snake_que = deque.copy(entry_string)
        if row % 2 == 0:
            current_row.append(snake_que.popleft())
        else:
            current_row.appendleft(snake_que.popleft())

    # snake_matrix.append(current_row)    # ver 1
    print("".join(current_row))

# print(snake_matrix)



