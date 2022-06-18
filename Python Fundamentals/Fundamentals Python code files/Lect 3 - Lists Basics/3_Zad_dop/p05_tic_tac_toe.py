row1 = input()
row2 = input()
row3 = input()
li = row1.split(" ") + row2.split(" ") + row3.split(" ")
check = 0
if li[1-1] == li[2-1] == li[3-1]:   #First row
    check = li[1-1]
if li[4-1] == li[5-1] == li[6-1]:   #Second row
    check = li[4-1]
if li[7-1] == li[8-1] == li[9-1]:   #Third row
    check = li[7-1]
if li[1-1] == li[4-1] == li[7-1]:   #First column
    check = li[1-1]
if li[2-1] == li[5-1] == li[7-1]:   #Second column
    check = li[2-1]
if li[3-1] == li[6-1] == li[9-1]:   #Third column
    check = li[3-1]
if li[1-1] == li[5-1] == li[9-1]:   #Main diagonal
    check = li[5-1]
if li[3-1] == li[5-1] == li[7-1]:   #Other diagonal
    check = li[5-1]

if check == "1":
    print("First player won")
elif check == "2":
    print("Second player won")
else:
    print("Draw!")

