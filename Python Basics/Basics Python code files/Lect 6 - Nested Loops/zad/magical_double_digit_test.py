# range_a = (0, 9) това е диапазона от числата 0 и 9, а не 0,1,2...9
# range_b = (2, 5) това е диапазона от числата 2 и 5, а не 2, 3...5
magical_number = 15

stop = False
# for a in range_a:
for a in range(9):
    # for b in range_b:
    for b in range(2, 5):
        if a + b == magical_number:
            print(f"Магическото число е: {magical_number}")
            print("Край на цикъла")
            stop = True
            break
    if stop:
        break
    # else:                                 # изпълнява се за целия range a
    #     print("Числото не е намерено")
if not stop:
    print("Числото не е намерено")
