#float input °C
#float output °F
#T (° F) = T (° C) × 9/5 + 32
#format 2f

cels = float(input())
farh = cels*9/5+32

print("{:.2f}".format(farh))
