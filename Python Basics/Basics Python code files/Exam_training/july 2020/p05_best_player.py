ten_goals = True
hat_trick = "."
best_player = ""
best_score = 0
while ten_goals:
    player = input()
    if player == "END":
        break
    goals = int(input())
    if goals >= 3:
        hat_trick = " and made a hat-trick !!!"
    if goals >= 10:
        ten_goals = False
    if goals > best_score:
        best_player = player
        best_score = goals
print(f"{best_player} is the best player!")
print(f"He has scored {best_score} goals{hat_trick}")

