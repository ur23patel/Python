str = input("Enter a string: ")
d = {}


for ch in str:
    if ch in d:
        d[ch] += 1
    else:
        d[ch] = 1
print(d)
