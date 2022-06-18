import math

c_skumriq = float(input())
c_caca = float(input())
palamud = float(input())
safrid = float(input())
midi = int(input())

c_palamud = c_skumriq*1.6
c_safrid = c_caca*1.8
c_midi = 7.5
total = c_palamud*palamud + c_safrid*safrid + c_midi*midi

#print(math.ceil(total*100)/100)
print("{:.2f}".format(total))
