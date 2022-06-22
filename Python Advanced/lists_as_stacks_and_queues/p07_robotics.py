from collections import deque


def convert_time(counter):
    if counter[2] >= 60:
        counter[1] += counter[2] // 60
        counter[2] %= 60
    if counter[1] >= 60:
        counter[0] += counter[1] // 60
        counter[1] %= 60
    if counter[0] >= 24:
        counter[0] %= 24
    return f'{counter[0]:02d}:{counter[1]:02d}:{counter[2]:02d}'


processing_robots = dict()
product_queue = deque()
production_time = 0
end = False
available_robots = deque(tuple(robot.split("-")) for robot in input().split(";"))
starting_time = [int(x) for x in input().split(":")]

while True:
    if not end:
        product_input = input()
        if product_input == "End":
            end = True
            continue
        product_queue.append(product_input)

    production_time += 1

    if product_queue:
        product_queue.append(product_queue.popleft())

    if end and not product_queue:
        break

    if production_time in processing_robots.keys():
        available_robots.append(processing_robots[production_time])
        processing_robots.pop(production_time)

    if available_robots and product_queue:
        product = product_queue.popleft()
        robot = available_robots.popleft()
        robot_name, processing_time = robot
        processing_robots[production_time + int(processing_time)] = robot
        current_time = [starting_time[0], starting_time[1], starting_time[2] + production_time]
        print(f"{robot_name} - {product} [{convert_time(current_time)}]")
