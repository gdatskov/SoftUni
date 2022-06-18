from math import floor

processors_to_be_manufactured = int(input())
employees = int(input())
working_days = int(input())

total_working_hours = working_days * employees * 8
manufactured_processors = floor(total_working_hours/3)

manufacturing_difference = abs(manufactured_processors - processors_to_be_manufactured)*110.1

if manufactured_processors >= processors_to_be_manufactured:
    print(f"Profit: -> {manufacturing_difference:.2f} BGN")
else:
    print(f"Losses: -> {manufacturing_difference:.2f} BGN")
