length = int(input('Length, cm: '))
width = int(input('Width, cm: '))
height = int(input('Height, cm:'))
fish_tank_volume = length*width*height
ballast_percent = int(input('Ballast volume percent, %: '))
ballast_volume = fish_tank_volume * ballast_percent / 100
water_volume = (fish_tank_volume-ballast_volume) / 1000
print(water_volume)
