key = (input("Enter a word, this will be count: ")).lower()

n = key.replace(" ", "")

dictionary = {}

for i in n:
    if i not in dictionary:
        dictionary[i] = 1
    else:
        dictionary[i] = dictionary[i] + 1

for m in sorted(dictionary):
    print(m, dictionary[m])