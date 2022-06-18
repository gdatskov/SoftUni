change = float(input())
coin_counter = 0
m0n3y = int(change*100)

# while m0n3y > 0:
for number in range(int(m0n3y//200)):
    coin_counter += 1
    m0n3y -= 200
for number in range(int(m0n3y//100)):
    coin_counter += 1
    m0n3y -= 100
for number in range(int(m0n3y//50)):
    coin_counter += 1
    m0n3y -= 50
for number in range(int(m0n3y//20)):
    coin_counter += 1
    m0n3y -= 20
for number in range(int(m0n3y//10)):
    coin_counter += 1
    m0n3y -= 10
for number in range(int(m0n3y//5)):
    coin_counter += 1
    m0n3y -= 5
for number in range(int(m0n3y//2)):
    coin_counter += 1
    m0n3y -= 2
for number in range(int(m0n3y//1)):
    coin_counter += 1
    m0n3y -= 1

print(coin_counter)