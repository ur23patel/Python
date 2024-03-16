a = int(input("Enter First Value : "))
b = int(input("Enter Second Value : "))
c = int(input("Enter Third Value : "))
sum = a+b+c

if a==b or b==c or c==a:
    print("Sum is Zero")
else:
    print("Sum is : ", sum)
