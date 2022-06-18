#Input
# - Float Side, Height
# - Calculate area A=a*h/2
# - Format f2

#Input code
# b1 = float(input("b1="))
# b2 = float(input('b2='))
# h = float(input('h='))
b1 = float(input())
b2 = float(input())
h = float(input())
#Process code
area = (b1+b2)*h/2

#Output code
print("{:.2f}".format(area))