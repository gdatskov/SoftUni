tax = input('Annual tax: ')
sneakers = float(tax) * (1-0.4)
team_kit = sneakers * 0.8
balls = team_kit/4
accessories = balls/5
total = float(tax)+sneakers+team_kit+balls+accessories
print(total)
