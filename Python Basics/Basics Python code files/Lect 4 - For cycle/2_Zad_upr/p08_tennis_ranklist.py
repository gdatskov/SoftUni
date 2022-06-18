import math

competitions = int(input())
starting_points = int(input())

winner_points = 2000
finals_points = 1200
semi_finals_points = 720

competition_points = 0
won_competitions = 0
position = ""

for tours in range(competitions):
    position = input()
    if position == "W":
        competition_points += winner_points
        won_competitions += 1
    if position == "SF":
        competition_points += semi_finals_points
    if position == "F":
        competition_points += finals_points

total_points = starting_points + competition_points
average_points = math.floor(competition_points/competitions)
percent_won_competitions = won_competitions/competitions*100

print(f"Final points: {total_points}")
print(f"Average points: {average_points}")
print(f"{percent_won_competitions:.2f}%")
