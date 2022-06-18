# Kids drink toddy, teens drink coke, young adults drink beer, and adults drink whisky.
# Create a program that receives an age and prints what they drink.
# Rules:
# A kid is defined as someone under or at the age of 14.
# A teen is defined as someone under or at the age of 18.
# A young adult is defined as someone under or at the age of 21.
# An adult is defined as someone above the age of 21.
# Note: All the values are inclusive except the last one!

customer = int(input())
if customer <= 14:  #Kid
    print("drink toddy")
elif customer <= 18:    #Teen
    print("drink coke")
elif customer <= 21:    #Young adult
    print("drink beer")
else:     #Adult
    print("drink whisky")