name_str = input("Enter String : ")
freq = {}
 
for i in name_str:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print("Count of all characters is :\n " ,str(freq))
