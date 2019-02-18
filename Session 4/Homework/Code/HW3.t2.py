print("Answer the following algebra question: \n If x = 8, then what is the value of 4(x + 3) ?")
print("1. 35\n2. 36\n3. 40\n4. 44")

n = input("Your choie:")
while not n.isdigit():
    n = input("You must input n digit. Your choie:")

if int(n) == 4:
    print("Bingo")
else:
    print(":(")


print("Jack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the means?")
print("1.About 55\n2.About 65\n3.About 75\n4.About 85")

m = input("Your choice: ")
while not m.isdigit():  
    m = int(input("Your choice: "))

if int(m) == 2:
    print("Bingo")
else:
    print(":(")   