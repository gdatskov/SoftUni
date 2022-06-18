#Inputs
x = float(input())
y = float(input())
h = float(input())

#Wall area calculations
front_w = x**2-1.2*2
back_w = x**2
side_w = x*y - 1.5**2
front_r = x*h/2
side_r = x*y

#Total area calculations
side_area = front_w+back_w+side_w*2
roof_area = front_r*2+side_r*2

#Consumption calculations
red_cons = roof_area/4.3
green_cons = side_area/3.4

#Output
print('{:.2f}'.format(green_cons))
print('{:.2f}'.format(red_cons))
