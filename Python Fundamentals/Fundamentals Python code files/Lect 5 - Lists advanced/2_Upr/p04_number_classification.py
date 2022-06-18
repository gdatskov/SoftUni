number_list = list(map(int, (input().split(", "))))

print(f'Positive: {str(", ".join(str(num) for num in number_list if num >= 0))}')
print(f'Negative: {str(", ".join(str(num) for num in number_list if num < 0))}')
print(f'Even: {str(", ".join(str(num) for num in number_list if num % 2 == 0))}')
print(f'Odd: {str(", ".join(str(num) for num in number_list if num % 2 != 0))}')
