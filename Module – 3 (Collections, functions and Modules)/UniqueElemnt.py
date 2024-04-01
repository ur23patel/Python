

test_list = [1, 5, 3, 6, 3, 5, 6, 1]
print("The Original List is : " + str(test_list)) 
uni = []
for i in test_list:
    if i not in uni:
        uni.append(i)

print("The Unique List Is : " + str(uni))
