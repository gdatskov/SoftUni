money = float(input())
end_year = int(input())
money_left = money
for years in range(1800, end_year+1):
    if years % 2 == 0:
        money_left -= 12000
    else:
        money_left -= (12000 + 50 * (18+years-1800))

if money_left >= 0:
    print(f"Yes! He will live a carefree life and will have {money_left:.2f} dollars left.")
else:
    print(f"He will need {abs(money_left):.2f} dollars to survive.")

# Да се отпечата на конзолата 1 ред.
# Сумата трябва да е форматирана до два знака след десетичната запетая:

# •	Ако парите са достатъчно:
# "Yes! He will live a carefree life and will have {N} dollars left." –
# # където N са парите, които ще му останат.

# •	Ако парите НЕ са достатъчно:
# "He will need {М} dollars to survive." – където M е сумата, която НЕ достига.
