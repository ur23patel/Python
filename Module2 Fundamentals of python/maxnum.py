a = int(input("Enter A:"))
b = int(input("Enter B:"))
c = int(input("Enter C:"))

if a > b:
    if a > c:
        print(a, "IS Max Number")
    else:
        print(c, "IS Max Number")
elif b > c:
    print(b, "IS Max Number")
else:
    print(c, "IS Max Number")
