#Using Join:-

#tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
#str = ''.join(tup)
#print(str)


t = ('p', 'y', 't', 'h', 'o', 'n', ' ', 3, '.', 10, '.', 0 )
print("Input tuple: ", t)
print(type(t))

s = ''   
for ele in t:
    s += str(ele)

print("String Output: ", s)
print(type(s))
