print("Hello, my name is Max and these are my sheep sizes")

s = [5,7,300,90,24,50,75]

print(s)
print()

print("Now my biggest sheep has size ",max(s) ,"let's shear it")
s[s.index(max(s))] = 8
print("After shearing, here's my flock")
print(s) 
print()

sum = 0
for m in range(3):
    print("MONTH", m+1)

    print("One month has passed, now here is my flock")
    s1=[]
    for i in s:
        i += 50
        s1.append(i)       
    print(s1)
    s = s1

    print("Now my biggest sheep has size ",max(s) ,"let's shear it")
    s[s.index(max(s))] = 8
    print("After shearing, here's my flock")
    print(s) 
    print()


for i in s:
    sum += i

print("My flock has size in total: ",sum,"\nI would get ",sum ,"* 2$ = ",sum * 2,sep='')