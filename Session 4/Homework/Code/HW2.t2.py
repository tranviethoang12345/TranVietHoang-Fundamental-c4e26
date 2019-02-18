print("Answer the following algebra question: \n If x = 8, then what is the value of 4(x + 3) ?")
print("1. 35\n2. 36\n3. 40\n4. 44")

n = input("Your choie:")
while not n.isdigit():
    n = input("You must input n digit. Your choie:")

if int(n) == 4:
    print("Bingo")
else:
    print(":(")
