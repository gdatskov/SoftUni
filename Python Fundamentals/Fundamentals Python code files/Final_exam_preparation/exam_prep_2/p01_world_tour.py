travel_stops = input()
while True:
    commands_input = input().split(":")
    command = commands_input[0]
    if command == "Travel":
        break
    if command == "Add Stop":
        _, idx, string = commands_input
        idx = int(idx)
        if 0 <= idx < len(travel_stops):
            travel_stops = travel_stops[:idx] + string + travel_stops[idx:]
        print(travel_stops)
    if command == "Remove Stop":
        _, start_idx, end_idx = commands_input
        start_idx = int(start_idx)
        end_idx = int(end_idx)
        if 0 <= start_idx < len(travel_stops) and 0 <= end_idx < len(travel_stops):
            travel_stops = travel_stops[:start_idx] + travel_stops[end_idx+1:]
        print(travel_stops)
    if command == "Switch":
        _, old_str, new_str = commands_input
        if old_str in travel_stops:
            travel_stops = travel_stops.replace(old_str,new_str)
        print(travel_stops)

print(f"Ready for world tour! Planned stops: {travel_stops}")

