def get_even_list(l):
        ls = []
        for i in range(len(l)):
                if(l[i]%2==0):
                        ls.append(l[i])
        print(ls)
        return ls

l = [1, 4, 5, -1, 10]
print(get_even_list(l)) 