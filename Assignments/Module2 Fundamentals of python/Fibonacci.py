n=int(input("Enter the Numbers: "))
a=0
b=1
if n<=0:
    print("Output is : ",a)
else:
    print(a,b,end=" ")
    for i in range(2,n):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
