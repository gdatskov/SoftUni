from math import pi

radius = float(input())
area = pi*radius**2
circumference = 2*pi*radius

print("{:.2f}".format(area))
print("{:.2f}".format(circumference))