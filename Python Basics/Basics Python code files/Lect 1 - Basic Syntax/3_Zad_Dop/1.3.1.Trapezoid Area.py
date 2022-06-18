#Input
# - Float Base1, Base2, Height
# - Calculate area A=(b1+b2)*h/2
# - Format f2

#Input code
a = float(input())
h = float(input())
#Process code
area = a*h/2

#Output code
print("{:.2f}".format(area))
