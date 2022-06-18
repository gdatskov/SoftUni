days_off = int(input())

play_days_off = days_off * 127
play_working_days = (365-days_off)*63
total_play_time = play_working_days+play_days_off

if total_play_time > 30000:
    print('Tom will run away')
    print(f"{(total_play_time-30000)//60} hours and "
          f"{(total_play_time-30000)%60} minutes more for play")
else:
    print('Tom sleeps well')
    print(f'{(30000-total_play_time)//60} hours and '
          f'{(30000-total_play_time)%60} minutes less for play')