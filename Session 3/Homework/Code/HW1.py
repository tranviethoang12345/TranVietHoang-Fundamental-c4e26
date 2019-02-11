items = ['T-Shirt', 'Sweater']

loop = True

while loop:
    c = input("Welcome to our shop, what do you want (C, R, U, D)? ").lower()

    if c == 'r':
        print(items)
        loop = False
    elif c == 'c':
        items.append(input("Enter new item: "))
        print(items)
    elif c == 'u':
        pos = int(input("Update position? "))
        items[pos-1] = input("New item? ")
        print(items)
    elif c == 'd':
        pos = int(input("Delete position? "))
        del items[pos-1]
        print(items)
    else:
        print("Please select one of the (C, R, U, D) options!")
