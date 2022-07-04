def draw(num):
    if num > 0:
        print("*" * num)
        draw(num-1)
        print("#" * num)


number = int(input())
draw(number)