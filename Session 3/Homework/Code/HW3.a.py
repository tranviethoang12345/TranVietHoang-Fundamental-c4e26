loop = True
count = 0

while loop:
    print ("e t b i n e f")
    print ("Your answer : ", end=" ")
    a = input()
    if (a == "benefit"):
        print ("Nice one :p")
        break
    else:
        print ("bobo :(")

    count += 1
    if count > 2:
        print()
        print('Next time sir :(')
        loop = False

