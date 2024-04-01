l = [] 
n = int(input("Enter the number of elements: "))
for i in range(1, n+1): 
    elem = int(input("Enter the elements: ")) 
    l.append(elem)
    
print("The second smallest value of this list: ",l[1])
