kilometers = int(input())
day_or_night = str(input())
taxi_tariff = 0.7+0.79*kilometers

if day_or_night == 'night':
    taxi_tariff = 0.7+0.9*kilometers

bus_tariff = 0.09*kilometers
train_tariff = 0.06*kilometers

if kilometers >= 100:
    price = train_tariff
elif kilometers >= 20:
    price = bus_tariff
else:
    price = taxi_tariff

print(f"{price:.2f}")